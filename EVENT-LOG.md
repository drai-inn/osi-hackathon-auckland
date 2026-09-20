# 📡 Live event log — Auckland Hub

**This file lives on the `event-log` branch and its pull request stays open until the final
presentations and reports are done.**

**To follow:** open the PR and click **Subscribe**. Every update is a commit here — you get those
and nothing else. No issue noise, no CI. **When the PR closes, the work is finished.** That's the
only signal you need.

**To post:** commit to `event-log`. Newest at the top. Short, dated, honest — including what broke.
A log that only records progress isn't worth following, and isn't what happened.

Cadence: weekly through the month, daily during 19-20 October.

| | |
| --- | --- |
| **Event** | Mon 19 - Tue 20 Oct 2026, University of Auckland |
| **Global event** | 21-22 Oct, [registration open to anyone](https://luma.com/ku88xh92) |
| **What this is** | [The narrative](docs/00-event/narrative.md) · [Pick a ladder](docs/00-event/onboarding/README.md) |
| **Plan** | [Critical path](docs/05-delivery/critical-path.md) · [Issues](https://github.com/drai-inn/drugs-surrogate-pipeline/issues) |

---

## Status board

Updated with each entry. The honest version, not the reassuring one.

| | |
| --- | --- |
| **Week** | Week 1 · 21–27 Sep · *unblock* |
| **Next gate** | Fri 25 Sep, we know what runs where |
| **🔴 Blocking** | Owners and hosts unnamed · architecture spike unclaimed · cuEST unresolved · H200 unbooked · invitations out Wednesday |
| **Compute** | GB10 ×2 assumed available, unconfirmed · H200 unbooked |
| **People** | 0 of 6 packages have a named owner. Today is when that changes |

---

## 2026-09-21 · Planning session this morning — here is the agenda

**👉 [The agenda](docs/05-delivery/monday-session.md)**, two hours, and it is a pre-read if you are
coming. Also worth twenty minutes beforehand: the [critical path](docs/05-delivery/critical-path.md)
and [engagement](docs/00-event/engagement.md). Not the whole repo.

**Four things have to be true when we walk out.** Every work package has an owner *and* a host, and
they are different people. The three week-1 spikes are assigned with a Friday deadline. The
invitation list is written and goes out Wednesday. And we have decided what we are explicitly not
doing in two days.

Nine decisions are on the table with a recommendation against each, so the room is editing rather
than inventing. If a technical argument starts we are noting it and moving on. **The session's
product is names and dates**, not a settled architecture.

**Since Saturday.** Two component-scale figures, both drawn from deposited coordinates. One is the
same site at six scales, from the whole complex down to what a quantum code actually receives, with
the heavy-atom count at each. Between a 4 Å region and a 15 Å crop the quantum cost moves by more
than two orders of magnitude, which is why the crop radius is swept rather than chosen. The other is
the twenty residues lining the CDK9 pocket against the same positions in the three counter-targets.
Two of the twenty are positions where CDK9 differs from all three, and one of them — Cys106 at the
hinge, 3.2 Å from the ligand — is the whole selectivity argument in one atom.

That one is worth a note on method. The sequence pass guessed it and said the mapping was indicative
only. The structures confirmed it. Guess, then check.

**One thing the crop figure turned up that we had not thought about.** No cyclin T1 residue falls
within 15 Å of the ligand, so every radius we are considering drops the cyclin — and the cyclin is
what holds the αC helix in the active position. We are cropping away the thing that sets the
conformation we are trying to score. Nobody has checked whether it matters. It is now
[C7](docs/02-scope/open-questions.md), and it is red.

**New on the agenda: agentic development and operations.** Reviewed properly rather than waved
through, because it was the dominant theme at last year's event and four of the 2025 projects sit
directly on our stages. [The review](docs/05-delivery/proposals/2026-09-21-agentic-dev-ops.md) says
yes to the development half now, yes to exactly one narrow experiment, and no to letting an agent
drive the pipeline or submit jobs. Eight stages compound: an agent running the whole chain is the
worst place to put one. What we think is ours is smaller and more interesting — an agent at a
decision point is another surrogate, so it owes a fidelity contract, and nobody in that field writes
down a trust region.

**Next.** Owners and hosts named by tonight, [roles.md](docs/05-delivery/roles.md) and the
[open questions](docs/02-scope/open-questions.md) updated with them, and the email to the organisers
about our dates and a Valence Labs introduction. Invitations Wednesday.

*— Nick*

---

## 2026-09-19 · Week 0, repo up and dates set

**Dates.** Mon 19 to Tue 20 October, which are the two days we have. Wednesday the 21st is left
open, and it's the global event's opening day, so that's a reasonable way to carry the work across
if people want to keep going. The global event runs 21-22 October and registration is open to
anyone, so sign up for that regardless.

**What landed.** Scope, the stage decomposition S0 to S7, parameter space, metrics and six stage
gates, all written before any data exists. The month-long critical path, because two days can't
absorb a build and the dual GB10 boxes give us roughly 180 H200-equivalent hours beforehand. Six
onboarding ladders. Outreach collateral, brand aligned to the global event and co-branded with
Waipapa Taumata Rau. An isometric figure of the pipeline with the gates marked.

**Framing.** Settled on the baseline argument. We're handing every expensive step to a learned
surrogate and measuring how far the whole chain gets. Individual steps have been done well by
others, we haven't found the whole chain attempted, and it might not be good enough yet. We'd still
like the number, because each step is improving quickly and at some point it crosses a threshold.

**Two things worth knowing.** GB10 is aarch64 and H200 is x86_64, so anything containerised has to
build for both. It'll work fine on GB10 through weeks 2 and 3 and then the H200 run won't start.
One day of spike work removes it, and it's unclaimed, [#2](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/2).
Separately, Michael Craig of Valence Labs was on the 2024 kickoff panel, and Valence make Nesso-1,
which is currently a blocker. The organisers have a route to them.

**Next.** Monday's planning session. Name an owner and a host for every work package, assign the
three week-1 spikes, invitations out by Wednesday. The chain is invitations, then people, then
chemistry judgement, then the manifest, then everything else.

*— Nick*

---

<!--
ENTRY TEMPLATE — copy, don't delete.

## YYYY-MM-DD · Week N — <what actually happened, in six words>

**What landed**
- …

**What slipped, and why**
- …

**What we learned**
- …

**Numbers** (tag every one: [measured] / [estimate])
- …

**Next**
- …

*— name*
-->
