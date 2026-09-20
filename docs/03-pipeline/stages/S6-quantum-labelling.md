# S6 — Selective quantum labelling

**Work package:** E · **Owner:** _unassigned_ · **Disciplines:** quantum chemistry, physics, HPC

> The only stage we treat as near-truth, and therefore the only stage whose own reliability has
> to be established **before** anything else depends on it.

## Purpose

Generate high-fidelity electronic-structure labels for a small, deliberately chosen set of
microstates: quantum interaction energies, electrostatic potential surfaces, partial charges.
These become the training signal that makes the cheap scorer chemistry-aware. `[source-doc]`

## Inputs

Shortlisted microstates from [S5](S5-equivariant-scoring.md) via `acquisition.csv` — top-ranked,
high-uncertainty, and **random control**.

## Outputs

`labels.parquet` plus verbatim raw outputs. See
[interfaces.md](../interfaces.md#s6--s7--quantum-labels).

## Parameters to perturb `[source-doc]`

| Parameter | Settings | Decision rule |
| --- | --- | --- |
| **Theory level** | two lightweight settings + one reference on a tiny subset | Cheapest level preserving relative ordering |
| Pocket-shell size | inherited from S2 (10/12/15 Å), possibly further reduced | Smallest shell with stable interaction energies |
| Acquisition source | top-ranked · high-uncertainty · random control | The comparison, not a tuning knob |
| **Label budget** | 20–50 for the hackathon | Hard ceiling. Not negotiable mid-run |

No large theory-level grid. `[source-doc]`

## How big is the thing we are sending to a quantum code

`[measured]`, CDK9 with flavopiridol. At a 4 Å shell the region is **16 residues and 153 heavy
atoms**, which is roughly 300 atoms once hydrogens are added — already at the upper end of what is
comfortable for hybrid DFT. At the 10 Å shell S2 inherits from, it is **504 heavy atoms**, which is
not a DFT calculation anyone runs 50 of in two days.

So "pocket-shell size inherited from S2, possibly further reduced" in the table above is not a
detail. It is the difference between a label budget we can meet and one we cannot. Whatever S2
settles on, **S6 needs its own smaller shell and a stated capping scheme**, and the truncation has
to be shown not to move the relative ordering. See
[the ladder](../figures/zoom-ladder.svg) and
[`data/pocket-anatomy.json`](../../../data/pocket-anatomy.json).

## The convergence check comes first

Before a single production label: **do the labels change the answer when you change the
settings?** `[source-doc]` calls this *quantum consistency* and it is the load-bearing check of
the whole hackathon.

On 3–5 representative systems, measure:

1. Interaction energy vs. **theory level** — does the *ordering* of a few known selective /
   non-selective pairs survive the cheap setting? Ordering is what we need; absolute accuracy is
   not.
2. Interaction energy vs. **shell size** — if energies drift monotonically with radius without
   plateauing, the crop is amputating real interactions and the labels are not a ground truth.
3. **Convergence rate** — fraction of SCF calculations converging within the wall-clock budget,
   and what the non-converged cases have in common (net charge? open shell? bad geometry from S1?).

If these fail, [contracts 3 and 4](../fidelity-contracts.md) have no foundation and S7 should not
run. Report that as a finding, not a setback — it is exactly the kind of thing a scoping exercise
exists to discover.

## Metrics

- Convergence rate and mean/median wall-clock per label
- **GPU-hours per label** — the denominator for every cost-effectiveness claim we make
- Sensitivity of electronic features to theory level and shell size
- Discrimination: do labels separate known selective from known non-selective examples? `[source-doc]`
- Fraction of the label budget consumed by failures

## Failure modes

- **Wrong protonation or tautomer state.** A quantum calculation on the wrong species is
  precisely accurate about nothing. (→ [C4](../../02-scope/open-questions.md))
- Net charge errors from the S2 crop boundary. Verify charges; do not infer them.
- Non-converged calculations silently dropped, biasing the label set toward easy systems. Keep
  them, flagged.
- Comparing interaction energies computed at different shell sizes as if commensurable.
- Basis set superposition error unaccounted for in interaction energies.
- **Budget exhausted by the convergence study**, leaving nothing for production labels. Ring-fence
  the split up front: ~10 labels for convergence, the rest for production.

## Candidate software

NVIDIA cuEST — implementation reference `NVIDIA/CUDALibrarySamples`, `cuEST/`. Availability and
licensing are [B1](../../02-scope/open-questions.md), a 🔴 blocker.

**Fallback ladder if cuEST is unavailable:** GPU4PySCF → TeraChem (licensed) → semi-empirical
(GFN2-xTB) as a much cheaper, much lower-fidelity stand-in. The fallback changes the cost model
by orders of magnitude and would need a scope conversation, not a substitution.

## First-day task

Do not generate labels. Run the three convergence checks on 3–5 systems and publish
GPU-hours-per-label at each theory level. WP-F cannot schedule and WP-D cannot plan acquisition
until this number exists.
