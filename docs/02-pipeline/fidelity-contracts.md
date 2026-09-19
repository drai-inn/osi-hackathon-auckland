# Fidelity contracts

> "Surrogates should be treated as accelerators, not unquestioned truth. The practical standard
> is to validate them against a small set of explicit simulations or experimental structure
> trends before using them to drive large downstream decisions." `[source-doc]`

This page turns that sentence into an obligation with a shape. **A surrogate does not enter the
pipeline without a completed contract.** The contract is short by design — if it takes more than
a page, the check is too expensive to actually run.

## Contract template

Every surrogate stage owner fills this in on their stage page:

```markdown
### Fidelity contract — <surrogate name>

| Field | Value |
| --- | --- |
| Replaces | <the expensive thing> |
| Ground truth | <what we compare against, concretely> |
| Validation set | <n, which items, why they are representative> |
| Agreement metric | <the number, with a threshold> |
| Trust region | <where it may be used> |
| Known-invalid region | <where it may NOT be used> |
| Cost of the check | <GPU-hours> |
| Re-validation trigger | <what change invalidates this> |
```

## Why "trust region" is the important field

The instinct is to report a single correlation and move on. That hides the failure mode that
actually bites: a surrogate with r=0.85 overall can be **systematically wrong on precisely the
subset that matters** — here, the close-call pairs where CDK9 and CDK7 scores are within noise.
Those are the compounds the whole pipeline exists to distinguish.

**So: report agreement on the discriminating subset separately from overall agreement.** If the
validation set contains no close calls, it is not a validation set.

## The four contracts

Filled in by stage owners; the rows below are the *starting proposals* to argue with, not
decisions. Cost figures are `[estimate]` until WP-F measures them.

### 1. Co-folding (S1) — replaces experimental structure determination

| Field | Proposal |
| --- | --- |
| Ground truth | Held-out co-crystal structures for CDK9/7/12/13 ligands from the PDB |
| Validation set | Every ligand in the manifest with an existing co-crystal (expect 5–15 of 12–20) |
| Agreement metric | Ligand-RMSD to crystal pose after pocket alignment; **fraction < 2.0 Å**. Plus hinge H-bond recovery rate |
| Trust region | ATP-site binders chemically similar to the co-folding model's training distribution |
| Known-invalid region | Allosteric/cryptic sites; covalent binders; anything with a cofactor we stripped |
| Re-validation trigger | New model version; new target family |

⚠️ **Circularity warning:** these co-crystals are almost certainly in the co-folding model's
training data. A 1.2 Å RMSD here means "it memorised", not "it generalises". Report it, but
weight the *held-out-by-date* or *held-out-by-scaffold* subset far more heavily. WP-A should
flag which PDB entries postdate the model's training cutoff.

### 2. Learned ensembles (S3) — replaces molecular dynamics

| Field | Proposal |
| --- | --- |
| Ground truth | Short explicit MD (OpenMM, a few ns) on a small subset |
| Validation set | 3–5 complexes spanning rigid → flexible, chosen by WP-A/WP-C |
| Agreement metric | Overlap of sampled pocket conformational space (RMSF profile correlation; cluster-population agreement over shared microstates) |
| Trust region | Pocket breathing and side-chain rearrangement on the timescale the surrogate was trained for |
| Known-invalid region | Large loop rearrangements, DFG flips, anything the reference MD also fails to sample |
| Cost of the check | The dominant validation cost in the hackathon — budget it explicitly |
| Re-validation trigger | New target family; change of force field or surrogate |

Note the honest limitation: a few ns of MD is itself not converged. This contract establishes
*consistency*, not correctness. Say so in the write-up.

### 3. Equivariant scorer (S5) — replaces physics-based rescoring

| Field | Proposal |
| --- | --- |
| Ground truth | Harmonised experimental activity (WP-A), and S6 quantum interaction energies where available |
| Validation set | The full manifest, with leave-one-scaffold-out splits |
| Agreement metric | Spearman ρ on **selectivity ratio** (not absolute affinity); enrichment of known-selective over known-non-selective; **calibration**: predicted uncertainty vs. actual residual |
| Trust region | Pockets geometrically similar to training; crop radii within the tested range |
| Known-invalid region | Ligand chemotypes absent from training; metal-coordinating chemistry |
| Re-validation trigger | Any retraining in S7 — this contract is re-checked every feedback iteration |

Calibration is not optional here: [S7](stages/S7-feedback-learning.md) *acquisition* depends on
the uncertainty estimate being meaningful. An uncalibrated scorer makes active learning
indistinguishable from random sampling — which is exactly what the random-acquisition control
will reveal.

### 4. Delta-learned correction (S7) — replaces running quantum on everything

| Field | Proposal |
| --- | --- |
| Ground truth | Held-out cuEST labels, never used for fitting |
| Validation set | A random-acquisition holdout reserved from the start (≥20% of the label budget) |
| Agreement metric | Error reduction per label vs. the random-acquisition control |
| Trust region | Within the chemical and geometric neighbourhood of labelled examples — quantify with a distance-to-training-set measure |
| Known-invalid region | Extrapolation beyond that neighbourhood. Report the fraction of scored candidates that fall outside it |
| Re-validation trigger | Every acquisition round |

**Reserve the holdout before the first label is computed.** With 20–50 labels total, a holdout
carved out afterwards is not a holdout.

## The meta-contract

The quantum layer (S6) is the only stage whose output we treat as near-truth, and it has its own
convergence obligation: **quantum consistency** — convergence rate and sensitivity of electronic
features to theory level and pocket-shell size. `[source-doc]` If S6 labels are not stable under
a change of crop radius, they are not a ground truth and contracts 3 and 4 have no foundation.

WP-E runs this check **first**, before generating any production labels. It is the load-bearing
check of the entire hackathon.
