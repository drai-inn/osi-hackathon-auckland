# 📡 Live event log — Auckland Hub

**This file lives on the `event-log` branch and its pull request stays open until the final
presentations and reports are done.**

**To follow:** open the PR and click **Subscribe**. Every update is a commit here — you get those
and nothing else. No issue noise, no CI. **When the PR closes, the work is finished.** That's the
only signal you need.

**To post:** commit to `event-log`. Newest at the top. Short, dated, honest — including what broke.
A log that only records progress isn't worth following, and isn't what happened.

Cadence: **weekly** through the month, **daily** during 19–20 October.

| | |
| --- | --- |
| **Event** | Mon 19 – Tue 20 Oct 2026, University of Auckland |
| **Global event** | 21–22 Oct — we run two days ahead |
| **What this is** | [The narrative](docs/00-event/narrative.md) · [Pick a ladder](docs/00-event/onboarding/README.md) |
| **Plan** | [Critical path](docs/05-delivery/critical-path.md) · [Issues](https://github.com/drai-inn/drugs-surrogate-pipeline/issues) |

---

## Status board

Updated with each entry. The honest version, not the reassuring one.

| | |
| --- | --- |
| **Week** | Week 0 — pre-kickoff |
| **Next gate** | Fri 25 Sep — *we know what runs where* |
| **🔴 Blocking** | Owners and hosts unnamed · architecture spike unclaimed · cuEST unresolved · H200 unbooked |
| **Recently resolved** | ✅ Dates: **19–20 Oct** ([ADR-0006](docs/adr/0006-run-19-20-october-as-a-precursor.md)) |
| **Compute** | GB10 ×2 assumed available, unconfirmed · H200 unbooked |
| **People** | 0 of 6 packages have a named owner |

---

## 2026-09-19 · Week 0 — the repo exists, and the dates are locked

**Dates settled: Mon 19 – Tue 20 October.** We can't run past the 21st and the 21st has competing
agendas, so we go two days ahead of the global hackathon rather than alongside it. Extending into
Wednesday the 21st stays an option we take in the moment — and since that's the global event's
opening day, an extension is a bridge rather than an overrun.
[ADR-0006](docs/adr/0006-run-19-20-october-as-a-precursor.md).

That turns out to be a better position than it first looked. We close 16 hours before the earliest
hub in the world opens and 33 before the US sites, so everything we produce is on the table before
anyone else starts. We're not hub number thirteen competing for attention mid-event — we're the
precursor supplying it. The line is **"two days ahead of the world"**; *"first hub to start"* was
true only on the official dates and has been removed everywhere.

**What landed this week**

- Scope, stage decomposition (S0–S8), parameter space, metrics and six stage gates — all written
  before any data exists, which is the point
- The month-long critical path. Two days can't absorb a build, so everything a five-day event would
  have put on "day 1" moves into the four weeks before. Dual GB10 boxes for the month are what make
  that possible: ~180 H200-equivalent hours, over half the whole workload
- Six onboarding ladders, because nobody should have to read this repo to be useful in it
- Outreach collateral, brand aligned to the global event, and an A3 poster
- Reviewed three years of the global hackathon — 14, 34 and 120 projects — and tabulated who to
  talk to

**Two things worth knowing**

**The architecture split.** GB10 is `aarch64`; H200 is `x86_64`. Everything will work beautifully on
GB10 through weeks 2 and 3 and then the H200 run won't start. One day of spike work removes it
entirely. It's the most under-appreciated risk in the project and it's unclaimed —
[#2](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/2).

**Valence Labs.** Michael Craig of Valence Labs — who make Nesso-1 — was on the 2024 kickoff panel.
Whether Nesso-1 is fine-tunable is currently a 🔴 blocker, and the organisers have a route to them.

**Next**

Monday's 2-hour planning session: name an owner *and* a host for every package, assign the three
week-1 spikes, and get invitations out by Wednesday. The chain is
*invitations → people → chemistry judgement → manifest → everything*, and it starts on Monday.

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
