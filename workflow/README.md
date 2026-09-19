# Workflow

**Nothing here runs yet.** [`Snakefile.sketch`](Snakefile.sketch) is a sketch whose job is to make
the DAG shape, artifact layout and config namespace concrete enough to argue about before the
hackathon starts.

## What WP-F ships on day 1

1. A real `Snakefile` derived from the sketch
2. Stub scripts for every stage — each produces well-formed fake output matching
   [interfaces.md](../docs/02-pipeline/interfaces.md)
3. `make smoke` — five synthetic ligand–target pairs through every stage, green before lunch
4. A failing contract test handed to each stage owner

Real implementations then replace stubs one at a time, behind a passing test. That ordering is the
whole defence against [R5 (integration fails on day 4)](../docs/05-feasibility/risks.md).

## Design commitments in the sketch

- **`config_hash` in the output path.** Different configurations coexist; reruns at an existing
  configuration are free. This is what makes the sweep strategy affordable.
- **Snakemake caching as the sweep mechanism.** WP-C and WP-D sweep their own parameters against
  S1/S2 output generated once ([ADR-0003](../docs/adr/0003-small-scale-search-before-scale-up.md)).
- **Every rule writes cost telemetry.** Gate 6 and the whole compute budget depend on GPU-seconds
  per item per stage being recorded, not estimated.
- **`static` mode in S3 is a GPU-free passthrough.** The baseline must stay cheap, because
  everything else is measured against it.
- **S6 enforces its own budget ceiling.** The rule refuses to exceed `s6.max_labels`. A
  budget you can overrun by accident is not a budget.

## Config

One YAML, defaults expanded and written to `config.yaml` in the run directory. Stages read their
own sub-tree and must not read another's. Key names are part of the interface — the sensitivity
analysis operates on them. See
[interfaces.md](../docs/02-pipeline/interfaces.md#configuration).

## Open

- **Snakemake on Kubernetes is less well-trodden than Snakemake on Slurm.** WP-F should validate
  the executor specifically, before the event ([ADR-0004](../docs/adr/0004-snakemake-containers-no-new-infra.md)).
- Whole-GPU jobs only for now; fractional GPU sharing is out of scope.
- `POSE_IDS` in the sketch comes from the `s1_complexes` checkpoint — the real implementation needs
  Snakemake's checkpoint machinery, which is the fiddliest part of the DAG.
