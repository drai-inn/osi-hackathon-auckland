# S3 — Ensemble generation

**Work package:** C · **Owner:** _unassigned_ · **Disciplines:** biophysics, molecular simulation, ML

> The stage with the widest cost range and the largest scientific uncertainty. Also the one
> where a surrogate buys the most — which is why its fidelity contract is the expensive one.

## Purpose

Capture pocket motion and ligand-state variation, so that scoring reflects an ensemble rather
than one arbitrary snapshot. Induced fit and pocket breathing are plausible carriers of paralog
selectivity signal; a static pose cannot express them.

## Inputs

Cropped pockets from [S2](S2-pocket-extraction.md).

## Outputs

Trajectory or multi-model PDB per `pose_id`, with a sampling-method sidecar. See
[interfaces.md](../interfaces.md#s3--s4--ensembles).

## The three modes `[source-doc]`

| Mode | Method | Cost class | Buys |
| --- | --- | --- | --- |
| **Static** | No sampling; the S1 pose as-is | ~0 | The baseline. Always run it |
| **Short relaxation** | OpenMM minimisation + short NVT/NPT, or MACE-driven relaxation | Low–moderate | Removes clashes and gross artefacts from predicted structures |
| **Surrogate ensemble** | BioEmu · AlphaFlow · Boltzmann-generator-style | Moderate | Equilibrium-ish conformer sets without trajectory cost |

Full MD is **out of scope** except as the validation reference on 3–5 systems. `[source-doc]`

## Parameters to perturb `[source-doc]`

| Parameter | Settings | Decision rule |
| --- | --- | --- |
| **Dynamics mode** | static · short relaxation · surrogate ensemble | Cheapest mode that improves stability over static |
| Frames generated | 20, 100, 500 | Enough that clustering is stable; check with a bootstrap |
| Relaxation length | 0, 100 ps, 1 ns | Only if mode = relaxation |
| Force field / MLIP | classical FF · MACE-class MLIP | MLIPs cost more per step; do they change the ensemble? |

Do not run long MD. Do not exceed the settings above. `[source-doc]`

## Metrics

- **Contact persistence** — fraction of frames retaining key hinge/gatekeeper contacts
- RMSD/RMSF spread of the pocket; does the ensemble explore, or jitter?
- **Ranking stability**: does ensemble-weighted scoring change the ranking vs. static, and is the
  change consistent across seeds?
- Agreement with reference MD on the validation subset (the fidelity contract)
- GPU-hours per complex per mode — the number that decides whether this stage survives

## Failure modes

- **Plausible-looking ensembles that miss the discriminating state.** The surrogate reproduces
  bulk flexibility and smooths away the rare conformer that distinguishes CDK9 from CDK7. Overall
  agreement with MD can be high while this is happening.
- **Sampling a cropped, capped system as if it were the protein.** Caps introduce artificial
  rigidity or floppiness at the boundary. Restrain boundary atoms, and say so.
- Non-independent frames treated as independent, inflating apparent cluster populations.
- The surrogate was trained on apo proteins and is applied to holo complexes — a real
  distribution shift for several published ensemble generators. Check what the model was trained on.

## Candidate software

OpenMM (GPU MD, short relaxation) · MACE / ANI-class MLIPs · BioEmu · AlphaFlow · PLUMED (only if
enhanced sampling proves necessary — likely out of scope) `[source-doc]`

## First-day task

Static vs. short relaxation on five complexes, with contact persistence measured for both. This
alone answers "does motion-awareness do anything here?" cheaply enough to decide whether the
surrogate arm is worth setting up.

## Fidelity contract

See [contract 2](../fidelity-contracts.md#2-learned-ensembles-s3--replaces-molecular-dynamics).
Be explicit that a few ns of reference MD establishes *consistency*, not correctness.
