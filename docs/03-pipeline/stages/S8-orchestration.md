# S8 — Orchestration, reproducibility and telemetry

**Work package:** F · **Owner:** _unassigned_ · **Disciplines:** research software engineering, HPC, MLOps, e-research

> Not a scientific stage, and the one most likely to decide whether the hackathon produces an
> integrated result or six demos.

## Purpose

Make the pipeline runnable in one command, reproducibly, with every cost and metric recorded —
and keep it simple enough that no one spends the week on infrastructure.

## Design constraint

**Snakemake DAG + containers + whole-GPU jobs on Kubernetes HGX H200. No additional distributed
systems.** `[source-doc]` If that is insufficient, the correct response is a smaller run, not more
machinery. This is a scope boundary, not a preference.

## Outputs

| Artifact | Description |
| --- | --- |
| `workflow/Snakefile` | The DAG. Sketch at [workflow/Snakefile.sketch](../../../workflow/Snakefile.sketch) |
| `make smoke` | Five synthetic pairs through every stage with stubs — ships day 1 |
| Container images | One per stage, digest-pinned |
| MLflow deployment | Metric and parameter tracking for every run |
| `provenance.json` writer | Image digests, weight hashes, git sha, GPU type |
| **Cost telemetry** | GPU-seconds per stage per item, written to the run record |
| `reproducibility_report.md` | Same manifest + config → same artifacts. The technical-reproducibility gate |

## Parameters to perturb `[source-doc]`

| Parameter | Settings |
| --- | --- |
| Snakemake concurrency | jobs in flight vs. cluster queue behaviour |
| GPU request shape | whole-GPU vs. fractional (start whole; fractional is a scope creep risk) |
| Artifact layout | see [interfaces.md](../interfaces.md#layout) |

## Cost telemetry is a first-class deliverable

Almost every gate in [stage-gates.md](../../06-feasibility/stage-gates.md) is of the form
*"is X worth its cost?"* — and every cost figure in
[compute-budget.md](../../06-feasibility/compute-budget.md) is currently `[estimate]`. WP-F's job
is to make every one of them `[measured]` by end of day 1.

Emit per stage, per item: GPU-seconds, wall-clock, peak memory, exit status. Write it to the run
record ([schema](../../../schemas/run_record.schema.json)) as well as MLflow, so it survives the
MLflow instance.

## Metrics

- Time from `git clone` to a passing smoke test, for a new team member
- Stage failure rate and mean time to diagnose
- Queue wait vs. compute time ratio — if queueing dominates, run size is the wrong lever
- Reproducibility: byte-identical or metric-identical reruns

## Failure modes

- **Six groups building six container stacks on day 1.** Pre-build base images before the
  hackathon. This is the single highest-value piece of pre-work in the project.
- Stages passing objects in memory during development, then failing when actually decoupled —
  the contract tests exist to prevent this
- MLflow as a single point of failure with no on-disk fallback
- Config drift: stages reading environment variables instead of the resolved `config.yaml`
- Cluster access or quota discovered to be inadequate on day 1 (→ [A2](../../02-scope/open-questions.md))

## Candidate software

Snakemake · Apptainer/Singularity or Docker · Kubernetes · MLflow · DVC or plain content-addressed
storage for artifacts

## First-day task

`make smoke` green, with every stage stubbed, before lunch. Then hand each stage owner a failing
test for their real implementation.

## Pre-hackathon work (highest priority in the project)

1. Confirm cluster access, quota, queue policy ([A2](../../02-scope/open-questions.md))
2. Build and publish base images for each stage
3. Stand up MLflow
4. Ship the stub DAG and `make smoke` so people arrive to a working repo
