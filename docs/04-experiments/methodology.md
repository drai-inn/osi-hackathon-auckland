# Experimental methodology

How we run experiments so that the results mean something at n≈20 and a few hundred GPU-hours.

Adapted from [Lourie et al. 2026](../01-context/source-notes/small-scale-experiments.md), with
the transfer caveats stated there taken seriously rather than waved through.

---

## The four commitments

### 1. Random search, not grids

The parameter space has ~8 dimensions
([parameter-space.md](parameter-space.md)). A 3-level grid over 8 dimensions is 6,561 runs; a grid
over the 3 "important" ones is 27 runs that tell you nothing about the other 5.

**Random search over the joint configuration**, log-uniform where the parameter is a scale,
uniform over the discrete settings otherwise. Random search gives marginal sensitivity estimates
for *every* parameter from the same budget, which is precisely what we need to answer "where are
the big wins".

Lourie et al. found the structure they were looking for was invisible at 4 and 16 configurations,
clear at 64, accurate at 256. `[literature]` We will not afford 256 full-pipeline runs — which is
why stages are searched independently first (below).

### 2. Search stages independently, integrate once

The whole point of the parallel work-package design. Each stage can be swept densely in isolation
because the upstream can be cached:

- Run S1–S2 once at a few settings → cache the complexes and pockets
- WP-C sweeps S3–S4 against the cache; WP-D sweeps S5 against the cache
- Only the surviving settings are combined into the integrated run

This converts a multiplicative cost into an additive one. It also assumes stage effects are
approximately separable — **which is an assumption, and a checkable one**: the integrated run
should land near where the per-stage sweeps predict. If it doesn't, interactions matter, and
that is itself a headline finding.

The known interaction to watch: S2 crop radius × S5 graph cutoff, and S4 state count ×
S6 label budget. Sweep those pairs jointly.

### 3. Every number gets an interval

At n≈20 ligands, a Spearman ρ has a standard error around ±0.2. A difference of 0.05 between two
configurations is nothing.

- **Bootstrap over ligands** (not over poses or states — the ligand is the unit of independence)
  for every ranking metric, 1,000 resamples, report the 95% interval.
- **Permutation test** for "is this better than baseline", not a t-test.
- **Pre-specify the primary comparison** per work package. Everything else is exploratory and
  labelled as such.

This is not statistical fussiness. With this sample size, the difference between a finding and a
plausible story is entirely in whether the interval was computed.

### 4. Diagnostics over extrapolation

We do **not** fit a curve and extrapolate to production scale. The metric is a small-sample
ranking statistic and the scales span at most two orders of magnitude; Lourie et al. show that
extrapolation mostly compares estimates of irreducible error, which are unstable. `[literature]`

Instead, four diagnostics, each a question with an instrument. They are adapted from the paper's
case study and restated for this pipeline.

| # | Question | Instrument | Owner |
| --- | --- | --- | --- |
| **D1** | Have we searched thoroughly enough? | Does the distribution of scores over random-search configurations approach the **noisy quadratic limit**? A short tail means we haven't found the optimum's neighbourhood | Methodology lead |
| **D2** | Will scaling up be easy? | Does the score distribution concentrate as we move up a size tier (12→20→50 ligands, 20→50→200 labels)? Concentration ⇒ tune small, carry up | Methodology lead |
| **D3** | Does the cheap proxy track what we care about? | Correlation between a cheap held-out metric and the expensive selectivity-enrichment metric, **across configurations** — our analogue of perplexity–capability | WP-D |
| **D4** | Does the regularity hold out of sample? | Fit sensitivity rankings on the small tier, validate the ordering on the next tier up | Methodology lead |

**A failed diagnostic is a result.** If D2 fails — sensitivity does *not* fall with scale — then
the "start small, scale up" strategy lacks its justification for this problem class, and we should
say so loudly. That is a genuinely useful thing to learn in a week, and it is more publishable
than a marginal enrichment improvement.

---

## Run protocol

```
1. Freeze manifest v1 and interfaces.                          (pre-hackathon)
2. `make smoke` green with stubs.                              (day 1 AM)
3. Each WP measures real per-item cost at one setting.         (day 1)
   → replace every [estimate] in compute-budget.md
4. Re-plan run sizes from measured costs.                      (day 1 PM — a real decision point)
5. Per-stage random search against cached upstream.            (days 2–3)
6. Sensitivity analysis; select surviving settings.            (day 3)
7. Integrated run at the selected configuration + baselines.   (day 4)
8. Gate assessment and write-up.                               (day 5)
```

Step 4 is the one people skip. The plan is built on estimates; the measurements will differ, some
by a lot; the run sizes must be re-derived rather than defended.

## Recording

Every run writes a [run record](../../schemas/run_record.schema.json): config, config hash,
git sha, image digests, GPU-seconds per stage, metrics, and the interval on each metric. To
MLflow *and* to disk.

An experiment that is not in the record did not happen. This is how day 5 produces a write-up
instead of an archaeology exercise.

## Pre-registration

One page per work package, before results exist: the primary question, the primary metric, the
comparison, the threshold. Cheap, and it converts "we found that..." into a claim with a
denominator. (→ [D5](../02-scope/open-questions.md))
