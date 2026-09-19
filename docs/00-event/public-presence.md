# Public presence — our dates, the main event site, and the micro-repo

**TL;DR:** We run **19–20 October**, two days ahead of the global OSI Hackathon, as a deliberate
precursor. Keep the connection to the global event, ask what a precursor can still join, publish a
**small public landing repo** for the Auckland hub, and **do not fork the main site**. This repo
stays private for now.

---

## ✅ Resolved: we run 19–20 October, two days ahead of the global event

The global [OSI Hackathon](the-global-event.md) is **21–22 October** and Auckland is listed as a
2026 site in planning. We are not aligning with it, for a plain reason: **we cannot run past the
21st, and the 21st itself collides with other commitments.** The two contiguous days we actually
have are the 19th and 20th.

**Extending into Wednesday 21 October is an option we keep, not a plan we make.** If the work is
live and people want to keep going, the 21st is available — and it is the global hackathon's
opening day, which makes the extension a bridge rather than an overrun.

Recorded in [ADR-0006](../adr/0006-run-19-20-october-as-a-precursor.md).

### What that timing actually gives us

| | NZDT | UTC | EDT |
| --- | --- | --- | --- |
| Our day 1 opens | Mon 19 Oct 09:00 | Sun 18 Oct 20:00 | Sun 18 Oct 16:00 |
| **Our day 2 closes** | **Tue 20 Oct 17:00** | **Tue 20 Oct 04:00** | **Tue 20 Oct 00:00** |
| Earliest global hub opens | Wed 21 Oct 09:00 | Tue 20 Oct 20:00 | Tue 20 Oct 16:00 |
| US east-coast hubs open | Thu 22 Oct 02:00 | Wed 21 Oct 13:00 | Wed 21 Oct 09:00 |

**We finish 16 hours before the earliest hub in the world starts, and 33 hours before the US
sites.** Everything we produce is on the table before anyone else begins.

Frame it as the position it is: we are not hub number thirteen competing for attention mid-event.
We are the **precursor** — we go first, we publish, and the global hackathon starts with our
benchmark, our workflow and our results already available.

**The line is "two days ahead of the world", not "first hub to start."** The second is no longer
true and has been removed from the collateral.

### What to ask the organisers

A precursor is an unusual thing to be, so ask rather than assume
([A10](../02-scope/open-questions.md)):

- Can we still **submit projects** and be credited in the write-up paper?
- Can we keep a presence in the Slack, and mentor access during our two days?
- Can we still hold the Auckland site listing, marked with our own dates?
- Would they like our outputs published into the event's opening — a benchmark and a working
  workflow arriving before day 1 is useful to other hubs, not just to us

Worst case all the answers are no, and we have still run a good two days with our own people and
our own hardware. Best case we are a genuinely useful contributor to an event we are not formally
inside.

## Micro-repo or contribute to the main site?

Short answer: **both, but not the way it first looks.** They serve different audiences.

| | Main event site | Auckland public micro-repo | This repo |
| --- | --- | --- | --- |
| Audience | Global participants | **Local prospective participants** | The team |
| Owner | Ben Blaiszik / organisers | Us | Us |
| Content | Dates, hubs, rules, prizes | Why come to *this* room, who we are, what we'll build | Scope, stages, gates, working docs |
| Lifetime | The event | Grows into the programme's public face | Until the work outgrows it |
| Visibility | Public | **Public** | Private for now |

### What to contribute upstream

Small, specific, useful — the things a hub is expected to provide:

1. **Register the Auckland site** via the express-interest form; confirm the listing moves from
   "in planning" to confirmed with a named local lead and contact, as Duke's has
   (Defne Çirci, defne.circi@duke.edu)
2. A short hub description and venue details for the sites page
3. Join the [Slack](https://llmhackathon.github.io/) and say what Auckland is working on — that is
   how mentors and collaborators find us
4. **After the event: our project submissions**, which is how we get into the write-up paper

**Do not fork or rebuild the main site.** It is theirs, it works, and a competing page splits the
signal. Contribute a hub entry and a Slack presence; that is the whole upstream ask.

### What the micro-repo is for

A public GitHub Pages site at `drai-inn.github.io/osi-auckland` (or similar) doing four jobs the
main site cannot:

- **Local recruitment.** "Auckland hub" on the global site is a line item. A page that says *who is
  running it, what we are building, which disciplines we want, and what you will personally get
  out of two days* is what converts a UoA researcher into a participant
- **The on-ramp landing page.** Pre-reads, the glossary, setup instructions, what to bring
- **A public face for the programme after the event.** Results, the benchmark release, the
  write-up, and the next thing
- **Somewhere to point an invitation email.** Every invitation needs one link

Keep it genuinely small: index, about the science, who should come, on-ramps, FAQ, contact. Four
or five pages. It links *to* the main site for registration rather than duplicating it — we do not
want to run our own registration.

**Recommendation:** create it in `drai-inn`, public, GitHub Pages from `main`. Source lives in
[`outreach/site/`](../../outreach/) in this repo initially and moves out once it stabilises, so
there is one place to edit while the details are still changing.

### What stays private

This repo, for now. Not because anything is secret — because
[open-questions.md](../02-scope/open-questions.md) and
[risks.md](../06-feasibility/risks.md) are candid working documents and they are more useful that
way. Revisit after the event: the benchmark, the methodology note and the workflow template are all
things worth releasing, and the repo is better evidence of how the work was done than a polished
summary would be. ([E2](../02-scope/open-questions.md))

## Sequence

| | By |
| --- | --- |
| ~~Resolve the dates~~ | ✅ **19–20 Oct** ([ADR-0006](../adr/0006-run-19-20-october-as-a-precursor.md)) |
| Email Ben Blaiszik (blaiszik@uchicago.edu): our dates, what a precursor can still join, and an intro to Valence Labs re: Nesso-1 | **Mon 21 Sep** |
| Join Slack; sort out the site listing | Tue 22 Sep |
| Micro-repo live with the one-pager and FAQ | **Wed 23 Sep**, before invitations |
| Invitations out, pointing at the micro-repo | **Wed 23 Sep** |
| Hub description to the sites page | Fri 25 Sep |
| Poster distributed around UoA | Week of 28 Sep |
| Submit projects upstream; contribute to the write-up | Post-event |
