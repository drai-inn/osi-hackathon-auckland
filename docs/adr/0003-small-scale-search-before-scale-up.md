# ADR-0003 — Thorough small-scale search before any scale-up

**Status:** accepted · **Date:** 2026-09-19 · **Deciders:** Nick Jones

## Context

The default instinct with a new pipeline is to build it end-to-end at a plausible scale and see
what happens. That produces one point in an eight-dimensional configuration space, at high cost,
with no way to know whether a different configuration would have worked much better — or whether
the result would survive at a larger scale.

[Lourie et al. (2026)](../00-context/source-notes/small-scale-experiments.md) argue this is the
central methodological error in small-scale ML experimentation: results are dismissed as
"unreliable at small scale" when they were simply undertuned. Their evidence: the regularity they
sought was invisible at 4 and 16 configurations, clear at 64, accurate at 256. `[literature]`

## Decision

**No end-to-end mega-run.** Instead:

1. Split into parallel work packages, each perturbing a limited parameter space against cached
   upstream output.
2. **Random search, not grids.**
3. Integrate only settings showing stable signal.
4. Treat the configuration space as the object of study, not as settings to be guessed
   ([microtopic](../03-experiments/hpo-microtopic.md)).
5. Diagnostics over extrapolation. We do **not** fit scaling curves and project to production.

This also commits us to testing whether the underlying assumption holds here — whether
hyperparameter sensitivity falls as scale rises in *this* pipeline, as it does with model scale in
theirs. That is diagnostic D2 and it is a headline deliverable.

## Alternatives considered

| Option | Why not |
| --- | --- |
| One end-to-end run at plausible settings | One sample from an 8-D space; no sensitivity information; cannot distinguish a bad method from a bad configuration |
| Grid search over "the important" parameters | Requires knowing which are important — the thing we are trying to find out. And grids are infeasible above ~3 dimensions |
| Bayesian optimisation | Better sample efficiency for *finding an optimum*; worse for *characterising the surface*, which is what we want. Reconsider for Phase 3 |

## Consequences

**Good:** sensitivity information for every parameter from one budget. Packages proceed in
parallel. A negative result is localisable. Produces a transferable methodological contribution.

**Bad:** assumes stage effects are approximately separable (→ [R11](../05-feasibility/risks.md)).
Needs a methodology lead and real statistical discipline. No single impressive end-to-end demo
until day 4.

**Revisit if:** the integrated run lands far from where per-stage sweeps predicted — separability
has failed and the strategy needs rethinking. Report that rather than patching around it.
