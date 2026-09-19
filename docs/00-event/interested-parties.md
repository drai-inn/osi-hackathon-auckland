# Interested parties, people, teams and institutions to reach out to

Compiled from the three previous LLM/OSI Hackathons and the 2026 site list:

| Year | Event | Output | Source |
| --- | --- | --- | --- |
| 2023 | 1st, 14 projects | [Digital Discovery 10.1039/D3DD00113J](https://doi.org/10.1039/D3DD00113J) · [arXiv:2306.06283](https://arxiv.org/abs/2306.06283) | Full per-project author + institution table |
| 2024 | 2nd, 34 projects, 7 hubs, 556 registered | [arXiv:2411.15221](https://arxiv.org/abs/2411.15221) | Full per-project author + institution table |
| 2025 | 3rd, **120 submissions / 88 documented**, 16 hubs, 350+ participants | [arXiv:2605.03205](https://arxiv.org/abs/2605.03205) | Project table + awards page |
| 2026 | 4th, **21–22 Oct** | [llmhackathon.github.io](https://llmhackathon.github.io/) | Sites and awards pages |

**How to use this:** Tier 1 are people whose published hackathon work overlaps our pipeline
directly, reach out before the event with something specific. Tier 2 are organisers and hub leads,
which is the institutional route in. Tier 3 is regional. Tier 4 is the broader watch-list.

⚠️ Affiliations are as recorded in the source at the time and people move. Verify before writing.
Where a source gave no institution, the cell says so rather than guessing.

---

## Tier 1. Directly adjacent work

These teams built, at a hackathon, something that overlaps a stage of our pipeline. They are the
highest-value conversations available to us, and several would plausibly join a session remotely.

| Project | Who | Institution | Overlaps | Why talk to them |
| --- | --- | --- | --- | --- |
| **UMADock / CafChem** (2025, Visionary) | Mauricio Cafiero | *not stated in source* | **S5, S3** | Docked ligands using Meta's UMA MLIP **as the scoring function**, on pruned DUD-E structures, with explicit desolvation and ligand-strain terms. This is our surrogate-scoring thesis, already prototyped |
| **DynaAgent + AdsKRK** (2025, Visionary) | Xuan-Vu Nguyen, Ryo Kuroki, Edvin Fako, Bojana Ranković, Cassandra Lynn Masschelein, Salomé Guilbert, Jeremy Goumaz | **EPFL, LIAC** (Schwaller group) | **S3, S8** | Autonomous **protein–ligand MD** orchestration over AmberTools/GROMACS, validated on 5 protein–ligand complexes. Exactly our ensemble-generation stage |
| **F.A.D.E. Fully Agentic Drug Engine** (2025) | *team not named on the awards page; see paper §31* |, | **S1, S5, whole funnel** | The closest existing thing to our pipeline: target ID → structure retrieval → **Boltz-based prediction when no structure exists** → binding-site ID → generation → affinity ranking. Validated on EGFR and CRBP1 |
| **MIDAS** (2025, Visionary) | David Alobo, Michael Jirasek, Sebastian Pagel | **University of Glasgow** | **S1, S5** | Language-guided structure-based drug design; DiffSBDD conditioned via FiLM; binding-pose analysis inside a protein pocket |
| **DFTPilot** (2025, Visionary) | Chiku Parida, Diptendu Roy, Martin H. Petersen (DTU); Savyasanchi Aggarwal (UCL); Bingcan Li (Cambridge); Andre Low (NTU) | DTU · UCL · Cambridge · NTU | **S6** | RAG + crystal GNNs to set up and *preview* DFT calculations. Directly relevant to picking theory levels without burning the budget |
| **LARA-HPC** (2025, Visionary) | Luigi Genovese, Étienne Polack, Yoann Curé, Damien Caliste, Cinthya Herrera Contreras (CEA); Giuseppe Fisicaro (CNR); Louis Beal (INRIA); William Dawson (RIKEN); Jan Janssen (MPI-SusMat); Youssef Briki (U Montréal); Leonid Didukh (Kyiv INR) | CEA · CNR · INRIA · RIKEN · MPI-SusMat | **S6, S8** | Electronic-structure workflows submitted to **HPC clusters** by an agent, with a "rehearsal mode" validator before real runs. Solves a problem we will hit in week 2 |
| **ACME** (2025, Lila 5th) | Hassan Harb, Hossam Farag, Rakesh Kamath, Adwaith Ravichandran, Tugba Isik, Cailin Buchanan, Suman Kumari, Sungil Hong, Yunkai Sun, Mustafa Unal, Shi Li | **Argonne National Laboratory** | **S6, S7** | Closed-loop discovery: conformer search → QM → selection rules → automated experiment → feedback. Our active-learning loop with a wet lab attached |
| **ChemCodeBench** (2025) | *not named in table* |, | **S6** | Benchmarks LLMs on generating accurate **PySCF** DFT code, directly useful if cuEST falls through and GPU4PySCF becomes the fallback |
| **Agent Learn** (2025) | *not named in table* |, | **S7** | LLM agent inside an **active-learning loop** proposing informative molecules |
| **MJS** (2025, Visionary) | Mattias Akke (Lund); Jurgis Ruza, Soojung Yang (MIT) | Lund · MIT | **HPO microtopic** | LLM-guided **Bayesian optimisation** with domain-knowledge priors and interpretable design strategies. The closest thing to our configuration-search question |
| **ATOMS Lab** (2025, Abstrax) | Tyler Josephson, Samiha Sharlin, Fariha Agbere, Kevin Ishimwe, Colin Jones + others | **UMBC** | **HPO microtopic** | Analogical prompting for property prediction on **50–300-item datasets**, with systematic support-set ablation. Small-data methodology, done carefully |
| **SmeLLMap** (2025, Abstrax) | Justice Lu | **Duke University** | **S2, S5** | ESM2 embeddings + AlphaFold structures, **voxelised binding cavities** for property prediction. A different answer to "how do you represent a pocket" |
| **GAINS** / **Scaffold Conscious Agent** (2025) | *not named in table* |, | **S0** | PAINS-motif removal and scaffold-preserving optimisation with cheminformatics guardrails, relevant to decoy and benchmark design |
| **MC-Peptide** (2024) | Andres M. Bran, Philippe Schwaller + team | **EPFL** | **S0** | Agentic workflow extracting literature data to design macrocyclic peptides for permeability, drug-relevant data curation at speed |
| **Geometric Geniuses** (2024) | Jan Weinreich | Quastify GmbH | **S5** | Encoding **3D molecular geometry** for models that otherwise only see strings |
| **MolFoundation** (2024) | Hassan Harb + team | Argonne | **S5, S7** | Benchmarked ChemBERTa and T5-Chem and found **pre-trained ≈ fine-tuned**, directly relevant to whether our S7 retraining is worth it |
| **Liverpool Materials** (2024) | Federico Ottomano, Dmytro Antypov, Judith Clymo, Chi Zhang, Elena Patyukova | **University of Liverpool** | **HPO microtopic** | Property prediction **with limited training data**, the low-data regime we are in |
| **ChemLoRA / Molecular Energy Predictions** (2023) | Ankur K. Gupta, Wibe A. de Jong (LBNL); Garrett W. Merz (UW–Madison); Alishba Imran (Berkeley) | LBNL · UW–Madison · Berkeley | **S7** | Reached chemical accuracy using a **Δ-ML scheme**, precisely the delta-learning correction our S7 proposes |
| **Text2Concrete / sequential learning** (2023) | Christoph Völker, Sabine Kruschwitz, Ghezal Ahmad Zia | **BAM Berlin** | **S7** | Active learning and sequential design in a genuinely data-poor domain |

### The single most actionable item on this page

The **2024 kickoff panel** included **Michael Craig of Valence Laboratories**, alongside Elsa
Olivetti (MIT), Jon Reifsneider (Duke) and Marwin Segler (Microsoft).

**Valence Labs are the people behind Nesso-1**, and
[B3](../02-scope/open-questions.md), *is Nesso-1 fine-tunable, or inference-only?*, is a 🔴
blocker that determines whether our S7 is retraining or calibration-only. The hackathon organisers
have a route to them. Ask on the Slack, or ask Ben Blaiszik for an introduction.

---

## Tier 2. Organisers, hub leads and the institutional route

| Person | Institution | Role | Why |
| --- | --- | --- | --- |
| **Ben Blaiszik** | University of Chicago / Argonne / Globus | **Lead organiser, corresponding author all three years** (blaiszik@uchicago.edu) | The one email that resolves the dates, the Auckland hub listing, and an introduction to anyone above |
| **Ian Foster** | University of Chicago / Argonne | Co-author 2023–2025 | Research computing at scale; the eResearch conversation |
| **Kevin Maik Jablonka** | Friedrich-Schiller-Universität Jena | Lead author 2023; LLM-for-chemistry in the low-data limit | His "Is GPT-3 all you need for low-data discovery in chemistry?" is upstream of our microtopic |
| **Philippe Schwaller** | EPFL (LIAC) | Author all three years; LIAC ran DynaAgent and AdsKRK in 2025 | The lab whose 2025 work overlaps ours most |
| **Andrew D. White** | University of Rochester | 2023 senior author; ChemCrow | Agentic chemistry |
| **Berend Smit** | EPFL | 2023 senior author |, |
| **Defne Çirci** | **Duke University** (defne.circi@duke.edu) | **2026 Durham hub organiser, the only confirmed 2026 site** | The obvious person to ask "how do you actually run one of these?" Author 2023, 2024 and 2025 |
| **Tyler R. Josephson** | UMBC | Ran ATOMS Lab 2025; author 2024 | Small-data methodology |
| **L. Catherine Brinson** | Duke University | Author 2023, 2024 |, |
| **Seyed Mohamad Moosavi** | University of Toronto / Acceleration Consortium | Author 2024 | Toronto hub; self-driving labs |
| **Taylor Sparks** | University of Utah | Author 2024 |, |
| **Matthew L. Evans** | UCLouvain / Matgenix | Author 2023, 2024 (datalab, yeLLowhaMMer) | Research data management, relevant to WP-A provenance |
| **Jan Janssen** | MPI for Sustainable Materials | LangSim 2024, LARA-HPC 2025 | Workflow orchestration for atomistic simulation |
| **Yuan Chiang** | UC Berkeley | LangSim 2024 | Natural-language interfaces to simulation |

### 2026 hub sites, our peers

Confirmed: **Durham, NC (Duke)**. In planning: Baltimore (JHU) · Boston (MIT) · Chicago (UChicago) ·
Lemont (Argonne) · Madison (UW) · New York · Raleigh (NC State) · San Francisco · Toronto ·
**Singapore** · **Sydney** · **Auckland, us**.

---

## Tier 3. Regional and Oceania

Thin, which is itself the opportunity: **Auckland and Sydney would be the only two hubs in the
southern hemisphere.**

| Who | Institution | Route |
| --- | --- | --- |
| **Jodie Yuwono** | **University of Adelaide** | On the *Material AI Agent* team, 2025, a named Australian participant with direct experience of the format. The natural first Oceania contact |
| **Sydney hub organiser** | *unnamed, site in planning* | Ask Ben Blaiszik who is leading it. A trans-Tasman pairing on adjacent time zones is an easy, high-visibility collaboration |
| **Singapore hub** | *unnamed, site in planning* | Nearest hub by time zone after Sydney; Andre Low (NTU) was on DFTPilot |
| **NeSI / NZ eResearch** | national | Not hackathon-connected, but the natural Phase-3 infrastructure partner and an [Activity 4](../05-delivery/adjacent-activities.md) constituency |

## Tier 4. Watch-list

Groups whose hackathon output is adjacent rather than overlapping, worth knowing about but not
worth an email before October:

- **NOMAD / Humboldt-Universität zu Berlin** (Nathan Daelman, Sascha Klawohn, José M. Pizarro,
  Markus Scheidgen, Bernadette Mohr), data infrastructure, universal parsers, **MCP-standard
  tooling**. Relevant if our artifact layout ever needs to interoperate
- **MCP4SDL**, Ivory Zhang (UBC / Acceleration Consortium), James Garrick (Tennessee),
  Alexander Wieczorek (ETH / Empa), Elsayed Abdelfatah (Unilever), self-driving-lab interfaces
- **Parse Patrol**, Nathan Daelman, Christina Etrural, Rubel Mozumber, Sascha Klawohn (HU Berlin,
  BAM), Remya Ann Mathews Kalapurakal (New Hampshire)
- **MuMMIE**, Abhijeet Gangan (UCLA), Defne Çirci (Duke), Shashank Kushwaha (UIUC), Mohd Zaki (JHU)
 , multilingual benchmark construction
- **AtomBridge**, Daniel Palmer, Tawfiqur Rakib, Hyewon Jeong (UIUC); Jennifer Garland
  (Northwestern); Ritesh Kumar (UChicago); Gabe Graves (Georgia Tech), literature → validated
  structures, with physical sanity checks
- **SKY / Materials Design Group** (2025 1st place), Ryan Nduma, Hyunsoo Park, Kinga Mastej,
  **Imperial College London**, nearest-neighbour retrieval grounded in a structure database
- **MixSense** (2025 3rd), Jesus Diaz Sanchez, Katharina Jäger, Lucia Viña Lopez, Magdalena
  Lederbauer, Mrigi Munjal, Sathya Edamadaka, Tatem Rios (**MIT**); Kevin Greenman (CatholicTech)
- **ARIA**, Yi Cao, Liaoyaqi Wang, Tung Yan Liu, Yanqi Huang, Jieneng Chen (**Johns Hopkins**) -
  causal knowledge graphs for inverse design

---

## Suggested outreach sequence

| When | Who | Ask |
| --- | --- | --- |
| **Mon 21 Sep** | Ben Blaiszik | **Resolve the dates.** Confirm the Auckland hub. Ask for an introduction to Valence Labs re: Nesso-1 ([B3](../02-scope/open-questions.md)) |
| Tue 22 Sep | Global Slack | Introduce the Auckland hub and what we are building. This is how mentors and collaborators find us |
| Wed 23 Sep | Defne Çirci (Duke) | "You are the only confirmed 2026 site, what do you wish you'd known?" Cheap, friendly, and she has run it before |
| Wed 23 Sep | Jodie Yuwono (Adelaide); Sydney lead via Ben | A southern-hemisphere pairing |
| Fri 25 Sep | **Tier 1, three or four only** | Something specific: *"We are building X, you built Y at the 2025 event, would you spend 30 minutes with our team during the hackathon?"* A targeted ask to someone whose work you have actually read gets answered |
| During the event | LIAC (EPFL), Mauricio Cafiero, the F.A.D.E team | Live remote sessions in the [adjacent activities](../05-delivery/adjacent-activities.md) |
| Post-event | All of the above + organisers | Submit projects; contribute to the write-up paper |

**Do not mass-mail Tier 1.** Four specific, well-informed emails will outperform forty generic ones,
and the generic version costs goodwill we will want later.
