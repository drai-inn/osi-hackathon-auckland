# Open questions

Everything here blocks or reshapes something. Each row: what we need to know, why it matters,
who resolves it, and by when. **Update this file in place — it is the project's honest edge.**

Status key: 🔴 blocking · 🟠 shapes design · 🟡 nice to resolve early · ✅ resolved (keep the row, add the answer)

---

## A. Logistics and commitment

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| A1 | **When is the hackathon, and how long?** | Every sizing estimate in [compute-budget.md](../05-feasibility/compute-budget.md) assumes a contiguous block. 2 days vs. 5 days changes the work-package design, not just the schedule | Nick | — | 🔴 |
| A2 | Is the 8× H200 block confirmed and bookable? Queue policy? | Determines whether "hackathon minimum" or only "tiny smoke test" is reachable | Nick + eResearch | — | 🔴 |
| A3 | How many people, and from which disciplines? | Six work packages need ~2–3 each. Below ~10 people we drop WP-C or WP-E | Nick | — | 🔴 |
| A4 | Is there budget for cloud burst if the cluster slips? | Single largest schedule risk | Nick | — | 🟠 |
| A5 | Which research leaders are we inviting to observe/participate? | Shapes [adjacent-activities.md](../04-hackathon/adjacent-activities.md) — the activities exist to give them a way in | Nick | — | 🟠 |

## B. Software and licensing

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| B1 | **Is cuEST actually available to us** — licence, container, CUDA/driver requirements, supported methods and basis sets? | WP-E does not exist without it. Fallback: PySCF-GPU / TeraChem / xTB ladder — but the cost model changes completely | WP-E owner | pre-hackathon | 🔴 |
| B2 | Boltz-2 licence and weights — redistribution terms for our container? | Affects whether the workflow is publicly reproducible | WP-B owner | pre-hackathon | 🟠 |
| B3 | Nesso-1 availability, licence, and whether it is fine-tunable at all (vs. inference-only) | Stage S5 feedback learning depends on this. If inference-only, the feedback loop becomes calibration-only, or we substitute an in-house equivariant GNN | WP-D owner | pre-hackathon | 🔴 |
| B4 | Which ensemble surrogate: BioEmu, AlphaFlow, or MACE-driven short relaxation? | Different install burdens and different validation obligations | WP-C owner | pre-hackathon | 🟠 |
| B5 | Container registry, image build pipeline, and where artifacts live | Six groups pushing images on day one is a predictable jam | WP-F owner | pre-hackathon | 🟠 |

## C. Science and benchmark design

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | **How do we harmonise assay values across CDK9/7/12/13?** Different assays, different ATP concentrations, different labs | Selectivity ratios computed across incomparable assays are worse than no data | WP-A owner | pre-hackathon | 🔴 |
| C2 | Decoy strategy — property-matched, DUD-E style, or literature non-selective compounds? | Determines whether "ranking signal" means anything. Property-matched decoys are the honest choice and the harder one | WP-A owner | pre-hackathon | 🔴 |
| C3 | Do we include known *non-selective* pan-CDK inhibitors as a distinct class? | Strongly recommended: they are the discriminating cases, and the ones a 2D baseline gets wrong | WP-A owner | pre-hackathon | 🟠 |
| C4 | Protonation, tautomer and metal/cofactor handling at the pocket boundary | Quantum labels are highly sensitive to this. Get it wrong and WP-E produces confident nonsense | WP-E + WP-A | pre-hackathon | 🟠 |
| C5 | Apo vs. holo starting structures; which PDB entries; how to handle the DFG/activation loop state | Induced fit is part of the selectivity signal we claim to capture | WP-B owner | pre-hackathon | 🟠 |
| C6 | What is the honest 2D baseline? (ECFP4+RF? A published CDK selectivity model?) | Without a real baseline, "better than 2D" is unfalsifiable | WP-A + WP-D | pre-hackathon | 🔴 |

## D. Methodology

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| D1 | **Does hyperparameter sensitivity decrease as benchmark/label scale increases in this pipeline?** | This is the load-bearing assumption behind "start small, scale up" — and it is the [microtopic](../03-experiments/hpo-microtopic.md). If it fails, small-scale tuning does not transfer and the whole strategy needs a different justification | Methodology lead | during hackathon | 🟠 |
| D2 | What is the cheap proxy metric that tracks selectivity enrichment, and does it? | Our analogue of the perplexity–capability correspondence. Without one, every configuration evaluation costs a full pipeline run | Methodology lead | during hackathon | 🟠 |
| D3 | How many random-search configurations can we actually afford per stage? | Lourie et al. needed 256 for a clean signal `[literature]`. We will not get 256 full-pipeline runs. Which stages can be searched densely in isolation? | Methodology + WP-F | pre-hackathon | 🟠 |
| D4 | Bootstrap/permutation protocol for ranking metrics on n≈20 | Determines whether any observed difference is reportable | Methodology lead | pre-hackathon | 🟠 |
| D5 | Do we pre-register the analysis plan? | Cheap, and it is the difference between a finding and a story | Nick | pre-hackathon | 🟡 |

## E. Beyond the hackathon

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| E1 | Who owns the resulting data asset and any IP? | Needs answering *before* people contribute, not after | Nick + UniServices | pre-hackathon | 🟠 |
| E2 | Publication intent — methods paper, benchmark release, or internal only? | Changes how rigorously WP-A must document provenance | Nick | pre-hackathon | 🟡 |
| E3 | Is there an industry/clinical partner who would use the output? | Sharpens target choice beyond CDK9 | Nick | post-hackathon | 🟡 |
| E4 | Would NeSI / national infrastructure host a follow-on campaign? | Phase 3–4 exceeds a single department's capacity | Nick + eResearch | post-hackathon | 🟡 |
