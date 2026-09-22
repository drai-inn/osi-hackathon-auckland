# The global event, and where Auckland fits

We're running **one hub of a global event**, which shapes what we build, how we present it, and
what we get back.

---

## What it is

The **Open Scientific Intelligence (OSI) Hackathon for the Physical Sciences & Mathematics** -
until this year the *LLM Hackathon for Applications in Materials Science and Chemistry*. Fourth
annual. Free. Hybrid: physical hubs worldwide plus an online hub.

Lead organiser: **Ben Blaiszik** (University of Chicago / Argonne / Globus), corresponding author
on all three write-ups. Registration: [luma.com/ku88xh92](https://luma.com/ku88xh92).
Site: [llmhackathon.github.io](https://llmhackathon.github.io/).

## Three years, and the trend

| | Projects | Hubs | Participants | Output |
| --- | --- | --- | --- | --- |
| **2023** | 14 | online |, | [Digital Discovery 10.1039/D3DD00113J](https://doi.org/10.1039/D3DD00113J) · [arXiv:2306.06283](https://arxiv.org/abs/2306.06283) |
| **2024** | 34 | 7 (Toronto, Montreal, San Francisco, Berlin, Lausanne, Tokyo + online) | 556 registered, 120 active | [arXiv:2411.15221](https://arxiv.org/abs/2411.15221) |
| **2025** | **120 submitted, 88 documented** | **16** | 350+ | [arXiv:2605.03205](https://arxiv.org/abs/2605.03205) |
| **2026** |, | 13+ listed, incl. **Auckland** |, | **21-22 Oct**, we run 19-20 |

**Every event produces a peer-reviewed or arXiv paper crediting every team.** The 2025 paper runs
to 140+ pages and lists every contributor. For a student in the room, that is a real publication
for two days' work, and it is the single most persuasive line in a recruitment email.

The trend the organisers themselves identify, 2023 → 2025: **from single-purpose LLM tools toward
integrated multi-agent workflows** that combine retrieval, reasoning, tool use and domain-specific
validation. They classify 2025's projects into two families, **Knowledge Infrastructure** (new
ways to *know* things) and **Action Systems** (new ways to *do* things).

## How the hub model works

**What a hub must provide:** reliable internet, a room with tables and power, a local site lead who
stays on site, and adherence to safety and accessibility standards. Optionally: refreshments, local
prizes, compute, documentation support.

**What the organisers provide:** scheduling materials, promotional assets, a shared Slack
workspace, mentorship from academics and industry, and post-event recognition.

**How to become one:** an express-interest form, then confirm requirements, promote locally, run
the event. Auckland is already listed as a **site in planning**, someone has put us on the map.

We run 19-20 Oct, because those are the two days we have
([ADR-0006](adr/0006-run-19-20-october-as-a-precursor.md)). Ben Blaiszik is supportive of our dates
and our approach, so we run on ours and register through theirs: **one free registration covers
every site, including this one.**

**2026 sites.** Confirmed: Durham NC (Duke, Defne Çirci). In planning: Baltimore (JHU) · Boston
(MIT) · Chicago · Lemont (Argonne) · Madison · New York · Raleigh (NC State) · San Francisco ·
Toronto · Singapore · **Sydney** · **Auckland**.

Note what that list implies: **Auckland and Sydney would be the only southern-hemisphere hubs.**

## Judging, prizes, submission

Judged on: **research impact · innovativeness and uniqueness · scalability · domain relevance.**

Prize tracks in 2025: the **Lila Prize** (top five overall), **Abstrax Prizes**, and **Visionary
Awards** for novelty, plus an invitation to a showcase session. Sponsors have included Lila,
Hugging Face, AIChemy, Cerebras, Fum, NSF, Abstrax Tech, biostate.AI, Advaita Capital and
Green Dynamics.

A submission is: a description, a **public code repository**, and a **video demo**. The 2025 paper
excluded 32 of 120 submissions for incomplete documentation, so the documentation is not optional
overhead, it is the difference between being in the paper and not.

## Where our themes sit

Several 2025 teams built things adjacent to our four themes
([the full list](interested-parties.md#tier-1-directly-adjacent-work)):

| Their project | What it did | Nearest theme |
| --- | --- | --- |
| **UMADock** | Docked ligands using an MLIP as the scoring function | 1, 2 |
| **DynaAgent** (EPFL LIAC) | Autonomous protein-ligand MD orchestration | 2 |
| **F.A.D.E** | Target → Boltz structure → binding site → generation → affinity | 1 |
| **DFTPilot** | RAG-assisted DFT setup and preview | 2 |
| **LARA-HPC** | Electronic-structure workflows submitted to HPC by an agent | 2 |
| **ACME** (Argonne) | Closed loop: QM → selection → automated experiment → feedback | 2, 3 |

So people have been working near all of this. A few things are still thin across the 88 documented
projects, and any of them is a reasonable place for a group to aim:

1. **A stated trust region for a surrogate.** Not one of the 88 says where its model can be relied
   on and where it cannot.
2. **Which settings mattered.** Everyone tunes; almost nobody reports which parameters moved the
   answer, with intervals. The [small-experiments thread](small-experiments.md) is about that.
3. **Selectivity.** One mention of the word in the entire 2025 paper.
4. **Evaluation that survives a change of metric.** Recent benchmarks show the ranking of models
   flipping when the metric changes.

That's a good position to be in: adjacent enough that people recognise the work, open enough that
there's something to find.

## What we owe and what we get

Running on other dates means some of this is to be negotiated rather than assumed.

**We owe:** a Slack presence and honesty about our dates; a room that works; and, afterwards -
documented submissions with code and demos, if they will have them.

**We hope to keep:** a route to the write-up paper for everyone in the room, the mentor pool and
Slack, the site listing marked with our own dates, and a standing relationship with the groups in
[interested-parties.md](interested-parties.md). Prizes and the live showcase are probably out, and
we should not plan around them.

**What we can offer back:** a working benchmark, a reproducible workflow and a set of results,
published before the global event opens, which other sites can pick up if useful.

**What to lead with:** the global event itself. It runs 21-22 October, one free registration covers
every site, and that registration is the one we point people at. We're a local site and the copy
reads that way.
