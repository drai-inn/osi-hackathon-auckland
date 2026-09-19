# Data sources

Owned by WP-A. Licence column matters: if we intend to release the benchmark
([E2](../02-scope/open-questions.md)), every source must permit it.

## Activity data

| Source | Content | Licence | Notes |
| --- | --- | --- | --- |
| **ChEMBL** | Curated bioactivity, incl. kinase panels | CC BY-SA 3.0 | Primary source. Assay heterogeneity is the main issue ([C1](../02-scope/open-questions.md)) |
| **BindingDB** | Binding affinities, often with assay detail | CC BY 3.0 | Good complement; check for overlap/duplication with ChEMBL |
| **Papyrus** or equivalent | Pre-harmonised bioactivity | Check per release | Harmonisation already done, but by someone else's rules — inspect them |
| Published kinase selectivity panels | Profiling across many kinases at fixed conditions | Varies | **The most internally comparable source.** Same assay, same conditions across targets — exactly what selectivity ratios need |
| Literature-curated sets | Known selective / pan-CDK compounds | Varies | Small, high value. These are the discriminating cases |

**The harmonisation problem stated plainly:** kinase IC50 depends on ATP concentration, and labs
use different ones. A CDK9 IC50 from lab X and a CDK7 IC50 from lab Y do not form a valid
selectivity ratio. Options: (a) restrict to sources reporting both targets under identical
conditions — small but clean; (b) convert to Ki via Cheng–Prusoff where Km(ATP) is known — more
data, more assumptions; (c) treat selectivity as ordinal only. **Recommendation: (a) for the
primary analysis, (c) as a sensitivity check.** This is Activity 1's first agenda item.

## Structural data

| Source | Content | Licence | Notes |
| --- | --- | --- | --- |
| **PDB** | Apo and holo structures for CDK9/7/12/13 | Public domain | Primary. Selection protocol must be written down ([C5](../02-scope/open-questions.md)) |
| PDBbind / BindingMOAD | Structure–affinity pairs | Check per release | Useful for scorer validation beyond our targets |
| AlphaFold DB | Predicted structures | CC BY 4.0 | Fallback for constructs without experimental structures |

**Record which PDB entries postdate the co-folding model's training cutoff.** That subset is the
only honest held-out set for [contract 1](../03-pipeline/fidelity-contracts.md#1-co-folding-s1--replaces-experimental-structure-determination).

## Decoys

| Approach | Pro | Con |
| --- | --- | --- |
| **Property-matched** (matched MW, logP, charge, HBD/HBA) | Honest. Forces the model to use structure | Harder; fewer available; may include unknown actives |
| DUD-E style | Established, easy to generate | Known to contain biases models exploit; a 2D model can win on them |
| Literature non-selective compounds | The *right* negative for selectivity — real binders that lack discrimination | Few of them; must be hand-curated |

**Recommendation:** property-matched decoys as the primary set, plus a hand-curated set of known
pan-CDK inhibitors as the discriminating negatives ([C3](../02-scope/open-questions.md)). The
pan-CDK set is small but it is the class that separates a real result from a molecular-weight
classifier.

## Target set

| Target | UniProt | Role | Why |
| --- | --- | --- | --- |
| CDK9 | P50750 | Primary | The driving case |
| CDK7 | P50613 | Counter-target | Close ATP site; the minimum-viable counter-target |
| CDK12 | Q9NYV4 | Counter-target | Transcriptional CDK; selectivity relevant |
| CDK13 | Q14004 | Counter-target | Closest paralog to CDK12; the hardest discrimination |

Minimum viable: CDK9 + CDK7. Preferred: all four. `[source-doc]`

## Provenance requirements

Every manifest row carries source, source identifier, retrieval date, assay type, and any
transformation applied. Recorded in `curation_notes.md`, not in someone's memory.

This is not bureaucracy — it is the difference between a benchmark others can use and a CSV nobody
can interpret in six months. If we intend to release it, this *is* the deliverable.
