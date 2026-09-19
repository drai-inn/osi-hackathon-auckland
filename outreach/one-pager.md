# How far can a chain of surrogates get us?

**Open Scientific Intelligence Hackathon · Auckland site**

**{{DATES}} · {{VENUE}} · University of Auckland · Free**

---

## What we're trying

**Three things, in order.**

**1. Hand every expensive step to a learned surrogate.**
Individual steps have been done well by other groups. We haven't found anyone who ran the whole
chain.

**2. Measure where that lands, as a baseline.**
It might not be good enough yet. We'd still like the number. Every step is improving quickly, and
at some point the chain crosses a threshold. Without a starting point we won't know when.

**3. Get there by starting small.**
Twelve compounds. Two targets. A handful of quantum labels. Explore the parameter space properly at
that size, then scale only what survives.

## The testbed

Most drugs fail on selectivity rather than potency. A compound built for one protein also hits its
close relatives, and conventional screening can't separate them, because it flattens a
three-dimensional pocket into a fingerprint and throws away what makes two pockets different.

Our case is **CDK9 against CDK7**. Two kinases with ATP sites similar enough that telling them
apart is the whole difficulty.

## The trajectory

Four tiers. Each gate has to be green before we move up.

| Tier | Size | What it answers |
| --- | --- | --- |
| Smoke test | 5 ligands, 2 targets | Do the containers run, do the formats line up |
| **Hackathon** | **12-20 ligands, 3 poses, 20-50 labels** | **Do parameter changes move the ranking** |
| Useful pilot | 50-100 ligands, 4 targets | Ranking stability, cost per label |
| Scale-up | thousands, after filtering | Throughput and prioritisation |

The pipeline has about eight configurable choices and each combination costs GPU hours, so nobody
explores it properly. Recent work says that's the mistake. Small experiments fail to transfer
because they're under-explored, not because they're small.

What we want answered: is this even feasible, what data would we need, and how small can we go
while still being usefully robust.

## Who we need

| | What you'd do |
| --- | --- |
| **Medicinal chemistry / pharmacology** | Break our benchmark. Find the compounds our baseline gets wrong for reasons a chemist would call obvious |
| **Structural biology** | Triage predicted poses. Tell us which are nonsense, which we can't work out without you |
| **Quantum chemistry / physics** | When is a cheap approximation good enough, and how would you know? |
| **Statistics / ML** | Bring your own small-data problem. Twenty samples, eight parameters, no budget |
| **Research software engineering** | Make a multi-stage GPU pipeline someone else can run |
| **New to all of this** | Own one configuration. One command, twenty minutes, your name on a data point in the final analysis |

## What you get

- Two days on real hardware. Dual GB10 boxes and H200 access, and a pipeline that already works when
  you arrive, because we spend the month beforehand building it
- A result with your name on it. Every participant's contribution lands in an artifact
- A room of people from other disciplines who have the piece you're missing

## Three levels of commitment

1. **Full participant**, both days, embedded in a team
2. **Clinic participant**, 90 minutes on day 1 plus the day-2 presentations
3. **Reviewer**, read the plan, tell us what's wrong with it, come to the closing session

## The global event

We're a local site for the global Open Scientific Intelligence Hackathon, in its fourth year with
hubs on four continents. **It runs 21-22 October and registration is open to anyone**, so sign up
for that whether or not you come to ours. We're on 19-20 October because those are the two days we
have, and Wednesday the 21st is open if people want to carry the work into the global event.

---

**Global event and registration:** {{REGISTER}} · **Our details:** {{LINK}}
**Contact:** Nick Jones, njon001@aucklanduni.ac.nz

*A clean "no" is a good outcome. Six gates were written before any data existed, and if the chain
doesn't hold we'd rather know in two days than two years.*
