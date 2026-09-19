# Chemistry-Aware Selectivity Surrogate Pipeline — Scoping Repo

**Status:** pre-hackathon scoping · **Owner:** Nick Jones (njon001@aucklanduni.ac.nz) · **Last updated:** 2026-09-19

This repo is the shared ground for a cross-disciplinary team at the University of Auckland
scoping a **3D, chemistry-aware, multi-fidelity surrogate pipeline** for drug-discovery
selectivity problems — and for the hackathon that will test whether it is worth scaling up.

It contains **no production pipeline code yet, and that is deliberate.** What it contains is
the scope, the stage decomposition, the parameter space, the metrics, the compute budget, and
the gates that decide whether we go further. Code lands after the stage owners agree on
interfaces.

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
| New to the project | [Problem statement](docs/00-context/problem-statement.md) → [Architecture](docs/02-pipeline/architecture.md) |
| Deciding whether to join | [Adjacent activities](docs/04-hackathon/adjacent-activities.md) |
| Owning a pipeline stage | [Your stage page](docs/02-pipeline/stages/) → [Interfaces](docs/02-pipeline/interfaces.md) |
| Here for the ML methodology | [Small-data HPO microtopic](docs/03-experiments/hpo-microtopic.md) |
| Worried about feasibility | [Compute budget](docs/05-feasibility/compute-budget.md) → [Risks](docs/05-feasibility/risks.md) |
| Running the hackathon | [Hackathon plan](docs/04-hackathon/plan.md) |
| Looking for what's undecided | [Open questions](docs/01-scope/open-questions.md) |

---

## Repo map

```
docs/
  00-context/   why this problem, and distilled notes on the two source documents
  01-scope/     what's in, what's out, what's still open, glossary
  02-pipeline/  stage-by-stage technical decomposition + data contracts between stages
  03-experiments/ methodology, parameter space, metrics, the small-data HPO microtopic
  04-hackathon/ plan, work packages, cross-disciplinary engagement tracks, roles
  05-feasibility/ compute budget, data sources, risk register, stage gates
  adr/          architecture decision records — why we chose what we chose
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

## Contributing

Work in the open, small commits, one topic per PR. Every stage owner maintains their own stage
page. Decisions that change scope or interfaces get an [ADR](docs/adr/). Numbers in docs carry
a provenance tag: `[measured]`, `[source-doc]`, `[literature]`, or `[estimate]` — an untagged
number is a bug.
