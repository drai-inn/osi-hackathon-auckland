# Chemistry-Aware Selectivity Surrogate Pipeline — Scoping Repo

**Status:** pre-hackathon build · **Owner:** Nick Jones (njon001@aucklanduni.ac.nz) · **Last updated:** 2026-09-19

> ## ⏱ 20 working days to go
> **Hackathon: 2 days in October** · **Planning session: Mon 21 Sep, 2 h**
>
> 🔴 **The dates need resolving before Wednesday.** The official OSI Hackathon is **21–22 Oct**;
> this repo had been planning to 19–20. Auckland is already listed as a 2026 hub.
> See [public-presence.md](docs/04-hackathon/public-presence.md).
>
> Two days is enough to *run* this pipeline and nowhere near enough to *build* it, so the month
> is the project and the event is the experiment. Start at
> **[critical-path.md](docs/04-hackathon/critical-path.md)**.

This repo is the shared ground for a cross-disciplinary team at the University of Auckland
scoping a **3D, chemistry-aware, multi-fidelity surrogate pipeline** for drug-discovery
selectivity problems — and for the hackathon that will test whether it is worth scaling up.

It contains the scope, the stage decomposition, the parameter space, the metrics, the compute
budget, and the gates that decide whether we go further — plus the week-by-week plan for building
the thing before 19 Oct. Stage code lands during the month, against frozen interfaces.

---

## The one-paragraph version

Conventional 1D/2D screening answers *"does this chemotype bind something?"* It does badly at
*"why would this bind **this** pocket and not its close paralog?"* — where the signal lives in
local 3D geometry, induced fit, electrostatics and conformational ensembles. The proposal is a
**staged funnel** in which cheap AI surrogates do the volume work (co-folding, learned
ensembles, equivariant pocket scoring) and an expensive high-fidelity method (GPU quantum
chemistry) is spent only where it buys the most information. The scientific bet is that a
**small, well-chosen set of 3D labels beats a large, indiscriminate one**. The methodological
bet — borrowed from [Lourie et al. 2026](docs/00-context/source-notes/small-scale-experiments.md) —
is that we can **find the settings that matter at tiny scale and carry them up**, provided we
search the configuration space far more thoroughly than teams usually do.

Driving case: **CDK9 vs. CDK7 / CDK12 / CDK13** paralog selectivity.

---

## Start here

| If you are… | Read |
| --- | --- |
| **Coming to Monday's session** | [Monday agenda](docs/04-hackathon/monday-session.md) → [critical path](docs/04-hackathon/critical-path.md) |
| **Doing something this week** | [Critical path, week 1](docs/04-hackathon/critical-path.md#week-1--2127-sep--unblock) |
| Want the story | **[The narrative](docs/00-context/narrative.md)** — everything in `outreach/` is cut from it |
| New to the project | [Problem statement](docs/00-context/problem-statement.md) → [Architecture](docs/02-pipeline/architecture.md) |
| Inviting someone | [`outreach/`](outreach/) — one-pager, seven invitation templates, poster, FAQ |
| Reaching out beyond Auckland | [Interested parties](docs/04-hackathon/interested-parties.md) — three years of hackathon projects and people |
| New to AI for science, coming to the event | [Engagement and on-ramps](docs/04-hackathon/engagement.md) → [Glossary](docs/01-scope/glossary.md) |
| Hosting newcomers | [Engagement](docs/04-hackathon/engagement.md) |
| Deciding whether to join | [Adjacent activities](docs/04-hackathon/adjacent-activities.md) |
| Owning a pipeline stage | [Your stage page](docs/02-pipeline/stages/) → [Interfaces](docs/02-pipeline/interfaces.md) |
| Here for the ML methodology | [Small-data HPO microtopic](docs/03-experiments/hpo-microtopic.md) |
| Worried about feasibility | [Compute budget](docs/05-feasibility/compute-budget.md) → [Risks](docs/05-feasibility/risks.md) |
| Running the hackathon | [Hackathon plan](docs/04-hackathon/plan.md) |
| Working out which machine to use | [Compute plan](docs/05-feasibility/compute-plan.md) |
| Coordinating with the US team | [US relay](docs/04-hackathon/us-handoff.md) |
| Looking for what's undecided | [Open questions](docs/01-scope/open-questions.md) |

---

## Repo map

```
docs/
  00-context/   why this problem, and distilled notes on the two source documents
  01-scope/     what's in, what's out, what's still open, glossary
  02-pipeline/  stage-by-stage technical decomposition + data contracts between stages
  03-experiments/ methodology, parameter space, metrics, the small-data HPO microtopic
  04-hackathon/ critical path, plan, work packages, engagement, US relay, roles
  05-feasibility/ compute plan (GB10/H200), compute budget, data, risks, stage gates
  adr/          architecture decision records — why we chose what we chose
outreach/       invitations, one-pager, A3 poster, short-form copy, FAQ
schemas/        JSON schemas for the shared benchmark manifest and run records
data/manifest/  example manifest (real curation is work package A)
tools/          small stdlib-only utilities: manifest validation, compute budgeting
workflow/       Snakemake DAG sketch (not runnable yet — intentionally a sketch)
refs/           pointers to the source PDFs and external references
```

## Two ideas worth internalising before you read further

1. **Every surrogate owes a fidelity contract.** A surrogate is only allowed into the pipeline
   with a stated ground truth, a validation set, and a bound on where it may be trusted. See
   [fidelity-contracts.md](docs/02-pipeline/fidelity-contracts.md). This is the difference
   between a pipeline and a stack of hopeful approximations.
2. **The pipeline *is* the model; its configuration is the hyperparameter vector.** Pocket crop
   radius, number of retained microstates, quantum theory level and scorer depth are not
   "settings" — they are the object of study. See
   [hpo-microtopic.md](docs/03-experiments/hpo-microtopic.md).
3. **A newcomer's experience is good when they personally own a result the group uses.** Not a
   tutorial, not shadowing — a real contribution made with expertise they already have. See
   [engagement.md](docs/04-hackathon/engagement.md).

## Contributing

Work in the open, small commits, one topic per PR. Every stage owner maintains their own stage
page. Decisions that change scope or interfaces get an [ADR](docs/adr/). Numbers in docs carry
a provenance tag: `[measured]`, `[source-doc]`, `[literature]`, or `[estimate]` — an untagged
number is a bug.
