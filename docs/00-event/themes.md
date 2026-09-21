# Four themes

Notional, deliberately. These describe the kind of thing we're interested in, not a project plan.
Bring your own problem and take a space — the point is that you own it.

---

## What all four have in common

The same three moves, whichever theme you're in.

**Find out what open-weight models exist in your area.** The landscape moved a long way in the last
eighteen months and most of us only know our own corner of it.

**Get one or two of them running on our hardware.** Dual GB10 and an HGX H200. One or two per area,
not a survey — anything we can't actually run isn't a candidate.

**Design a small experiment, and work out how you'd evaluate it.** This is the hard part and it's
the part we're most interested in. Not "does it work" but *how would you know*, and *what would
change your mind*.

That third one is a live question, not a formality. A recent benchmark found single-cell foundation
models don't beat a simple linear baseline at predicting perturbation effects `[literature]`, and
another found that the choice of metric flips the model rankings outright `[literature]`. Nobody has
settled how to evaluate most of these things. That's the opportunity.

---

## 1 · Screening at scale, with physics in the loop

Moving from data-driven screening of very large libraries towards models that know something about
shape and structure, used to filter before you spend anything on physics-based docking.

**This might look like…** a small, well-tuned graph model against a large pretrained one, on equal
tuning budget · measuring what a filter throws away by spiking a known set into a big library · 3D
versus 2D on the same task, with the cost difference measured · pose prediction where no structure
exists.

**Open-weight worth a look.** **Boltz-2** for co-folding with affinity prediction — note that 2.1 is
API-only, so 2 is the open one. **OpenFold3** and **Chai-1r** as alternatives. **IntFold**, which
reports beating Boltz-2 on affinity and ships open weights. Protein and molecular language models
for the cheap end of the comparison.

---

## 2 · Molecules in motion

Machine-learned interatomic potentials in molecular dynamics. Near-quantum forces at a cost that
lets you actually run the trajectory.

**This might look like…** an MLIP-driven ensemble against a classical force field on the same system
· finding where the potential leaves its training distribution, and whether it tells you · how many
microstates you actually need · conformational change that a static structure can't show you.

**Open-weight worth a look.** **MACE** (MACE-OFF for organics, MACE-MP for materials) · **UMA** ·
**eSEN** · **Orb-v3** · **NequIP**. Two honest caveats: several of the strongest are trained on
materials or small molecules rather than protein–ligand interfaces, and some OMol25-derived weights
carry a non-commercial licence. Both are worth knowing before you build on them, and neither is a
reason not to try.

---

## 3 · From a binding event to a whole system

Multi-scale modelling — carrying a molecular signal up to functional and physiological change.
Physiological outcomes come from molecules interacting; this is the part of the chain where that
stops being a slogan.

**This might look like…** a perturbation model against a linear baseline on the same data · whether
an off-target effect is visible at the cell level at all · connecting a binding profile to a pathway
readout · anything that carries a signal between two scales and checks whether it survived.

**Open-weight worth a look.** **STATE** (Arc Institute) · **scGPT** · **Geneformer** ·
**scFoundation**. The 2026 Virtual Cell Challenge is live and is a ready-made evaluation setting if
you want one. The benchmark result above — foundation models not beating linear baselines — makes
this the most interesting theme to be sceptical in.

---

## 4 · Repurposing what we already have

Genotype, structure and approved drugs, with deliberately small models. The constraint is the point:
a bounded search space and something that runs on a laptop.

**This might look like…** a knowledge-graph model against a structure-aware one · whether a variant
changes which approved drug fits · a retrospective hold-out that the field mostly skips · how small
a model can get before it stops working.

**Open-weight worth a look.** **TxGNN** on **PrimeKG** · lightweight knowledge-graph embeddings
(under a million parameters, and competitive) · **ESM-2** embeddings where you need sequence ·
structure-aware scoring from theme 1 if you want to cross over.

---

## Targets and chemistry

We have default targets and chemistry ready to go, with structures and data prepared, so nobody has
to start from a blank page. Take one, or bring your own — both are fine, and a team working on its
own problem is exactly what we're hoping for.

## If none of these is quite it

Say so. Four themes is a starting shape, not a boundary. If your work sits between two of them, or
underneath all of them, that's usually the interesting place to be and we'd rather hear it now than
discover it on the day.
