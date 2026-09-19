# Handing over — publishing into the global event's opening

**Us:** Mon 19 – Tue 20 Oct, Auckland (NZDT, UTC+13) — a deliberate precursor
([ADR-0006](../adr/0006-run-19-20-october-as-a-precursor.md))
**The global OSI Hackathon:** 21–22 Oct, 16 hubs
**US counterparts:** _names TBC_ ([W1.8](critical-path.md#week-1--2127-sep--unblock))

---

## The timing is unusually good

| Moment | NZDT | UTC | EDT |
| --- | --- | --- | --- |
| **Our day-2 close** | **Tue 20 Oct 17:00** | **Tue 20 Oct 04:00** | **Tue 20 Oct 00:00** |
| Earliest global hub opens (NZ/Sydney) | Wed 21 Oct 09:00 | Tue 20 Oct 20:00 | Tue 20 Oct 16:00 |
| US east-coast hubs open | Thu 22 Oct 02:00 | Wed 21 Oct 13:00 | Wed 21 Oct 09:00 |

**We finish 16 hours before the earliest hub in the world starts, and 33 hours before the US
sites.** Everything we produce is on the table before anyone else begins — which is the whole
argument for running early rather than an apology for it.

Two audiences, then:

1. **The global event**, which opens 16 hours after we close. Our benchmark, workflow and results
   are available to every hub from their first minute
2. **The US counterparts specifically**, for the deeper conversation

## What "handing over" should mean

Not a status report. **Their two days should extend ours, not repeat them.** That requires us to be
specific about three things, in this order of usefulness to them:

1. **What we settled** — so they don't re-derive it
2. **What we could not answer, and why** — so they can attack it with fresh compute
3. **What surprised us** — the highest-value content, and the part most likely to be omitted in a
   tired 16:30 write-up if we haven't planned for it

## The handoff package

Written **live on screen during day 2, 15:30–16:30**, with everyone in the room. Not afterwards.
A brief written by one person at 19:00 loses everything the room knew.

| # | Item | Owner | Format |
| --- | --- | --- | --- |
| 1 | **One-page brief** — what we did, what we found, what we recommend they do first | Nick | Markdown, in repo |
| 2 | **Gate report** with colours and intervals | methodology | `artifacts/.../gate_report.json` + a table |
| 3 | **Runnable pipeline** — clean clone, pinned images, one command | WP-F | Repo + registry |
| 4 | **The manifest and all artifacts** | WP-A + WP-F | Frozen, hashed |
| 5 | **Measured costs** per stage per item, both architectures | WP-F | Table |
| 6 | **Sensitivity ranking** — which parameters moved the result | methodology | With bootstrap intervals |
| 7 | **The open questions we want them to take** — ranked, with what each would cost | Nick + owners | The most important item on this list |
| 8 | **The surprises board**, transcribed | hosts | Verbatim, unpolished |
| 9 | **Filled fidelity contracts** | stage owners | [Template](../03-pipeline/fidelity-contracts.md#contract-template) |
| 10 | **A 10-minute screen recording** walking through a run | WP-F | Because nobody reads setup docs at 05:00 |

Template for item 1 lands in week 4 ([W4.5](critical-path.md#week-4--1218-oct--rehearse-and-pre-compute)),
so that day 2 is filling in a structure rather than inventing one.

## Ranking what we ask them to take

The single most useful thing we can give them is a **ranked list of open questions with costs
attached**, because their constraint is the same as ours: two days.

Expected shape, to be replaced with the real list on the day:

| Rank | Question | Why we couldn't | Est. cost |
| --- | --- | --- | --- |
| 1 | Does the acquisition advantage survive at 200 labels? | Our label budget was 20–50 | H200 block |
| 2 | Does the sensitivity ranking hold at the next benchmark tier? | We had two tiers; two points is not a trend | Moderate |
| 3 | Do the results hold on a second target family? | Single family, so generality is untested | Needs a new benchmark |
| 4 | Does the surrogate ensemble match longer MD? | Our reference MD was a few ns and unconverged | Large |

## Before the event

| | Item | By |
| --- | --- | --- |
| ☐ | Counterparts identified and introduced | Week 1 |
| ☐ | **They have read this repo** — especially [scope](../02-scope/scope.md) and [stage-gates](../06-feasibility/stage-gates.md) | Week 2 |
| ☐ | Agreement on what *not* to duplicate | Week 2 |
| ☐ | Shared artifact location that works across both institutions, **tested with a real file** | Week 3 |
| ☐ | Their compute and constraints known — so item 7 is ranked against what they can actually run | Week 3 |
| ☐ | Live call booked, 21 Oct 09:00 NZDT / 20 Oct 16:00 EDT | Week 4 |
| ☐ | Handoff brief template in repo | Week 4 |

## Reciprocity

This works in both directions. Agree in week 2 what we want back: their gate assessment against the
same criteria, their measured costs on their hardware, and their answers to the questions we hand
over. Two teams running the same gates on different hardware two days apart is a genuinely
interesting comparison — and a much stronger joint result than either set alone.

Worth raising with them early: **if they run the same manifest and the same gates, we have a
replication.** That is rare, cheap here, and more publishable than either event separately.
