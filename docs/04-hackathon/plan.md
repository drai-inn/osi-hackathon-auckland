# Hackathon plan

**Dates:** TBC ([A1](../01-scope/open-questions.md) — 🔴 blocking) ·
**Assumed shape:** 5 days · **Assumed compute:** 8× H200 `[source-doc, unconfirmed]`

If the event is shorter, cut scope by dropping WP-C's surrogate arm and reducing to two targets,
not by compressing the schedule. The day-1 measurement/re-plan cycle and the day-4 integration are
both load-bearing.

---

## The three questions the week must answer `[source-doc]`

1. **Which parameters matter?**
2. **Which stages add measurable value?**
3. **How small can the benchmark be while still producing signal robust enough to guide investment?**

Note what is *not* on this list: "does the pipeline find good compounds?" That is a Phase-3
question and we cannot answer it at this n. Saying so up front prevents the week's result being
judged against the wrong standard.

## Target scope `[source-doc]`

> 12–20 ligands, CDK9 plus one close counter-target, three poses or states per ligand–target pair,
> 20–50 targeted cuEST labels.

Small enough for parallel experimentation, large enough to expose whether there is real
selectivity signal.

## Schedule

### Pre-hackathon (the part that decides the outcome)

| Item | Owner | Why it cannot wait |
| --- | --- | --- |
| Confirm dates, compute block, queue policy | Nick + eResearch | Everything is sized against it |
| Resolve cuEST availability ([B1](../01-scope/open-questions.md)) | WP-E owner | WP-E does not exist without an answer |
| Resolve Nesso-1 fine-tunability ([B3](../01-scope/open-questions.md)) | WP-D owner | Determines whether S7 is retraining or calibration |
| **Manifest v1** | WP-A owner | Blocks all five other packages |
| **Base container images built and published** | WP-F owner | Highest-value pre-work in the project |
| Stub DAG + `make smoke` | WP-F owner | People arrive to a working repo |
| Pre-registration pages | All WP owners | One page each |

A hackathon that starts with a working smoke test and a validated manifest gets four days of
science. One that doesn't gets two.

### Day 1 — Clinics, measurement, and re-planning

| | |
| --- | --- |
| **09:00** | Framing: the three questions, the gates, what a negative result looks like (30 min) |
| **09:30** | Three [adjacent-activity clinics](adjacent-activities.md) in parallel (90 min) — before anyone touches a GPU |
| **11:00** | Interfaces frozen. `make smoke` green. Every owner has a failing test for their real stage |
| **13:00** | Each WP measures **real** per-item cost at one setting |
| **16:00** | **Re-planning meeting.** Replace every `[estimate]` in the compute budget with `[measured]`. Re-derive run sizes. This is a decision meeting |
| **17:00** | WP-E reports the quantum convergence check. If it fails, re-plan around it tonight |

### Day 2 — Per-stage sweeps

Each WP runs random search over its own parameters against cached upstream. WP-F keeps the DAG and
telemetry working. Methodology lead starts collecting score distributions.

**End of day:** each WP posts its score distribution and the first marginal sensitivity estimates.

### Day 3 — Sensitivity, joint sweeps, selection

- Variance decomposition across all stage sweeps → the ranked parameter list
- The three [joint interaction blocks](../03-experiments/parameter-space.md#interactions-to-sweep-jointly)
- **Selection meeting:** agree the single configuration for the integrated run, plus the baselines

**End of day:** configuration frozen. Nothing after this point is tuned.

### Day 4 — Integrated run + baselines

The integrated configuration, the 2D baseline, the static-3D baseline, and the random-acquisition
control — all on the same manifest, all with intervals.

Also: does the integrated result land where the per-stage sweeps predicted? Disagreement means
stage effects are not separable, and that is a reportable finding.

**Reserve the last four hours for the run failing and being re-run.** It will.

### Day 5 — Gates, write-up, and what happens next

| | |
| --- | --- |
| **Morning** | Gate assessment against [stage-gates.md](../05-feasibility/stage-gates.md). Honest colour on each |
| **Midday** | Each adjacent activity presents its artifact — separately from the pipeline result |
| **Afternoon** | Pipeline result + recommendation. Phase-2 plan or a documented stop |

## Definition of done

The week is successful if, regardless of whether the pipeline works:

- [ ] A validated, documented benchmark exists and could be released
- [ ] Every stage has a measured cost and a named owner who understands its failure modes
- [ ] Every surrogate has a completed [fidelity contract](../02-pipeline/fidelity-contracts.md)
- [ ] A ranked list of which parameters move selectivity ranking, with intervals
- [ ] One integrated run reproducible from a clean clone
- [ ] Each of the three adjacent activities has produced its artifact
- [ ] An explicit, evidence-backed go / no-go / go-differently recommendation

**A clean "no" against the gates is a successful hackathon.** The failure mode to avoid is an
ambiguous result that lets the project drift forward on optimism — which is what happens when the
gates aren't pre-specified.

## Facilitation notes

- **One room, six tables.** Cross-WP conversation is most of the value and it does not happen over
  chat.
- **15-minute standup, 09:00, all hands.** Blockers only.
- **A visible burn-down of GPU-hours consumed vs. budgeted.** WP-F owns the board. Nothing
  concentrates minds like watching the quantum budget disappear.
- **A "surprises" board.** Anything that contradicts an assumption in this repo gets written up
  there and folded back into [open-questions.md](../01-scope/open-questions.md).
- **Visiting research leaders attend the day-1 clinics and the day-5 presentations.** Those are the
  two sessions worth their time; days 2–4 are not spectator sport.
