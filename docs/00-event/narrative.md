# The narrative

What this is, why it matters, and why anyone should give it two days. Written to be read start to
finish by someone who has never heard of it — a prospective participant, a head of department, a
funder, a journalist. Everything in [`outreach/`](../../outreach/) is cut from this.

---

## 0. The one sentence

> ### Start small. Search hard. Scale only what survives.
>
> **We're testing whether a deliberately small experiment can predict what a large one would do.**

That is the project. The pipeline, the gates, the two days, the shape of the month before them —
all of it orients around that sentence, and **[§4](#4-the-idea-the-whole-thing-orients-around)** is
where it gets precise.

Everything between here and there is the testbed: a real problem, hard enough that the answer
matters, small enough that we can afford to explore it properly.

---

## 1. The testbed, and why it's worth using

A drug that works is not the hard part any more. A drug that works **only where you want it to** is.

Most modern therapeutics fail not because they miss their target but because they also hit
something adjacent — a protein so similar that no amount of chemical intuition separates them. In
the CDK family, the enzyme CDK9 sits beside CDK7, CDK12 and CDK13 with binding pockets so alike
that a compound designed for one routinely hits all four. The consequence is toxicity, a narrow
therapeutic window, and a programme that dies late and expensively.

Conventional computational screening is very good at the first question — *does this molecule bind
something?* — and close to useless at the second. It flattens a three-dimensional pocket into a
chemical fingerprint, and in doing so throws away precisely the information that distinguishes one
pocket from its near-twin: local geometry, induced fit, electrostatics, the way both protein and
ligand move.

**We want to know whether AI can put that information back, cheaply enough to be useful.**

## 2. Why now

Three things became true in the last eighteen months, and none of them individually is enough.

**Structure prediction became routine.** Open-weight co-folding models now produce plausible
protein–ligand complexes for targets with no crystal structure. Not truth — but a usable starting
hypothesis, generated in minutes, where previously there was nothing.

**Geometry-aware scoring started to generalise.** Equivariant neural networks that operate on the
local binding pocket transfer to pockets they have never seen, because geometry is a shared
language in a way that chemical descriptors are not.

**Quantum chemistry moved onto the GPU.** Electronic-structure calculations at a level that
actually distinguishes two similar pockets are now tractable in batch — not for millions of
compounds, but for the few thousand where the answer is genuinely in doubt.

Put together, those three permit a shape of workflow that was not previously affordable: **cheap AI
does the volume, expensive physics does the discrimination, and the expensive part is spent only
where it changes the answer.**

## 3. The idea

A staged funnel. Each stage is allowed to be wrong in a characterised way, and the next stage exists
to correct the errors the previous one is known to make.

> Generate plausible complexes → crop the pocket → sample how it moves → score the geometry →
> send only the genuinely uncertain cases to quantum chemistry → learn from those labels → repeat.

At four points in that chain, a learned model stands in for something expensive: co-folding for
crystallography, learned ensembles for molecular dynamics, an equivariant network for physics-based
scoring, and a learned correction for running quantum chemistry on everything.

That is where it gets interesting, and where most projects of this shape quietly fail.

**A surrogate can be fast, confident and wrong.** Worse, it can be accurate *on average* while
being systematically wrong on exactly the close calls the whole pipeline exists to resolve. So we
impose a rule: **every surrogate owes a fidelity contract** — a stated ground truth, a validation
set that actually contains close calls, and an explicit trust region beyond which it may not be
believed. A surrogate without a trust region is not a method, it is a hope.

## 4. The idea the whole thing orients around

Back to the lead. Here is the problem nobody talks about. That pipeline has about eight configurable choices — how
much protein to include, how many conformations to sample, how accurate the quantum calculation
needs to be, how aggressively to spend the expensive budget. Each combination costs GPU-hours.
Nobody can afford to explore them at production scale.

So everyone does the same thing: guess most of it, tune two or three knobs on a small grid, and
hope the result transfers when they scale up.

There is now good evidence that this is exactly the wrong move. Work published this August on
small-scale machine-learning experiments found that **thorough exploration of the configuration
space is the single ingredient that determines whether small experiments transfer at all** — and,
counterintuitively, that small-scale systems are *more* sensitive to their settings than large
ones, not less. In their experiments, searching four configurations showed nothing. Sixteen showed
nothing. Two hundred and fifty-six gave a clean, predictive answer. Most published small-scale
results are not wrong; they are undertuned.

**So we are treating the pipeline itself as the object of study.** The configuration is not a set of
settings to be guessed — it is the thing we are measuring. Hence the lead:

> ### Start small. Search hard. Scale only what survives.
>
> **When does what you learn from a small experiment actually transfer to the scale you care about?**

That reaches far beyond drug discovery.

An ecologist with one field season has that question. A clinical researcher with a small cohort has
it. A materials group whose synthesis takes three weeks has it. Every one of them has a pipeline of
configurable choices, an expensive evaluation, and no ability to grid-search. We happen to have a
convenient testbed.

## 5. What we are actually doing on the day

Not building a drug. Running an experiment about a method, and finding out whether it deserves to
be scaled.

Concretely: twelve to twenty compounds, CDK9 against one close counter-target, and a deliberately
small budget of expensive quantum calculations. Small enough that a room of people can explore it
in two days; large enough to reveal whether there is real selectivity signal.

Six pre-specified gates decide what happens next, and they were written before any data existed —
which is the difference between a finding and a story. **A clean "no" against those gates is a
successful event.** The outcome we are actively trying to avoid is the ambiguous one that lets a
project drift forward on optimism.

## 6. Why a hackathon, and why Auckland

Because the interesting parts of this cannot be done by one discipline.

The benchmark needs a medicinal chemist who knows that two IC50 values measured at different ATP
concentrations do not form a valid ratio — a fact that, if missed, invalidates everything
downstream, silently, for the entire event. The pocket predictions need a structural biologist to
look at them and say which are nonsense. The quantum layer needs someone who knows when a
calculation has converged and when it has merely stopped. The statistics need someone willing to
say out loud that a difference of 0.05 on twenty compounds is nothing. And the whole thing needs a
research software engineer, or it will not run twice.

Those people exist at the University of Auckland. They mostly have not worked together.

This event is the excuse. And the thing being built — a reusable benchmark, a reproducible GPU
workflow, a methodology for small-data experimentation — outlasts the two days regardless of what
the pipeline does.

## 7. Why you should come, specifically

If you are new to AI for science, the honest pitch is this: **you will personally own a result the
group uses.** Not a tutorial, not shadowing someone else's screen. Within the first hour you will
either be running a configuration that becomes a data point in the final analysis, or looking at
predicted molecular structures and telling the computational team which ones are wrong — a
judgement they cannot make without you, and the result is worse without it.

If you are already deep in this: we have dual GB10 boxes for a month beforehand and H200 access for
the benchmarks, a pipeline that will already run when you arrive, and a genuinely open methodological
question at the centre of it.

And if two days isn't enough, Wednesday the 21st is the global hackathon's opening day — you can
carry whatever we build straight into it.

And we go first. Auckland runs **two days ahead of the global hackathon**, closing sixteen hours
before the earliest hub in the world opens — so whatever we produce is available to every other
hub from the moment they start.

## 8. What happens afterwards

Three things, in increasing order of ambition:

1. **A benchmark other people use.** There is a real gap: a curated, documented, honestly-caveated
   CDK selectivity benchmark with a written statement of what it can and cannot support.
2. **A methods contribution.** The small-data configuration question is publishable on its own, and
   it is discipline-agnostic.
3. **A capability and a group.** A cross-disciplinary team at Auckland that has actually built
   something together, and a reproducible GPU workflow that the next project starts from instead of
   rebuilding.

If the gates come back green, there is a pilot and then a campaign. If they come back red, we will
have found that out in two days for the cost of two days — which is the entire point of running the
small experiment first.

---

## The short versions

**One sentence:** We're testing whether a deliberately small experiment can predict what a large one
would do — on an AI-surrogate pipeline for drug-target selectivity.

**One paragraph:** Most drugs fail on selectivity, not potency, and conventional screening cannot
distinguish a target from its close relatives because it discards the 3D information that makes
them different. We are building a staged pipeline where fast AI models do the volume work and
GPU quantum chemistry is spent only where it changes the answer — and where every surrogate has to
declare where it may be trusted. The deeper question is methodological: when does a small,
affordable experiment actually predict the large, expensive one? That question belongs to every
field with slow experiments, which is why this is a cross-disciplinary event rather than a
computational chemistry one.

**For a newcomer:** Two days, dedicated GPUs, a pipeline that already works when you walk in, and a
job that uses what you already know. You will own a piece of the result.
