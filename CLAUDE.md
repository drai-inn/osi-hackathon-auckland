# Working notes for AI agents in this repo

## What this repo is

The team repo for the **Auckland hub of the Open Scientific Intelligence Hackathon 2026** — a
global, 16-hub event now in its fourth year. Our project is a 3D chemistry-aware multi-fidelity
surrogate pipeline for drug-target selectivity.

Both halves matter. It is a research project *and* a public, cross-disciplinary event we are
recruiting for, and the repo is structured to keep those visible at once.

**Key dates:** hackathon **Mon 19 – Tue 20 Oct 2026** (2 days) · US relay 20–21 Oct · the month
before it is the build ([docs/05-delivery/critical-path.md](docs/05-delivery/critical-path.md)).

It is currently mostly documents, because the stage implementations land during the month against
frozen interfaces. Do not scaffold a Python package or implement pipeline stages unprompted —
premature code would freeze decisions that are deliberately still open. Check
[critical-path.md](docs/05-delivery/critical-path.md) for what week we are in and what is due.

## Hardware, which affects everything

Two architectures: **dual GB10 (`aarch64`)** for development, pre-computation and the event's
interactive load; **HGX H200 (`x86_64`)** for benchmarks and batch. Anything containerised must
build for both. See [compute-plan.md](docs/06-feasibility/compute-plan.md) and
[ADR-0005](docs/adr/0005-two-tier-compute-gb10-h200.md). This is the most commonly missed
constraint in the repo.

## Conventions that matter

### Provenance tags on every number

Every quantitative claim carries one of:

| Tag | Meaning |
| --- | --- |
| `[measured]` | Someone ran it and recorded it |
| `[source-doc]` | From the origin document — see `docs/01-context/source-notes/pipeline-options.md` |
| `[literature]` | From a published source, cited |
| `[estimate]` | A guess, and flagged as one |

**An untagged number is a bug.** The compute budget is almost entirely `[estimate]` right now and
says so loudly; day 1 of the hackathon converts those to `[measured]`.

### Two framings the docs are built on

- **Every surrogate owes a fidelity contract** (`docs/03-pipeline/fidelity-contracts.md`) — a
  stated ground truth, validation set, agreement metric, and trust region. Four surrogates, four
  contracts.
- **The pipeline is the model; its configuration is the hyperparameter vector**
  (`docs/04-experiments/hpo-microtopic.md`). Crop radius and microstate count are the object of
  study, not settings to be guessed.

### Engagement is a first-class concern

Several participants will be new to AI for science. The design principle is that a newcomer's
experience is good when they **personally own a result the group uses** — see
[engagement.md](docs/00-event/engagement.md). When editing event-facing docs, keep the
on-ramps and the host/owner split intact.

### The structure, and the split that matters

| | |
| --- | --- |
| `docs/00-event/` | **Outward-facing.** Narrative, the global event, public presence, engagement, outreach targets. What people outside the team read |
| `docs/01-context` → `04-experiments` | The science |
| `docs/05-delivery/` | **Inward-facing.** Critical path, plan, work packages, roles, US relay. How we run it |
| `docs/06-feasibility/` | Compute, budget, risks, gates |
| `outreach/` | The collateral itself |

When adding something, ask whether an outsider reads it. If yes it belongs in `00-event` or
`outreach`; if no, it belongs in `05-delivery`. Do not let event material drift into the science
sections — that is what the restructure fixed.

All recruitment copy is **cut from [narrative.md](docs/00-event/narrative.md)**. Rewrite the pitch
there and re-cut, or the versions drift apart within a fortnight.

### Stage / work-package naming

- **Stages** are technical: `S0`–`S8`, one page each under `docs/03-pipeline/stages/`
- **Work packages** are people: `A`–`F`, in `docs/05-delivery/work-packages.md`
- Mapping in `docs/03-pipeline/architecture.md#stage-pages`. Don't invent a third scheme.

### Decisions

Anything that changes scope, an interface, or a methodological commitment gets an ADR in
`docs/adr/`. Six exist. Use `0000-template.md`.

Reasoning that is not a formal decision — what was tried, what was rejected, why the copy reads the
way it does — goes in `docs/05-delivery/sessions/`. **That is the only place in the repo that shows
the evolution of our thinking.** Everywhere else states the current position, with no
strikethroughs and no before-and-after. Read the latest session file before rewriting framing or
copy; most of it has been argued once already.

### Open questions

`docs/02-scope/open-questions.md` is the project's honest edge. When you discover something
uncertain, add a row with an owner — don't paper over it with a plausible assumption. When
something gets resolved, keep the row and add the answer.

## Tone

Written for a mixed-discipline audience: medicinal chemists, quantum chemists, statisticians, RSEs.
Assume intelligence, not shared vocabulary. Name failure modes explicitly — most of the value in
these documents is in the "failure modes" and "risks" sections, because that is where a week gets
wasted or saved.

Be concrete about what is not known. This repo is more useful for being honest about its gaps
than it would be for sounding confident.

## Tools

Standard library only, so anyone can run them on day 1 without an environment:

```bash
python3 tools/validate_manifest.py data/manifest/benchmark_v0.example.csv
python3 tools/compute_budget.py hackathon_minimum
```

If you change the per-unit costs in `compute_budget.py`, reconcile the walkthrough tables in
`docs/06-feasibility/compute-budget.md` — they are generated by hand from the tool's output and
will drift otherwise.

## Source material

Two documents seeded everything, distilled under `docs/01-context/source-notes/`. Read the source
notes before proposing changes to the pipeline design — most "new" ideas are already considered
and rejected there, with reasons.
