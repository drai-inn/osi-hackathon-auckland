# Critical path — 20 working days to 19 Oct

**Event:** Mon 19 – Tue 20 Oct 2026 (2 days, Wed 21 optional) · **Global event:** 21–22 Oct ·
**Today:** Sat 19 Sep · **Planning session:** Mon 21 Sep, 2 h ([agenda](monday-session.md))

---

## The strategic point, stated once

**Two days is not enough time to build this. It is enough time to *run* it.**

With a five-day event you can afford a day of setup. With two, anything not working before people
arrive will not work at all. So the month is the project and the event is the experiment:

> **Arrive on 19 Oct with a pipeline that runs end-to-end and a pile of pre-computed baselines, so
> the two days are spent on the things that actually need a room full of people** — cross-disciplinary
> judgement, exploration, interpretation, and the engagement of people new to AI for science.

Everything I had on "day 1" in the five-day plan now lands in the month. What stays in the room is
listed in [plan.md](plan.md#what-genuinely-needs-people-in-a-room).

The enabler is that we have **dual GB10 boxes for the whole month**. A month of unattended
development and pre-computation on real hardware is worth more than three extra hackathon days.

## Tracked as issues

The highest-priority items are GitHub issues; this page stays the narrative, the issues carry the
state.

| Issue | Item | Due | |
| --- | --- | --- | --- |
| ~~[#12](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/12)~~ | ~~W1.0 Resolve the dates~~ | — | ✅ **19–20 Oct** |
| [#2](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/2) | W1.1 Architecture spike — `aarch64` **and** `x86_64` | Fri 25 Sep | 🔴 |
| [#3](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/3) | W1.2 H200 access — with a job that actually ran | Fri 25 Sep | 🔴 |
| [#4](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/4) | W1.3 cuEST reality check, or pick the fallback | Fri 25 Sep | 🔴 |
| [#5](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/5) | W1.5 Invitations out | **Wed 23 Sep** | 🔴 |
| [#6](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/6) | W1.6 Owner **and** host named per package | **Mon 21 Sep** | 🔴 |
| [#7](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/7) | W2.3 Manifest v1 frozen | Fri 2 Oct | 🔴 |
| [#8](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/8) | W2.2/W2.4 Smoke test, multi-arch images, interfaces frozen | Fri 2 Oct | 🟠 |
| [#9](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/9) | W3.3/W3.4 Quantum convergence study on H200 | Fri 9 Oct | 🔴 |
| [#10](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/10) | W4.2 Novice dry run, under 30 minutes | Fri 16 Oct | 🟠 |
| [#11](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/11) | W1.8/W4.5 US relay and handoff package | Fri 25 Sep → Fri 16 Oct | 🟠 |
| [#13](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/13) | Public micro-repo live before invitations go out | **Wed 23 Sep** | 🔴 |

Dates are settled, which unblocks the chain: **#6 is Monday**, then **#13 and #5 are Wednesday** —
the micro-repo must be live before invitations go out, because every invitation carries the link.
Everything else in week 1 depends on #6 producing names.

---

## Five tracks

Tracks run in parallel and have different owners. Track 1 gates tracks 3–5, so it goes first and
fastest.

| # | Track | Owner | Why it is on the critical path |
| --- | --- | --- | --- |
| **1** | **Compute & architecture** | WP-F + Nick | GB10 is `aarch64`, H200 is `x86_64`. If the stack won't build for both, week 3 discovers it and the event is lost |
| **2** | **Benchmark** | WP-A | Blocks every other package. Needs human judgement, so it needs people recruited first |
| **3** | **Stage implementations** | WP-B/C/D/E | Must be real, not stubs, before 19 Oct |
| **4** | **Pre-computation campaign** | WP-F coordinating | Unattended GB10 + booked H200 time. The month's compute dividend |
| **5** | **People & engagement** | Nick + hosts | Recruitment, on-ramps, the US relay. A 2-day event needs people who arrive ready |

---

## Week 1 · 21–27 Sep — *unblock*

The week is about removing uncertainty, not producing science. Three spikes and a recruitment push.

| # | Item | Track | Owner | Done when |
| --- | --- | --- | --- | --- |
| **W1.1** | **🔴 The aarch64 spike.** On a GB10: build/run PyTorch + CUDA, Boltz-2, RDKit, OpenMM, the scorer. List what has no `aarch64` build | 1 | WP-F | A written table: works / needs building / impossible |
| **W1.2** | **🔴 H200 access secured** — booking mechanism, quota, queue policy, container runtime, a *test job that actually ran* | 1 | Nick + eResearch | A job ID, not an email promise |
| **W1.3** | **🔴 cuEST reality check** — licence, `aarch64` and/or `x86_64` builds, supported methods. Pick the fallback now if the answer is no | 1 | WP-E | Either a working container or a decided fallback ([S6](../03-pipeline/stages/S6-quantum-labelling.md#candidate-software)) |
| **W1.4** | **Model licences and weights** — Boltz-2, Nesso-1 (and is Nesso-1 fine-tunable at all?) | 3 | WP-B, WP-D | Weights downloaded, hashes recorded |
| **W1.0** | ✅ ~~Resolve the dates~~ — **19–20 Oct, locked** ([ADR-0006](../adr/0006-run-19-20-october-as-a-precursor.md)). Now: email the organisers about what a precursor can still join, and ask for a Valence Labs intro re: Nesso-1 | 5 | Nick | Reply received, or asked on Slack. **Monday** ([A10](../02-scope/open-questions.md)) |
| **W1.4b** | **Register Auckland as an official hub**; join the global Slack; stand up the public micro-repo | 5 | Nick | Listing confirmed with a named lead, as Duke's is. Micro-repo live **before** invitations |
| **W1.5** | **🔴 Invitations out** | 5 | Nick | Sent by Wed 23 Sep, pointing at the micro-repo. [Templates ready](../../outreach/invitations.md). Four weeks is already short notice |
| **W1.5b** | Four targeted Tier-1 emails to previous hackathon teams whose work overlaps ours | 5 | Nick | [interested-parties.md](../00-event/interested-parties.md). Four specific emails, not forty generic |
| **W1.6** | Work-package owners named | 5 | Nick | Monday's session ([agenda](monday-session.md)) |
| **W1.7** | Manifest v0.5 — targets fixed, 12 ligands, provisional labels | 2 | WP-A | `make validate` passes |
| **W1.8** | US counterparts contacted; relay shape agreed | 5 | Nick | [us-handoff.md](us-handoff.md) has names and a call slot |

**Week 1 gate (Fri 25 Sep):** we know what runs where. If W1.1 or W1.3 comes back badly, the scope
conversation happens *now*, with four weeks to adapt — not in week 3 with one.

## Week 2 · 28 Sep – 4 Oct — *skeleton*

| # | Item | Track | Owner | Done when |
| --- | --- | --- | --- | --- |
| **W2.1** | **Multi-arch base images** built and published for both architectures | 1 | WP-F | `docker manifest inspect` shows both |
| **W2.2** | **`make smoke` green on GB10** — five synthetic pairs through all stages with stubs | 1 | WP-F | CI or a recorded run |
| **W2.3** | **🔴 Manifest v1 frozen** | 2 | WP-A | Committed, validated, ADR if it changes after |
| **W2.4** | **Interfaces frozen** | 3 | WP-F + owners | [interfaces.md](../03-pipeline/interfaces.md) marked frozen; each owner has a failing contract test |
| **W2.5** | S1 real on GB10 — one complex, measured cost | 3 | WP-B | A GPU-hours number replacing an `[estimate]` |
| **W2.6** | 2D baseline computed | 2 | WP-A | The number everything is measured against exists |
| **W2.7** | **H200 benchmark run** — the same S1 job on H200, to measure the GB10:H200 ratio | 1/4 | WP-F | A measured factor, replacing the `[estimate]` in [compute-plan.md](../06-feasibility/compute-plan.md) |
| **W2.8** | On-ramp design agreed; who hosts whom | 5 | Nick + hosts | [engagement.md](../00-event/engagement.md) has names against on-ramps |

**Week 2 gate (Fri 2 Oct):** the skeleton runs on GB10 and the manifest is frozen. Every downstream
package can now work against a stable input.

## Week 3 · 5–11 Oct — *make it real*

| # | Item | Track | Owner | Done when |
| --- | --- | --- | --- | --- |
| **W3.1** | S2, S3, S4 real on GB10 | 3 | WP-B, WP-C | Static + relaxation modes working; surrogate arm if feasible |
| **W3.2** | S5 real; uncertainty estimates produced | 3 | WP-D | Scores + `acquisition.csv` with the random control |
| **W3.3** | **🔴 Quantum convergence study on H200** — theory level and shell size, 3–5 systems | 3/4 | WP-E | The load-bearing check, done *before* the event, not during |
| **W3.4** | **Measured cost per label** | 4 | WP-E | The single most important number in the budget |
| **W3.5** | Start unattended pre-computation: all S1 complexes, reference MD | 4 | WP-F | Jobs running overnight on GB10 |
| **W3.6** | **Live dashboard** — runs appear with the runner's name | 5 | WP-F | Works on a phone in the room |
| **W3.7** | **Sealed-forecast questions drafted** | 5 | Nick | Six binary questions matching the gates |
| **W3.8** | Pre-reads sent to participants | 5 | Nick | One page per on-ramp, not the whole repo |

**Week 3 gate (Fri 9 Oct):** the pipeline runs end-to-end on real data at least once. If it does
not, week 4 is a rescue and the event's scope gets cut on Mon 12 Oct.

## Week 4 · 12–18 Oct — *rehearse and pre-compute*

The temptation this week is to add features. Don't. This week is for pre-computation, rehearsal,
and making the room work.

| # | Item | Track | Owner | Done when |
| --- | --- | --- | --- | --- |
| **W4.1** | **Pre-computation campaign completes** — all complexes, ensembles, reference MD, baselines | 4 | WP-F | Results in `artifacts/`, referenced by the day-1 launcher |
| **W4.2** | **🔴 Dry run with a real novice** — someone genuinely new to AI for science does on-ramp A unaided, timed | 5 | Hosts | Under 30 minutes to first result, or the on-ramp gets fixed |
| **W4.3** | **H200 block confirmed and tested for the event dates** | 1 | Nick + WP-F | A reservation, and a job that ran under it |
| **W4.4** | Pose triage viewer ready and loaded with real poses | 5 | WP-B + hosts | A structural biologist can use it cold |
| **W4.5** | Handoff brief template + US call booked (21 Oct 09:00 NZDT) | 5 | Nick | Invite accepted |
| **W4.6** | Pre-registration pages, one per package | 3 | Owners | Primary question, metric, threshold — before data |
| **W4.7** | **Freeze.** No new features after Thu 15 Oct | all | Nick | Announced, and meant |

**Week 4 gate (Fri 16 Oct):** a clean clone runs the integrated pipeline on the real manifest,
and a novice reached a result unaided. If both are true, the event is about science. If not, it is
about setup, and we should say so and cut scope.

---

## The three things most likely to sink this

1. **W1.1 — the architecture split.** GB10 is `aarch64`; H200 is `x86_64`. This is invisible until
   somebody tries to run the GB10-developed container on H200 in week 3 and it doesn't. One day of
   spike work in week 1 costs almost nothing and removes the risk entirely.
2. **W1.3 — cuEST.** If it is unavailable, WP-E's whole premise changes and the fallback ladder has
   a different cost model by orders of magnitude. Four weeks is enough to adapt. One week is not.
3. **W2.3 — the manifest.** It blocks five packages and it needs human chemistry judgement, which
   means it needs people recruited in week 1. The dependency chain is
   *invitations → people → judgement → manifest → everything*, and it starts on Monday.

## What to cut, in order, if the month slips

1. The S3 surrogate-ensemble arm → static + short relaxation only (keeps the mode comparison alive)
2. Targets → CDK9 + CDK7 only (already the minimum-viable assumption)
3. S7 feedback learning → calibration-only rather than retraining
4. The integrated run → per-stage results plus an honest statement that integration was not reached

**Do not cut:** the quantum convergence study, the random-acquisition control, or the novice dry
run. The first two make gates assessable; the third is the difference between a good experience and
a bad one for the people we are trying to bring in.
