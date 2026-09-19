# S0 — Benchmark & front-end filter

**Work package:** A · **Owner:** _unassigned_ · **Disciplines:** medicinal chemistry, pharmacology, cheminformatics, data stewardship

> Every other group runs from this manifest. If S0 slips, everything slips. It is the only stage
> with no upstream dependency, so it starts before the hackathon.

## Purpose

Produce **one canonical input table** — ligands, targets, structures, harmonised activity labels,
decoys, and splits — that every work package uses unchanged. Plus the honest 2D baseline.

## Inputs

- ChEMBL / BindingDB activity data for CDK9, CDK7, CDK12, CDK13
- PDB structures (apo and holo) for all four
- Literature-curated selective and pan-CDK compounds

## Outputs

| Artifact | Description |
| --- | --- |
| `manifest.csv` | One row per ligand–target pair. [Schema](../../../schemas/benchmark_manifest.schema.json) |
| `structures/` | Chosen PDB entries, cleaned, with a written cleaning protocol |
| `splits.json` | Scaffold-based train/val/test; leave-one-scaffold-out folds |
| `baseline_2d/` | ECFP4 + RF/GBM selectivity model, its metrics, and its code |
| `curation_notes.md` | Every judgement call, with a reason. This is the scientific audit trail |

## Sizing `[source-doc]`

| | Minimum viable | Preferred |
| --- | --- | --- |
| Targets | CDK9 + one counter-target | CDK9, CDK7, CDK12, CDK13 |
| Known ligands | 12–20 compounds | 50–100 |
| Activity labels | Binary active/inactive or selective/non-selective | pIC50 / Ki / Kd across targets |
| Decoys | 20–50 matched | 100–500 |
| Reference poses | Any co-crystals for a few ligands | Multiple ligand-bound structures |

## Parameters to perturb

Mostly *choices* rather than continuous knobs, but they belong in the sensitivity analysis:

| Parameter | Settings | What it changes |
| --- | --- | --- |
| Decoy strategy | property-matched · DUD-E style · literature non-selective | Whether "enrichment" is meaningful or trivially achievable |
| Selectivity definition | ratio threshold (10×, 30×, 100×) · continuous ΔpIC50 | Class balance and the metric's sensitivity |
| Assay harmonisation | strict (single assay type only) · permissive (pooled, with a correction) | Sample size vs. label noise |
| Split strategy | random · scaffold · time-based | How optimistic every downstream number is |

## Metrics

- Class balance and effective sample size per target pair
- Label noise estimate: variance across replicate/multi-source measurements for the same pair
- 2D baseline performance — the number everything else must beat
- Fraction of manifest ligands with a co-crystal (feeds the S1 fidelity contract)

## Failure modes

- **Selectivity ratios computed across incomparable assays.** Different ATP concentrations make
  kinase IC50s non-comparable. This is the single most likely way to produce a benchmark that
  rewards the wrong thing. (→ [C1](../../02-scope/open-questions.md))
- **Trivially separable decoys.** If decoys differ in molecular weight and logP, a 2D model gets
  0.95 AUC and the 3D pipeline has nothing left to demonstrate.
- **Activity cliffs treated as noise**, when they are exactly the discriminating cases.
- **Data leakage via scaffold.** Random splits on a congeneric series measure memorisation.

## Candidate software

RDKit · ChEMBL web services · Papyrus or an equivalent harmonised bioactivity set · PDBFixer /
OpenMM for structure prep · DeepCoy or property-matched decoy generation

## First-day task

Ship `manifest.csv` with 12 ligands × 2 targets, even if half the fields are provisional, and
make `tools/validate_manifest.py` pass on it. Every other WP is blocked until this exists.

## Fidelity contract

Not a surrogate stage — but it owes the equivalent: **a written statement of what the benchmark
can and cannot support.** With n≈20, it cannot support a claim about prospective performance. It
can support a claim about *relative* ranking between configurations. Write that down before
anyone sees a result.
