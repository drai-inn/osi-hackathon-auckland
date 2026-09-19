# Open questions

Everything here blocks or reshapes something. Each row: what we need to know, why it matters,
who resolves it, and by when. **Update this file in place — it is the project's honest edge.**

Status key: 🔴 blocking · 🟠 shapes design · 🟡 nice to resolve early · ✅ resolved (keep the row, add the answer)

---

## A. Logistics and commitment

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| A1 | ~~When is the hackathon?~~ | — | Nick | — | ✅ **Mon 19 – Tue 20 Oct 2026, 2 days.** US relay 20–21 Oct. Drove the rewrite of [plan.md](../04-hackathon/plan.md) and the creation of [critical-path.md](../04-hackathon/critical-path.md) |
| A2 | **Is the H200 bookable — mechanism, quota, queue policy?** Need blocks in weeks 2, 3, 4 *and* 19–20 Oct | Without a week-3 block the quantum convergence study cannot happen before the event, and gates 4–5 become unassessable | Nick + eResearch | **Fri 25 Sep** ([W1.2](../04-hackathon/critical-path.md)) | 🔴 |
| A2b | Dual GB10 — confirmed ours continuously to 18 Oct and during the event? Exact spec? | The whole month's plan rests on it ([compute-plan.md](../05-feasibility/compute-plan.md)) | Nick + WP-F | Fri 25 Sep | 🟠 |
| A3 | **How many people, and from which disciplines?** | Six packages need an owner *and* a host each. Below ~10 we cut WP-C's surrogate arm | Nick | **Mon 21 Sep** ([session](../04-hackathon/monday-session.md)) | 🔴 |
| A4 | Is there budget for cloud burst if a block slips? | Schedule risk, now with only four weeks of slack | Nick | Fri 2 Oct | 🟠 |
| A5 | **Which research leaders are we inviting?** | Invitations must go out by **Wed 23 Sep** — four weeks is already short notice | Nick | **Wed 23 Sep** | 🔴 |
| A6 | Who are the US counterparts, and what can they run? | Item 7 of the handoff ranks questions against *their* compute ([us-handoff.md](../04-hackathon/us-handoff.md)) | Nick | Fri 25 Sep | 🟠 |

## B. Software and licensing

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| **B0** | **🔴 Does our stack build for `aarch64` (GB10) *and* `x86_64` (H200)?** | **The most under-appreciated risk in the project.** Everything works on GB10 through weeks 2–3, then the H200 run doesn't start. One day of spike work removes it entirely ([compute-plan.md](../05-feasibility/compute-plan.md#the-architecture-split)) | WP-F | **Fri 25 Sep** ([W1.1](../04-hackathon/critical-path.md)) | 🔴 |
| B1 | **Is cuEST actually available to us** — licence, container, driver requirements, supported methods, **and which architecture**? | WP-E does not exist without it. Fallback: GPU4PySCF / TeraChem / xTB — a different cost model by orders of magnitude | WP-E owner | **Fri 25 Sep** ([W1.3](../04-hackathon/critical-path.md)) | 🔴 |
| B2 | Boltz-2 licence and weights — redistribution terms for our container? | Affects whether the workflow is publicly reproducible | WP-B owner | Fri 25 Sep | 🟠 |
| B3 | Nesso-1 availability, licence, and whether it is fine-tunable at all (vs. inference-only) | S7 depends on this. If inference-only, the feedback loop becomes calibration-only, or we substitute an in-house equivariant GNN | WP-D owner | **Fri 25 Sep** | 🔴 |
| B4 | Which ensemble surrogate: BioEmu, AlphaFlow, or MACE-driven short relaxation? | Different install burdens and validation obligations — and different odds of an `aarch64` build | WP-C owner | Fri 2 Oct | 🟠 |
| B5 | Container registry, **multi-arch** build pipeline, and where artifacts live | Multi-arch manifests are the clean answer; decide before anyone builds | WP-F owner | Fri 2 Oct | 🟠 |
| B6 | Shared storage between GB10 and H200 — or must artifacts be copied? | An unglamorous detail that eats whole days | WP-F owner | Fri 2 Oct | 🟡 |

## C. Science and benchmark design

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | **How do we harmonise assay values across CDK9/CDK7?** Different assays, ATP concentrations, labs | Selectivity ratios across incomparable assays are worse than no data. Activity 1's first agenda item | WP-A owner | **Fri 2 Oct** (manifest v1) | 🔴 |
| C2 | Decoy strategy — property-matched, DUD-E style, or literature non-selective compounds? | Determines whether "ranking signal" means anything. Property-matched decoys are the honest choice and the harder one | WP-A owner | Fri 2 Oct | 🔴 |
| C3 | Do we include known *non-selective* pan-CDK inhibitors as a distinct class? | Strongly recommended: they are the discriminating cases, and the ones a 2D baseline gets wrong | WP-A owner | Fri 2 Oct | 🟠 |
| C4 | Protonation, tautomer and metal/cofactor handling at the pocket boundary | Quantum labels are highly sensitive to this. Get it wrong and WP-E produces confident nonsense | WP-E + WP-A | Fri 9 Oct | 🟠 |
| C5 | Apo vs. holo starting structures; which PDB entries; how to handle the DFG/activation loop state | Induced fit is part of the selectivity signal we claim to capture | WP-B owner | Fri 2 Oct | 🟠 |
| C6 | What is the honest 2D baseline? (ECFP4+RF? A published CDK selectivity model?) | Without a real baseline, "better than 2D" is unfalsifiable | WP-A + WP-D | Fri 2 Oct | 🔴 |

## D. Methodology

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| D1 | **Does hyperparameter sensitivity decrease as benchmark/label scale increases in this pipeline?** | This is the load-bearing assumption behind "start small, scale up" — and it is the [microtopic](../03-experiments/hpo-microtopic.md). If it fails, small-scale tuning does not transfer and the whole strategy needs a different justification | Methodology lead | during the event | 🟠 |
| D2 | What is the cheap proxy metric that tracks selectivity enrichment, and does it? | Our analogue of the perplexity–capability correspondence. Without one, every configuration evaluation costs a full pipeline run | Methodology lead | during the event | 🟠 |
| D3 | How many random-search configurations can we actually afford per stage? | Lourie et al. needed 256 for a clean signal `[literature]`. We will not get 256 full-pipeline runs. Which stages can be searched densely in isolation? | Methodology + WP-F | Fri 9 Oct | 🟠 |
| D4 | Bootstrap/permutation protocol for ranking metrics on n≈20 | Determines whether any observed difference is reportable | Methodology lead | Fri 9 Oct | 🟠 |
| D5 | Do we pre-register the analysis plan? | Cheap, and it is the difference between a finding and a story | Nick | Fri 16 Oct | 🟡 |

## D2. Engagement (new — the event is 2 days and several participants are new to AI for science)

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| G1 | **Who hosts each work package's newcomers?** Host ≠ owner | In a 2-day sprint the owner will choose the technical work every time. The split is the fix ([engagement.md](../04-hackathon/engagement.md#the-structural-fix-split-the-host-role)) | Nick | **Mon 21 Sep** | 🔴 |
| G2 | Can a genuine novice reach a first result in under 30 minutes? | The on-ramp promise. Untested until someone tries it | Hosts | **Fri 16 Oct** ([W4.2](../04-hackathon/critical-path.md)) | 🟠 |
| G3 | What are the six sealed-forecast questions? | They must map onto the gates to be worth opening on day 2 | Nick | Fri 9 Oct | 🟡 |
| G4 | Does the interactive GB10 load hold up with ~15 people launching runs? | A newcomer's first run must not queue behind a sweep | WP-F | Fri 16 Oct | 🟠 |

## E. Beyond the hackathon

| # | Question | Why it matters | Owner | By | Status |
| --- | --- | --- | --- | --- | --- |
| E1 | Who owns the resulting data asset and any IP? | Needs answering *before* people contribute, not after | Nick + UniServices | **Wed 23 Sep** (before invitations) | 🟠 |
| E2 | Publication intent — methods paper, benchmark release, or internal only? | Changes how rigorously WP-A must document provenance | Nick | Fri 16 Oct | 🟡 |
| E3 | Is there an industry/clinical partner who would use the output? | Sharpens target choice beyond CDK9 | Nick | post-hackathon | 🟡 |
| E4 | Would NeSI / national infrastructure host a follow-on campaign? | Phase 3–4 exceeds a single department's capacity | Nick + eResearch | post-hackathon | 🟡 |
