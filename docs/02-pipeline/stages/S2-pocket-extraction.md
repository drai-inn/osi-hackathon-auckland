# S2 — Pocket extraction

**Work package:** B · **Owner:** _unassigned_ · **Disciplines:** computational chemistry, structural biology

> Computationally trivial, scientifically load-bearing. The crop radius is one of the few
> parameters that affects *every* downstream stage's cost and quality simultaneously.

## Purpose

Crop a binding-site shell around the ligand and key residues, producing a system small enough for
ensemble sampling and quantum treatment while retaining the interactions that determine
selectivity.

## Inputs

Predicted or experimental complexes from [S1](S1-complex-generation.md).

## Outputs

PDB per `pose_id` plus a sidecar recording radius, retained residue set, capping scheme, and
protonation assignment. See [interfaces.md](../interfaces.md#s2--s3--cropped-pockets).

## Parameters to perturb `[source-doc]`

| Parameter | Settings | Decision rule |
| --- | --- | --- |
| **Crop radius** | 10, 12, 15 Å | Smallest radius that preserves known contacts and selectivity signal |
| Capping | hydrogen caps · methyl caps · constrained whole residues | Affects quantum labels more than it affects scoring |
| Residue selection | radius only · radius + known hinge/gatekeeper residues always retained | Guaranteeing key residues reduces variance across poses |
| Protonation | PROPKA · fixed pH 7.4 rules · manual for known cases | (→ [C4](../../01-scope/open-questions.md)) |
| Waters | strip all · retain crystallographic · retain by conservation | Bridging waters are a real selectivity mechanism in kinases |

Do not exceed three radii during the hackathon. `[source-doc]`

## Why crop radius deserves careful treatment

Cost of the quantum stage scales steeply with system size, so radius is the main lever on the
hackathon's dominant cost. But the selectivity difference between CDK9 and CDK7 may reside in
second-shell residues that a 10 Å crop excludes. **The radius sweep is therefore not a tuning
exercise; it is a measurement of where the selectivity signal physically lives.** Report it that
way — it is one of the more interesting results available from a small run.

## Metrics

- Retention of known key contacts (hinge, gatekeeper, front/back pocket) at each radius
- Atom count and net charge distribution per radius — the direct input to S6 cost
- Score/ranking stability across radii: if rankings are radius-invariant, pick the cheapest
- Divergence of CDK9-vs-counter-target contact sets by radius

## Failure modes

- **Charged residues split by the crop boundary**, leaving unphysical net charges. Check the
  charge distribution, don't assume it.
- Capping scheme differing between S3 and S6 — sampling one molecule and labelling another.
- Stripping a structurally conserved water that mediates a selectivity-determining H-bond.
- Inconsistent residue numbering between predicted and experimental structures, breaking joins.

## Candidate software

RDKit / MDAnalysis / MDTraj for selection · PDBFixer · PROPKA · OpenBabel

## First-day task

Produce the three radii for five complexes and publish the atom-count and net-charge table. WP-E
needs exactly this to size the quantum budget.
