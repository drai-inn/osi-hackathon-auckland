<img src="outreach/brand/readme-banner.png" alt="How far can a chain of surrogates get us? Open Scientific Intelligence Hackathon, Auckland site, Mon 19 – Tue 20 October 2026" width="100%">

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## How far can a chain of surrogates get us?

We want to try a more AI-intensive approach to a structure-based pipeline, where every expensive
step is handed to a learned surrogate, and see how far that actually gets us today.

Other groups have done individual steps well. We haven't found anyone who has run the whole chain
end to end, with the expensive physics kept only for the places where it changes the answer.

It might not be good enough yet. We'd still like the number. Every step in the chain is improving
quickly, and at some point the chain crosses a threshold and becomes useful. Without a measured
starting point we won't know when that happens. So this is a baseline, taken carefully enough to be
worth repeating.

📖 **[Read the narrative](docs/00-event/narrative.md)** for the whole thing, about ten minutes.

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## The chain

Eight steps. Each one cheap enough to run on everything that reaches it, and each allowed to be
wrong in a characterised way that the next step corrects.

![The eight steps, what passes between them, and where the gates sit](docs/03-pipeline/figures/pipeline-isometric.svg)

Four steps hand an expensive calculation to a learned model. A surrogate can be fast, confident and
wrong, and it can be accurate on average while being wrong on the close calls the pipeline exists to
resolve. So each one has to declare where it can be trusted, which is what the
[fidelity contracts](docs/03-pipeline/fidelity-contracts.md) are for.

The testbed is **CDK9 against CDK7**. Two kinases with ATP sites similar enough that telling them
apart is the whole difficulty.

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## How we're measuring it

The pipeline has about eight configurable choices, each combination costs GPU hours, and nobody can
explore that at production scale. The usual approach is to guess most of it and tune two or three
knobs on a small grid. Recent work suggests that's the thing that goes wrong: small experiments fail
to transfer because they're under-explored, not because they're small.

So we start small and explore the parameter space properly, in parallel across the phases, before
trying an integrated run. The questions we actually want answered are: is this even feasible, what
data would we need, and how small can we go while still being usefully robust.

That last one isn't chemistry-specific. Anyone with one field season, a small cohort or a three-week
synthesis has the same problem, which is part of why this is cross-disciplinary.
[More on the method](docs/04-experiments/hpo-microtopic.md).

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## New here? Pick a ladder

You shouldn't have to read this repo to be useful in it. Six pathways, each a set of rungs you climb
in order. Each rung is small enough to finish in a sitting, and you can stop at any of them.

| | Ladder | For you if… | Rung 1 is |
| --- | --- | --- | --- |
| **A** | [New to AI for science](docs/00-event/onboarding/newcomer.md) | You're expert in something else and haven't done this | Running one configuration, your name on the dashboard |
| **B** | [Domain expert](docs/00-event/onboarding/domain-expert.md) | Chemistry, pharmacology, structural biology | Judging five predicted poses |
| **C** | [ML and statistics](docs/00-event/onboarding/ml-stats.md) | You model things, and the method is the draw | Telling us where our small-data design breaks |
| **D** | [Builder](docs/00-event/onboarding/builder.md) | RSE, HPC, or you want to write the pipeline | `make smoke` green on your machine |
| **E** | [Following along](docs/00-event/onboarding/follower.md) | Can't commit, but want to know how it goes | Subscribing to the live log |
| **F** | [Stage owner](docs/00-event/onboarding/stage-owner.md) | You've said yes to a work package | Filing three questions about your stage |

Not sure, start at [Ladder A rung 0](docs/00-event/onboarding/newcomer.md#rung-0--orient-10-minutes).
Ten minutes, and it'll point you somewhere better if you're in the wrong place.

**New to AI for science?** Within the first hour you'll own one configuration of the pipeline. One
command, twenty minutes, and your run becomes a data point in the final analysis. Bring a laptop,
that's all.

### Following without joining

We keep a [live event log](EVENT-LOG.md) as a single pull request that stays open until the final
presentations and reports are done. Subscribe and you'll get every update and nothing else.

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## The global event

We're a local site for the [Open Scientific Intelligence Hackathon](docs/00-event/the-global-event.md),
now in its fourth year, with hubs on four continents and over a thousand participants last year.

**The global event runs 21-22 October and [registration is open to anyone](https://luma.com/ku88xh92).**
If you're interested in this space at all, sign up for that whether or not you come to ours. We're
running 19-20 October because those are the two days we have. Wednesday the 21st is open if people
want to keep going, and it's the global event's opening day, so that's a straightforward way to
carry the work across.

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## Where things are

| | |
| --- | --- |
| Doing something this week | [Critical path](docs/05-delivery/critical-path.md) · [open issues](https://github.com/drai-inn/drugs-surrogate-pipeline/issues) |
| Inviting someone | [`outreach/`](outreach/), one-pager, templates, poster, [brand](outreach/brand/README.md) |
| The science | [Problem statement](docs/01-context/problem-statement.md) → [Architecture](docs/03-pipeline/architecture.md) → [Stages](docs/03-pipeline/stages/) |
| The method | [Small-data HPO](docs/04-experiments/hpo-microtopic.md) · [Methodology](docs/04-experiments/methodology.md) · [Metrics](docs/04-experiments/metrics.md) |
| Compute | [GB10 / H200 plan](docs/06-feasibility/compute-plan.md) · [Budget](docs/06-feasibility/compute-budget.md) |
| What's undecided | [Open questions](docs/02-scope/open-questions.md) · [Risks](docs/06-feasibility/risks.md) |
| Who to talk to elsewhere | [Interested parties](docs/00-event/interested-parties.md) |
| How we work | [CONTRIBUTING.md](CONTRIBUTING.md) · [Glossary](docs/02-scope/glossary.md) |

```
docs/
  00-event/       narrative, the global event, engagement, onboarding ladders,
                  who to reach out to                         OUTWARD-FACING
  01-context/     why this problem; notes on the source documents
  02-scope/       in, out, undecided, glossary
  03-pipeline/    S0–S8 stages, fidelity contracts, data contracts, figures
  04-experiments/ methodology, parameter space, metrics, the HPO microtopic
  05-delivery/    critical path, plan, work packages, roles   INWARD-FACING
  06-feasibility/ compute, budget, data sources, risks, gates
  adr/            decision records
outreach/         collateral, brand tokens, marks, UoA assets
schemas/ data/ tools/ workflow/ refs/
```

## Try it now

Standard library only, nothing to install:

```bash
make validate && make budget TIER=hackathon_minimum
python3 tools/make_figures.py
```

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

A clean "no" is a good outcome. Six gates were written before any data existed, and if the chain
doesn't hold we'd rather know in two days than two years.

Nick Jones · njon001@aucklanduni.ac.nz ·
[Global event](https://llmhackathon.github.io/) · [Live log](EVENT-LOG.md) · [Contributing](CONTRIBUTING.md)
