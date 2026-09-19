# S4 — Ensemble reduction

**Work package:** C · **Owner:** _unassigned_ · **Disciplines:** statistics, molecular simulation, ML

## Purpose

Reduce an ensemble to a small set of representative microstates with population weights, so
downstream scoring and quantum labelling operate on a handful of structures rather than hundreds
of frames.

## Inputs

Ensembles from [S3](S3-ensemble-generation.md).

## Outputs

One PDB per `state_id` plus `states.parquet` with population weights summing to 1.0 per pose. See
[interfaces.md](../interfaces.md#s4--s5--microstates).

## Parameters to perturb `[source-doc]`

| Parameter | Settings | Decision rule |
| --- | --- | --- |
| **Retained microstates** | 1, 3, 5 | Smallest count preserving robust ranking |
| Clustering method | k-means on pocket RMSD · hierarchical · on a learned embedding | Compare on cluster stability, not on silhouette alone |
| Feature space | heavy-atom RMSD · contact map · torsions of key side chains | Contact-map clustering is closer to what the scorer sees |
| Representative selection | cluster medoid · lowest-energy frame | Medoid is the defensible default |

Do not exceed five states per complex. `[source-doc]`

## Metrics

- **Cluster stability under bootstrap resampling of frames** — if clusters move when you resample,
  the populations are not meaningful and downstream weighting is noise amplification
- Within-cluster RMSD spread vs. between-cluster separation
- Ranking sensitivity to `n_states`: 1 vs. 3 vs. 5
- Population weight entropy — a near-uniform distribution over 5 states means the ensemble had no
  structure to find

## Why this small stage matters more than it looks

S4 sets the **multiplier on S5 and S6 cost**. Going from 1 to 5 states multiplies the quantum
budget fivefold. With 20–50 labels total `[source-doc]`, that is the difference between labelling
10 poses and labelling 2. The parameter is therefore jointly a quality knob and the dominant
budget knob, and should be swept jointly with `s6.max_labels`, not independently.

## Failure modes

- **Clustering noise rather than conformational substates.** Especially likely with short
  relaxation, where the "ensemble" is thermal jitter around one minimum. The bootstrap check
  catches this; nothing else will.
- Population weights from non-independent frames — a long trajectory in one basin looks like a
  dominant state because it was slow to leave, not because it is favoured.
- Choosing representatives by energy with an inconsistent energy function across modes.

## Candidate software

MDAnalysis · MDTraj · scikit-learn · PyEMMA-style tooling if MSM machinery becomes relevant
(likely beyond hackathon scope)

## First-day task

Implement the bootstrap cluster-stability check before implementing anything else. It is ~30
lines, and it determines whether the rest of the stage is measuring anything.
