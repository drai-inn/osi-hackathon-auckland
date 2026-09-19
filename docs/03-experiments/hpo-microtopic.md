# Microtopic — hyperparameter optimisation on small data, and which wins scale

**Status:** proposed research thread · **Cuts across:** every work package ·
**Primary adjacent activity:** [Activity 2](../04-hackathon/adjacent-activities.md#activity-2--small-data-hyperparameter-science)

> This is the thread that makes the project interesting to people who will never care about CDK9,
> and it is the one that decides whether "start small, scale up" is a strategy or a hope.

---

## The framing

**The pipeline is the model. Its configuration is the hyperparameter vector.**

Crop radius, pose count, dynamics mode, retained microstates, scorer capacity, graph cutoff,
quantum theory level, acquisition threshold — eight knobs, each with 2–3 candidate settings, each
costing GPU-hours to evaluate. That is structurally the same problem as tuning a neural network,
with two differences that matter:

1. Several of our knobs change the **problem**, not just the search — a 10 Å crop is a different
   physical system from a 15 Å crop, not a differently-optimised one.
2. Our evaluation metric is a **small-sample ranking statistic**, not a smooth loss. It is noisy,
   bounded, and non-differentiable in the parameters.

Whether the geometry results that hold for neural-network hyperparameters survive those two
differences is an open question, and it is worth a week of somebody's attention.

## What the literature gives us

From [Lourie et al. 2026](../00-context/source-notes/small-scale-experiments.md) `[literature]`:

- **Tuning budget dominates every other methodological choice.** 4 configs: no signal. 16: no
  signal. 64: visible but imprecise. 256: accurate.
- **Small scales are *more* hyperparameter-sensitive than large ones**, not less. This is the
  counterintuitive bit and the reason small-scale results are so often dismissed as unreliable —
  they were undertuned, not uninformative.
- **The mechanism is geometric**: as scale grows, the intrinsic dimension of the hyperparameter
  loss surface falls; the "effective number of hyperparameters" drops toward one, so good
  configurations fill more of the space and become easy to find.
- **The prescription**: explore thoroughly where it is cheap, then carry up with simple rules.

## The three questions for this project

### Q1 — Which pipeline parameters actually matter?

The immediately useful one. From a random search over the joint configuration, estimate marginal
and interaction effects on selectivity ranking.

**Method:** random search (≥64 configurations per stage against cached upstream — see
[methodology.md](methodology.md#2-search-stages-independently-integrate-once)), then functional
ANOVA / variance decomposition over the resulting score surface. Report each parameter's share of
explained variance with a bootstrap interval.

**Expected output:** a ranked list. Our prior, to be falsified: crop radius and dynamics mode
dominate; scorer capacity and batch size are near-noise. If that prior is right, it tells the
scale-up exactly where to spend.

### Q2 — Does sensitivity fall as scale rises? *(the headline)*

This is diagnostic D2, and it is the assumption the entire "start small" strategy rests on.

**Our scale axes are not theirs.** We have several, and they are not interchangeable:

| Axis | Small | Medium | Large |
| --- | --- | --- | --- |
| Benchmark size (ligands × targets) | 12 × 2 | 20 × 2 | 50 × 4 |
| Structural budget (poses × states) | 1 × 1 | 3 × 3 | 5 × 5 |
| Label budget | 10 | 30 | 100+ |
| Scorer capacity | low | medium | high |

**Method:** run the same random search at two or three tiers of one axis. Compare the score
distributions. If mass concentrates near the optimum as the tier rises — as it does with model
scale in the paper — then tuning at the small tier transfers, and we are entitled to the strategy.

**What each outcome means:**

| Result | Implication |
| --- | --- |
| Sensitivity falls with scale, as in the paper | Tune small, carry up. Strategy validated. Estimate γ and report it |
| Sensitivity is flat | Small-scale tuning still gives the *ranking* of important parameters but not settings. Carry the ranking, re-tune at scale |
| Sensitivity *rises* with scale | The strategy is wrong for this problem class. Say so. This is the most valuable negative result available to us |

Note which axis is most likely to behave like theirs: **scorer capacity**, because it is the
closest analogue to model parameters. The structural axes (crop radius, states) have no reason to
obey the same geometry and may well not — which is the interesting part.

### Q3 — Do the winners transfer across scale, or only the rankings?

The weaker, more robust version of Q2. Even if optimal *settings* shift with scale, the *ordering*
of parameter importance may be stable. That would still be enough to guide a scale-up: it tells
you what to re-tune and what to leave alone.

**Method:** compute the sensitivity ranking at each tier; measure rank correlation between tiers.
Rank stability is a much lower bar than setting stability, and much more likely to hold.

---

## Why other research leaders should care

Strip out the chemistry and this is a question every empirical discipline has:

> *I can afford a small experiment. Under what conditions does what I learn from it transfer to
> the scale I actually care about?*

Ecology with limited field seasons. Clinical research with small cohorts. Materials with slow
synthesis. Education with one cohort per year. Each has a pipeline of configurable choices, an
expensive evaluation, and no ability to grid-search.

The deliverable that travels is **a protocol and a small toolkit**: a shared search-space
specification format, a random-search driver, a variance-decomposition report, and the four
diagnostics. Nothing in it is chemistry-specific. It is a plausible methods contribution in its
own right, and it is the natural hook for statisticians and ML methodologists who would otherwise
have no reason to attend a drug-discovery hackathon.

## Deliverables

| # | Deliverable | Owner |
| --- | --- | --- |
| 1 | Shared search-space spec format, one file, used by all WPs | Methodology lead |
| 2 | Random-search driver + resumable run ledger | Methodology lead + WP-F |
| 3 | Variance-decomposition report with bootstrap intervals | Methodology lead |
| 4 | The four diagnostics, computed and written up | Methodology lead |
| 5 | Sensitivity ranking at two scale tiers + rank correlation | Methodology lead |
| 6 | Two-page transferable protocol note, discipline-agnostic | Methodology lead |

## Honest risks

- **We may not afford enough configurations for the noisy-quadratic diagnostic to be meaningful.**
  It needs enough samples to characterise a tail. Mitigate by concentrating the budget on the
  cheapest stage (S5 scoring), where hundreds of configurations are genuinely affordable, and
  accept weaker conclusions elsewhere.
- **The metric is noisy enough to swamp the signal.** With n≈20 ligands, between-configuration
  variance may be dominated by resampling variance. Mitigate: pair configurations on the same
  bootstrap resamples so comparisons are within-resample.
- **Stage separability may not hold**, making the per-stage sweeps a poor guide to the joint
  surface. Mitigate: the integrated run is the check, and disagreement is itself reportable.
- **Two scale tiers is thin** for any claim about a trend. Three would be better; three may not be
  affordable. State the limitation rather than over-reading two points.
