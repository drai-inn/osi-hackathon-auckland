# References

## Source documents

Place local copies here (they are gitignored — check licensing before committing anything):

| File | Description |
| --- | --- |
| `diway-3D-chemistry-aware-selectivity-pipeline-options.pdf` | The origin document. Distilled in [pipeline-options.md](../docs/01-context/source-notes/pipeline-options.md) |
| `2608.11859v1.pdf` | Lourie, Cho, Ullrich & Lotfi, *Small-Scale Experiments: Are We There Yet?* Distilled in [small-scale-experiments.md](../docs/01-context/source-notes/small-scale-experiments.md) |

Originals as supplied: `~/Downloads/diway-3D Chemistry-Aware Selectivity Pipeline Options-180926-094602.pdf`
and `~/Downloads/2608.11859v1.pdf`.

## Key external references

**Methodology**
- Lourie, Cho, Ullrich & Lotfi (2026). *Small-Scale Experiments: Are We There Yet?* arXiv:2608.11859
- Lourie et al. (2025). The noisy quadratic limit — cited within the above as the tuning-completeness diagnostic
- Kaplan et al. (2020); Hoffmann et al. (2022) — the scaling-law lineage
- Porian et al. (2024) — reconciling Kaplan vs. Hoffmann; methodological choices at small scale

**Software**
- `NVIDIA/CUDALibrarySamples` — cuEST implementation reference
- Boltz-2 — open co-folding / complex prediction
- Nesso-1 (Valence Labs) — equivariant protein–ligand binding affinity model
- OpenMM — GPU molecular dynamics
- MACE — machine-learned interatomic potentials
- MDAnalysis / MDTraj — trajectory analysis and clustering
- PLUMED — enhanced sampling (likely out of hackathon scope)
- BioEmu, AlphaFlow — generative ensemble surrogates
- Snakemake, MLflow — orchestration and tracking

**Data**
- ChEMBL · BindingDB · PDB · PDBbind · AlphaFold DB

> Versions and exact citations are WP-A/WP-F's responsibility to pin before the hackathon. A
> reference without a version is not reproducible.
