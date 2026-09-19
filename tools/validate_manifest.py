#!/usr/bin/env python3
"""Validate a benchmark manifest CSV against schemas/benchmark_manifest.schema.json.

Standard library only, on purpose: every work package must be able to run this on day 1
without setting up an environment.

    python3 tools/validate_manifest.py data/manifest/benchmark_v0.example.csv

Beyond schema conformance it applies the cross-row checks that catch the failure modes in
docs/03-pipeline/stages/S0-benchmark.md -- duplicate ids, selectivity ratios built from
incomparable assays, and decoy sets that a 2D model would separate trivially.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "schemas" / "benchmark_manifest.schema.json"

BOOL_TRUE = {"true", "1", "yes", "y"}
BOOL_FALSE = {"false", "0", "no", "n"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def emit(self) -> int:
        for w in self.warnings:
            print(f"  WARN  {w}")
        for e in self.errors:
            print(f"  ERROR {e}")
        print()
        print(f"{len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        return 1 if self.errors else 0


def coerce(value: str, spec: dict):
    """Turn a CSV string into the type the schema expects. Empty string means null."""
    if value == "":
        return None
    types = spec.get("type", "string")
    types = [types] if isinstance(types, str) else types
    if "boolean" in types:
        low = value.lower()
        if low in BOOL_TRUE:
            return True
        if low in BOOL_FALSE:
            return False
        raise ValueError(f"not a boolean: {value!r}")
    if "number" in types or "integer" in types:
        return float(value) if "number" in types else int(value)
    if "array" in types:
        return [v.strip() for v in value.split("|") if v.strip()]
    return value


def check_row(row: dict, idx: int, schema: dict, rep: Report) -> dict:
    props = schema["properties"]
    required = set(schema["required"])
    where = f"row {idx}"

    unknown = set(row) - set(props)
    if unknown:
        rep.error(f"{where}: unknown column(s): {', '.join(sorted(unknown))}")

    parsed: dict = {}
    for key, spec in props.items():
        raw = row.get(key, "")
        try:
            val = coerce(raw, spec)
        except ValueError as exc:
            rep.error(f"{where}.{key}: {exc}")
            continue
        parsed[key] = val

        if val is None:
            if key in required:
                rep.error(f"{where}.{key}: required field is empty")
            continue

        if "enum" in spec and val not in spec["enum"]:
            allowed = ", ".join(str(e) for e in spec["enum"] if e is not None)
            rep.error(f"{where}.{key}: {val!r} not in [{allowed}]")
        if "pattern" in spec and isinstance(val, str) and not re.match(spec["pattern"], val):
            rep.error(f"{where}.{key}: {val!r} does not match {spec['pattern']}")
        if spec.get("format") == "date" and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(val)):
            rep.error(f"{where}.{key}: {val!r} is not an ISO date")

    return parsed


def check_semantics(rows: list[dict], rep: Report) -> None:
    """The checks that matter scientifically, which a JSON schema cannot express."""
    # Duplicate ligand-target pairs would silently double-count in every metric.
    pairs = Counter((r.get("ligand_id"), r.get("target_id")) for r in rows)
    for pair, n in pairs.items():
        if n > 1:
            rep.error(f"duplicate ligand-target pair {pair[0]}/{pair[1]} appears {n} times")

    # One ligand_id must mean one molecule.
    by_ligand = defaultdict(set)
    for r in rows:
        if r.get("ligand_id") and r.get("inchikey"):
            by_ligand[r["ligand_id"]].add(r["inchikey"])
    for lig, keys in by_ligand.items():
        if len(keys) > 1:
            rep.error(f"{lig} maps to {len(keys)} different InChIKeys -- ligand_id must be stable")

    # A selectivity ratio across different assay types is an artefact, not a measurement.
    assays = defaultdict(set)
    for r in rows:
        if r.get("activity_value") is not None and r.get("ligand_id"):
            assays[r["ligand_id"]].add((r.get("activity_type"), r.get("assay_atp_conc_uM")))
    for lig, combos in assays.items():
        types = {c[0] for c in combos}
        if len(types) > 1:
            rep.error(
                f"{lig}: activity reported as {sorted(t for t in types if t)} across targets -- "
                "cross-target ratios from mixed assay types are not valid (see open-questions C1)"
            )
        atps = {c[1] for c in combos if c[1] is not None}
        if len(atps) > 1:
            rep.warn(
                f"{lig}: ATP concentrations differ across targets ({sorted(atps)}) -- "
                "kinase IC50 ratios are not comparable without a Cheng-Prusoff correction"
            )

    # Measured activity with no assay id cannot be harmonised later.
    for r in rows:
        if r.get("activity_value") is not None and not r.get("assay_id"):
            rep.warn(f"{r.get('ligand_id')}/{r.get('target_id')}: activity_value with no assay_id")

    # Scaffold overlap across splits is leakage.
    split_scaffolds = defaultdict(set)
    for r in rows:
        if r.get("scaffold_id"):
            split_scaffolds[r["split"]].add(r["scaffold_id"])
    train, test = split_scaffolds.get("train", set()), split_scaffolds.get("test", set())
    if train & test:
        rep.error(f"{len(train & test)} scaffold(s) appear in both train and test -- leakage")

    # Sizing and balance, against the source-doc minimum.
    ligands = {r.get("ligand_id") for r in rows if not r.get("is_decoy")}
    decoys = {r.get("ligand_id") for r in rows if r.get("is_decoy")}
    targets = {r.get("target_id") for r in rows}
    print(f"  {len(rows)} rows | {len(ligands)} ligands | {len(decoys)} decoys | {len(targets)} targets")

    if len(targets) < 2:
        rep.error("fewer than 2 targets -- selectivity is not measurable")
    if len(ligands) < 12:
        rep.warn(f"{len(ligands)} ligands is below the hackathon minimum of 12-20 [source-doc]")
    if decoys and len(decoys) < 20:
        rep.warn(f"{len(decoys)} decoys is below the minimum viable 20-50 [source-doc]")

    classes = Counter(r.get("selectivity_class") for r in rows if r.get("selectivity_class"))
    if classes:
        print(f"  selectivity classes: {dict(classes)}")
    if classes.get("non_selective", 0) == 0:
        rep.warn(
            "no compounds labelled 'non_selective' -- these are the discriminating negatives; "
            "without them enrichment may be achievable on molecular weight alone (see risks R6)"
        )

    strategies = {r.get("decoy_strategy") for r in rows if r.get("is_decoy")}
    if "dude_style" in strategies and "property_matched" not in strategies:
        rep.warn("DUD-E style decoys only -- known to carry biases a 2D baseline can exploit")

    cocrystals = sum(1 for r in rows if r.get("has_cocrystal"))
    print(f"  {cocrystals} row(s) with a co-crystal -- the S1 fidelity contract validation set")
    if cocrystals == 0:
        rep.warn("no co-crystals: contract 1 (co-folding accuracy) cannot be validated")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"no such file: {path}")
        return 2

    schema = json.loads(SCHEMA.read_text())
    rep = Report()

    print(f"validating {path}")
    with path.open(newline="") as fh:
        rows = [check_row(r, i, schema, rep) for i, r in enumerate(csv.DictReader(fh), start=2)]

    if not rows:
        rep.error("manifest is empty")
        return rep.emit()

    check_semantics(rows, rep)
    return rep.emit()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
