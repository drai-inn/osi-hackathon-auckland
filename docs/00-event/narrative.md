# The narrative

What we're doing and why. All the outreach copy in [`outreach/`](../../outreach/) is cut from
this, so change it here first.

---

## The short version

> ### How far can a chain of surrogates get us?

We want to try a more AI-intensive approach to a structure-based pipeline, where every expensive
step is handed to a learned surrogate, and see how far that actually gets us today.

Other groups have done individual steps well. We haven't found anyone who has run the whole chain
end to end, with the expensive physics kept only for the places where it changes the answer.

It might not be good enough yet. We'd still like the number. Every step in the chain is improving
quickly, and at some point the chain crosses a threshold and becomes useful. Without a measured
starting point we won't know when that happens.

So this is a baseline, taken carefully enough to be worth repeating.

---

## 1. The problem we're testing it on

Most drugs fail on selectivity rather than potency. A compound built for one protein also hits its
close relatives, and the programme fails late and expensively.

Conventional screening is good at "does this bind something" and poor at "why would this bind this
pocket and not its near-twin". It flattens a three-dimensional pocket into a fingerprint, which
throws away the things that separate two similar pockets: local geometry, induced fit,
electrostatics, and how both protein and ligand move.

Our case is CDK9 against CDK7. Two kinases with ATP sites similar enough that telling them apart is
the whole difficulty. There's enough public data to build a defensible benchmark, and there are
known selective and known pan-CDK compounds, so we have real discriminating cases rather than
actives against random decoys.

## 2. The chain

Eight steps. Each one cheap enough to run on everything that reaches it, and each allowed to be
wrong in a characterised way that the next step is there to correct.

Generate plausible complexes, crop the pocket, sample how it moves, score the geometry, send only
the genuinely uncertain cases to quantum chemistry, learn from those labels, repeat.

![The eight steps, what passes between them, and where the gates sit](../03-pipeline/figures/pipeline-isometric.svg)

Four of those steps hand an expensive calculation to a learned model: co-folding instead of
experimental structure determination, learned ensembles instead of molecular dynamics, an
equivariant network instead of physics-based rescoring, and a learned correction instead of running
quantum chemistry on everything.

Versions of each exist. At the 2025 hackathon alone there was a docking tool using a machine-learned
potential as its scoring function, an agent that ran protein-ligand MD end to end, and an assistant
for setting up DFT calculations. What we haven't found is the four assembled into one chain with a
budget discipline across it, which is the thing we'd like to measure.

## 3. Why it's worth measuring even if it fails

A surrogate can be fast, confident and wrong. It can also be accurate on average while being wrong
on exactly the close calls the pipeline exists to resolve. Chain four of them together and the
errors compound in ways nobody has characterised, because nobody has chained them.

So each one has to declare where it can be trusted. Every surrogate in the pipeline carries a
fidelity contract: a stated ground truth, a validation set that contains close calls, and a region
outside which it isn't believed. A surrogate with a correlation coefficient and no trust region
isn't a method, it's a hope.

What we expect to come out is a number for how far the chain gets, and which links are dragging.
That's useful now for deciding where to spend, and useful later as the comparison point when we run
it again with better components.

## 4. How we're measuring it

The pipeline has around eight configurable choices. How much protein to include, how many
conformations to sample, how accurate the quantum calculation needs to be, how aggressively to
spend the expensive budget. Each combination costs GPU hours, and nobody can explore that at
production scale, so the usual approach is to guess most of it and tune two or three knobs on a
small grid.

Recent work on small-scale machine learning experiments suggests that's the thing that goes wrong.
Small experiments fail to transfer not because they're small, but because they're under-explored,
and small systems turn out to be more sensitive to their settings than large ones. In that work,
four configurations showed nothing, sixteen showed nothing, and 256 gave a clean predictive answer.

So we're treating the configuration as the object of study rather than a set of settings to guess.
Start small, explore the parameter space properly, and carry up only what survives. The questions
we actually want answered are: is this even feasible, what data would we need, and how small can we
go while still being usefully robust.

That last one travels well beyond drug discovery. Anyone with one field season, a small cohort, or
a three-week synthesis has the same problem. A pipeline of choices, an expensive evaluation, and no
way to grid-search. It's part of why this is a cross-disciplinary event.

*(This thread came out of a conversation with Jack Flanagan, who suggested hyperparameter
optimisation on small datasets as a microtopic and asked where the big wins are that scale. It's
written up in [hpo-microtopic.md](../04-experiments/hpo-microtopic.md).)*

## 5. What we'll actually do

Twelve to twenty compounds, CDK9 against one close counter-target, and a deliberately small budget
of quantum calculations. Small enough for a room of people to explore in two days, large enough to
show whether there's real selectivity signal.

The phases get worked on in parallel first, so each one is understood on its own, and then we do an
integrated small-scale run.

Six gates decide what happens next, and they were written before any data existed. A clean "no"
against those gates is a good outcome. The result we're trying to avoid is the ambiguous one that
lets a project drift forward on optimism.

## 6. Why a hackathon, and why Auckland

The interesting parts can't be done by one discipline.

The benchmark needs a medicinal chemist who knows that two IC50 values measured at different ATP
concentrations don't form a valid ratio. Get that wrong and everything downstream is an artefact,
quietly, until the write-up. The pocket predictions need a structural biologist to say which are
nonsense. The quantum layer needs someone who knows when a calculation has converged and when it
has merely stopped. The statistics need someone willing to say out loud that a difference of 0.05
on twenty compounds is nothing. And the whole thing needs a research software engineer or it won't
run twice.

Those people are at the University of Auckland and mostly haven't worked together. This is the
excuse.

## 7. The global event

We're a local site for the [Open Scientific Intelligence Hackathon](the-global-event.md), which is
in its fourth year with hubs on four continents and over a thousand participants last year. Three
years of write-ups, every team credited.

**The global event runs 21-22 October and registration is open to anyone.** If you're interested in
this space at all, sign up for that whether or not you come to ours.

We're running 19-20 October because those are the two days we have. Wednesday the 21st is open if
people want to keep going, and it's the global event's opening day, so that's a straightforward way
to carry the work across.

## 8. What you get out of it

If you're new to this, you'll own a result the group uses. In the first hour you'll be running a
configuration that becomes a data point in the final analysis, or looking at predicted structures
and telling the computational people which ones are wrong, which is a judgement they can't make
without you.

If you already work in this area: dual GB10 boxes for the month beforehand and H200 access for the
benchmarks, a pipeline that runs when you arrive, and an open question in the middle of it.

## 9. Afterwards

A curated CDK selectivity benchmark with a written statement of what it can and can't support.
There's a real gap there and other groups would use it.

A methods note on small-data configuration search, which isn't chemistry-specific.

A measured baseline for the surrogate chain, and a workflow that makes re-running it cheap. That
last one matters most. The components will improve, and we want to be able to answer "has it
crossed the threshold yet" without rebuilding everything.

---

## The short versions

**One line.** How far can a chain of surrogates get us? We're measuring it on drug-target
selectivity and setting a baseline we'll come back to.

**A paragraph.** Most drugs fail on selectivity, and conventional screening can't separate a target
from its close relatives because it discards the 3D information that distinguishes them. We're
building a pipeline that hands every expensive step to a learned surrogate and keeps quantum
chemistry for the cases where it changes the answer. Other groups have built individual steps, but
we haven't found the whole chain attempted. It might not be good enough yet, which is still worth
knowing, because each step is improving quickly and we want a measured starting point to compare
against. We're exploring the parameter space properly rather than guessing settings, which is a
problem every field with slow experiments shares.

**For someone new.** Two days, dedicated GPUs, a pipeline that already works when you arrive, and a
job that uses what you already know.
