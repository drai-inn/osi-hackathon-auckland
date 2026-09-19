# Metrics

Four categories, following the origin document's structure, with the statistical treatment this
repo adds. `[source-doc]` unless noted.

**Every metric reported with a bootstrap 95% interval over ligands.** A metric without an interval
at n≈20 is not a result. This is stated once here and assumed everywhere.

---

## 1. Biological usefulness

| Metric | Definition | Why | Owner |
| --- | --- | --- | --- |
| **Selectivity** | Differential target vs. off-target score | The primary objective | WP-D |
| Selectivity Spearman ρ | Rank correlation between predicted and experimental selectivity ratio | The headline number | WP-D |
| Enrichment | Known-selective ranked above known-non-selective, vs. baseline | Decision-relevant framing | WP-A/D |
| Baseline deltas | The above, minus the 2D and static-3D baselines | Nothing is reportable in absolute terms | WP-A |

**The confound diagnostic**, and it belongs in this table: correlation between predicted Δscore
and simple ligand properties (MW, logP, HBD). If Δscore is predictable from MW alone, the pipeline
is an expensive property calculator. Cheap to compute, and it can invalidate everything above.

## 2. Physical fidelity

| Metric | Definition | Why | Owner |
| --- | --- | --- | --- |
| **Pose quality** | Stability of representative poses across ensemble states | Distinguishes brittle from robust binders | WP-B/C |
| **Pocket interaction fidelity** | Hydrogen-bond persistence, key-contact retention | Tracks mechanistic plausibility | WP-C |
| Ligand-RMSD to crystal | On the co-crystal subset, held-out where possible | The S1 fidelity contract | WP-B |
| **Quantum consistency** | Convergence rate; sensitivity of electronic features to theory level and shell size | Ensures quantum labels are a ground truth at all | WP-E |

Quantum consistency gates the others. See [S6](../02-pipeline/stages/S6-quantum-labelling.md#the-convergence-check-comes-first).

## 3. Model behaviour

| Metric | Definition | Why | Owner |
| --- | --- | --- | --- |
| **Model calibration** | Predicted uncertainty vs. actual residual error | Determines whether active learning is meaningful at all | WP-D |
| **Sample efficiency** | Gain per expensive label added | Shows whether enrichment is paying off | WP-D |
| Acquisition advantage | Error reduction per label, uncertainty vs. random control | The acquisition-value gate | WP-D |
| Ranking stability | Rank correlation across seeds, states, and configurations | Distinguishes signal from run-to-run noise | WP-C/D |
| Out-of-neighbourhood fraction | Share of scored candidates outside the labelled region | Where the correction should not be trusted | WP-D |

## 4. Operational cost

| Metric | Definition | Why | Owner |
| --- | --- | --- | --- |
| **GPU time per validated hit / per informative label** | The efficiency denominator | Determines scale-up viability | WP-F |
| GPU-seconds per item per stage | Telemetry from every run | Replaces every `[estimate]` in the budget | WP-F |
| Stage failure rate | Fraction of jobs needing intervention | Predictability for scheduling | WP-F |
| Queue-to-compute ratio | Wait time vs. run time | If queueing dominates, size is the wrong lever | WP-F |

---

## Statistical protocol

- **Unit of independence is the ligand.** Bootstrap over ligands, never over poses or states —
  states from one pose are not independent samples.
- **1,000 resamples**, 95% percentile intervals.
- **Paired comparisons** between configurations use the same resamples, so the interval is on the
  *difference*, which is much tighter than the difference of two intervals.
- **Permutation tests** for "beats baseline", not parametric tests. Ranking statistics on n=20 are
  not normal.
- **Pre-specify one primary metric per work package.** Everything else is exploratory and labelled
  as such in the write-up.
- **Report the interval even when it is embarrassing.** A wide interval is the finding when the
  finding is that the run was too small — and that is exactly the information a scoping exercise
  is supposed to produce.

## What we are not measuring, and why

- **Absolute binding affinity accuracy.** Different question, needs FEP-class methods, out of scope.
- **Prospective hit rate.** Requires wet-lab validation, out of scope.
- **Anything requiring more than ~20 ligands to detect.** If an effect needs n=200, we cannot see
  it this week; note it as a Phase-3 question rather than reporting a null.
