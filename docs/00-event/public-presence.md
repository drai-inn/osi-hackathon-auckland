# Public presence

**TL;DR:** We run 19-20 October. Keep the connection to the global event and promote its
registration, ask what a site on other dates can still join, publish a small public landing page
for Auckland, and don't fork the main site. This repo stays private for now.

---

## Our dates

We run **Monday 19 to Tuesday 20 October**. The global event runs 21-22 October. Ours are the two
days we have ([ADR-0006](../adr/0006-run-19-20-october-as-a-precursor.md)), and Wednesday the 21st
is left open in case people want to carry the work into the global event's opening day.

Posture: we're a local site, not a headline act. The copy points people at the global event and its
registration, which is open to anyone, and doesn't make anything of our scheduling. Most of the
audience won't notice or care about the offset, and there's more value in giving the global event
exposure than in explaining ours.

### What to ask the organisers

Running on other dates is unusual, so ask rather than assume
([A10](../02-scope/open-questions.md)):

- Can we still submit projects and be credited in the write-up paper?
- Can we keep a Slack presence, and mentor access during our two days?
- Can we hold the Auckland site listing with our own dates on it?
- Would our outputs be useful to other sites if we publish them before the 21st?

Worst case the answers are no, and we've still run a good two days with our own people and our own
hardware.

### Staying connected

Auckland is already listed as a 2026 site on the
[sites page](https://llmhackathon.github.io/sites/), alongside Sydney, Singapore, Toronto, MIT,
Argonne, Johns Hopkins, NC State, UW-Madison, Chicago, Duke, New York and San Francisco.

What's worth protecting, in order:

1. **The write-up paper.** The 2025 event produced a 120-project arXiv paper crediting every team.
   That's a real publication for everyone in the room, including students, and it's the most
   persuasive line in a recruitment email. Ask whether we can still submit
2. **The Slack and the mentor pool**, which is how collaborators find us
3. **The site listing**, with our dates on it
4. Prizes and the showcase, which we probably aren't eligible for and shouldn't plan around

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

Small, specific, useful, the things a hub is expected to provide:

1. **Register the Auckland site** via the express-interest form; confirm the listing moves from
   "in planning" to confirmed with a named local lead and contact, as Duke's has
   (Defne Çirci, defne.circi@duke.edu)
2. A short hub description and venue details for the sites page
3. Join the [Slack](https://llmhackathon.github.io/) and say what Auckland is working on, that is
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
or five pages. It links *to* the main site for registration rather than duplicating it, we do not
want to run our own registration.

**Recommendation:** create it in `drai-inn`, public, GitHub Pages from `main`. Source lives in
[`outreach/site/`](../../outreach/) in this repo initially and moves out once it stabilises, so
there is one place to edit while the details are still changing.

### What stays private

This repo, for now. Not because anything is secret, because
[open-questions.md](../02-scope/open-questions.md) and
[risks.md](../06-feasibility/risks.md) are candid working documents and they are more useful that
way. Revisit after the event: the benchmark, the methodology note and the workflow template are all
things worth releasing, and the repo is better evidence of how the work was done than a polished
summary would be. ([E2](../02-scope/open-questions.md))

## Sequence

| | By |
| --- | --- |
| Email Ben Blaiszik (blaiszik@uchicago.edu): our dates, what we can still join, and an intro to Valence Labs re: Nesso-1 | **Mon 21 Sep** |
| Join Slack; sort out the site listing | Tue 22 Sep |
| Micro-repo live with the one-pager and FAQ | **Wed 23 Sep**, before invitations |
| Invitations out, pointing at the micro-repo | **Wed 23 Sep** |
| Hub description to the sites page | Fri 25 Sep |
| Poster distributed around UoA | Week of 28 Sep |
| Submit projects upstream; contribute to the write-up | Post-event |
