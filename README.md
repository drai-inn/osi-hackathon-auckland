<img src="outreach/brand/readme-banner.png" alt="How far can a chain of surrogates take us in biomolecular interactions? Open Scientific Intelligence Hackathon, Auckland site, Mon 19 – Tue 20 October 2026" width="100%">

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## How far can a chain of surrogates take us in biomolecular interactions?

**Systems · proteins · ligand binding · drug discovery · pharmacology**

Physiological outcomes come from molecules interacting. Those interactions produce functional
change. Function is driven by spatial and structural change. Pharmacology is the effect of drugs on
that system.

Nobody can currently carry a signal cleanly from one end of that to the other.

Biology has a ladder of scales. Machine learning now has one running alongside it — association
models over sequence, 3D-aware models over structure, interatomic potentials over atoms and motion,
multi-scale models over cells and tissue. Most are open-weight. Most arrived recently. Very few of us
know more than our own rung.

**So: how far up that second ladder do you have to climb to get an answer you can trust, and how
would you know?**

📖 **[Read the pitch](docs/00-event/narrative.md)** · 🧭 **[The four themes](docs/00-event/themes.md)** · 🙋 **[Taking part](docs/00-event/taking-part.md)**

> ### 🌏 The global event
> We're one local site of the **Open Scientific Intelligence Hackathon**. Fourth year, hubs on four
> continents, over a thousand participants last year, and a write-up each year crediting every team.
>
> **It runs 21–22 October and [registration is open to anyone](https://luma.com/ku88xh92).** Sign up
> for that whether or not you come to ours. Auckland runs 19–20 October, which are the two days we
> have, and Wednesday the 21st is open if people want to carry the work across.
>
> [llmhackathon.github.io](https://llmhackathon.github.io/) · [how we fit in](docs/00-event/the-global-event.md)

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## Four themes

Notional, all four. They describe the kind of thing we're interested in, not a project plan. Bring
your own problem and own a space.

| | |
| --- | --- |
| **1 · Screening at scale, with physics in the loop** | Models that know something about shape, used to filter before you pay for docking |
| **2 · Molecules in motion** | Machine-learned interatomic potentials in MD — near-quantum forces you can afford to run |
| **3 · From a binding event to a whole system** | Carrying a molecular signal up to functional and physiological change |
| **4 · Repurposing what we already have** | Genotype, structure and approved drugs, with deliberately small models |

In each one, the same three moves: **find out what open-weight models exist in your area · get one
or two running on our hardware · work out what to measure, and report it back.**

That third move is the hard part and the one we care most about. How to evaluate these models is
genuinely unsettled — one recent benchmark found single-cell foundation models don't beat a simple
linear baseline, and another found the choice of metric flips the rankings outright. That's the
opportunity, not a caveat.

**There's no central benchmark team and no manifest handed out.** Each group sources its own, because
working out what to measure *is* the intellectual content. What makes the groups comparable is that
everyone answers [the same four questions](docs/00-event/taking-part.md#the-four-questions) about
whatever they picked, reported back at the end of day 1.

**[The themes in full](docs/00-event/themes.md)**, with the open-weight models worth a look in each.

![The chain: what passes between stages, and where the gates sit](docs/03-pipeline/figures/pipeline-isometric.svg)

We have default targets and chemistry prepared, so nobody starts from a blank page. Take one or
bring your own.

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## Who it's for

**Come and explore the broader opportunity while getting hands-on with AI in your own area.** Come
prepared to work with agents and with code, to find out where your own methods are moving under the
new models.

That sounds like a filter and it's the opposite of one. **The agent writes the code; you supply the
judgement about whether the answer is any good** — and that judgement is the scarce part. If you
haven't written anything in fifteen years, or ever, you are not behind here.

We're inviting **project teams**. A group leader brings their team, their expertise, and a problem or
candidate. **If you can only come for the opening, come for the opening** and leave your team to it —
that's an expected way to take part, not a lesser one. Coming on your own is fine too.

Chemists · physicists · structural biologists · statisticians · ML researchers · systems biologists ·
pharmacologists · clinicians · bioinformaticians · research software engineers · and anyone new to
all of it.

## What the two days look like

**Day 1** — get running, do something, work out what to measure, report back. That order is
deliberate: you can't pick a benchmark for a model you haven't seen behave.
**Day 2** — measure it, and report what you actually got, negatives included.

Bookends each day, lightning talks each day, work in ones, twos and threes, and food and a social
occasion both days. Nobody is assigned to anything. **Setup is agentic support plus our team** — you
shouldn't spend day 1 fighting an install, and we'll have at least one model per theme known to run
on our hardware before anyone arrives.

**No stupid questions. Safe to experiment. A negative is a result.**

**[More on taking part](docs/00-event/taking-part.md)** · **[How we work](CONTRIBUTING.md)**

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## Practical

| | |
| --- | --- |
| **When** | Mon 19 – Tue 20 October 2026. Wednesday 21st open if people want to keep going |
| **Where** | University of Auckland |
| **Cost** | Free |
| **Bring** | A laptop. Compute, targets, data and environments are set up before you arrive |
| **Compute** | Dual GB10 and an HGX H200 |
| **Contact** | Nick Jones · njon001@aucklanduni.ac.nz |

We keep a [live event log](EVENT-LOG.md) as a single pull request that stays open until the final
presentations and reports are done. Subscribe and you'll get every update and nothing else.

## Where things are

| | |
| --- | --- |
| The pitch, and all copy cut from it | [narrative.md](docs/00-event/narrative.md) |
| The four themes | [themes.md](docs/00-event/themes.md) |
| Coming along | [taking-part.md](docs/00-event/taking-part.md) · [the global event](docs/00-event/the-global-event.md) |
| Inviting someone | [`outreach/`](outreach/) — one-pager, templates, poster, [brand](outreach/brand/README.md) |
| Compute | [GB10 / H200 plan](docs/06-feasibility/compute-plan.md) — the two architectures, and why it matters |
| What's undecided | [Open questions](docs/02-scope/open-questions.md) · [Risks](docs/06-feasibility/risks.md) |
| Who to talk to elsewhere | [Interested parties](docs/00-event/interested-parties.md) |
| **The worked example** | A CDK selectivity pipeline we can offer as a default: [problem](docs/01-context/problem-statement.md) · [architecture](docs/03-pipeline/architecture.md) · [stages](docs/03-pipeline/stages/) · [figures](docs/03-pipeline/figures/) |
| The method thread | [Small-data experiments](docs/04-experiments/hpo-microtopic.md) — how to learn a parameter space when every run is expensive |

## Try it now

Standard library only, nothing to install:

```bash
make check
python3 tools/make_figures.py
open tools/render/viewer.html
```

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

We don't know how far this gets — that's the experiment. Some of these models may turn out not to
beat much simpler things on the problems we care about. **We'd still like the number.** A
well-founded *"not yet, and here's why"* is a result we'd be happy to present.

Nick Jones · njon001@aucklanduni.ac.nz ·
[Global event](https://llmhackathon.github.io/) · [Live log](EVENT-LOG.md) · [Contributing](CONTRIBUTING.md)
