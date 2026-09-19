#!/usr/bin/env python3
"""Fetch CDK family sequences and compute the numbers behind the protein-space figure.

    python3 tools/fetch_protein_space.py        # needs network + biopython

Writes data/protein-space.json, which is committed, so tools/make_figures.py can
regenerate the figure offline and anyone can check the numbers without rerunning
the fetch.

Two measurements:

  whole-region identity   local alignment over the aligned kinase region. CDK12
                          and CDK13 carry long disordered tails, so a global
                          alignment would report nonsense.

  ATP-site identity       18 positions taken from the CDK2 ATP site and mapped
                          onto each sequence by global pairwise alignment.

CAVEAT worth keeping in mind: the site mapping is sequence-based. Structural
superposition would be better and may shift a position or two. Treat these as
indicative rather than definitive, and check against structures before anything
depends on them.
"""
from __future__ import annotations

import itertools
import json
import urllib.request
from pathlib import Path

try:
    from Bio import Align
except ImportError:
    raise SystemExit("needs biopython:  pip install biopython")

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "protein-space.json"
CACHE = ROOT / ".cache" / "seqs"

# The transcriptional CDKs we care about, plus enough of the cell-cycle family
# to show where they sit.
FAMILY = {
    "CDK1": "P06493", "CDK2": "P24941", "CDK4": "P11802", "CDK6": "Q00534",
    "CDK7": "P50613", "CDK8": "P49336", "CDK9": "P50750", "CDK12": "Q9NYV4",
    "CDK13": "Q14004", "CDK19": "Q9BWU1",
}
ORDER = list(FAMILY)

# CDK2 ATP-site positions, 1-based. Glycine-rich loop, beta-3 lysine, gatekeeper,
# hinge, catalytic loop, DFG.
SITE = {
    10: "β1", 11: "G-loop", 13: "G-loop", 18: "β2", 31: "β3", 33: "β3 Lys",
    64: "αC-β4", 80: "gatekeeper", 81: "hinge", 82: "hinge", 83: "hinge",
    84: "hinge", 86: "—", 89: "—", 131: "—", 132: "cat. Asn", 134: "—", 145: "DFG",
}
HINGE = [80, 81, 82, 83, 84]


def fetch(name: str, acc: str) -> str:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{name}.fasta"
    if not f.exists():
        url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
        with urllib.request.urlopen(url, timeout=30) as r:
            f.write_bytes(r.read())
    return "".join(l for l in f.read_text().splitlines() if not l.startswith(">"))


def main() -> None:
    seqs = {n: fetch(n, a) for n, a in FAMILY.items()}

    local = Align.PairwiseAligner(scoring="blastp"); local.mode = "local"
    glob = Align.PairwiseAligner(scoring="blastp"); glob.mode = "global"

    ident: dict[str, float] = {}
    for a, b in itertools.combinations(ORDER, 2):
        aln = local.align(seqs[a], seqs[b])[0]
        A, B = aln[0], aln[1]
        m = sum(1 for x, y in zip(A, B) if x == y and x != "-")
        n = sum(1 for x, y in zip(A, B) if x != "-" and y != "-")
        ident[f"{a}|{b}"] = ident[f"{b}|{a}"] = round(100 * m / n, 1) if n else 0.0

    ref, pos = seqs["CDK2"], sorted(SITE)
    site: dict[str, dict[str, str]] = {}
    for n in ORDER:
        if n == "CDK2":
            site[n] = {str(p): ref[p - 1] for p in pos}
            continue
        a = glob.align(ref, seqs[n])[0]
        out, ri = {}, 0
        for x, y in zip(a[0], a[1]):
            if x != "-":
                ri += 1
                if ri in SITE:
                    out[str(ri)] = y
        site[n] = out

    def pid(a: str, b: str, keys: list[int]) -> float:
        m = sum(1 for k in keys
                if site[a].get(str(k)) == site[b].get(str(k))
                and site[a].get(str(k)) not in ("-", None))
        return round(100 * m / len(keys), 1)

    site_id = {f"{a}|{b}": pid(a, b, pos) for a, b in itertools.combinations(ORDER, 2)}
    site_id.update({f"{b}|{a}": v for k, v in list(site_id.items())
                    for a, b in [k.split("|")]})
    hinge_id = {f"{a}|{b}": pid(a, b, HINGE) for a, b in itertools.combinations(ORDER, 2)}
    hinge_id.update({f"{b}|{a}": v for k, v in list(hinge_id.items())
                     for a, b in [k.split("|")]})

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "source": "UniProt, fetched by tools/fetch_protein_space.py",
        "caveat": ("ATP-site positions are mapped from CDK2 by sequence alignment, "
                   "not structural superposition. Indicative, not definitive."),
        "accessions": FAMILY, "order": ORDER,
        "site_positions": {str(k): v for k, v in SITE.items()},
        "hinge_positions": HINGE,
        "region_identity": ident, "site_identity": site_id,
        "hinge_identity": hinge_id, "site_residues": site,
    }, indent=1))
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  CDK9 region vs CDK7/12/13: "
          f"{ident['CDK9|CDK7']}, {ident['CDK9|CDK12']}, {ident['CDK9|CDK13']}")
    print(f"  CDK9 ATP site  vs CDK7/12/13: "
          f"{site_id['CDK9|CDK7']}, {site_id['CDK9|CDK12']}, {site_id['CDK9|CDK13']}")
    print(f"  CDK8 vs CDK19 at the ATP site: {site_id['CDK8|CDK19']}")


if __name__ == "__main__":
    main()
