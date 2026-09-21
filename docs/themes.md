# Four themes

Notional, all four. They describe the kind of thing we're interested in. Bring your own problem and
take a space.

---

## What all four have in common

The same three moves, whichever theme you're in.

**Find out what open-weight models exist in your area.** The landscape moved a long way in the last
eighteen months and most of us know our own corner of it.

**Get one or two of them running on our hardware.** Dual GB10 and an HGX H200. One or two per area
is plenty, and being able to run it is the main filter.

**Work out what to measure, and report it back.** *How would you know it worked, and what would
change your mind?* Each group sources its own data and picks its own benchmark. Evaluation looks
different at every rung, so it's yours to design.

This is the move we care most about. A recent benchmark found single-cell foundation models level
with a simple linear baseline at predicting perturbation effects `[literature]`, and another found
that the choice of metric changes which model comes out on top `[literature]`. How to evaluate most
of these things is genuinely unsettled, and there's a lot of room to do useful work there.

End of day 1, every group reports back against
[the same four questions](taking-part.md#the-four-questions). A shared shape rather than a shared
dataset, so the groups stay comparable while working on whatever they like.

## Language models run through all of it

Worth saying plainly, because it's easy to read the four themes as being about specialist
architectures. Language models now sit at nearly every rung, and in several places they're the
thing to beat.

| Over | Models |
| --- | --- |
| **Protein sequence** | ESM-2, ESM-3, AMPLIFY, and the structure-aligned variants |
| **DNA and genomes** | Evo 2, Nucleotide Transformer, HyenaDNA |
| **Molecules as text** | ChemBERTa-2, MolFormer, SELFIES-based models |
| **Gene expression** | Geneformer, scGPT and STATE are transformers over gene tokens |
| **The literature, and the tools** | General LLMs, reading papers and driving code |

Three things follow from that.

**Sequence models are competitive with structure-aware ones more often than you'd expect.**
ChemBERTa-2 beat D-MPNN, a strong graph network, on six of eight MoleculeNet tasks `[literature]`.
Embeddings from Evo 2 reach 0.997 AUROC on ClinVar variant classification `[literature]`. Whether
that holds on the problems we care about is a good question to spend two days on.

**The cheapest useful thing an LLM does here is build your dataset.** Each group sources its own
data, and schema-guided extraction from the literature gets you there in an afternoon. Verify what
comes out — benchmarks of the current tools show a real accuracy-against-hallucination trade-off
`[literature]` — and small self-hosted open models do well enough for this.

**Physics-informed language models are a live area with no single model to download.** Worth being
precise about, because the phrase covers two different things:

- **The language model builds or steers the physics.** Lang-PINN turns a natural-language problem
  description into a trainable physics-informed network, handling PDE parsing, architecture choice
  and code generation. PINNsAgent automates PDE surrogation. LLM-PINN pulls constitutive relations
  out of a domain knowledge base with RAG and wires them in. These are frameworks and agent systems
  rather than checkpoints, and they sit close to how we're working anyway.
- **Physics is fused into the representation.** Physics-informed equivariant graph networks aligned
  with a language model through cross-modal fusion, as in 3D-MolGL.

One result keeps this open. **A general transformer with no built-in physical constraints can match
or beat physics-constrained models on molecular dynamics when it has enough data** `[literature]`,
learning approximate equivariance instead of having it imposed. Whether the physics prior earns its
keep at our data scale is a good two days of work, and theme 1 asks the same question about model
class.

The [Awesome Physics-Informed LLMs](https://github.com/qiaosun22/AwesomePhysicsInformedLLMs) list is
the best single starting point.

---

## 1 · Screening at scale, with physics in the loop

Moving from data-driven screening of very large libraries towards models that know something about
shape and structure, used to filter before you spend anything on physics-based docking.

**This might look like…** a small, well-tuned graph model against a large pretrained one on equal
tuning budget · measuring what a filter throws away, by spiking a known set into a big library ·
3D against 2D on the same task, with the cost difference measured · pose prediction where no
structure exists.

**Open-weight worth a look.** **Boltz-2** for co-folding with affinity prediction; 2.1 is API-only,
so 2 is the open one. **OpenFold3** and **Chai-1r** as alternatives. **IntFold** ships open weights
and reports stronger affinity numbers than Boltz-2.

On the language-model side: **ChemBERTa-2**, **MolFormer** and SELFIES-based models over the
compound, **ESM-2** or **ESM-3** over the protein. These are the cheap arm of a model-class
comparison, and cheap doesn't mean worse — ChemBERTa-2 beat a strong graph network on most of
MoleculeNet.

---

## 2 · Molecules in motion

Machine-learned interatomic potentials in molecular dynamics. Near-quantum forces at a cost that
lets you actually run the trajectory.

**This might look like…** an MLIP-driven ensemble against a classical force field on the same
system · finding where the potential leaves its training distribution, and whether it tells you ·
how many microstates you actually need · conformational change a static structure won't show you.

**Open-weight worth a look.** **MACE** (MACE-OFF for organics, MACE-MP for materials) · **UMA** ·
**eSEN** · **Orb-v3** · **NequIP**. Two things worth knowing up front: several of the strongest are
trained on materials or small molecules rather than protein–ligand interfaces, and some
OMol25-derived weights carry a non-commercial licence.

This is the most physics-native theme. Language models still have a role: the physics-informed
frameworks above build and steer simulations from a description, and there's a live finding that a
plain transformer trained on enough data can match a physics-constrained model on MD `[literature]`.
Testing that on a protein-ligand interface, where the data is thinner than in materials, would be a
genuinely useful two days.

---

## 3 · From a binding event to a whole system

Multi-scale modelling — carrying a molecular signal up to functional and physiological change.
Physiological outcomes come from molecules interacting; this is the part of the chain where that
stops being a slogan.

**This might look like…** a perturbation model against a linear baseline on the same data · whether
an off-target effect is visible at the cell level · connecting a binding profile to a pathway
readout · anything that carries a signal between two scales and checks whether it survived.

**Open-weight worth a look.** **STATE** (Arc Institute) · **scGPT** · **Geneformer** ·
**scFoundation**. These are language models over gene tokens rather than words, which makes the
comparison against a linear baseline especially interesting. The 2026 Virtual Cell Challenge is live
and gives you a ready-made evaluation setting if you want one.

---

## 4 · Repurposing what we already have

Genotype, structure and approved drugs, with deliberately small models. A bounded search space and
something that runs on a laptop.

**This might look like…** a knowledge-graph model against a structure-aware one · whether a variant
changes which approved drug fits · a retrospective hold-out · how small a model can get and still
work.

**Open-weight worth a look.** **Evo 2** (7B and 40B, open weights) for variant effect — embeddings
from it reach 0.997 AUROC on ClinVar `[literature]` — and **Nucleotide Transformer** alongside it.
**TxGNN** on **PrimeKG** for the drug-disease side, plus lightweight knowledge-graph embeddings that
come in under a million parameters and hold their own. **ESM-2** where you need the protein.

---

## Targets and chemistry

We have default targets and chemistry ready to go, with structures and data prepared, so nobody has
to start from a blank page. There's a [worked example](worked-example.md) if you'd like to see one.
Bringing your own problem is very welcome.

## If none of these is quite it

Say so. Four themes is a starting shape. Work that sits between two of them, or underneath all of
them, is usually the interesting kind, and we'd like to hear about it early.
