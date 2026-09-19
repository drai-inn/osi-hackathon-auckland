# Public presence — micro-repo, the main event site, and a date to resolve

**TL;DR:** Register Auckland as an **official hub of the OSI Hackathon**, run on the **official
dates (21–22 Oct NZDT)** rather than 19–20, keep this repo private as the team's working space,
and publish a **small public landing repo** for the Auckland hub. Do not fork the main site.

---

## 🔴 First: the dates do not match, and it matters

| Source | Dates |
| --- | --- |
| The flier you shared (`2026hackathon.pdf`) | **October 21–22, 2026** |
| [llmhackathon.github.io](https://llmhackathon.github.io/) | **October 21–22, 2026** |
| What this repo has been planning to | **19–20 Oct**, with US colleagues on 20–21 Oct |

That is a two-day offset, not a timezone artifact. It needs one email to resolve, and it should be
resolved before invitations go out on Wed 23 Sep — the date is on the poster.

### The case for moving to 21–22 Oct

**Auckland is already listed as a 2026 site in planning** on the
[sites page](https://llmhackathon.github.io/sites/), alongside Sydney, Singapore, Toronto, MIT,
Argonne, Johns Hopkins, NC State, UW–Madison, Chicago, Duke, New York and San Francisco. Someone
has already put us on the map. Running two days early forfeits most of what that gets us:

- the global Slack, the mentor pool, and 1000+ participants to interact with live
- eligibility for the Lila and Abstrax prizes and the Visionary awards
- **inclusion in the write-up paper** — the 2025 event produced a 120-project arXiv paper with
  every team credited. That is a publication for everyone in the room, including students
- the showcase session, and the audience that comes with it

And here is the part worth pausing on:

### On the official dates, Auckland is the first hub in the world to start

New Zealand is the first time zone. On 21–22 Oct NZDT:

| | NZDT | UTC | EDT | PDT |
| --- | --- | --- | --- | --- |
| **Auckland day 1 opens** | Wed 21 Oct 09:00 | Tue 20 Oct 20:00 | **Tue 20 Oct 16:00** | Tue 20 Oct 13:00 |
| Auckland day 1 closes | Wed 21 Oct 17:00 | Wed 21 Oct 04:00 | Wed 21 Oct 00:00 | Tue 20 Oct 21:00 |
| Auckland day 2 opens | Thu 22 Oct 09:00 | Wed 21 Oct 20:00 | Wed 21 Oct 16:00 | Wed 21 Oct 13:00 |
| **Auckland day 2 closes** | Thu 22 Oct 17:00 | Thu 22 Oct 04:00 | **Thu 22 Oct 00:00** | Wed 21 Oct 21:00 |

**Auckland opens the global hackathon**, sixteen hours before the US hubs wake up, and closes as
the US enters its final day. The handoff you wanted works *better* on the official dates than on
19–20 Oct: our close lands at midnight Eastern with the US teams' last day ahead of them, and
**21 Oct 09:00 NZDT is already 20 Oct 16:00 EDT** — a natural live slot on either side.

"First hub in the world to start" is also the single best line in every invitation and on the
poster. It is true, it is specific, and it is the kind of thing people show up for.

### If the 19–20 dates are deliberate

They might be — a deliberate precursor, or a constraint we don't know about. If so, the framing
changes but nothing breaks: Auckland becomes a **feeder event** that hands a working pipeline into
the global hackathon two days later, which is a legitimate and interesting thing to be. Say so
explicitly in the collateral, and consider sending one or two people into the global event to
carry the work forward.

**Either way: pick one, and pick it before Wednesday.** ([A7](../01-scope/open-questions.md))

---

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
[open-questions.md](../01-scope/open-questions.md) and
[risks.md](../05-feasibility/risks.md) are candid working documents and they are more useful that
way. Revisit after the event: the benchmark, the methodology note and the workflow template are all
things worth releasing, and the repo is better evidence of how the work was done than a polished
summary would be. ([E2](../01-scope/open-questions.md))

## Sequence

| | By |
| --- | --- |
| **Resolve the dates** — email Ben Blaiszik (blaiszik@uchicago.edu) or ask on Slack | **Mon 21 Sep** |
| Register the Auckland site; join Slack | Tue 22 Sep |
| Micro-repo live with the one-pager and FAQ | **Wed 23 Sep**, before invitations |
| Invitations out, pointing at the micro-repo | **Wed 23 Sep** |
| Hub description to the sites page | Fri 25 Sep |
| Poster distributed around UoA | Week of 28 Sep |
| Submit projects upstream; contribute to the write-up | Post-event |
