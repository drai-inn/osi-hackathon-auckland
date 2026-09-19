# Auckland Hub · Open Scientific Intelligence Hackathon 2026

**A chemistry-aware selectivity surrogate pipeline** — the New Zealand hub of the 4th annual global
[OSI Hackathon](docs/00-event/the-global-event.md) for the Physical Sciences & Mathematics.

**Owner:** Nick Jones (njon001@aucklanduni.ac.nz) · **Org:** University of Auckland ·
**Updated:** 2026-09-19

> ## ⏱ 20 working days out
> **Planning session: Mon 21 Sep, 2 h** → [agenda](docs/05-delivery/monday-session.md)
>
> 🔴 **The dates need resolving before Wednesday.** The official event is **21–22 Oct**; this repo
> had been planning to 19–20. **Auckland is already listed as a 2026 hub**, and on the official
> dates New Zealand — first time zone — is the *first hub in the world to start*.
> → [public-presence.md](docs/00-event/public-presence.md) · [issue #12](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/12)
>
> Two days is enough to *run* this pipeline and nowhere near enough to *build* it, so the month is
> the project and the event is the experiment. → [critical-path.md](docs/05-delivery/critical-path.md)

---

## What we're building, in a paragraph

Most drugs fail on **selectivity**, not potency. Conventional screening can't separate a target
from its close relatives because it flattens a 3D pocket into a fingerprint and discards exactly
what makes them different. We're building a **staged funnel** where fast AI surrogates do the
volume work — co-folding, learned ensembles, equivariant pocket scoring — and **GPU quantum
chemistry is spent only where it changes the answer**. Driving case: **CDK9 vs CDK7**.

The deeper question is methodological, and it belongs to every field with expensive experiments:
**when does what you learn from a small experiment actually predict the large one?**

Full version: **[the narrative](docs/00-event/narrative.md)**.

## Start here

| If you are… | Read |
| --- | --- |
| **Coming to Monday's session** | [Monday agenda](docs/05-delivery/monday-session.md) → [critical path](docs/05-delivery/critical-path.md) |
| **Doing something this week** | [Critical path, week 1](docs/05-delivery/critical-path.md#week-1--2127-sep--unblock) · [open issues](https://github.com/drai-inn/drugs-surrogate-pipeline/issues) |
| **Deciding whether to come** | [The narrative](docs/00-event/narrative.md) → [one-pager](outreach/one-pager.md) → [FAQ](outreach/faq.md) |
| **New to AI for science** | [Engagement and on-ramps](docs/00-event/engagement.md) → [Glossary](docs/02-scope/glossary.md) |
| **Inviting someone** | [`outreach/`](outreach/) — templates, poster, short-form copy |
| **Reaching beyond Auckland** | [Interested parties](docs/00-event/interested-parties.md) — three years of projects and people |
| **Wondering how we fit the global event** | [the-global-event.md](docs/00-event/the-global-event.md) |
| New to the science | [Problem statement](docs/01-context/problem-statement.md) → [Architecture](docs/03-pipeline/architecture.md) |
| Owning a pipeline stage | [Your stage page](docs/03-pipeline/stages/) → [Interfaces](docs/03-pipeline/interfaces.md) |
| Here for the ML methodology | [Small-data HPO microtopic](docs/04-experiments/hpo-microtopic.md) |
| Worried about feasibility | [Compute plan](docs/06-feasibility/compute-plan.md) → [Budget](docs/06-feasibility/compute-budget.md) → [Risks](docs/06-feasibility/risks.md) |
| Hosting newcomers | [Engagement](docs/00-event/engagement.md) |
| Coordinating with the US team | [US relay](docs/05-delivery/us-handoff.md) |
| Looking for what's undecided | [Open questions](docs/02-scope/open-questions.md) |

---

## Repo map

```
docs/
  00-event/       ← the front end: narrative, the global event, public presence,
                    engagement, who to reach out to.  OUTWARD-FACING
  01-context/     why this problem; distilled notes on the two source documents
  02-scope/       what's in, what's out, what's still open, glossary
  03-pipeline/    S0–S8 stage decomposition, fidelity contracts, data contracts
  04-experiments/ methodology, parameter space, metrics, the small-data HPO microtopic
  05-delivery/    ← running it: critical path, plan, work packages, roles, US relay.
                    INWARD-FACING
  06-feasibility/ compute plan (GB10/H200), budget, data sources, risks, stage gates
  adr/            five decision records — why we chose what we chose

outreach/         one-pager, seven invitation templates, A3 poster, short-form, FAQ
schemas/          JSON schemas for the benchmark manifest and run records
data/manifest/    example manifest (real curation is work package A)
tools/            stdlib-only: manifest validation, compute budgeting
workflow/         Snakemake DAG sketch (not runnable yet — intentionally a sketch)
refs/             pointers to the source PDFs and external references
```

The split that matters: **`00-event` is what outsiders read, `05-delivery` is how we run it.**
Everything between them is the science.

## Three ideas the repo is built on

1. **Every surrogate owes a fidelity contract.** A stated ground truth, a validation set containing
   close calls, and an explicit trust region. Four surrogates, four contracts. A surrogate can be
   fast, confident and wrong on exactly the cases that matter.
   → [fidelity-contracts.md](docs/03-pipeline/fidelity-contracts.md)
2. **The pipeline *is* the model; its configuration is the hyperparameter vector.** Crop radius and
   microstate count are the object of study, not settings to guess.
   → [hpo-microtopic.md](docs/04-experiments/hpo-microtopic.md)
3. **A newcomer's experience is good when they personally own a result the group uses.** Not a
   tutorial, not shadowing. → [engagement.md](docs/00-event/engagement.md)

## Tools

Standard library only, so anyone can run them on day 1 without an environment:

```bash
make validate && make budget TIER=hackathon_minimum
```

## Contributing

Small commits, one topic per PR. Every stage owner maintains their own stage page. Decisions that
change scope or interfaces get an [ADR](docs/adr/). Numbers carry a provenance tag — `[measured]`,
`[source-doc]`, `[literature]` or `[estimate]`. **An untagged number is a bug.**
