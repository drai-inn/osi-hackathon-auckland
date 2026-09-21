# Taking part

Two days, 19–20 October, at the University of Auckland. A local site of the global
[Open Scientific Intelligence Hackathon](the-global-event.md).

<<<<<<< HEAD:docs/00-event/taking-part.md
## What it actually is

A hackathon, not a workshop and not a conference. You come with your expertise and a problem, you
work on it for two days with people who don't share your background, and you show what happened.

**Come prepared to work with AI agents and with code.** That sounds like a filter and it's the
opposite of one. The agent writes the code; you supply the judgement about whether the answer is
any good, and that judgement is the part that's actually scarce. If you haven't written anything in
fifteen years, or ever, you are not behind here.

## How the two days run

**Bookends.** Each day opens and closes together. The opening sets what we're trying to find out;
the close is what we found, including what didn't work.

**Lightning talks, both days.** Short, rough, no slides required. The point is cross-pollination
between themes, not polish.

**Work in whatever grouping fits.** A theme might be twelve people or three. Inside it, work in ones,
twos and threes on specifics. Nobody is assigned. If two people from different themes want to spend
an afternoon on something neither team planned, that's a good sign, not a problem.

**Food and a social occasion each day.** The conversations that matter usually happen there.

## Coming as a team

We're inviting **project teams**. A group leader brings their team, their expertise, and a problem or
candidate they want to look at.

**If you can only come for the start, come for the start.** Be there for the opening, get your hands
on it, then leave your team to it. That's an expected pattern and a completely legitimate way to take
part — we'd much rather have your group in the room than lose all of you to a diary.

## Coming on your own

Also fine. Turn up, pick a [theme](themes.md), find one or two people to work with.

## The rules of the room

- **No stupid questions.** Most of us are new to most of this. The person asking the basic question
  is usually asking the one everyone else wanted to.
- **It's safe to experiment.** Nothing here is production. Breaking something is a result.
- **A negative is a result.** "We tried it, here's where it fell over" is more useful to everyone
  else in the room than a demo that worked.
- **Show the thing, not the slides.**

## What to bring

A laptop. A problem you care about, or the willingness to pick one up. That's it — the compute,
the targets, the data and the environments are set up before you arrive.

## Following along without coming

The [live log](../../EVENT-LOG.md) is one pull request you can subscribe to. It closes when the work
is finished, and that's the only signal you need.
=======
## What it is

A hackathon. You come with your expertise and a problem, work on it for two days with people who
don't share your background, and show what happened.

**Come prepared to work with AI agents and with code.** The agent writes the code. You bring the
judgement about whether the answer is any good. Everyone is welcome here, whatever you last wrote
and whenever you last wrote it.

## The shape of the two days

**Day 1 — get running, do something, work out what to measure, report back.** You can pick a
benchmark once you've seen a model behave, so that comes after the running. The end of day 1 is
everyone reporting what they found and what they think their benchmark should be.

**Day 2 — measure it, and report what you got.** Including the negatives, which are often the more
useful half.

## Benchmarks and data

Each group conceptualises and sources its own. Measuring what a filter throws away at the top of a
library and detecting when an interatomic potential has left its training distribution are
different problems, so each theme designs its own evaluation.

Working out what to measure is a good part of the work.

### The four questions

Groups stay comparable by answering the same four questions about whatever they picked. This is the
day-1 report-back:

1. **What's your ground truth?**
2. **What are you comparing against, and is there a simple baseline in there?**
3. **What would change your mind?**
4. **Where would it break?**

Question 2 is worth taking seriously. A recent benchmark found single-cell foundation models level
with a simple linear baseline at predicting perturbation effects, and another found the choice of
metric changes which model comes out on top. Running the simple baseline is how you find out.

## Getting set up

**Agentic support plus our team.** Ask the agent first and us second, and you shouldn't need to
spend day 1 on an environment. The models behind that are open-weight and chosen in advance —
see [agentic-models.md](agentic-models.md).

At least one model per theme will be known to run on our hardware before anyone arrives, so there's
always something that starts.

## How the two days run

**Bookends.** Each day opens and closes together. Day 1 closes on the four questions, day 2 on what
you got.

**Lightning talks, both days.** Short, rough, no slides required, so themes hear what the others are
finding.

**Work in whatever grouping fits.** A theme might be twelve people or three. Inside it, work in ones,
twos and threes on specifics. Nobody is assigned. Two people from different themes spending an
afternoon on something neither group planned is a good sign.

**Food and a social occasion each day.** Some of the best conversations happen there.

## Coming as a team

We're inviting **project teams**. A group leader brings their team, their expertise, and a problem
or candidate they want to look at.

**If you can only come for the start, come for the start.** Be there for the opening, get your hands
on it, then leave your team to it. That's a completely normal way to take part, and we'd rather have
your group in the room than lose all of you to a diary.

## Coming on your own

Also welcome. Turn up, pick a [theme](themes.md), find one or two people to work with.

## The rules of the room

- **No stupid questions.** Most of us are new to most of this, and the basic question is usually the
  one everyone else wanted answered.
- **It's safe to experiment.** Nothing here is production. Breaking something is a result.
- **A negative is a result.** "We tried it, here's where it fell over" is useful to everyone in the
  room.
- **Show the thing. Slides optional.**

## What to bring

A laptop, and a problem you care about or the willingness to pick one up. The compute, the targets,
the data and the environments are set up before you arrive.

## Following along without coming

The [live log](../EVENT-LOG.md) is one pull request you can subscribe to. It closes when the work is
finished.
>>>>>>> main:docs/taking-part.md
