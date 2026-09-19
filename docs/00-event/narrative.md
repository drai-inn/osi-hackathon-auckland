# The narrative

What we're doing and why. All the outreach copy in [`outreach/`](../../outreach/) is cut from this,
so change it here first.

---

## The short version

> ### How far can a chain of surrogates get us?

**Three things, in order.**

**1. Hand every expensive step to a learned surrogate.**
Individual steps have been done well by other groups.
We haven't found anyone who ran the whole chain.

**2. Measure where that lands, as a baseline.**
It might not be good enough yet. We'd still like the number.
Every step is improving quickly. At some point the chain crosses a threshold.
Without a starting point we won't know when.

**3. Get there by starting small.**
Twelve compounds. Two targets. A handful of quantum labels.
Explore the parameter space properly at that size.
Scale only what survives.

---

## 1. The testbed

Most drugs fail on selectivity, not potency.

A compound built for one protein also hits its close relatives. The programme fails late and
expensively.

Conventional screening is good at "does this bind something". It's poor at "why this pocket and not
its near-twin". It flattens a 3D pocket into a fingerprint, and that throws away what separates two
similar pockets: local geometry, induced fit, electrostatics, and how both protein and ligand move.

**Our case is CDK9 against CDK7.** Same fold, same ligand, different answer.

Enough public data exists to build a defensible benchmark. Known selective and known pan-CDK
compounds give us real discriminating cases, not actives against random decoys.

![The four CDK targets, and what each phase of the pipeline actually holds](../03-pipeline/figures/objects-of-study.svg)

## 2. The chain

Eight steps.

Each cheap enough to run on everything reaching it. Each allowed to be wrong in a characterised way
that the next step corrects.

Generate plausible complexes. Crop the pocket. Sample how it moves. Score the geometry. Send only
the genuinely uncertain cases to quantum chemistry. Learn from those labels. Repeat.

![The eight steps, what passes between them, and where the gates sit](../03-pipeline/figures/pipeline-isometric.svg)

Four steps hand an expensive calculation to a learned model:

| Step | Replaces |
| --- | --- |
| Co-folding | Experimental structure determination |
| Learned ensembles | Molecular dynamics |
| Equivariant scoring | Physics-based rescoring |
| Delta-learned correction | Running quantum chemistry on everything |

Versions of each exist. At the 2025 hackathon alone there was a docking tool using a
machine-learned potential as its scoring function, an agent that ran protein-ligand MD end to end,
and an assistant for setting up DFT.

What we haven't found is the four assembled into one chain, with a budget discipline across it.
That's the thing we want to measure.

## 3. Why it's worth measuring even if it fails

A surrogate can be fast, confident and wrong.

It can also be accurate on average while being wrong on exactly the close calls the pipeline exists
to resolve.

Chain four together and the errors compound in ways nobody has characterised, because nobody has
chained them.

So each one declares where it can be trusted. Every surrogate carries a **fidelity contract**: a
stated ground truth, a validation set containing close calls, and a region outside which it isn't
believed. A surrogate with a correlation coefficient and no trust region isn't a method, it's a
hope.

What comes out: a number for how far the chain gets, and which links are dragging. Useful now for
deciding where to spend. Useful later as the comparison point when we run it again with better
components.

## 4. Start small, then scale

The pipeline has about eight configurable choices. Crop radius. Conformers sampled. Quantum theory
level. How aggressively to spend the expensive budget.

Each combination costs GPU hours. Nobody can explore that at production scale.

So the usual approach is to guess most of it and tune two or three knobs on a small grid.

Recent work on small-scale machine learning experiments suggests that's the thing that goes wrong.
Small experiments fail to transfer because they're **under-explored**, not because they're small.
Four configurations showed nothing. Sixteen showed nothing. 256 gave a clean predictive answer.

![Four tiers, from smoke test to scale-up, with a gate between each](../03-pipeline/figures/scale-trajectory.svg)

The trajectory runs in four tiers, and each gate has to be green before we move up.

**Smoke test.** Five ligands, two targets, one pose. Do the containers run, do the formats line up.

**Hackathon minimum.** Twelve to twenty ligands, three poses, twenty to fifty quantum labels. Do
parameter changes move the ranking, is each stage feasible.

**Useful pilot.** Fifty to a hundred ligands, four targets, hundreds of labels. Ranking stability,
selectivity trend, cost per label.

**Scale-up.** Thousands of candidates after front-end filtering. Only once the gates below it pass.

The questions we actually want answered are: is this even feasible, what data would we need, and
how small can we go while still being usefully robust.

That last one travels well beyond drug discovery. Anyone with one field season, a small cohort or a
three-week synthesis has the same problem. A pipeline of choices, an expensive evaluation, and no
way to grid-search. It's part of why this is cross-disciplinary.

*(This thread came out of a conversation with Jack Flanagan, who suggested hyperparameter
optimisation on small datasets as a microtopic and asked where the big wins are that scale. Written
up in [hpo-microtopic.md](../04-experiments/hpo-microtopic.md).)*

## 5. What we'll actually do

The hackathon sits at tier two.

Twelve to twenty compounds. CDK9 against one close counter-target. A deliberately small budget of
quantum calculations.

Small enough for a room of people to explore in two days. Large enough to show whether there's real
selectivity signal.

The phases get worked on in parallel first, so each is understood on its own. Then an integrated
small-scale run.

Six gates decide what happens next, written before any data existed. A clean "no" against those
gates is a good outcome. What we're trying to avoid is the ambiguous result that lets a project
drift forward on optimism.

## 6. Why a hackathon, and why Auckland

The interesting parts can't be done by one discipline.

The benchmark needs a medicinal chemist who knows that two IC50 values measured at different ATP
concentrations don't form a valid ratio. Get that wrong and everything downstream is an artefact,
quietly, until the write-up.

The pocket predictions need a structural biologist to say which are nonsense.

The quantum layer needs someone who knows when a calculation has converged and when it has merely
stopped.

The statistics need someone willing to say out loud that a difference of 0.05 on twenty compounds
is nothing.

And the whole thing needs a research software engineer or it won't run twice.

Those people are at the University of Auckland and mostly haven't worked together. This is the
excuse.

## 7. The global event

We're a local site for the [Open Scientific Intelligence Hackathon](the-global-event.md). Fourth
year, hubs on four continents, over a thousand participants last year. Three years of write-ups,
every team credited.

**The global event runs 21-22 October and registration is open to anyone.** If you're interested in
this space at all, sign up for that whether or not you come to ours.

We're on 19-20 October because those are the two days we have. Wednesday the 21st is open if people
want to keep going, and it's the global event's opening day.

## 8. What you get out of it

**New to this.** You'll own a result the group uses. In the first hour you'll be running a
configuration that becomes a data point in the final analysis, or looking at predicted structures
and telling the computational people which ones are wrong. That's a judgement they can't make
without you.

**Already in this area.** Dual GB10 boxes for the month beforehand, H200 access for the benchmarks,
a pipeline that runs when you arrive, and an open question in the middle of it.

## 9. Afterwards

A curated CDK selectivity benchmark, with a written statement of what it can and can't support.
There's a real gap there and other groups would use it.

A methods note on small-data configuration search. Not chemistry-specific.

A measured baseline for the surrogate chain, and a workflow that makes re-running it cheap.

That last one matters most. The components will improve. We want to answer "has it crossed the
threshold yet" without rebuilding everything.

---

## The short versions

**One line.** How far can a chain of surrogates get us? We're measuring it on drug-target
selectivity, starting small, as a baseline we'll come back to.

**A paragraph.** Most drugs fail on selectivity, and conventional screening can't separate a target
from its close relatives because it discards the 3D information that distinguishes them. We're
handing every expensive step to a learned surrogate and keeping quantum chemistry for the cases
where it changes the answer. Other groups have built individual steps. We haven't found the whole
chain attempted. It might not be good enough yet, which is still worth knowing, because each step
is improving quickly and we want a starting point to compare against. We get there by starting
small and exploring the parameter space properly, then scaling only what survives.

**For someone new.** Two days, dedicated GPUs, a pipeline that already works when you arrive, and a
job that uses what you already know.
