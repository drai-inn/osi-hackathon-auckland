<div align="center">

<img src="outreach/brand/readme-banner.png" alt="Start small. Search hard. Scale only what survives. — Open Scientific Intelligence Hackathon, Auckland Hub, Mon 19 – Tue 20 October 2026" width="100%">

</div>

## Start small. Search hard. Scale only what survives.

> **We're testing whether a deliberately small experiment can predict what a large one would do.**

That sentence is the whole project. Everything below — the pipeline, the gates, the two days, the
way we've structured the month — orients around it.

<img src="outreach/brand/uoa-motif.svg" width="36" alt="">

### Why it's a real question

You can afford the small version of your experiment. Under what conditions does what you learn from
it transfer to the scale you actually care about?

Work published this August argues the usual answer is wrong. Small-scale experiments fail to
transfer not because they are small but because they are **undertuned** — and, counterintuitively,
small systems are *more* sensitive to their configuration than large ones. Searching four
configurations showed nothing. Sixteen showed nothing. **256 gave a clean, predictive answer.** Most
published small-scale results, on that account, aren't wrong so much as under-explored.

So we treat the **configuration as the object of study**, not as settings to guess. Crop radius,
ensemble size, theory level, acquisition policy — those *are* the experiment.

That question belongs to ecology with one field season, clinical work with small cohorts, materials
with slow synthesis. We happen to have a good testbed.

<img src="outreach/brand/uoa-motif.svg" width="36" alt="">

### The testbed — can AI tell two near-identical drug targets apart?

Most drugs fail on **selectivity**, not potency. A compound built for one protein hits its close
relatives too, and the programme dies late and expensively. Conventional screening can't separate
them: it flattens a three-dimensional pocket into a fingerprint and throws away exactly what makes
two pockets different.

We're building a **staged pipeline** where fast AI models do the volume work and **GPU quantum
chemistry is spent only where it changes the answer**. Four times in that chain a learned surrogate
stands in for something expensive, and every one has to declare where it may be trusted.

Driving case: **CDK9 vs CDK7** — two kinases similar enough that telling them apart is the whole
problem.

📖 **[Read the narrative](docs/00-event/narrative.md)** — the whole story, ten minutes.

<div align="center"><img src="outreach/brand/uoa-motif.svg" width="44" alt=""></div>

## 👋 New here? Pick a ladder

Nobody should have to read this repo to be useful in it. Six pathways, each a set of **rungs** you
climb in order — each small enough to finish in a sitting, each leaving you genuinely more useful.
**You can stop at any rung.**

| | Ladder | For you if… | Rung 1 is |
| --- | --- | --- | --- |
| **A** | [**New to AI for science**](docs/00-event/onboarding/newcomer.md) | You're expert in something else and have never done this | Running one configuration, your name on the dashboard |
| **B** | [**Domain expert**](docs/00-event/onboarding/domain-expert.md) | Chemistry, pharmacology, structural biology | Judging five predicted poses |
| **C** | [**ML & statistics**](docs/00-event/onboarding/ml-stats.md) | You model things; the methodology is the draw | Telling us where our small-data design breaks |
| **D** | [**Builder**](docs/00-event/onboarding/builder.md) | RSE, HPC, or you want to write the pipeline | `make smoke` green on your machine |
| **E** | [**Following along**](docs/00-event/onboarding/follower.md) | Can't commit, but want to know how it goes | Subscribing to the live log |
| **F** | [**Stage owner**](docs/00-event/onboarding/stage-owner.md) | You've said yes to a work package | Filing three questions about your stage |

Not sure? **[Start at Ladder A, rung 0](docs/00-event/onboarding/newcomer.md#rung-0--orient--10-minutes)**
— ten minutes, and it'll point you somewhere better if you're in the wrong place.

> **New to AI for science? Good.** Within the first hour you'll own one configuration of the
> pipeline — one command, twenty minutes, and your run becomes a data point in the final analysis.
> Not a tutorial. The actual experiment. **Bring a laptop; that's all.**

### 📡 Following without joining

We keep a **[live event log](EVENT-LOG.md)** as a single pull request that stays open from now until
the final presentations and reports are done. Subscribe and you'll get every update and nothing
else. **When it closes, the work is finished.**

<div align="center"><img src="outreach/brand/uoa-motif.svg" width="44" alt=""></div>

## Where things are

| | |
| --- | --- |
| 🎯 **Doing something this week** | [Critical path](docs/05-delivery/critical-path.md) · [open issues](https://github.com/drai-inn/drugs-surrogate-pipeline/issues) |
| 📣 **Inviting someone** | [`outreach/`](outreach/) — one-pager, seven templates, A3 poster, [brand](outreach/brand/README.md) |
| 🌏 **How we fit the global event** | [the-global-event.md](docs/00-event/the-global-event.md) · [who to contact](docs/00-event/interested-parties.md) |
| 📐 **The method** | [Small-data HPO](docs/04-experiments/hpo-microtopic.md) · [Methodology](docs/04-experiments/methodology.md) · [Metrics](docs/04-experiments/metrics.md) |
| 🔬 **The science** | [Problem statement](docs/01-context/problem-statement.md) → [Architecture](docs/03-pipeline/architecture.md) → [Stages](docs/03-pipeline/stages/) |
| 💻 **Compute** | [GB10 / H200 plan](docs/06-feasibility/compute-plan.md) · [Budget](docs/06-feasibility/compute-budget.md) |
| ⚠️ **What's undecided** | [Open questions](docs/02-scope/open-questions.md) · [Risks](docs/06-feasibility/risks.md) |
| 🤝 **How we work** | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 📖 **Jargon** | [Glossary](docs/02-scope/glossary.md) |

```
docs/
  00-event/       the front end — narrative, the global event, engagement,
                  onboarding ladders, who to reach out to     OUTWARD-FACING
  01-context/     why this problem; notes on the source documents
  02-scope/       in, out, undecided, glossary
  03-pipeline/    S0–S8 stages, fidelity contracts, data contracts
  04-experiments/ methodology, parameter space, metrics, the HPO microtopic
  05-delivery/    critical path, plan, work packages, roles   INWARD-FACING
  06-feasibility/ compute, budget, data sources, risks, gates
  adr/            six decision records
outreach/         collateral + brand tokens, marks and UoA assets
schemas/ data/ tools/ workflow/ refs/
```

<div align="center"><img src="outreach/brand/uoa-motif.svg" width="44" alt=""></div>

## Three ideas the whole thing rests on

**1 · The pipeline *is* the model; its configuration is the hyperparameter vector.**
Crop radius and microstate count are the object of study, not settings to guess. This is the lead,
restated. → [hpo-microtopic.md](docs/04-experiments/hpo-microtopic.md)

**2 · Every surrogate owes a fidelity contract.**
A stated ground truth, a validation set containing close calls, and an explicit trust region. A
surrogate can be fast, confident and wrong on exactly the cases that matter.
→ [fidelity-contracts.md](docs/03-pipeline/fidelity-contracts.md)

**3 · A newcomer's experience is good when they personally own a result the group uses.**
Not a tutorial, not shadowing. → [engagement.md](docs/00-event/engagement.md)

## Try it now

Standard library only — no environment, no install:

```bash
make validate && make budget TIER=hackathon_minimum
```

<div align="center">

<img src="outreach/brand/uoa-motif.svg" width="44" alt="">

**A clean "no" is a successful outcome.**
Six gates were written before any data existed.
If the method doesn't work we'd like to know in two days rather than two years.

Nick Jones · njon001@aucklanduni.ac.nz
[Global event](https://llmhackathon.github.io/) · [Live log](EVENT-LOG.md) · [Contributing](CONTRIBUTING.md)

</div>
