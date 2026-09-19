# Roles, people, and who to invite

Names are deliberately blank. **Filling them in is Monday's job** and the top of the critical path
([A3](../02-scope/open-questions.md), [A5](../02-scope/open-questions.md),
[monday-session.md](monday-session.md)).

## Core roles

| Role | Responsibility | Name |
| --- | --- | --- |
| **Programme lead** | Scope, gates, the go/no-go call, external engagement | Nick Jones |
| **Methodology lead** | The four diagnostics, sensitivity analysis, statistical protocol. Cross-cutting, not attached to a WP | _unassigned_ |
| **WP-A owner** | Benchmark and data | _unassigned_ |
| **WP-B owner** | Structure generation and pocket extraction | _unassigned_ |
| **WP-C owner** | Ensembles | _unassigned_ |
| **WP-D owner** | Scoring and feedback learning | _unassigned_ |
| **WP-E owner** | Quantum labelling | _unassigned_ |
| **WP-F owner** | Workflow, infrastructure, telemetry | _unassigned_ |

A work package without a named owner by **Fri 2 Oct** should be cut, not hoped for.

## Hosts — a separate, mandatory role

Each package also needs a **host**, who is *not* the owner: responsible for the newcomers attached
to that package, for getting them started, and for making sure their contribution lands in the
output. [Why the split is mandatory](../00-event/engagement.md#the-structural-fix-split-the-host-role).

| Package | Host | Their on-ramps |
| --- | --- | --- |
| A | _unassigned_ | [C break the benchmark](../00-event/engagement.md#c-break-the-benchmark--medicinal-chemistry-pharmacology--60-min) |
| B | _unassigned_ | [B pose triage](../00-event/engagement.md#b-pose-triage--structural-biology-medicinal-chemistry--zero-code) |
| C | _unassigned_ | [A your run](../00-event/engagement.md#a-your-run-your-parameter--anyone-including-non-coders--20-min) |
| D | _unassigned_ | [A your run](../00-event/engagement.md#a-your-run-your-parameter--anyone-including-non-coders--20-min) |
| E | _unassigned_ | [Activity 3](adjacent-activities.md#activity-3--the-fidelity-ladder-quantum-surrogates-and-knowing-when-to-trust-them) |
| F | _unassigned_ | [A your run](../00-event/engagement.md#a-your-run-your-parameter--anyone-including-non-coders--20-min) |

## Skills needed, by discipline

| Discipline | Where it is load-bearing | Minimum |
| --- | --- | --- |
| Medicinal chemistry / pharmacology | WP-A: assay harmonisation, decoy design, activity cliffs | 1 |
| Structural biology | WP-A/B: structure selection, kinase conformational states | 1 |
| Computational chemistry | WP-B/C/E: pocket prep, protonation, quantum setup | 1–2 |
| Quantum chemistry | WP-E: theory levels, convergence, error cancellation | 1 |
| Molecular simulation / biophysics | WP-C: MD, ensembles, clustering | 1–2 |
| Machine learning (geometric DL) | WP-D: equivariant models, uncertainty | 1–2 |
| Statistics / experimental design | Methodology: sensitivity, intervals, pre-registration | 1 |
| Research software engineering / HPC | WP-F: Snakemake, containers, Kubernetes GPU | 1–2 |

The two most commonly under-resourced, in projects of this shape: **statistics** and **RSE**. Both
are cross-cutting, neither produces a headline result, and both are the reason the headline result
is or isn't believable.

## Who to invite, and with what ask

Invitations should name the thing the person's field owns, not the project. See the framing at the
foot of [adjacent-activities.md](adjacent-activities.md#invitation-framing).

| Constituency | The ask | Their activity |
| --- | --- | --- |
| Med chem / pharmacology groups | "Tell us why our benchmark is wrong before we build on it" | [1](adjacent-activities.md#activity-1--selectivity-benchmark-clinic) |
| Statistics / ML methods groups | "Help us answer when small experiments transfer" | [2](adjacent-activities.md#activity-2--small-data-hyperparameter-science) |
| Empirical groups with expensive experiments (ecology, clinical, materials, education) | "Bring your own pipeline to the small-data clinic" | [2](adjacent-activities.md#activity-2--small-data-hyperparameter-science) |
| Physics / quantum chemistry / numerical analysis | "When is a cheap approximation good enough, and how would you know?" | [3](adjacent-activities.md#activity-3--the-fidelity-ladder-quantum-surrogates-and-knowing-when-to-trust-them) |
| eResearch / RSE / NeSI | "A reusable pattern for GPU research pipelines on campus" | [4](adjacent-activities.md#activity-4-alternate--reproducible-gpu-research-workflows) |
| Industry / clinical partners | Observers on day 1 and day 5; they sharpen the target choice | — |

## Levels of commitment to offer

Not everyone can give a week. Offer three doors:

1. **Full participant** — embedded in a work package, all five days
2. **Clinic participant** — 90 minutes on day 1 in one activity, plus the day-5 presentations
3. **Reviewer** — reads this repo, comments on [open-questions.md](../02-scope/open-questions.md),
   attends day 5

Door 3 costs an hour and is how several of the most useful contributions will arrive. Make it easy
to take.

**Invitations go out by Wed 23 Sep.** Four weeks is already short notice for a two-day commitment;
five days from now is not a notice period at all.
