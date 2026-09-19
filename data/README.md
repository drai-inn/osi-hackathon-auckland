# Data

## What lives here

| Path | Content | Status |
| --- | --- | --- |
| `manifest/benchmark_v0.example.csv` | **Placeholder.** Six synthetic rows illustrating the required columns and the shape of a valid selectivity pair. Not real chemistry | committed |
| `manifest/benchmark_v1.csv` | The real manifest, produced by WP-A | **does not exist yet** — [S0](../docs/03-pipeline/stages/S0-benchmark.md) |
| `structures/` | Cleaned PDB structures + the cleaning protocol | not yet |
| `splits.json` | Scaffold-based splits and leave-one-scaffold-out folds | not yet |

The example rows are deliberately fake — placeholder SMILES, placeholder InChIKeys, an invented
assay id. They exist so the validator and the smoke test have something to chew on, and so WP-A
starts from a shape rather than a blank page. **Do not treat any value in that file as chemistry.**

## Validate before committing

```bash
python3 tools/validate_manifest.py data/manifest/benchmark_v1.csv
```

Standard library only — no environment setup needed. The validator checks schema conformance plus
the cross-row problems that actually invalidate a selectivity benchmark:

- duplicate ligand–target pairs (silent double-counting)
- one `ligand_id` mapping to multiple molecules
- **activity reported under different assay types across targets** — a selectivity ratio built
  from mixed assays is an artefact, not a measurement ([C1](../docs/02-scope/open-questions.md))
- differing ATP concentrations across targets (warning — needs a Cheng–Prusoff correction)
- scaffold overlap between train and test
- no `non_selective` compounds — without discriminating negatives, enrichment may be achievable on
  molecular weight alone ([R6](../docs/06-feasibility/risks.md))
- DUD-E-only decoys, which carry biases a 2D baseline can exploit

Warnings are judgement calls; errors are not. Do not merge a manifest with errors.

## Large artifacts

Structures, ensembles and quantum outputs do **not** go in git. They live under `artifacts/`
(gitignored) with the layout in [interfaces.md](../docs/03-pipeline/interfaces.md#layout). Storage
plan is WP-F's; budget ~1 TB for the hackathon minimum `[estimate]`.

## Licensing

If we intend to release the benchmark ([E2](../docs/02-scope/open-questions.md)), every source must
permit it. ChEMBL is CC BY-SA 3.0, which is share-alike — check the implications before mixing
sources. See [data-sources.md](../docs/06-feasibility/data-sources.md).
