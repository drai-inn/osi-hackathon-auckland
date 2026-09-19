# ADR-0004 — Snakemake + containers; no new distributed infrastructure

**Status:** accepted · **Date:** 2026-09-19 · **Deciders:** Nick Jones

## Context

Multi-stage GPU pipelines attract infrastructure. Workflow engines, feature stores, schedulers,
experiment platforms — each defensible, and collectively capable of consuming an entire hackathon
without producing a scientific result.

The origin document is explicit that this is unnecessary: a Snakemake-based workflow can
orchestrate independent containerised stages with no additional distributed systems, and standard
whole-GPU jobs on Kubernetes HGX H200 are enough for a strong pilot. `[source-doc]`

## Decision

**Snakemake DAG + containers + whole-GPU Kubernetes jobs + MLflow. Nothing else.**

If that proves insufficient, the response is **a smaller run, not more machinery**. This is a
scope boundary, not a preference, and WP-F owns enforcing it.

## Alternatives considered

| Option | Why not |
| --- | --- |
| Nextflow | Comparable; Snakemake's Python-native config suits the configuration-sweep workload better |
| Airflow / Prefect / Argo | Built for scheduled production workloads; heavier than a research sweep needs |
| Ray / Dask | Would help if we needed dynamic distributed scheduling. We don't — stages are embarrassingly parallel over independent items |
| Shell scripts | Tempting at this scale, but loses the DAG, resumability and provenance we need for gate 1 |

## Consequences

**Good:** low setup cost. Familiar to RSE/eResearch communities, so it is a transferable artifact
([Activity 4](../05-delivery/adjacent-activities.md#activity-4-alternate--reproducible-gpu-research-workflows)).
Resumable. Snakemake's caching directly enables the cached-upstream sweep strategy in
[ADR-0003](0003-small-scale-search-before-scale-up.md).

**Bad:** manual GPU allocation, no dynamic rebalancing. Snakemake on Kubernetes is less
well-trodden than on Slurm — WP-F should validate this specifically before the event. Fractional
GPU sharing is out of scope, so small jobs waste capacity.

**Revisit if:** queue-to-compute ratio exceeds 1 and the cause is job granularity rather than
cluster contention — then fractional GPUs or job batching becomes worth the complexity.
