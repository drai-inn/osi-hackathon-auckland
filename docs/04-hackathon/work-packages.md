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
[the diagnostics and sensitivity analysis](../03-experiments/hpo-microtopic.md).

Total: **13–20 people**. Below ~10, drop WP-C (keep static + relaxation only, no surrogate arm)
before dropping anything else — it has the widest cost range and the weakest prior.

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
| A | [S0 Benchmark](../02-pipeline/stages/S0-benchmark.md) |
| B | [S1 Complex generation](../02-pipeline/stages/S1-complex-generation.md) · [S2 Pocket extraction](../02-pipeline/stages/S2-pocket-extraction.md) |
| C | [S3 Ensemble generation](../02-pipeline/stages/S3-ensemble-generation.md) · [S4 Ensemble reduction](../02-pipeline/stages/S4-ensemble-reduction.md) |
| D | [S5 Equivariant scoring](../02-pipeline/stages/S5-equivariant-scoring.md) · [S7 Feedback learning](../02-pipeline/stages/S7-feedback-learning.md) |
| E | [S6 Quantum labelling](../02-pipeline/stages/S6-quantum-labelling.md) |
| F | [S8 Orchestration](../02-pipeline/stages/S8-orchestration.md) |

## Day-1 obligations

Non-negotiable, because everything else depends on them. All by end of day 1:

| WP | Obligation |
| --- | --- |
| A | Manifest v1 validated and committed, even with provisional fields |
| B | **Measured** GPU-hours per complex, published |
| C | Static vs. relaxation contact persistence on 5 complexes |
| D | Off-the-shelf scorer run on static pockets + the MW/logP confound diagnostic |
| E | Quantum convergence check on 3–5 systems + **measured** GPU-hours per label. **No production labels** |
| F | `make smoke` green with stubs, before lunch |
| Methodology | Pre-registration pages collected from every WP |

Note that three of these are measurements that replace `[estimate]`s in the
[compute budget](../05-feasibility/compute-budget.md). **The day-1 close is a re-planning
meeting**, not a status update — run sizes get re-derived from real numbers.

## Anti-patterns to name out loud on day 1

- **Building end-to-end before interfaces are frozen.** The integration happens once, on day 4.
- **Generating production quantum labels before the convergence check.** The most expensive way to
  waste the week.
- **Reporting a point estimate.** See [metrics.md](../03-experiments/metrics.md).
- **Skipping the random-acquisition control** because it "obviously" won't win. It sometimes wins,
  and when it does that is the result.
- **Six people building six container stacks.** WP-F pre-builds base images before the event.
