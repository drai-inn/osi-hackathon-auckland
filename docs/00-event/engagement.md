> **⚠️ Pre-pivot. Kept for reference, not current.**
> On 21 Sep we moved from work packages and named owners to **four open themes and invited
> project teams**. Start at [the themes](themes.md) and [taking part](taking-part.md).
> Superseded by taking-part.md. The design principle — you should own a result — survives.

# Engagement design, high-impact experiences for people new to AI for science

**Priority, stated plainly:** several participants will be experts in their own field and new to
this way of working. A two-day event can give them a genuinely formative experience or two days of
watching other people debug. The difference is entirely in what we build during the month.

---

## The design principle

> A newcomer's experience is good when they **personally own a result the group actually uses**.

Not a tutorial. Not shadowing. Not a demo. A real, small, owned contribution that appears in the
final analysis with their name on it, produced using expertise they already have.

Three corollaries that shape everything below:

1. **Time to first result under 30 minutes.** Measured, with a real novice, in week 4
   ([W4.2](../05-delivery/critical-path.md#week-4--1218-oct--rehearse-and-pre-compute)). If it takes longer, the
   on-ramp is broken, not the person.
2. **Their domain expertise is the input, not their coding.** A medicinal chemist contributes by
   looking at poses and saying which are wrong, a judgement we cannot generate computationally and
   genuinely need.
3. **Visible contribution to the shared result.** Their run appears on the dashboard. Their
   annotations appear in the metrics. Their name is on it.

## The structural fix: split the host role

In a two-day sprint the work-package owner cannot both drive the technical work and look after
newcomers. They will choose the technical work, every time, and nobody will have done anything
wrong.

**Each work package has a named *host* who is not the owner.** The host's job is the people
attached to that package: getting them started, keeping them unblocked, making sure their
contribution lands in the output. It is a real job and it should be assigned by name on Monday.

---

## The on-ramps

Six, each independently valuable. Pre-built during the month; none require setup on the day.

### A, "Your run, your parameter" · *anyone, including non-coders* · 20 min

Each person is allocated one configuration from the random search. One command on a GB10 box. Their
run appears on the live dashboard within twenty minutes, and their data point is in the day-2
sensitivity analysis.

This is the highest-value on-ramp because it is *literally* the experiment: the
[methodology](../04-experiments/methodology.md) needs many configurations, and a room of people
each owning one is a better use of the room than a queue script.

**Build (month):** launcher script, allocation scheme, live dashboard ([W3.6](../05-delivery/critical-path.md)).
**Owner:** WP-F.

### B. Pose triage · *structural biology, medicinal chemistry* · zero code

A viewer showing co-folded poses. Mark each plausible / implausible / uncertain, with a one-line
reason. Produces the human ground truth for
[fidelity contract 1](../03-pipeline/fidelity-contracts.md#1-co-folding-s1--replaces-experimental-structure-determination)
and a labelled set we cannot produce any other way.

Say this out loud when introducing it: **the computational team cannot do this, and the result is
worse without it.** That is true, and it is the difference between feeling useful and being useful.

**Build (month):** pre-generate poses; simple web or PyMOL-based viewer with a results file
([W4.4](../05-delivery/critical-path.md)). **Owner:** WP-B + host.

### C. Break the benchmark · *medicinal chemistry, pharmacology* · 60 min

Here are the 2D baseline's predictions on our compounds. Find the ones it gets wrong for reasons a
chemist would call obvious. Every hit is a benchmark improvement, a talking point, and evidence
about whether our negatives are discriminating or trivial.

This directly attacks [R2](../06-feasibility/risks.md), the highest-probability project-threatening
risk in the register.

**Build (month):** baseline computed and presented as a browsable table ([W2.6](../05-delivery/critical-path.md)).
**Owner:** WP-A + host.

### D. Sealed forecast · *everyone* · 10 min, day 1 opening

Before any results, everyone writes down their predictions on six binary questions matching the
[gates](../06-feasibility/stage-gates.md): *Will motion-awareness improve ranking stability? Will
uncertainty-guided labelling beat random?* Sealed. Opened on day 2.

Costs nothing, creates investment, makes the day-2 reveal a moment, and it teaches the single most
transferable lesson in AI for science, which is that expert intuition about what will work is
poorly calibrated and worth checking. A newcomer who discovers they predicted better than the
experts has had a very good two days.

**Build (month):** six questions drafted ([W3.7](../05-delivery/critical-path.md)), a form, sealed envelopes or a
locked sheet. **Owner:** Nick.

### E. Bring your own small-data problem · *visiting researchers, statisticians, any empirical field* · 90 min

The [Activity 2 clinic](../05-delivery/adjacent-activities.md#activity-2--small-data-hyperparameter-science).
Participants map their own expensive-experiment problem onto the search-space spec and leave with a
protocol for their own work.

The widest door in the programme: the question, *when does a small experiment predict the large
one?*, belongs to ecology, clinical research, materials and education just as much as to us.

**Build (month):** the spec format and a worked example. **Owner:** methodology lead.

### F. Explainer pairs · *everyone* · 5 min per package, day 1

Each work package explains itself to a newcomer in five minutes, no slides. The newcomer's questions
are the deliverable.

Cheapest quality control available: the assumptions that survive because everyone in a subfield
shares them are exactly the ones a smart outsider asks about in the first two minutes.

**Build (month):** nothing. **Owner:** each host.

---

## Matching people to on-ramps

| Background | Start with | Then |
| --- | --- | --- |
| Medicinal chemistry / pharmacology | C, break the benchmark | B, then embed in WP-A |
| Structural biology | B, pose triage | Embed in WP-B |
| Quantum chemistry / physics | A, your run | [Activity 3](../05-delivery/adjacent-activities.md#activity-3--the-fidelity-ladder-quantum-surrogates-and-knowing-when-to-trust-them), embed in WP-E |
| Statistics / ML methods | E, bring your own problem | A, then the sensitivity analysis |
| RSE / eResearch | A, your run | Embed in WP-F |
| Empirical researcher from an unrelated field | D, then E | A |
| Student / early career, any field | A, your run | B or C depending on background |

Everyone does D. Nobody does more than two on-ramps before embedding.

## Rules for the room

- **No one debugs alone.** A newcomer stuck for fifteen minutes is a host's failure, not theirs.
- **The dashboard is public and shows names.** Contribution should be visible without anyone having
  to claim it.
- **Questions from newcomers go on the surprises board**, not into a private conversation. Several
  will be better than the assumptions they question.
- **No jargon without a glossary link.** [glossary.md](../02-scope/glossary.md) exists for this and
  should be printed and on the tables.
- **Two-minute rule at standup:** if you cannot explain what you did yesterday to someone outside
  your discipline in two minutes, that is the finding.

## How we know it worked

Not a feedback form. Three observable things:

1. Every participant's name appears in at least one artifact in `artifacts/` by the end of day 2.
2. The novice dry run in week 4 hit first result in under 30 minutes.
3. At least three questions on the surprises board came from people outside the package they
   questioned.

If all three hold, the engagement worked whatever the pipeline did.
