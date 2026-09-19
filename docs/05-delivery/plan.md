# Hackathon plan — Mon 19 & Tue 20 Oct 2026

**Two days.** US colleagues run 20–21 Oct; we hand our outcomes to them as they start
([us-handoff.md](us-handoff.md)). Compute: dual GB10 for the room, HGX H200 for batch
([compute-plan.md](../06-feasibility/compute-plan.md)).

> Read [critical-path.md](critical-path.md) first. **This plan is only achievable if the month
> before it happens.** Two days is enough to run this pipeline and nowhere near enough to build it.

---

## The three questions the event must answer `[source-doc]`

1. **Which parameters matter?**
2. **Which stages add measurable value?**
3. **How small can the benchmark be while still producing signal robust enough to guide investment?**

Not on the list: *does the pipeline find good compounds?* That needs a scale we cannot reach, and
saying so up front prevents the work being judged against the wrong standard.

## What genuinely needs people in a room

The filter for what stays in the two days. Everything else belongs in the month.

| Stays | Why |
| --- | --- |
| **Cross-disciplinary judgement** — pose triage, benchmark critique, assay harmonisation arguments | Cannot be automated, and the disagreements are the value |
| **Human-in-the-loop exploration** — people choosing what to try next from live results | A queue script cannot do this, and it is more fun |
| **Integration and debugging under pressure** | Needs everyone present and interruptible |
| **Interpretation** — what the numbers mean and what to do about them | The actual deliverable |
| **Engagement** — the [on-ramps](../00-event/engagement.md) | The point of holding an event rather than doing the work quietly |

| Moves to the month | Where |
| --- | --- |
| Containers, smoke test, stage implementations | [Weeks 1–3](critical-path.md) |
| Benchmark curation | Week 1–2 |
| Cost measurement | Weeks 2–3 |
| **Quantum convergence study** | Week 3, on H200 |
| Reference MD, all co-folded complexes, baselines | Week 4 pre-computation campaign |

## Scope

12–20 ligands, CDK9 + one close counter-target, three poses/states per pair, 20–50 quantum labels.
`[source-doc]` Unchanged by the shorter event, because the month absorbs the build.

---

## Day 1 · Monday 19 Oct — *explore*

| Time | What | Who |
| --- | --- | --- |
| **09:00** | Welcome and framing: the three questions, the gates, what a negative result looks like | Nick |
| **09:20** | **Sealed forecast** — six binary predictions, sealed until tomorrow ([on-ramp D](../00-event/engagement.md#d--sealed-forecast--everyone--10-min-day-1-opening)) | all |
| **09:30** | **Explainer pairs** — each package explains itself to a newcomer in 5 minutes, no slides ([on-ramp F](../00-event/engagement.md#f--explainer-pairs--everyone--5-min-per-package-day-1)) | hosts |
| **10:00** | **On-ramps run in parallel.** Pose triage · break the benchmark · your run, your parameter · bring-your-own-problem clinic | hosts |
| **11:30** | First results on the dashboard. Everyone has a name against something | — |
| **12:30** | Lunch, and the first look at the pose-triage and benchmark-critique findings | all |
| **13:30** | **Parameter sweeps.** Packages drive; newcomers own configurations. Human-chosen next steps, not a fixed grid | all |
| **16:00** | **Checkpoint.** What is moving, what is noise, what looks broken. Decide day-2 focus | all |
| **17:00** | Sensitivity analysis on the day's runs; overnight batch queued on H200 | methodology + WP-F |

**End of day 1:** every participant's name on at least one artifact; enough configurations for a
first sensitivity ranking; overnight jobs running.

## Day 2 · Tuesday 20 Oct — *integrate, interpret, hand over*

| Time | What | Who |
| --- | --- | --- |
| **09:00** | Overnight results. **Open the sealed forecasts** — who called it? | all |
| **09:30** | **Integrated run** at the selected configuration, plus the three baselines (2D, static-3D, random-acquisition) | WP-F + owners |
| **11:00** | Analysis: does the integrated result land where the per-stage sweeps predicted? Disagreement is a finding, not a bug | methodology |
| **12:00** | Lunch | |
| **13:00** | **Gate assessment** against [stage-gates.md](../06-feasibility/stage-gates.md). Honest colour on each, intervals shown | all |
| **14:30** | **Adjacent-activity presentations** — each artifact presented separately from the pipeline result | activity leads |
| **15:30** | **Handoff brief written live**, on screen, with everyone in the room ([us-handoff.md](us-handoff.md)) | Nick + owners |
| **16:30** | Recommendation: go / no-go / go-differently. Phase-2 plan or a documented stop | Nick |
| **17:00** | **Close. Handoff package published** — 00:00 EDT, as the US team's day 1 begins | — |
| *21 Oct 09:00* | *Live handoff call — 16:00 EDT, their day-1 afternoon* | Nick + owners |

**Reserve 15:00–16:30 for the integrated run failing and being re-run.** It will, and a two-day
event has no other slack.

---

## Definition of done

Successful regardless of what the pipeline does:

- [ ] A validated, documented benchmark that could be released
- [ ] Every stage has a measured cost and an owner who understands its failure modes
- [ ] Every surrogate has a completed [fidelity contract](../03-pipeline/fidelity-contracts.md)
- [ ] A ranked list of which parameters move selectivity ranking, with intervals
- [ ] One integrated run reproducible from a clean clone
- [ ] **Every participant's name on at least one artifact**
- [ ] **The handoff package delivered before the US team starts**
- [ ] An explicit, evidence-backed go / no-go / go-differently recommendation

**A clean "no" against the gates is a successful event.** The failure mode to avoid is an ambiguous
result that lets the project drift forward on optimism.

## Facilitation

- **One room, six tables**, hosts distinct from owners ([why](../00-event/engagement.md#the-structural-fix-split-the-host-role))
- **09:00 standup, 15 minutes, blockers only.** Two-minute rule: explain yesterday to someone
  outside your discipline in two minutes
- **A visible GPU-hour burn-down** — WP-F owns the board
- **A surprises board.** Anything contradicting an assumption in this repo goes up and gets folded
  back into [open-questions.md](../02-scope/open-questions.md)
- **The dashboard shows names.** Contribution should be visible without anyone claiming it
- **Visiting research leaders:** day 1 morning (framing + on-ramps) and day 2 afternoon (gates +
  presentations). Days of debugging are not spectator sport
