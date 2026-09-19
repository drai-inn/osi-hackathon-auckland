#!/usr/bin/env python3
"""Estimate GPU-hours for a run tier from per-unit costs.

    python3 tools/compute_budget.py                    # all tiers
    python3 tools/compute_budget.py hackathon_minimum  # one tier
    python3 tools/compute_budget.py --costs measured_costs.json

EVERY DEFAULT COST BELOW IS A GUESS. They are order-of-magnitude placeholders chosen to make
the arithmetic visible, not predictions. Day 1 of the hackathon exists partly to replace them:
each work package measures its real per-item cost, WP-F writes them to a JSON file, and the run
sizes get re-derived at the day-1 close.

    python3 tools/compute_budget.py --costs artifacts/measured_costs.json

Cost file format: {"s1_complex": 0.12, "s6_label_light": 3.4, ...} -- any subset of the keys
in COSTS below.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# --- Assumptions to attack -------------------------------------------------------------------
# GPU-hours per unit of work. [estimate] unless a measured file overrides.
COSTS: dict[str, float] = {
    "s1_complex": 0.05,          # one co-folded target-ligand complex
    "s2_crop": 0.0,              # CPU-bound, negligible
    "s3_relaxation": 0.10,       # short relaxation, one complex
    "s3_surrogate": 0.05,        # surrogate ensemble, one complex
    "s3_reference_md": 4.0,      # validation-only reference MD, one complex
    "s4_cluster": 0.0,           # CPU-bound
    "s5_score": 0.001,           # one scored pocket graph
    "s6_label_light": 0.5,       # one quantum label, lightweight theory  <-- THE critical number
    "s6_label_reference": 4.0,   # one quantum label, reference theory
    "s7_retrain": 0.25,          # one scorer retraining round
}

# Cluster assumption: 8x H200, ~20 usable GPU-hours per card per day after queueing and failures.
GPU_HOURS_PER_DAY = 8 * 20

# Multiplier for failures, reruns and unplanned exploration. Historically optimistic at 1.6.
OVERHEAD = 1.6

# --- Run tiers, from the origin document ------------------------------------------------------
TIERS: dict[str, dict] = {
    "tiny_smoke_test": dict(
        ligands=5, targets=2, poses=1, states=1,
        labels_light=5, labels_reference=2, ref_md=1,
        search_configs=20, retrain_rounds=1, relaxation_arm=False,
    ),
    "hackathon_minimum": dict(
        ligands=20, targets=2, poses=3, states=3,
        labels_light=40, labels_reference=10, ref_md=5,
        search_configs=200, retrain_rounds=10, relaxation_arm=True,
    ),
    "useful_pilot": dict(
        ligands=100, targets=4, poses=3, states=3,
        labels_light=450, labels_reference=50, ref_md=20,
        # Fewer configs than the hackathon tier, deliberately: the thesis of ADR-0003 is that
        # you search thoroughly where it is cheap and carry the winners up.
        search_configs=64, retrain_rounds=20, relaxation_arm=True,
    ),
    "scale_up": dict(
        ligands=2000, targets=4, poses=3, states=3,
        labels_light=5000, labels_reference=100, ref_md=50,
        search_configs=8, retrain_rounds=30, relaxation_arm=False,
    ),
}


def estimate(tier: dict, costs: dict[str, float]) -> list[tuple[str, int, float, float]]:
    """Return [(stage label, volume, unit cost, total GPU-hours)]."""
    complexes = tier["ligands"] * tier["targets"] * tier["poses"]
    graphs = complexes * tier["states"]

    lines: list[tuple[str, int, float, float]] = [
        ("S1 complex generation", complexes, costs["s1_complex"], complexes * costs["s1_complex"]),
        ("S3 surrogate ensembles", complexes, costs["s3_surrogate"], complexes * costs["s3_surrogate"]),
    ]
    if tier["relaxation_arm"]:
        lines.append(
            ("S3 relaxation (comparison arm)", complexes, costs["s3_relaxation"],
             complexes * costs["s3_relaxation"])
        )
    lines += [
        ("S3 reference MD (validation)", tier["ref_md"], costs["s3_reference_md"],
         tier["ref_md"] * costs["s3_reference_md"]),
        ("S5 scoring (single pass)", graphs, costs["s5_score"], graphs * costs["s5_score"]),
        ("S5 random search", graphs * tier["search_configs"], costs["s5_score"],
         graphs * tier["search_configs"] * costs["s5_score"]),
        ("S6 labels (lightweight)", tier["labels_light"], costs["s6_label_light"],
         tier["labels_light"] * costs["s6_label_light"]),
        ("S6 labels (reference/convergence)", tier["labels_reference"], costs["s6_label_reference"],
         tier["labels_reference"] * costs["s6_label_reference"]),
        ("S7 retraining", tier["retrain_rounds"], costs["s7_retrain"],
         tier["retrain_rounds"] * costs["s7_retrain"]),
    ]
    return lines


def report(name: str, tier: dict, costs: dict[str, float]) -> None:
    lines = estimate(tier, costs)
    subtotal = sum(total for *_, total in lines)
    with_overhead = subtotal * OVERHEAD

    complexes = tier["ligands"] * tier["targets"] * tier["poses"]
    print(f"\n{'=' * 74}")
    print(f"{name}")
    print(f"{tier['ligands']} ligands x {tier['targets']} targets x {tier['poses']} poses "
          f"= {complexes} complexes; {tier['states']} states; "
          f"{tier['labels_light'] + tier['labels_reference']} labels")
    print("=" * 74)
    print(f"{'stage':<36}{'volume':>10}{'GPU-h/unit':>13}{'GPU-h':>12}")
    print("-" * 74)
    for label, volume, unit, total in lines:
        if total < 0.05 and volume:
            print(f"{label:<36}{volume:>10}{unit:>13.4f}{'~0':>12}")
        else:
            print(f"{label:<36}{volume:>10}{unit:>13.4f}{total:>12.1f}")
    print("-" * 74)
    print(f"{'subtotal':<36}{'':>10}{'':>13}{subtotal:>12.1f}")
    print(f"{f'with {OVERHEAD}x overhead':<36}{'':>10}{'':>13}{with_overhead:>12.1f}")
    print(f"{'days on 8x H200':<36}{'':>10}{'':>13}{with_overhead / GPU_HOURS_PER_DAY:>12.1f}")

    # Where the money goes, and whether the dominant line is the one we intended.
    biggest = max(lines, key=lambda r: r[3])
    share = biggest[3] / subtotal * 100 if subtotal else 0
    print(f"\ndominant line: {biggest[0]} ({share:.0f}% of subtotal)")
    quantum = sum(t for label, _, _, t in lines if label.startswith("S6"))
    if subtotal and quantum / subtotal > 0.5:
        print("WARNING: quantum labelling is over half the budget. Re-check s6_label_light -- "
              "if it is 10x the estimate, this tier is not affordable (see risks R4).")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tier", nargs="?", choices=list(TIERS), help="one tier (default: all)")
    ap.add_argument("--costs", type=Path, help="JSON file of measured per-unit GPU-hours")
    args = ap.parse_args(argv[1:])

    costs = dict(COSTS)
    if args.costs:
        measured = json.loads(args.costs.read_text())
        unknown = set(measured) - set(COSTS)
        if unknown:
            print(f"unknown cost keys ignored: {', '.join(sorted(unknown))}", file=sys.stderr)
        costs.update({k: v for k, v in measured.items() if k in COSTS})
        print(f"using measured costs from {args.costs} "
              f"({len(set(measured) & set(COSTS))} of {len(COSTS)} keys overridden)")
    else:
        print("using DEFAULT costs -- every figure below is [estimate]. "
              "Replace with measurements on day 1 (see docs/06-feasibility/compute-budget.md).")

    for name in ([args.tier] if args.tier else TIERS):
        report(name, TIERS[name], costs)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
