# Planning session — Mon 21 Sep, 2 hours

**Purpose:** leave the room with names against work packages, the week-1 spikes assigned, and
invitations ready to send. Nothing else in the month can start until those three things exist.

**Pre-read (20 minutes, send Sunday):** [README](../../README.md) ·
[critical-path.md](critical-path.md) · [engagement.md](../00-event/engagement.md). Not the whole repo.

---

## What must be true when we walk out

Four decisions. If we get these and nothing else, the session succeeded.

1. **Every work package has a named owner and a named host** (two different people)
2. **The week-1 spikes are assigned with a Friday 25 Sep deadline** — architecture, H200 access, cuEST
3. **The invitation list is written and the invitations go out by Wed 23 Sep**
4. **The scope cut is decided** — what we are explicitly not doing in two days

## Agenda

| | | |
| --- | --- | --- |
| **0:00–0:05** | **✅ Dates locked: Mon 19 – Tue 20 Oct**, two days ahead of the global event, Wed 21 optional. Note what changes: we are a precursor, and the collateral now says *"two days ahead of the world"* ([ADR-0006](../adr/0006-run-19-20-october-as-a-precursor.md)) | Nick |
| **0:05–0:15** | **Framing.** Two days, not five. The month is the project; the event is the experiment. 20 working days | Nick |
| **0:15–0:25** | **The compute picture.** GB10 now through the end; H200 for benchmarks. The `aarch64`/`x86_64` split and why it is the most under-appreciated risk ([compute-plan.md](../06-feasibility/compute-plan.md)) | Nick / WP-F candidate |
| **0:25–0:50** | **🔴 People.** Walk the six packages. Name an owner and a host for each. Identify gaps honestly and decide what we cut rather than hoping ([work-packages.md](work-packages.md), [roles.md](roles.md)) | all |
| **0:50–1:05** | *Break* | |
| **1:05–1:25** | **Week-1 spikes.** Assign the three blockers with Friday deadlines. Agree what "done" looks like for each ([W1.1–W1.3](critical-path.md#week-1--2127-sep--unblock)) | all |
| **1:25–1:45** | **Engagement.** Confirm the on-ramps, assign hosts, agree the novice dry run in week 4. This is where the newcomer experience is won or lost ([engagement.md](../00-event/engagement.md)) | all |
| **1:45–1:55** | **Invitations.** Who, by name; which activity each is invited into; who sends. Out by Wed | Nick |
| **1:55–2:00** | Confirm the weekly gate meeting (Fridays, 30 min) and close | Nick |

## Decisions to force, with a recommendation each

Bring a recommendation to every decision so the room is editing rather than inventing. Mine:

| # | Decision | Recommendation | Why |
| --- | --- | --- | --- |
| D1 | Two targets or four? | **CDK9 + CDK7 only** | Two days. Four targets doubles everything for a generality claim we cannot support at n≈20 anyway. Note it as a Phase-2 question |
| D2 | Which three [adjacent activities](adjacent-activities.md)? | **1, 2, 3** — benchmark clinic, small-data HPO, fidelity ladder. Activity 4's work happens under WP-F regardless | Protects the two things most likely to invalidate the project, and gives the methodology thread room |
| D3 | Does the S3 surrogate arm survive? | **Only if WP-C has two people.** Otherwise static + short relaxation | Widest cost range, weakest prior, heaviest install burden |
| D4 | Owner and host as separate people? | **Yes, mandatory** | In a two-day sprint the owner will choose the technical work over the newcomer, every time, and nobody will have done anything wrong |
| D5 | Where does development happen? | **GB10, validated on H200 weekly** | Iterating behind an H200 queue wastes the month |
| D6 | Pre-register the analysis plan? | **Yes, one page per package by week 4** | Cheap, and it is the difference between a finding and a story at n≈20 |
| D7 | What do we hand the US team? | **A ranked list of open questions with costs**, not a status report | Their constraint is the same as ours. Make their two days extend ours ([us-handoff.md](us-handoff.md)) |
| ~~D8~~ | ~~Which dates?~~ | ✅ **Resolved: 19–20 Oct.** We cannot run past the 21st and the 21st has competing agendas. Extending into Wed 21 stays an option we take in the moment, not a plan | [ADR-0006](../adr/0006-run-19-20-october-as-a-precursor.md) |
| D9 | Micro-repo, or contribute to the main site? | **Both, differently.** Register the hub upstream and publish a small public Auckland landing page. **Do not fork the main site** | Different audiences ([public-presence.md](../00-event/public-presence.md)) |

## What not to spend the two hours on

Tempting and wrong, because each can be resolved asynchronously by one person:

- Debating pocket crop radius, theory levels, or any other parameter — that is what the event is for
- Reviewing the pipeline architecture in detail — read the ADRs and object in writing
- Choosing models (Boltz-2 vs. alternatives) — subject to week-1 licence answers anyway
- The benchmark's chemistry — that is WP-A's job and Activity 1's clinic

If a technical argument starts, note it on the surprises list and move on. **The session's product
is names and dates.**

## Immediately after

| | By | Who |
| --- | --- | --- |
| Update [open-questions.md](../02-scope/open-questions.md) with owners and dates from the session | Mon evening | Nick |
| Update [roles.md](roles.md) with names | Mon evening | Nick |
| **Email Ben Blaiszik** — our dates, what a precursor can still join ([A10](../02-scope/open-questions.md)), and an intro to Valence Labs re: Nesso-1 | **Mon evening** | Nick |
| Micro-repo live | Wed 23 Sep | Nick |
| Send invitations (templates in [`outreach/`](../../outreach/)) | Wed 23 Sep | Nick |
| Book the H200 week-3 block | Tue 22 Sep | Nick + WP-F |
| First weekly gate meeting | Fri 25 Sep | all |

## The one-line version to open with

> *We have twenty working days and two GB10 boxes. If we use them, the hackathon is two days of
> science and a genuinely good experience for people new to this. If we don't, it is two days of
> installing software in front of guests.*
