# S7 — Feedback learning

**Work package:** D · **Owner:** _unassigned_ · **Disciplines:** machine learning, active learning, statistics

## Purpose

Use quantum labels to improve the cheap scorer, and — more importantly for the scoping question —
**measure the gain per expensive label** so we can say whether the enrichment strategy pays.
`[source-doc]`

## Inputs

`labels.parquet` from [S6](S6-quantum-labelling.md); current scorer from [S5](S5-equivariant-scoring.md).

## Outputs

Retrained or recalibrated scorer + `model_card.md`. See
[interfaces.md](../interfaces.md#s7--s5--improved-scorer).

## Parameters to perturb `[source-doc]`

| Parameter | Settings | Decision rule |
| --- | --- | --- |
| **Acquisition strategy** | uncertainty · top-ranked · random (control) | Best error reduction per label |
| **Acquisition threshold** | top 5% · 10% · 20% most uncertain | Strongest error reduction per label |
| Learning mode | delta/residual learning · fine-tuning · calibration-only | Delta learning is the default; calibration-only is the fallback if the scorer is not fine-tunable ([B3](../../02-scope/open-questions.md)) |
| Rounds | 1 · 2 · 3 | More rounds means fewer labels per round at a fixed budget |

## The design constraint nobody likes

With **20–50 labels total** `[source-doc]`, this stage is statistically fragile by construction.
Three consequences that must be designed in, not discovered:

1. **Reserve the random-acquisition holdout before the first label.** Carved out afterwards it is
   not a holdout. ≥20% of the budget.
2. **Report a confidence interval on "gain per label", not a point estimate.** Bootstrap over
   labels. The interval will be wide; that is the honest result and it is still decision-relevant
   — a wide interval that excludes zero is a green gate.
3. **Prefer calibration improvement over accuracy improvement as the primary readout.** Accuracy
   on 20 labels is noise; calibration curves use every prediction and move detectably.

An alternative worth considering if the label budget stays this tight: treat S7 as a
**pre-registered, powered comparison of two acquisition strategies** rather than an attempt to
actually improve the model. That is a cleaner question, answerable at this n, and it directly
serves the acquisition-value gate.

## Metrics

- **Error reduction per label**, uncertainty-guided vs. random control — the acquisition-value
  gate `[source-doc]`
- Calibration before vs. after (reliability diagram, ECE)
- Selectivity-ranking change on held-out compounds
- Fraction of the scored set falling outside the labelled neighbourhood — where the correction
  should not be trusted
- Cumulative GPU-hours per unit of error reduction

## Failure modes

- **Overfitting to 20–50 labels** and reporting the training-set improvement as a result
- Holdout constructed post hoc
- Comparing against a random control drawn from a different candidate pool than the uncertainty
  selection — the pools must be identical
- The correction extrapolating confidently outside the labelled neighbourhood; quantify and report
  the out-of-neighbourhood fraction
- Multiple testing across acquisition strategies × thresholds × rounds without correction. With
  this n, three comparisons is already a lot. Pre-specify which one is primary.

## Candidate software

scikit-learn / PyTorch · modAL or a hand-rolled acquisition loop (simpler and more auditable at
this scale) · MLflow for tracking

## First-day task

Write the pre-registered analysis plan: the primary comparison, the holdout, the bootstrap
procedure, and the threshold for calling the acquisition gate green. One page, agreed before any
label exists.

## Fidelity contract

See [contract 4](../fidelity-contracts.md#4-delta-learned-correction-s7--replaces-running-quantum-on-everything).
