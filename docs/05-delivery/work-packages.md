# Work packages

Six parallel packages on a shared manifest, then integration. Structure from the origin document
`[source-doc]`; owners, first-day tasks and dependencies added here.

**The design rule:** each package perturbs a limited parameter space against cached upstream
output, so packages do not block each other. Only settings that show stable signal are integrated.

---

## Summary

| WP | Focus | Parameter perturbations | Primary outputs | Success signal | People |
| --- | --- | --- | --- | --- | --- |
| **A** | Data curation & benchmarks | Target set, ligand set, decoy strategy, assay harmonisation | Canonical input table, structures, labels, splits | Every other group can run from the same manifest | 2–4 |
| **B** | Static structural baseline | Pose count 1/3/5; pocket radius 10/12/15 Å | Baseline ranking, pose quality, runtime table | Stable ranking, actives vs. decoys | 2–3 |
| **C** | Motion-aware sampling | Static vs. relaxation vs. surrogate; states 1/3/5 | Contact persistence, RMSD spread, stability metrics | Ensembles improve ranking stability or explain failures | 2–3 |
| **D** | Equivariant scoring | Model depth/order, graph cutoff, batch size | Score distributions, uncertainty, throughput | Uncertainty correlates with error | 2–3 |
| **E** | cuEST quantum labelling | Theory-level matrix, shell size, acquisition source | Label schema, convergence rate, cost per label | Labels discriminate selective from non-selective | 2–3 |
| **F** | Workflow & integration | Snakemake concurrency, GPU request shape, artifact layout | Runnable DAG, MLflow logging, reproducibility report | One-command repeatable mini-pipeline | 2–3 |

Plus a **methodology lead** (1 person, cross-cutting) owning
[the diagnostics and sensitivity analysis](../04-experiments/hpo-microtopic.md).

Total: **13–20 people**. Below ~10, drop WP-C's surrogate arm (keep static + relaxation) before
dropping anything else — widest cost range, weakest prior, heaviest install burden.

**Each package also needs a named *host*, who is not the owner** — responsible for the newcomers
attached to that package. In a two-day sprint the owner will choose the technical work every time.
See [engagement.md](../00-event/engagement.md#the-structural-fix-split-the-host-role).

---

## Dependencies

```
A ──────┬──► B ──► C ──► D ──► E ──► (integration)
        │         ▲      ▲      │
        └─────────┴──────┴──────┘
                  cached upstream

F ──► everything (stubs day 1, real DAG day 2+)
Methodology lead ──► reads all, writes the sensitivity analysis
```

**A blocks everything and therefore starts before the hackathon.** F must ship stubs on day 1 so
that B–E can develop against a working interface rather than against each other's availability.

## Per-package detail

Each package maps to stage pages, which carry the real content:

| WP | Stage pages |
| --- | --- |
| A | [S0 Benchmark](../03-pipeline/stages/S0-benchmark.md) |
| B | [S1 Complex generation](../03-pipeline/stages/S1-complex-generation.md) · [S2 Pocket extraction](../03-pipeline/stages/S2-pocket-extraction.md) |
| C | [S3 Ensemble generation](../03-pipeline/stages/S3-ensemble-generation.md) · [S4 Ensemble reduction](../03-pipeline/stages/S4-ensemble-reduction.md) |
| D | [S5 Equivariant scoring](../03-pipeline/stages/S5-equivariant-scoring.md) · [S7 Feedback learning](../03-pipeline/stages/S7-feedback-learning.md) |
| E | [S6 Quantum labelling](../03-pipeline/stages/S6-quantum-labelling.md) |
| F | [S8 Orchestration](../03-pipeline/stages/S8-orchestration.md) |

## These were day-1 obligations. Now they are month obligations.

The event is **two days**. Everything below must be true *before* 19 Oct, not on it. Dates from
[critical-path.md](critical-path.md).

| WP | Obligation | By |
| --- | --- | --- |
| F | Architecture spike answered: what builds for `aarch64` and `x86_64` | **Fri 25 Sep** |
| E | cuEST availability resolved, or the fallback decided | **Fri 25 Sep** |
| A | Manifest v1 frozen and validated | **Fri 2 Oct** |
| F | `make smoke` green on GB10; multi-arch images published | **Fri 2 Oct** |
| B | **Measured** GPU-hours per complex, on both architectures | Fri 2 Oct |
| A | 2D baseline computed — the number everything is measured against | Fri 2 Oct |
| C | Static vs. relaxation contact persistence on 5 complexes | Fri 9 Oct |
| D | Scorer running with uncertainty + the MW/logP confound diagnostic | Fri 9 Oct |
| E | **Quantum convergence study on H200** + **measured** GPU-hours per label | **Fri 9 Oct** |
| F | Live dashboard showing runs by name | Fri 9 Oct |
| F | Pre-computation campaign complete | **Fri 16 Oct** |
| Hosts | Novice dry run: first result in under 30 minutes | **Fri 16 Oct** |
| Methodology | Pre-registration pages, one per package | Fri 16 Oct |

Several of these are measurements that replace `[estimate]`s in the
[compute budget](../06-feasibility/compute-budget.md). The **Friday gate meetings** are where run
sizes get re-derived from real numbers — not a status update.

## Event-day obligations

What each package actually does in the room, now that the build is behind us:

| WP | Day 1 | Day 2 |
| --- | --- | --- |
| A | Host [break-the-benchmark](../00-event/engagement.md#c--break-the-benchmark--medicinal-chemistry-pharmacology--60-min); fold findings into the manifest | Benchmark limitations section of the handoff |
| B | Host [pose triage](../00-event/engagement.md#b--pose-triage--structural-biology-medicinal-chemistry--zero-code); collect human pose labels | Close fidelity contract 1 with real human ground truth |
| C | Mode comparison sweeps | Motion-value gate evidence |
| D | Scoring sweeps; uncertainty and acquisition | Acquisition-value gate; feedback round |
| E | Production labels from the acquisition list | Quantum-value gate |
| F | Keep the DAG and dashboard alive; burn-down board | Integrated run; handoff package |
| Methodology | Collect score distributions; first sensitivity ranking | Diagnostics, intervals, gate report |

## Anti-patterns to name out loud on day 1

- **Building end-to-end before interfaces are frozen.** Integration happens once, on day 2.
- **Treating the month as optional.** Two days cannot absorb a build.
- **Generating production quantum labels before the convergence check.** The most expensive way to
  waste the week.
- **Reporting a point estimate.** See [metrics.md](../04-experiments/metrics.md).
- **Skipping the random-acquisition control** because it "obviously" won't win. It sometimes wins,
  and when it does that is the result.
- **Six people building six container stacks.** WP-F pre-builds base images before the event.
