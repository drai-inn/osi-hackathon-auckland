# Risk register

Ordered by expected impact. Probability and impact are `[estimate]` — the point is the mitigation
and the owner, not the arithmetic.

## 🔴 Project-threatening

| # | Risk | P | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |
| R1 | **cuEST unavailable or unusable** on our stack (licence, container, driver) | Med | WP-E does not exist; the differentiating stage is gone | Resolve [B1](../01-scope/open-questions.md) **now**. Pre-agree the fallback ladder (GPU4PySCF → xTB) and accept that it changes the cost model by orders of magnitude | WP-E |
| R2 | **Benchmark is not fit for purpose** — incomparable assays or trivially separable decoys | **High** | Every result is an artefact; the week is wasted and we may not notice | Activity 1 clinic on day 1, before GPUs. Property-matched decoys. Report the 2D baseline first — if it gets 0.95 AUC, the benchmark is broken | WP-A |
| R0 | **🔴 The stack does not build for both `aarch64` (GB10) and `x86_64` (H200)** | **Med-High** | Everything works on GB10 through weeks 2–3, then the H200 run doesn't start. Discovered late, it costs the event | **The week-1 spike ([W1.1](../04-hackathon/critical-path.md)).** Multi-arch manifests; run the real S1 container on both before week 2. Any stage that can't build for `aarch64` develops on H200 and loses the month's benefit — know which by Fri 25 Sep | WP-F |
| R0b | **🔴 The month is treated as optional and the build lands in the two days** | **Med** | Two days of installing software in front of guests. The single worst outcome available | Weekly Friday gates with a written cut decision. Freeze Thu 15 Oct. [critical-path.md](../04-hackathon/critical-path.md) is the plan, not aspiration | Nick |
| R3 | **Compute block slips or is smaller than assumed** | Med | Drop to tiny-smoke-test scale; no gate assessable | Confirm [A2](../01-scope/open-questions.md) in writing, with a job that actually ran. **Book the week-3 H200 block now** — it has no slack. Cloud-burst fallback costed ([A4](../01-scope/open-questions.md)) | Nick |
| R4 | **Quantum cost per label is 10× the estimate** | Med | S6 consumes the whole budget for ~5 labels | WP-E measures on day 1 and generates no production labels until it has. Day-1 re-planning meeting exists for exactly this | WP-E |
| R5 | **Integration fails on day 4** — six stages that never ran together | Med | Six demos, no pipeline result, gate 1 red | Frozen interfaces day 1; stub `make smoke` before lunch; contract tests before science | WP-F |

## 🟠 Result-distorting

| # | Risk | P | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |
| R6 | **Scorer ranks binders, not selectivity** — Δscore is a property calculator | **High** | The core claim is unsupported | The MW/logP confound diagnostic on day 1. Evaluate on Δscore throughout, never per-target score | WP-D |
| R7 | **Co-folding memorisation mistaken for accuracy** | High | Overconfidence in S1; the contract is meaningless | Flag PDB entries postdating model training cutoffs; weight held-out-by-date heavily | WP-B |
| R8 | **Everything is within noise at n≈20** | **High** | All gates amber; ambiguous ending | Accept it as a likely outcome. Paired bootstrap for tighter difference intervals. Pre-commit to reporting amber as "answerable at tier N", with the required n | Methodology |
| R9 | **Uncalibrated uncertainty** makes acquisition ≈ random | Med | Gate 5 unassessable | Calibration is a day-1 metric, not a day-4 one. The random control makes this visible either way | WP-D |
| R10 | **Surrogate ensembles miss the discriminating state** while agreeing well overall | Med | Confident wrong ensembles | Report agreement on the discriminating subset separately from overall — see [fidelity-contracts](../02-pipeline/fidelity-contracts.md#why-trust-region-is-the-important-field) | WP-C |
| R11 | **Stage effects are not separable**, so per-stage sweeps mislead | Med | Day-3 selection picks a bad joint configuration | The integrated run is the check; sweep the three known interaction pairs jointly; report disagreement as a finding | Methodology |

## 🟡 Manageable

| # | Risk | P | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |
| R12 | Nesso-1 not fine-tunable → S7 becomes calibration-only | Med | Weaker feedback loop | Resolve [B3](../01-scope/open-questions.md). Calibration-only is still a valid, testable S7 | WP-D |
| R13 | Team under-assembled; a WP has no owner or host | Med | Drop WP-C's surrogate arm | Decide by Fri 2 Oct, not on the day. Invitations out **Wed 23 Sep** | Nick |
| R19 | **Newcomers have a poor experience** — stuck, idle, or watching others debug | **Med-High** | The stated priority missed, and the engagement goal with it | Host role separate from owner; on-ramps pre-built; **novice dry run in week 4** ([W4.2](../04-hackathon/critical-path.md)); no-one-debugs-alone rule | Hosts |
| R20 | **Handoff package is thin** because day 2 ran late | Med | The US team repeats our work instead of extending it | Write it live 15:30–16:30 with the room present, from a template prepared in week 4 ([us-handoff.md](../04-hackathon/us-handoff.md)) | Nick |
| R21 | GB10 interactive load collapses under ~15 people launching runs at once | Low-Med | The on-ramps stall in the first hour | Size it in the week-4 dry run; keep on-ramp runs to the cheap S5 configurations; H200 takes the batch | WP-F |
| R14 | Six groups building containers on day 1 | High | Half a day lost | WP-F pre-builds and publishes base images | WP-F |
| R15 | Protonation/tautomer errors invalidate quantum labels | Med | Precise answers about the wrong molecule | [C4](../01-scope/open-questions.md); joint WP-A/E protocol agreed pre-hackathon | WP-E |
| R16 | Queue waits dominate wall-clock | Med | Fewer configurations than planned | Track queue-to-compute from day 1; if >1, reduce run size rather than waiting | WP-F |
| R17 | Results not reproducible after the event | Med | Nothing is citable | `provenance.json`; on-disk metrics as well as MLflow; reproducibility report as a day-5 deliverable | WP-F |
| R18 | IP/ownership unresolved, contributors uncomfortable | Low | Reputational, and it surfaces late | [E1](../01-scope/open-questions.md) answered **before** invitations go out | Nick |

## The three to watch

If attention is limited, these are the ones:

- **R0 (architecture split)** — newly the most urgent, because it is cheap to eliminate this week
  and expensive to discover in week 3. One day of spike work.
- **R2 (bad benchmark)** — highest probability × impact for the *result*, and the one most likely
  to go unnoticed until after the write-up.
- **R6 (selectivity vs. affinity)** — the specific way this class of pipeline produces a
  convincing false positive. The diagnostic costs three lines of code.
- **R8 (everything within noise)** — the most likely actual outcome. Planning for it in advance is
  what makes an amber result useful rather than deflating.

R6 and R19 are the runners-up: one produces a convincing false positive, the other wastes the
goodwill of the people we are trying to bring in. Both are cheap to prevent and hard to repair.
