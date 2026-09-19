# Pipeline architecture

## The shape of it

![The eight steps, what passes between them, and where the gates sit](figures/pipeline-isometric.svg)

![What each phase actually holds, and what is measured on it](figures/objects-of-study.svg)

Figures regenerate from [`tools/make_figures.py`](../../tools/make_figures.py). The protein space
they operate in is in [visualisation.md](visualisation.md).

## Design principle

**A staged funnel with monotonically increasing cost per candidate and monotonically decreasing
candidate count.** Every stage is permitted to be wrong in a characterised way; the next stage
exists to correct the errors the previous one is known to make. Expensive physics is never the
front door.

The second principle, which is what makes this "AI-intensive": **at four points a learned
surrogate stands in for something expensive.** Each such substitution must carry a
[fidelity contract](fidelity-contracts.md).

```
                          cost/candidate  ──────────────────────►
    candidate count  ◄──────────────────────

  S0  Benchmark & front-end filter        10^3–10^6      cheap       WP-A
       │  curated ligands, targets, decoys, harmonised labels
       ▼
  S1  Complex generation                  10^2–10^3      moderate    WP-B
       │  Boltz-2 / Chai-class co-folding  ⟨surrogate for crystallography⟩
       ▼
  S2  Pocket extraction                   10^2–10^3      trivial     WP-B
       │  crop 10 / 12 / 15 Å shell around ligand + key residues
       ▼
  S3  Ensemble generation                 10^2–10^3      moderate    WP-C
       │  static | short relaxation | learned ensemble  ⟨surrogate for MD⟩
       ▼
  S4  Ensemble reduction                  10^2–10^3      trivial     WP-C
       │  cluster → 1 / 3 / 5 representative microstates
       ▼
  S5  Equivariant pocket scoring          10^2–10^4      low         WP-D
       │  Nesso-1 class  ⟨surrogate for physics-based scoring⟩
       ├──► selectivity ranking
       └──► uncertainty list
       ▼
  S6  Selective quantum labelling         10^1–10^2      HIGH        WP-E
       │  cuEST DFT / ESP / partial charges  ⟨the label oracle⟩
       ▼
  S7  Feedback learning                   —              low         WP-D
       │  delta-learning / calibration; measure gain per expensive label
       └──► back to S5 with an improved scorer
```

Orchestration (**WP-F**) wraps all of it: Snakemake DAG, containers, MLflow, artifact layout.

## Stage pages

Each stage has its own page with inputs, outputs, parameters, metrics, failure modes, candidate
software and a first-day task. Owners maintain their own.

| Stage | Page | WP |
| --- | --- | --- |
| S0 | [Benchmark & front-end filter](stages/S0-benchmark.md) | A |
| S1 | [Complex generation](stages/S1-complex-generation.md) | B |
| S2 | [Pocket extraction](stages/S2-pocket-extraction.md) | B |
| S3 | [Ensemble generation](stages/S3-ensemble-generation.md) | C |
| S4 | [Ensemble reduction](stages/S4-ensemble-reduction.md) | C |
| S5 | [Equivariant scoring](stages/S5-equivariant-scoring.md) | D |
| S6 | [Quantum labelling](stages/S6-quantum-labelling.md) | E |
| S7 | [Feedback learning](stages/S7-feedback-learning.md) | D |
| — | [Orchestration](stages/S8-orchestration.md) | F |

## The surrogate cascade

This is the part that is genuinely different from a conventional structure-based workflow, and
the part most likely to fail quietly.

| # | Surrogate | Replaces | Speed-up class | Failure mode if unvalidated |
| --- | --- | --- | --- | --- |
| 1 | Co-folding (S1) | Experimental structure determination | ~∞ (enables the impossible) | Confident wrong poses; systematic bias toward training-set-like geometries |
| 2 | Learned ensembles (S3) | Molecular dynamics | 10²–10⁴× `[estimate]` | Ensembles that look plausible but miss the state that actually discriminates |
| 3 | Equivariant scorer (S5) | Physics-based rescoring | 10²–10³× `[estimate]` | Good at ranking binders, blind to *selectivity* — the exact failure we care about |
| 4 | Delta-learned correction (S7) | Running quantum on everything | 10³×+ | Corrections that interpolate within the labelled set and mislead outside it |

**Each of these is a place where the pipeline can be fast, confident and wrong.** The
countermeasure is not more validation in general; it is a specific, cheap, pre-agreed check per
surrogate. That is what [fidelity-contracts.md](fidelity-contracts.md) enumerates.

## Static vs. dynamic

The source doc frames three modes; we carry them as the single most important structural
parameter to perturb. `[source-doc]`

| Mode | Models | Pros | Cons | When |
| --- | --- | --- | --- | --- |
| **Static** | One or a few fixed complexes | Simple, fast, easy to benchmark | Misses relevant conformational states | Pilot baseline — always run this |
| **Dynamic ensemble** | Representative microstates over time | Realistic for induced fit and selectivity | Sampling is expensive | Flexible pockets, advanced selectivity work |
| **Dynamic surrogate** | Approximate ensemble, no full MD | Strong cost/quality compromise | Needs careful validation | Scaling ensemble-aware screening |

**Decision rule:** keep the cheapest mode that measurably improves ranking stability over static.
Move up only when static results are unstable or non-discriminative. `[source-doc]`

## Baselines we must beat

A funnel this elaborate has to justify itself against cheaper things. Three baselines, all owned
by WP-A/WP-D, all run on the identical manifest:

1. **2D baseline** — ECFP4 + gradient-boosted/RF classifier on the same labels. The honest
   control. If we don't beat this on selectivity ranking, nothing else matters.
2. **Static-3D baseline** — S1 → S2 → S5 with one pose, one crop radius, no ensembles, no quantum.
   Isolates the value of everything downstream of static scoring.
3. **Random-acquisition control** — S6 labels chosen at random rather than by uncertainty.
   Isolates whether *active* learning is doing work, or just *more* learning.

Baseline 3 is the one teams skip and the one that most often changes the conclusion.

## Execution pattern

Containerised, whole-GPU Snakemake jobs on Kubernetes HGX H200 — no additional distributed
machinery. `[source-doc]`

| Stage | Execution | Complexity | Note |
| --- | --- | --- | --- |
| S1 structure generation | One GPU job per target–ligand batch | Moderate | Record all inputs and versions |
| S3 ensemble generation | One GPU job per complex or batch | Moderate | Start with relaxation/surrogate, not long MD |
| S5 pocket scoring | GPU batch jobs | Low | Cheap relative to S3 and S6 |
| S6 quantum refinement | Independent GPU jobs, shortlisted cases | Moderate | High value when tightly scoped |
