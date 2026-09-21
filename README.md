<img src="outreach/brand/readme-banner.png" alt="How far can a chain of surrogates take us in biomolecular interactions? Open Scientific Intelligence Hackathon, Auckland site, Mon 19 – Tue 20 October 2026" width="100%">

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## How far can a chain of surrogates take us in biomolecular interactions?

**Systems · proteins · ligand binding · drug discovery · pharmacology**

Physiological outcomes come from molecules interacting. Those interactions produce functional
change. Function is driven by spatial and structural change. Pharmacology is the effect of drugs on
that system.

Biology has a ladder of scales, and machine learning now has one running alongside it. Association
models over sequence, 3D-aware models over structure, interatomic potentials over atoms and motion,
multi-scale models over cells and tissue. **Language models sit at nearly every rung too** — over
protein sequence, over DNA, over molecules written as text, over gene expression, and over the
literature itself. Most are open-weight and most arrived recently.

Two days to find out how far up that second ladder you have to climb to get an answer you can trust.

📖 **[The pitch](docs/narrative.md)** · 🧭 **[Four themes](docs/themes.md)** · 🙋 **[Taking part](docs/taking-part.md)**

> ### 🌏 The global event
> We're one local site of the **Open Scientific Intelligence Hackathon**. Fourth year, hubs on four
> continents, over a thousand participants last year, and a write-up each year crediting every team.
>
> **It runs 21–22 October and [registration is open to anyone](https://luma.com/ku88xh92).** Sign up
> for that whether or not you come to ours. Auckland runs 19–20 October, and Wednesday the 21st is
> open if people want to carry the work across.
>
> [llmhackathon.github.io](https://llmhackathon.github.io/) · [how we fit in](docs/the-global-event.md)

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## Four themes

Notional, all four. They describe the kind of thing we're interested in. Bring your own problem and
take a space.

<p>
<img src="docs/cards/theme-1.svg" width="49%" alt="Theme 1, screening at scale: models that know something about shape, used to filter before you pay for docking. Boltz-2, OpenFold3, Chai-1r, IntFold">
<img src="docs/cards/theme-2.svg" width="49%" alt="Theme 2, molecules in motion: machine-learned interatomic potentials in MD, near-quantum forces you can afford to run. MACE, UMA, eSEN, Orb-v3, NequIP">
<img src="docs/cards/theme-3.svg" width="49%" alt="Theme 3, binding to whole system: carrying a molecular signal up to functional and physiological change. STATE, scGPT, Geneformer, scFoundation">
<img src="docs/cards/theme-4.svg" width="49%" alt="Theme 4, repurposing what we have: genotype, structure and approved drugs with deliberately small models. TxGNN, PrimeKG, lightweight KG embeddings">
</p>

In each one, the same three moves: **find out what open-weight models exist in your area · get one
or two running on our hardware · work out what to measure, and report it back.**

That third move is the one we care most about. How to evaluate these models is genuinely unsettled.
A recent benchmark found single-cell foundation models level with a simple linear baseline, and
another found the choice of metric changes which model comes out on top. There's a lot of room to
do useful work there.

Each group sources its own data and picks its own benchmark. What makes the groups comparable is
that everyone answers [the same four questions](docs/taking-part.md#the-four-questions) about
whatever they picked, reported back at the end of day 1. Schema-guided extraction with an LLM is a
quick way to get a dataset together.

**Language models are in scope everywhere**, not just as the agent writing your code. ESM and
AMPLIFY over protein sequence, Evo 2 over DNA, ChemBERTa over molecules as text, Geneformer and
scGPT over gene expression. In several of these places they're the thing to beat.

**[The themes in full](docs/themes.md)** · **[a worked example](docs/worked-example.md)** if you'd
rather start with something ready to go.

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## Who it's for

**Come and explore the broader opportunity while getting hands-on with AI in your own area.** Come
prepared to work with agents and with code, to find out where your own methods are moving under the
new models.

The agent writes the code. You bring the judgement about whether the answer is any good, which is
the scarce half. Everyone is welcome here, whatever you last wrote and whenever you last wrote it.

We're inviting **project teams**. A group leader brings their team, their expertise, and a problem
or candidate. **If you can only come for the opening, come for the opening** and leave your team to
it. Coming on your own works too.

Chemists · physicists · structural biologists · statisticians · ML researchers · systems biologists ·
pharmacologists · clinicians · bioinformaticians · research software engineers · and anyone new to
all of it.

## The two days

**Day 1** — get running, do something, work out what to measure, report back. You can pick a
benchmark once you've seen a model behave, so that comes after the running.

**Day 2** — measure it, and report what you got, including the negatives.

Bookends each day, lightning talks each day, work in ones, twos and threes, and food and a social
occasion both days. Setup is agentic support plus our team, and we'll have at least one model per
theme known to run on our hardware before anyone arrives.

**[More on taking part](docs/taking-part.md)** · **[How we work](CONTRIBUTING.md)**

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

## Practical

| | |
| --- | --- |
| **When** | Mon 19 – Tue 20 October 2026. Wednesday 21st open if people want to keep going |
| **Where** | University of Auckland |
| **Cost** | Free |
| **Bring** | A laptop |
| **Compute** | Dual GB10 and an HGX H200 · [the detail](docs/compute.md) |
| **Contact** | Nick Jones · njon001@aucklanduni.ac.nz |

We keep a [live event log](EVENT-LOG.md) as a single pull request that stays open until the final
presentations and reports are done. Subscribe and you'll get every update and nothing else.

## Where things are

| | |
| --- | --- |
| The pitch, and all copy cut from it | [narrative.md](docs/narrative.md) |
| The four themes | [themes.md](docs/themes.md) |
| Coming along | [taking-part.md](docs/taking-part.md) · [the global event](docs/the-global-event.md) |
| Something ready to work on | [worked-example.md](docs/worked-example.md) · [figures](docs/figures/) |
| Compute | [compute.md](docs/compute.md) — two architectures, and what that means |
| The models behind the agents | [agentic-models.md](docs/agentic-models.md) — the open-weight shortlist, and what actually fits |
| Small experiments | [small-experiments.md](docs/small-experiments.md) — learning a parameter space when every run is expensive |
| Inviting someone | [`outreach/`](outreach/) · [brand](outreach/brand/README.md) |
| Who to talk to elsewhere | [interested-parties.md](docs/interested-parties.md) |
| Decisions | [`docs/adr/`](docs/adr/) · [glossary](docs/glossary.md) |

## Try it

```bash
make check                            # links and anchors across the repo
python3 tools/make_cards.py           # the four theme cards
open tools/render/viewer.html         # four kinase structures, rotatable
```

<br>

<img src="outreach/brand/uoa-motif.svg" width="40" alt="">

<br>

We don't know how far this gets, and finding out is the work. Some of these models may land level
with much simpler things on the problems we care about. We'd like the number either way, and a
well-founded *"not yet, and here's why"* is a result we'd be happy to present.

Nick Jones · njon001@aucklanduni.ac.nz ·
[Global event](https://llmhackathon.github.io/) · [Live log](EVENT-LOG.md) · [Contributing](CONTRIBUTING.md)
