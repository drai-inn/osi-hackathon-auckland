# Scope

## Objective

Determine, with evidence, whether a 3D chemistry-aware multi-fidelity surrogate pipeline
produces **better paralog-selectivity discrimination per unit of compute** than a 2D or
static-3D baseline — and establish which stages and settings are responsible.

Two deliverables, weighted equally:

1. **A scoping answer.** Each stage understood, costed and optimised; one integrated small-scale
   run; a go/no-go recommendation against explicit [gates](../05-feasibility/stage-gates.md).
2. **A capability and a community.** A reusable benchmark, a reproducible workflow, and a
   cross-disciplinary group at UoA who have actually worked together on it.

## Driving case

**CDK9 selectivity against CDK7 / CDK12 / CDK13.** Chosen because: closely related ATP sites make
it a genuine discrimination problem; public structural and activity data exist for all four; and
selectivity failure in this family has real therapeutic-window consequences, so the question is
not academic. Alternatives considered in [ADR-0002](../adr/0002-cdk9-selectivity-as-driving-case.md).

**Minimum viable target set:** CDK9 + one close counter-target. **Preferred:** all four. `[source-doc]`

## In scope

| | |
| --- | --- |
| **Stages** | Complex generation → pocket crop → ensemble generation → ensemble reduction → equivariant scoring → selective quantum labelling → feedback learning → orchestration |
| **Scale** | 12–20 ligands × 2–4 targets × 3 poses/states; 20–50 quantum labels `[source-doc]` |
| **Compute** | GPU jobs on the available HGX H200 Kubernetes cluster; whole-GPU, containerised, Snakemake-orchestrated |
| **Methodology** | Random search over the joint pipeline configuration; sensitivity analysis; the four diagnostics; cost-per-informative-label accounting |
| **Outputs** | Benchmark manifest, per-stage cost/quality tables, sensitivity ranking, one reproducible end-to-end run, gate assessment |

## Out of scope (for the hackathon)

Explicitly, so nobody spends a day on them:

- **Long MD.** Short relaxation and surrogate ensembles only. `[source-doc]`
- **Free-energy methods (FEP/TI).** Different cost class, different question.
- **Large theory-level grids for quantum.** Two lightweight settings plus one reference on a tiny
  subset. `[source-doc]`
- **Full architecture search on the scorer.** Low/medium/high capacity only. `[source-doc]`
- **Generative molecule design.** We are scoring and ranking a fixed set, not proposing new ones.
- **Prospective validation / compound purchase.** No wet-lab commitment arises from this.
- **Extrapolating scaling laws to production scale.** See caveat 3 in the
  [methodology source note](../00-context/source-notes/small-scale-experiments.md).
- **Anything requiring a new distributed-systems layer.** If Snakemake + containers is not
  enough, the answer is a smaller run, not more infrastructure.

## Deliberate non-goals

- **Beating a specialist docking/scoring package on a public benchmark.** We are measuring
  *marginal value of added fidelity*, not entering a leaderboard.
- **Picking winning models.** Boltz-2, Nesso-1, MACE, cuEST occupy roles. The roles are the
  design; the occupants are replaceable and should be treated as such.

## Phasing

| Phase | Content | Gate to pass |
| --- | --- | --- |
| **0 — Scoping** *(now)* | This repo. Benchmark defined, interfaces frozen, compute confirmed, team assembled | Manifest v1 agreed; every stage has a named owner |
| **1 — Hackathon** | Six work packages in parallel on a shared manifest, then one integrated run | Technical reproducibility + ranking signal |
| **2 — Motion & quantum value** | Does motion-awareness help? Does uncertainty-guided labelling beat random? | Motion value + quantum value + acquisition value |
| **3 — Useful pilot** | 50–100 ligands × 4 targets; 200–1,000 labels `[source-doc]` | Operational cost predictable |
| **4 — Scale-up** | 1k–10k candidates post-filtering | All gates green |

Phases 2+ are conditional. Phase 1 is designed so that a negative result is still a good outcome:
knowing that motion-awareness does *not* pay for itself on this target class is worth the week.

## Assumptions this scope rests on

Each is tracked in [open-questions.md](open-questions.md) with an owner and a resolve-by date.

- 8× H200 (or equivalent) available for a contiguous multi-day block `[source-doc, unconfirmed]`
- cuEST usable on that cluster — licensing, container, and driver stack `[unconfirmed]`
- Public data suffices for a defensible benchmark (ChEMBL/BindingDB + PDB) `[likely]`
- A cross-disciplinary team of roughly 10–18 can be assembled `[unconfirmed]`
