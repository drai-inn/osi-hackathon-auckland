# Interfaces and data contracts

Six groups working in parallel integrate on the last day or they don't integrate at all. The way
that goes wrong is never the science — it's that WP-C emits a trajectory directory and WP-D
expects a single PDB with a specific residue numbering.

**Rule: interfaces are frozen at the start of day 1 and changed only by ADR.** A stage may be a
stub returning fake-but-well-formed data; it may not have an undefined output shape.

## Identity and provenance

Two things every artifact carries, everywhere:

```
run_id      ULID, one per pipeline invocation
config_hash sha256 of the canonicalised configuration dict
```

Plus the identity triple that threads through S1→S7:

```
ligand_id   stable key from the manifest (not a SMILES string, not a name)
target_id   UniProt accession + construct tag, e.g. P50750_CDK9_full
pose_id     f"{ligand_id}__{target_id}__p{n}"
state_id    f"{pose_id}__s{m}"     # microstate after S4
```

`ligand_id` is assigned once by WP-A and never regenerated. If two groups independently
canonicalise SMILES they will disagree on stereochemistry, and the join will silently drop rows.

## Layout

One directory per run, immutable once written:

```
artifacts/{run_id}/
  config.yaml            resolved configuration, including every default
  manifest.csv           snapshot of the input manifest (copied, not referenced)
  s1_complexes/{pose_id}.cif
  s2_pockets/{pose_id}.pdb
  s3_ensembles/{pose_id}/frames.xtc | conformers.pdb
  s4_states/{state_id}.pdb
  s5_scores/scores.parquet
  s6_labels/labels.parquet
  s6_labels/raw/{state_id}/          native quantum outputs, kept verbatim
  s7_models/{iteration}/
  metrics/                           everything MLflow also logs, on disk as well
  provenance.json        image digests, model weights hashes, git sha, GPU type
```

`provenance.json` matters more than it looks. "Which Boltz-2 weights produced this?" is asked on
day 4 and unanswerable if not recorded on day 1.

## Stage contracts

### S0 → S1 · benchmark manifest
`manifest.csv`, schema at [`schemas/benchmark_manifest.schema.json`](../../schemas/benchmark_manifest.schema.json),
validated by [`tools/validate_manifest.py`](../../tools/validate_manifest.py).
One row per ligand–target pair. Carries `ligand_id`, `target_id`, canonical SMILES, InChIKey,
activity value + unit + assay type + source, `is_decoy`, `selectivity_class`, `split`.

### S1 → S2 · predicted complexes
mmCIF per `pose_id`. Required: full complex coordinates, per-residue and per-atom confidence
(pLDDT/PAE equivalents), model identity and version, and the ranking score used to select the
pose. Author residue numbering preserved and mapped to UniProt numbering in a sidecar.

### S2 → S3 · cropped pockets
PDB per `pose_id`. Required: crop radius used, the residue set retained, how boundaries were
capped, protonation states assigned and by what tool, ligand in a separate chain. **Cap
treatment must be identical between S3 and S6** or the quantum labels describe a different
molecule than the one that was sampled.

### S3 → S4 · ensembles
Either a trajectory (`.xtc` + topology) or a multi-model PDB. Required sidecar: sampling method,
number of frames, timestep or generation parameters, and whether frames are statistically
independent. That last field determines whether clustering populations mean anything.

### S4 → S5 · microstates
One PDB per `state_id`, plus `states.parquet` with `state_id`, `pose_id`, cluster population
weight, and representative-selection method. **Weights must sum to 1.0 per pose** — S5's
ensemble-weighted score depends on it.

### S5 → S6 · scores and the uncertainty list
`scores.parquet`: `state_id`, `score`, `score_std` (or full predictive distribution), `model_id`,
`config_hash`. Plus `acquisition.csv`: the shortlist for S6 with the acquisition reason
(`top_ranked` | `high_uncertainty` | `random_control`). **The `random_control` rows are not
optional** — they are the denominator for the acquisition-value gate.

### S6 → S7 · quantum labels
`labels.parquet`: `state_id`, interaction energy, ESP-derived features, partial charges summary,
theory level, basis set, convergence flag, wall-clock, GPU-hours. Non-converged calculations are
**retained with the flag set**, never silently dropped — the convergence rate is one of our
metrics. Raw outputs kept under `s6_labels/raw/`.

### S7 → S5 · improved scorer
Model artifact + `model_card.md` recording: training set composition, which labels were used,
which holdout was reserved, validation metrics, and the re-run fidelity contract from
[fidelity-contracts.md](fidelity-contracts.md#3-equivariant-scorer-s5--replaces-physics-based-rescoring).

## Contract tests before the science

WP-F ships, on day 1, a `make smoke` that pushes **five synthetic ligand–target pairs** through
every stage with stub implementations. Each stage owner's first commit makes their stub pass.
Real implementations then replace stubs one at a time behind a passing test.

This costs half a day and is the difference between an integrated run and six demos.

## Configuration

One YAML, one schema, resolved and written to `config.yaml` with defaults expanded. Every stage
reads its own sub-tree and **must not read another stage's**. The flat key namespace is what the
sensitivity analysis in [hpo-microtopic.md](../04-experiments/hpo-microtopic.md) operates on, so
key names are part of the interface:

```yaml
s1: {model: boltz2, n_poses: 3, seed: 0}
s2: {crop_radius_A: 12, cap: h, protonation: propka}
s3: {mode: surrogate, method: bioemu, n_frames: 100}
s4: {n_states: 3, clustering: kmeans_rmsd}
s5: {model: nesso1, capacity: medium, graph_cutoff_A: 5.0}
s6: {theory: r2scan-3c, shell_A: 8, max_labels: 50}
s7: {acquisition: uncertainty, threshold_pct: 10, holdout_pct: 20}
```
