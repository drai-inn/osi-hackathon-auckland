# S1 — Complex generation

**Work package:** B · **Owner:** _unassigned_ · **Disciplines:** structural biology, computational chemistry, ML

## Purpose

Generate plausible 3D target–ligand complexes where co-crystal structures are absent or
incomplete — the structural hypotheses everything downstream operates on.

## Inputs

`manifest.csv` (ligand SMILES, target sequences/structures) from [S0](S0-benchmark.md).

## Outputs

mmCIF per `pose_id` with confidence estimates and model provenance. See
[interfaces.md](../interfaces.md#s1--s2--predicted-complexes).

## Parameters to perturb `[source-doc]`

| Parameter | Settings | Decision rule |
| --- | --- | --- |
| **Pose count** | 1, 3, 5 | Increase only if rankings change materially |
| Model | Boltz-2 · Chai-class | Compare on the co-crystal subset |
| Template use | none · apo template · holo template | Templates likely help but risk locking in one conformation |
| Seed | ≥3 seeds at fixed config | Measures generation variance — a cost of doing business, not a hyperparameter |

Do not exceed five poses per complex during the hackathon. `[source-doc]`

## Metrics

- **Ligand-RMSD to crystal** on the co-crystal subset; fraction < 2.0 Å
- **Hinge H-bond recovery** — kinase-specific, and more diagnostic than global RMSD
- Confidence calibration: does predicted confidence track actual RMSD?
- Pose diversity across seeds (are 3 poses actually 3 hypotheses, or 3 copies?)
- Wall-clock and GPU-hours per complex `[measure on day 1]`

## Failure modes

- **Training-set memorisation** mistaken for accuracy. Most CDK co-crystals predate these models'
  cutoffs. → see the circularity warning in [fidelity-contracts.md](../fidelity-contracts.md#1-co-folding-s1--replaces-experimental-structure-determination)
- **Mode collapse across seeds** — n_poses=5 that are the same pose five times, paying 5× for no
  information. Check this explicitly; it is cheap to check and easy to miss.
- **Conformational state locked by the template.** If all four CDKs are modelled from a DFG-in
  template, we have assumed away part of the selectivity signal.
- Protonation/tautomer state chosen implicitly by the model and inconsistent with S2/S6.

## Candidate software

Boltz-2 · Chai-class predictors · pocket-conditioned diffusion pose generators (as a contrast
arm, if time allows)

## First-day task

Run one ligand × two targets end-to-end, record GPU-hours, and publish the real per-complex cost.
Every sizing estimate in [compute-budget.md](../../05-feasibility/compute-budget.md) is currently
`[estimate]` and should be replaced by this measurement before anyone commits to a run size.

## Fidelity contract

See [contract 1](../fidelity-contracts.md#1-co-folding-s1--replaces-experimental-structure-determination).
Owner completes the table on this page before S1 output is used downstream.
