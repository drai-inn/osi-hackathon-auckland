# How far can a chain of surrogates get us?

**Open Scientific Intelligence Hackathon · Auckland site**

**{{DATES}} · {{VENUE}} · University of Auckland · Free**

---

## What we're trying

We want to try a more AI-intensive approach to a structure-based pipeline, where every expensive
step is handed to a learned surrogate, and see how far that actually gets us today.

Other groups have done individual steps well. We haven't found anyone who has run the whole chain
end to end, with the expensive physics kept only for the places where it changes the answer.

It might not be good enough yet. We'd still like the number. Every step in the chain is improving
quickly, and at some point it crosses a threshold and becomes useful. Without a measured starting
point we won't know when that happens. So this is a baseline, taken carefully enough to be worth
repeating.

## The testbed

Most drugs fail on selectivity rather than potency. A compound built for one protein also hits its
close relatives, and conventional screening can't separate them, because it flattens a
three-dimensional pocket into a fingerprint and throws away what makes two pockets different.

Our case is **CDK9 against CDK7**. Two kinases with ATP sites similar enough that telling them
apart is the whole difficulty.

## How we're measuring it

The pipeline has about eight configurable choices and each combination costs GPU hours, so nobody
explores it properly. Recent work suggests that's the thing that goes wrong: small experiments fail
to transfer because they're under-explored, not because they're small.

So we start small and explore the parameter space in parallel across the phases, then try an
integrated run. What we want to answer is whether this is even feasible, what data we'd need, and
how small we can go while still being usefully robust.

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
