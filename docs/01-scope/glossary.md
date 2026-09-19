# Glossary

For a team spanning medicinal chemistry, quantum chemistry, molecular simulation, machine learning,
statistics and research software engineering. Everyone here is an expert in something and a
beginner in most of the rest — that is the point of the exercise, and this page exists so nobody
has to pretend otherwise.

## The problem

**Paralog selectivity** — binding one protein and not its close relatives. CDK9 vs. CDK7/12/13 is
our case. Hard because the ATP sites are very similar.

**Counter-target / off-target** — the protein you want *not* to hit. Selectivity is always
measured against something specific.

**Pan-CDK inhibitor** — binds several CDKs indiscriminately. Our most useful negatives: real
binders that lack discrimination, so they cannot be separated by "does it bind?" alone.

**Selectivity ratio** — activity against the off-target divided by activity against the target.
Only valid when both numbers come from comparable assays (→ [C1](open-questions.md)).

**Decoy** — a compound presumed inactive, included so that "ranks actives highly" means something.
**Property-matched** decoys share MW/logP/charge with actives, so a model cannot separate them on
bulk properties alone.

**Activity cliff** — two structurally similar compounds with very different activity. The
discriminating cases, and the ones that look like noise.

**Induced fit** — the pocket changing shape on ligand binding. A static structure cannot express it.

**Cryptic / allosteric pocket** — a site that is not the main functional one, or not visible in the
apo structure.

**Holo / apo** — with ligand bound / without.

**Hinge, gatekeeper, DFG** — kinase anatomy. The hinge makes the conserved H-bonds most ATP-site
binders use; the gatekeeper residue controls access to a back pocket; DFG-in/DFG-out are two
activation-loop conformations that change the pocket shape substantially.

## The methods

**Co-folding** — predicting the 3D structure of a protein–ligand complex directly. Boltz-2 is an
open-weight example. Our [S1](../02-pipeline/stages/S1-complex-generation.md).

**Pocket crop / pocket shell** — the subset of the protein within some radius of the ligand.
Makes the system small enough for ensemble sampling and quantum treatment.

**Equivariant GNN** — a graph neural network whose predictions rotate with the input. Physically
sensible for 3D structure, and generalises to unseen pockets better than global descriptors.

**Microstate** — one representative conformation from an ensemble, with a population weight.

**MD (molecular dynamics)** — simulating atomic motion over time. Accurate, expensive.

**MLIP (machine-learned interatomic potential)** — a learned approximation to the energy surface,
used to make simulation cheaper. MACE is an example.

**Generative ensemble surrogate** — a model that produces a conformational ensemble directly,
without simulating a trajectory. BioEmu, AlphaFlow.

**DFT (density functional theory)** — quantum-chemical method giving electronic-structure
properties. Our high-fidelity label source, via cuEST. Expensive and scales steeply with system
size.

**ESP (electrostatic potential)** — the charge landscape around a molecule; part of what
distinguishes binding in similar-shaped pockets.

**Theory level / basis set** — the accuracy and cost dials of a quantum calculation.

**SCF convergence** — whether the quantum calculation actually reached a solution. Non-converged
results are kept and flagged, never silently dropped.

## The methodology

**Surrogate** — a cheap approximation to an expensive computation. This pipeline has
[four](../02-pipeline/architecture.md#the-surrogate-cascade).

**Fidelity contract** — our term: the stated ground truth, validation set, agreement metric and
**trust region** a surrogate must have before it is allowed into the pipeline.
[Details](../02-pipeline/fidelity-contracts.md).

**Trust region** — where a surrogate may be believed. The field people skip, and the one that
matters, because a surrogate can be accurate overall and systematically wrong on exactly the
close-call cases the pipeline exists to resolve.

**Multi-fidelity / delta learning** — train broadly on cheap labels, learn a correction from a
smaller high-fidelity set.

**Active learning** — choosing which expensive labels to compute, usually where the model is most
uncertain. Only better than random if the uncertainty is **calibrated**.

**Calibration** — whether predicted uncertainty matches actual error. Uncalibrated uncertainty
makes active learning equivalent to random sampling.

**Acquisition strategy / threshold** — the rule for picking the next labels, and how aggressively.

**Random-acquisition control** — labelling a randomly chosen subset alongside the
uncertainty-chosen one, to test whether "active" learning is doing anything. Frequently skipped,
occasionally wins.

**Scaling law** — how performance improves with scale. In our context, borrowed as a framing, not
as a curve we extrapolate ([why not](../00-context/source-notes/small-scale-experiments.md#4-extrapolation-is-statistically-fragile)).

**Noisy quadratic limit** — a diagnostic from Lourie et al.: near an optimum, the distribution of
scores from random search takes a characteristic shape. If it hasn't appeared, the search probably
missed the optimum.

**Intrinsic dimension / effective number of hyperparameters (γ)** — how many directions of the
configuration space actually matter. Lourie et al. find it falls toward one as model scale rises,
which is why large models are easier to tune than small ones.

**Random search vs. grid search** — random sampling of the configuration space beats a grid above
about three dimensions, and gives marginal sensitivity for every parameter from one budget.

**Functional ANOVA / variance decomposition** — attributing variation in outcome to individual
parameters and their interactions. How we answer "which knobs matter".

**Bootstrap interval** — resampling the data to get a confidence interval. At n≈20 ligands, a
metric without one is not a result.

## The plumbing

**Snakemake** — the workflow engine. Defines stages and dependencies as a DAG, caches completed
work, reruns only what changed.

**DAG** — the stage dependency graph.

**Container / image digest** — the pinned environment a stage runs in. The digest is what makes
"we ran version X" verifiable.

**MLflow** — experiment tracking: parameters, metrics, artifacts per run.

**Provenance** — the record of what produced an artifact: git sha, image digests, model weight
hashes, GPU type. Written on day 1, needed on day 4.

**Contract test** — a test that a stage's *output shape* is correct, independent of whether the
science is right. What lets six groups develop in parallel.

**Stage gate** — a pre-specified evidence threshold that must be met before scaling up. Ours are
in [stage-gates.md](../05-feasibility/stage-gates.md).
