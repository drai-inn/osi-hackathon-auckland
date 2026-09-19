# Parameter space

The object of study. Eight families, mostly 2–3 settings each, sourced from the origin document
and extended where this repo adds structure.

## The grid `[source-doc unless noted]`

| Family | Stage | Key | Settings | Do not exceed | Decision rule |
| --- | --- | --- | --- | --- | --- |
| Pose count | S1 | `s1.n_poses` | 1, 3, 5 | >5 states/complex | Increase only if rankings are unstable |
| Pocket radius | S2 | `s2.crop_radius_A` | 10, 12, 15 | >3 radii | Smallest preserving known contacts + selectivity signal |
| Dynamics mode | S3 | `s3.mode` | static, short relaxation, surrogate ensemble | long MD | Cheapest mode improving stability over static |
| Retained microstates | S4 | `s4.n_states` | 1, 3, 5 | >5 | Smallest count preserving robust ranking |
| Scorer settings | S5 | `s5.capacity`, `s5.graph_cutoff_A` | low/med/high; 4.0/5.0/6.0 Å | full architecture search | Lowest capacity retaining ranking + uncertainty quality |
| Quantum settings | S6 | `s6.theory`, `s6.shell_A` | 2 lightweight + 1 reference on a tiny subset | large theory grid | Cheapest setting preserving relative ordering |
| Quantum subset | S6 | `s6.acquisition` | top-ranked, high-uncertainty, random control | labelling everything | Best error reduction per label |
| Acquisition threshold | S7 | `s7.threshold_pct` | 5, 10, 20 | — | Strongest error reduction per label |

Added by this repo (not in the origin doc, justified on the stage pages):

| Family | Stage | Key | Settings | Why |
| --- | --- | --- | --- | --- |
| Decoy strategy | S0 | `s0.decoys` | property-matched, DUD-E style, literature non-selective | Determines whether enrichment means anything ([S0](../03-pipeline/stages/S0-benchmark.md)) |
| Ensemble aggregation | S5 | `s5.aggregation` | weighted mean, Boltzmann, min | Changes what "the score" means ([S5](../03-pipeline/stages/S5-equivariant-scoring.md)) |
| Uncertainty method | S5 | `s5.uncertainty` | deep ensemble, MC dropout, evidential | Acquisition depends on it being calibrated |

## Size

The full discrete product is ~10⁵ configurations. The hackathon will evaluate on the order of
10²–10³ **stage-level** configurations and ~10 **integrated** ones. That ratio is the design:
dense search where it's cheap, sparse where it isn't.

## Interactions to sweep jointly

Random search gives marginals for free but needs deliberate attention for interactions. Three
pairs where an interaction is expected on physical grounds:

| Pair | Why they interact |
| --- | --- |
| `s2.crop_radius_A` × `s5.graph_cutoff_A` | The scorer cannot see beyond the crop. A 6 Å cutoff on a 10 Å crop wastes the cutoff; a 4 Å cutoff on a 15 Å crop wastes the crop |
| `s4.n_states` × `s6.max_labels` | States multiply the label budget. 5 states × 50 labels = 10 poses labelled |
| `s3.mode` × `s4.n_states` | Static mode makes `n_states` meaningless; the surrogate mode is where state count earns its cost |

Sweep these as 2D blocks rather than trusting the marginals.

## Cost sensitivity

Roughly, which parameters dominate GPU-hours (to be replaced with `[measured]` on day 1):

```
s6.theory        ████████████████████  steepest — theory level dominates everything
s2.crop_radius_A ██████████████        quantum cost scales steeply with system size
s4.n_states      ██████████            multiplies S5 and S6 volume
s3.mode          ████████              surrogate ≪ relaxation ≪ MD
s1.n_poses       ██████                multiplies everything downstream
s5.capacity      ██                    S5 is cheap relative to S3 and S6
s5.graph_cutoff  █                     near-free
s7.threshold_pct ·                     free — it only reallocates the label budget
```

The two steepest are also the two with the strongest scientific argument for mattering. That is
the tension the hackathon exists to resolve.

## Search-space specification

One shared file, consumed by the random-search driver and by every work package, so that
sensitivity results are comparable across stages. Proposed format:

```yaml
# search_space.yaml
s2.crop_radius_A:  {type: choice, values: [10, 12, 15], cost_weight: high}
s4.n_states:       {type: choice, values: [1, 3, 5],    cost_weight: high}
s5.capacity:       {type: choice, values: [low, medium, high]}
s5.graph_cutoff_A: {type: choice, values: [4.0, 5.0, 6.0]}
s7.threshold_pct:  {type: choice, values: [5, 10, 20]}
```

`cost_weight` lets the driver bias sampling toward cheap regions early, and is the hook for a
cost-aware acquisition strategy later if anyone wants to build one.
