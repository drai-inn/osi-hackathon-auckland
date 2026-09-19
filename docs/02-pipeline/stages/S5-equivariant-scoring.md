# S5 — Equivariant pocket scoring

**Work package:** D · **Owner:** _unassigned_ · **Disciplines:** machine learning, geometric deep learning, computational chemistry

> The throughput workhorse, and the stage that produces both of the pipeline's primary outputs:
> the selectivity ranking, and the uncertainty list that decides where expensive labels go.

## Purpose

Score pocket–ligand microstates with a 3D equivariant model operating on the cropped local graph.
Produce (a) a selectivity-relevant ranking and (b) calibrated uncertainty.

## Inputs

Microstates from [S4](S4-ensemble-reduction.md), or S2 pockets directly in static mode.

## Outputs

`scores.parquet` and `acquisition.csv`. See
[interfaces.md](../interfaces.md#s5--s6--scores-and-the-uncertainty-list).

## Parameters to perturb `[source-doc]`

| Parameter | Settings | Decision rule |
| --- | --- | --- |
| **Model capacity** | low · medium · high | Lowest capacity retaining ranking and uncertainty quality |
| Graph cutoff | 4.0, 5.0, 6.0 Å | Interacts with S2 crop radius — sweep jointly, not independently |
| Batch size | throughput-driven | Not a quality parameter; tune for GPU utilisation only |
| Uncertainty method | deep ensemble (n=3–5) · MC dropout · evidential | Ensembles are the reliable default and cost n× inference |
| Ensemble aggregation | weighted mean · Boltzmann-weighted · min over states | This is a modelling choice, not a detail — it changes what "the score" means |

No full architecture search. `[source-doc]`

## Metrics

- **Spearman ρ on the selectivity ratio** — the primary number, not absolute affinity correlation
- Enrichment of known-selective over known-non-selective compounds
- **Calibration**: predicted uncertainty vs. actual residual. Report a reliability diagram, not
  just a correlation
- Score distribution shape across random-search configurations — the input to the noisy-quadratic
  diagnostic in [hpo-microtopic.md](../../03-experiments/hpo-microtopic.md)
- Throughput: scored graphs per GPU-hour

## The selectivity-vs-affinity trap

A scorer trained on binding affinity can rank binders well and be **useless for selectivity**,
because both CDK9 and CDK7 scores shift together with ligand size and lipophilicity. The
differential cancels the signal we want.

Consequences for this stage:
- Evaluate on **Δscore between targets**, never on per-target score alone.
- Consider training or calibrating directly on the differential.
- Include a diagnostic: correlation between Δscore and simple ligand properties (MW, logP, HBD).
  If Δscore is predictable from MW alone, the 3D machinery is not contributing.

That last diagnostic is three lines of pandas and could save the project from a false positive.

## Failure modes

- Ranking binders well while being blind to selectivity (above)
- **Uncertainty that is uninformative**, making the acquisition strategy equivalent to random —
  which the random-acquisition control will expose, so run it
- Distribution shift: trained on crystal structures, applied to co-folded predictions with
  different geometric statistics
- Leakage through scaffold overlap between the model's training data and our manifest. Check
  whether manifest ligands appear in the scorer's training set; report the overlap

## Candidate software

Nesso-1 (availability → [B3](../../01-scope/open-questions.md)) · e3nn / MACE-style equivariant
GNNs as an in-house fallback · TorchMD-Net

## First-day task

Score the S2 static pockets with the off-the-shelf model, compute Spearman ρ on the selectivity
ratio, and run the MW/logP confound diagnostic. If Δscore is strongly predictable from molecular
properties, that reframes the rest of the week.

## Fidelity contract

See [contract 3](../fidelity-contracts.md#3-equivariant-scorer-s5--replaces-physics-based-rescoring).
Re-checked after every S7 retraining.
