# Source note — "3D Chemistry-Aware Selectivity Pipeline Options"

**Source:** internal working document (Diway), 16pp, exported 2026-09-18.
Local copy expected at `refs/` — see [refs/README.md](../../../refs/README.md).
**Role in this repo:** this is the *origin document*. Most of the pipeline shape, the parameter
ranges, the work-package split and the sizing estimates come from here. Where a doc in this repo
says `[source-doc]`, it means this.

---

## Its core argument

Treat the problem as a **staged funnel**, not a single model choice. Use fast open-weight 3D
models to generate and score candidate complexes, then apply higher-fidelity dynamic and quantum
methods **only where they add the most value**.

## The approach landscape, as it frames it

| Approach | Role | Strength | Main limitation |
| --- | --- | --- | --- |
| 2D screening models | Large-scale triage | Very high throughput | Weak pocket awareness; poor selectivity resolution |
| 3D co-folding / complex prediction | Generate target–ligand structural hypotheses | Works when crystal complexes are absent | Predictions are static and uncertain |
| Pocket-cropped equivariant GNNs | Fast local 3D scoring | Generalises to unseen pockets via geometry | Needs meaningful 3D labels to become chemistry-aware |
| Quantum refinement (cuEST) | High-fidelity electronic labels | Captures electrostatics, polarization, interaction detail | Too expensive for brute-force use |
| Dynamic ensemble generation | Pocket motion, ligand-state variation | Realism for flexible kinases and linkers | MD can dominate runtime |
| Dynamics surrogates / MLIPs | Approximate ensembles cheaply | Large cost reduction vs. classical or ab initio MD | Needs validation per chemistry regime |

## Where cuEST sits

**A refinement and labelling layer, not the front door.** Useful once the candidate set is
already narrow. Specific uses it names:

- rescore top candidates using quantum interaction energies
- generate pocket-aware 3D electronic features (ESP surfaces, partial charges)
- create target-specific labels for active learning and transfer learning
- distinguish subtle binding differences between closely related pockets

Implementation reference: `NVIDIA/CUDALibrarySamples`, `cuEST` directory.

## The enrichment thesis

> "The key is not to try to label everything." A few thousand to tens of thousands of
> well-chosen 3D labels can materially improve a target-specific model if concentrated around
> the chemistry and pocket states that matter.

Four enrichment methods, all rated feasible: active learning on high-uncertainty poses;
multi-fidelity / delta learning; self-supervised 3D field pretraining; pocket-shell quantum
labels (reduced binding-site clusters rather than whole proteins).

## The recommended workflow (8 stages)

1. Front-end filtering → manageable candidate set
2. Complex generation (Boltz-2 or equivalent)
3. Local pocket extraction (crop binding-site shell)
4. Ensemble generation (short dynamics **or** surrogate conformers)
5. Ensemble reduction (cluster into representative microstates)
6. 3D equivariant scoring (Nesso-1 class)
7. Selective quantum refinement (cuEST on top + uncertain cases)
8. Feedback learning (labels improve the local 3D model)

Orchestration: **containerised Snakemake DAG**, whole-GPU jobs, on Kubernetes HGX H200. It is
explicit that no additional distributed-systems machinery is needed for a strong pilot.

## Its hackathon guidance (which this repo adopts)

> "Yes, this is feasible as a hackathon-scale exploration **if we deliberately avoid an
> end-to-end mega-run**. The right design is to split the workflow into small, parallel work
> packages, each perturbing a limited parameter space on a shared curated benchmark, then
> integrate only the settings that show stable signal."

**Recommended target:** 12–20 ligands, CDK9 plus one close counter-target, three poses or states
per ligand–target pair, 20–50 targeted cuEST labels.

Six parallel work packages: A data/benchmarks · B static structural baseline · C motion-aware
sampling · D equivariant scoring · E cuEST quantum labelling · F workflow and integration.
Carried into [work-packages.md](../../05-delivery/work-packages.md).

Sizing tiers (tiny smoke test / hackathon minimum / useful pilot / scale-up) and the full
parameter grid are carried into [parameter-space.md](../../04-experiments/parameter-space.md)
and [compute-budget.md](../../06-feasibility/compute-budget.md).

Six scale-up gates (technical reproducibility, ranking signal, motion value, quantum value,
acquisition value, operational cost) are carried into
[stage-gates.md](../../06-feasibility/stage-gates.md).

---

## What this repo adds on top of it

The source doc is strong on *what to build* and *how big*. Three things it leaves implicit that
this repo makes explicit:

1. **A validation obligation per surrogate.** It says surrogates "should be treated as
   accelerators, not unquestioned truth" and should be validated — but does not say against
   what, by whom, or to what threshold. → [fidelity-contracts.md](../../03-pipeline/fidelity-contracts.md)
2. **A search strategy for the parameter space.** It lists discrete settings per parameter but
   implies a grid. Grids over 7+ parameters are the thing that does not scale.
   → [hpo-microtopic.md](../../04-experiments/hpo-microtopic.md)
3. **Data contracts between stages.** Six groups working in parallel need frozen interfaces on
   day one, or integration on the last day fails. → [interfaces.md](../../03-pipeline/interfaces.md)
