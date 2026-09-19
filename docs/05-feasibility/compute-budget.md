# Compute budget

> **Every number on this page marked `[estimate]` is a guess and should be treated as one.**
> Day 1 of the hackathon exists partly to replace them with `[measured]` values, after which run
> sizes are re-derived. See [plan.md](../04-hackathon/plan.md#day-1--clinics-measurement-and-re-planning).
>
> Use [`tools/compute_budget.py`](../../tools/compute_budget.py) to recompute any tier after
> editing the per-unit costs.

## Assumed resource

8× H200 `[source-doc, unconfirmed — see A2]`. Treating a day as ~20 usable GPU-hours per card
after queueing and failures gives **~160 GPU-hours/day**, ~800 over a five-day event.

That headline number is comfortable. The binding constraint is not total GPU-hours — it is
**wall-clock on the critical path** and **the quantum stage**, which is the only thing that can
consume the budget faster than it can produce insight.

## Run-size tiers `[source-doc]`

| Stage | Tiny smoke test | Hackathon minimum | Useful pilot | Scale-up |
| --- | --- | --- | --- | --- |
| Complex generation | 10–30 complexes | 72–120 | 600–2,000 | 5k–50k after filtering |
| Dynamic / surrogate states | 1–3 per complex | 3 per complex | 3–5 per complex | surrogate broadly; explicit dynamics on subsets only |
| Pocket scoring | <100 scored graphs | 200–500 | 2k–10k | 100k+ plausible |
| cuEST labels | 5–10 | 20–50 | 200–1,000 | 5k–50k, only after acquisition is validated |
| **Wall-clock target on 8× H200** | **1–3 h incl. setup** | **1–2 days with parallel groups** | **several days to 1–2 weeks** | campaign scale, after gates |

## Per-unit cost assumptions `[estimate]`

These are the numbers to attack on day 1. They are order-of-magnitude placeholders chosen to make
the arithmetic visible, not predictions.

| Unit | Assumed cost | Confidence | Replaced by |
| --- | --- | --- | --- |
| Co-folded complex (S1) | 0.05 GPU-h | Low | WP-B day 1 |
| Pocket crop (S2) | ~0 (CPU) | High | — |
| Short relaxation, 1 complex (S3) | 0.10 GPU-h | Low | WP-C day 1 |
| Surrogate ensemble, 1 complex (S3) | 0.05 GPU-h | **Very low** | WP-C day 1 |
| Reference MD, 1 complex (S3 validation) | 4.0 GPU-h | Low | WP-C day 2 |
| Clustering (S4) | ~0 (CPU) | High | — |
| Scored graph (S5) | 0.001 GPU-h | Medium | WP-D day 1 |
| **Quantum label (S6), lightweight theory** | **0.5 GPU-h** | **Very low** | **WP-E day 1 — the critical number** |
| Quantum label, reference theory | 4.0 GPU-h | Very low | WP-E day 1 |
| Scorer retraining (S7) | 0.25 GPU-h | Medium | WP-D day 2 |

The S6 figure could plausibly be off by an order of magnitude in either direction depending on
theory level, system size and cuEST's actual performance. **The entire budget hinges on it**,
which is why WP-E's day-1 obligation is to measure it and generate no production labels.

## Hackathon-minimum walkthrough `[estimate]`

20 ligands × 2 targets = 40 pairs × 3 poses = 120 complexes.

| Stage | Volume | Unit cost | Total GPU-h |
| --- | --- | --- | --- |
| S1 complex generation | 120 | 0.05 | 6.0 |
| S3 surrogate ensembles | 120 | 0.05 | 6.0 |
| S3 short relaxation (comparison arm) | 120 | 0.10 | 12.0 |
| S3 reference MD (validation only) | 5 | 4.0 | 20.0 |
| S4 clustering | 120 | ~0 | ~0 |
| S5 scoring, single pass | 360 | 0.001 | 0.4 |
| **S5 random search, 200 configs** | 72,000 | 0.001 | **72.0** |
| S6 convergence study (reference theory) | 10 | 4.0 | 40.0 |
| S6 production labels (lightweight) | 40 | 0.5 | 20.0 |
| S7 retraining × 10 rounds | 10 | 0.25 | 2.5 |
| **Subtotal** | | | **178.9** |
| With 1.6× overhead for failures and reruns | | | **286.2** |

Reproduce with `python3 tools/compute_budget.py hackathon_minimum`.

**~290 GPU-hours against ~800 available — about 1.8 days of the cluster.** Comfortable, *if* the
S6 unit cost holds. At 5 GPU-h per label instead of 0.5, S6 production alone becomes 200 GPU-h and
the picture changes materially.

Two things worth noticing in that table:

- **The S5 random search (72 GPU-h) is the single largest line, at 40% of the subtotal.** That is
  the methodologically important spend, and it is affordable precisely because scoring is cheap —
  which is why [the microtopic](../03-experiments/hpo-microtopic.md) concentrates its configuration
  budget on S5 rather than spreading it evenly.
- **The convergence study (40 GPU-h) costs twice the production labels.** That is the correct
  ratio at this scale, and it is the line people will be tempted to cut. Don't: without it, gates
  4 and 5 cannot be assessed at all.

## Useful-pilot walkthrough `[estimate]`

100 ligands × 4 targets × 3 poses = 1,200 complexes; 500 labels.

| Stage | Total GPU-h |
| --- | --- |
| S1 | 60 |
| S3 surrogate + relaxation | 180 |
| S3 reference MD | 80 |
| S5 scoring + random search (64 configs) | 234 |
| S6 convergence (50 @ reference) | 200 |
| S6 production (450 @ lightweight) | 225 |
| S7 | 5 |
| **Subtotal** | **984** |
| With 1.6× overhead | **1,574** |

Note the search budget **drops** from 200 configurations to 64 between tiers. That is not a
concession — it is the thesis of [ADR-0003](../adr/0003-small-scale-search-before-scale-up.md):
search thoroughly where it is cheap, carry the winners up. Whether that is legitimate is exactly
what [diagnostic D2](../03-experiments/hpo-microtopic.md#q2--does-sensitivity-fall-as-scale-rises-the-headline) tests.

~10 days of dedicated 8× H200, or 2–3 weeks realistically with queueing. Consistent with the
origin document's "several days to 1–2 weeks" for this tier. `[source-doc]`

## What to cut, in order, if compute is short

1. Reference MD validation → 3 systems instead of 5 (saves ~8 GPU-h, weakens
   [contract 2](../02-pipeline/fidelity-contracts.md))
2. The relaxation comparison arm → surrogate only (saves ~12 GPU-h, loses a mode comparison)
3. Random-search configuration count → 64 instead of 200 (saves ~50 GPU-h, and Lourie et al.
   suggest 64 is where signal becomes visible but imprecise `[literature]`)
4. Targets → 2 instead of 4 (halves everything; already the minimum-viable assumption)
5. Quantum labels → 20 instead of 50 (saves ~10 GPU-h; do this last — it is the differentiating
   stage)

**Do not cut the random-acquisition control or the convergence study.** They cost little and
without them the two most important gates cannot be assessed.

## Non-GPU constraints, which will bite first

- **Queue wait time.** If jobs wait hours, wall-clock, not GPU-hours, sets the pace. WP-F tracks
  the queue-to-compute ratio from day 1.
- **Storage.** Ensembles and raw quantum outputs add up. Budget ~1 TB for the hackathon minimum
  `[estimate]`.
- **Human attention.** Six packages × 2–3 people is the real bottleneck on days 2–3, not silicon.
