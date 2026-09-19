# Contributing

This repo belongs to a **hackathon**, and hackathons have a different shape from software projects.
Worth being explicit about it, because the usual contributing guide would give you the wrong idea.

---

## What kind of thing this is

**A two-day event with a month of preparation in front of it and a report behind it.** Not a
product. Not a long-running codebase. It exists to answer three questions and then either scale up
or stop:

1. Which parameters matter?
2. Which stages add measurable value?
3. How small can the benchmark be and still produce signal worth acting on?

Three consequences that shape everything below.

**Deadlines are real and short.** [critical-path.md](docs/05-delivery/critical-path.md) has dates,
and 19 October does not move. A contribution that lands on the 21st is a contribution to phase 2.

**A negative result is a success.** Six [gates](docs/06-feasibility/stage-gates.md) were written
before any data existed. Nobody here is trying to make the method work, we're trying to find out
whether it does. If your analysis kills a stage, you have done the most valuable thing available.

**Most contributions are not code.** A medicinal chemist saying "those two IC50s aren't comparable"
prevents a week of wasted work. That is a larger contribution than any pull request, and the repo
should make it as easy to record.

## What counts as a contribution

All of these. In rough order of how often they're undervalued:

| | How to make it |
| --- | --- |
| **Telling us something is wrong** | Issue, PR comment, or the surprises board. No format required |
| **Domain judgement**, pose annotations, benchmark critique, assay calls | Your host records it; it lands in an artifact with your name |
| **A question from outside your discipline** | Surprises board. Assumptions survive because everyone in a subfield shares them |
| **Running a configuration** | The launcher. Your run is a data point in the analysis |
| **A measurement replacing an `[estimate]`** | PR to the relevant doc, tagged `[measured]` |
| **Documentation, a diagram, a clearer sentence** | PR |
| **Code** | PR against a frozen interface |

## How we work

### Provenance tags on every number

Each quantitative claim carries one:

| Tag | Meaning |
| --- | --- |
| `[measured]` | Someone ran it and recorded it |
| `[source-doc]` | From the origin document |
| `[literature]` | Published, cited |
| `[estimate]` | A guess, flagged as one |

**An untagged number is a bug.** Most of the compute budget is `[estimate]` and says so loudly;
converting those to `[measured]` is much of the month's work.

### Intervals, not point estimates

At n≈20 ligands a Spearman ρ has a standard error around ±0.2. A difference of 0.05 between two
configurations is nothing. **Every reported metric carries a bootstrap 95% interval over ligands.**
Protocol in [metrics.md](docs/04-experiments/metrics.md#statistical-protocol).

This is not fussiness. With this sample size it is the entire difference between a finding and a
plausible story.

### Interfaces are frozen; decisions get an ADR

[interfaces.md](docs/03-pipeline/interfaces.md) freezes on **2 Oct**. Object before then, freely.
Afterwards, changing one needs an [ADR](docs/adr/), cheap to write, and it stops the same argument
recurring every three weeks. Same for anything that moves scope.

### Open questions stay open

[open-questions.md](docs/02-scope/open-questions.md) is the project's honest edge. When you find
something uncertain, add a row with an owner. Don't paper over it with a plausible assumption. When
it resolves, keep the row and add the answer.

## Norms in the room

- **No one debugs alone.** Fifteen minutes stuck is a host's failure, not yours. Say something at
  minute fourteen
- **The two-minute rule.** At standup, explain yesterday to someone outside your discipline in two
  minutes. If you can't, that's a finding about the work
- **Questions go on the surprises board**, not into a private conversation. Several will be better
  than the assumptions they question
- **Owners and hosts are different people.** Owners drive the technical work; hosts look after the
  people attached to it. In a two-day sprint the owner would choose the work every time and nobody
  would have done anything wrong. [Why](docs/00-event/engagement.md#the-structural-fix-split-the-host-role)
- **No jargon without a [glossary](docs/02-scope/glossary.md) link.** Six disciplines are in the
  room and nobody understands more than two of them

## Git

Small commits, one topic per PR. Work on `main`; branch for anything reviewable. Every stage owner
maintains their own stage page.

One exception: **`EVENT-LOG.md` lives on the long-running `event-log` branch** and is not merged
until the work is finished. See below.

```bash
make validate    # check a benchmark manifest
make budget      # recompute the GPU-hour estimate
make check       # everything
```

Both tools are standard-library-only on purpose: anyone can run them on day 1 without setting up an
environment.

## The live event log

We keep **[`EVENT-LOG.md`](EVENT-LOG.md)** as a single pull request that stays open from now until
the final presentations and reports are done. It is the project's public heartbeat.

**To follow:** open the PR, click **Subscribe**. You'll get every update and nothing else, no issue
noise, no CI. It closes when the work is finished, which is the only signal anyone needs.

**To post an update:** commit to the `event-log` branch. Newest entry at the top, dated, short.
Weekly through the month, daily during the event.

**Write down what went wrong too.** A log that only records progress isn't worth following, and it
is not what happened.

## Credit

- **Everyone in the room is named in the artifacts.** That's a design goal, tracked as one of the
  three [engagement outcomes](docs/00-event/engagement.md#how-we-know-it-worked)
- If we submit to the global event's write-up, previous years have **credited every team member** -
  the 2025 paper documented 88 projects and listed every contributor
- Anything published out of this credits contributors by contribution, not by seniority. If you
  curated the benchmark, you're on the benchmark paper
- Ownership and IP: [E1](docs/02-scope/open-questions.md), being resolved before invitations go out.
  Ask if it matters to you, better now than after

## Conduct

Be decent. Assume the person asking the obvious question is the one who will spot the thing everyone
else missed, because that is usually what happens. The event follows the global hackathon's safety
and accessibility expectations; if something's wrong, tell Nick.
