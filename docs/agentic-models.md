# Open-weight models for agentic development

Agents write a lot of the code during the two days, so which model sits behind them is a platform
decision we make in advance.

**Search-derived as of 21 Sep 2026 and moving quickly. Verify before committing budget or a
booking.**

## Where things run

Three tiers, and they do different jobs. Full detail in [compute.md](compute.md).

| | Memory | Bandwidth | Runs |
| --- | --- | --- | --- |
| **Coder dev workspaces** · 2× RTX PRO 6000 Blackwell Max-Q | 96 GB GDDR7 each, 192 GB across the pair | ~1.79 TB/s each `[literature]` | Day-to-day development, and an agent model that fits |
| **Dual GB10** | 128 GB unified each | ~273 GB/s | Domain models — Boltz, Nesso-1, MLIPs. Not the large LLMs |
| **HGX H200**, whole node | 8 × 141 GB ≈ 1.1 TB | ~4.8 TB/s | The large agent models, benchmarks, batch |

The GB10s hold the small chemistry-side models comfortably and there's no reason to put a 500B MoE
on them.

## The shortlist

| Model | Total / active | Context | Modalities | Licence | Reported |
| --- | --- | --- | --- | --- | --- |
| **DeepSeek V4.1 Flash** | 552B / 8–16B | — | text, code | — | 90.6 Terminal-Bench 2.1 · 74.2 DeepSWE. Leads the board including closed models `[literature]` |
| **GLM 5.3** | 753B | — | **text, image, video** | bespoke GLM-5.3 | 1769 GDPval-AA v2, ahead of Claude Fable 5 and GPT-5.6 Sol `[literature]` |
| **GLM 5.3 Flash** | 320B / 18B | — | **text, image, video** | **MIT** | First natively multimodal GLM-5 `[literature]` |
| **MiniMax M3** | 428B / ~23B | 1M | **text, image, video** | — | 59.0 SWE-bench Pro · 66.0 Terminal-Bench 2.1 · 74.2 MCP Atlas `[literature]` |
| **Kimi K3** | 2.8T / 104B | 1M | text, code | — | 88.3 Terminal-Bench 2.1 `[literature]` |

**Kimi K3 is the one missing from the original three.** Qwen3 and the DeepSeek V4 Pro variant are
also in the conversation if the list needs widening.

**GLM 5.3 is multimodal.** GLM-5.3-Flash, released 26 August, is the first natively multimodal model
in the GLM-5 series and takes text, image and video. It's also MIT-licensed and only 18B active,
which makes it the easiest thing on this list to place.

## What fits where

Weights at 4-bit, roughly half a byte per parameter, before KV cache and overhead `[estimate]`:

| Model | Weights | Dev workspaces · 192 GB | H200 node · ~1.1 TB |
| --- | --- | --- | --- |
| GLM 5.3 Flash | ~160 GB | **fits** | yes, easily |
| MiniMax M3 | ~214 GB | no | yes |
| DeepSeek V4.1 Flash | ~276 GB | no | yes |
| GLM 5.3 | ~377 GB | no | yes |
| Kimi K3 | ~1.4 TB | no | **marginal** — needs ~3-bit and leaves little for KV cache |

A whole H200 node takes everything except Kimi K3 comfortably, several of them at FP8 rather than
4-bit. The interesting constraint has moved to the dev workspaces.

## The dev-workspace case for GLM 5.3 Flash

The RTX PRO 6000 pair is fast memory in a small amount: 192 GB at ~1.79 TB/s, about six and a half
times GB10's bandwidth. That rewards a model with few active parameters.

At 4-bit, 18B active is about 9 GB read per token, so ~1.79 TB/s gives a ceiling near **200 tokens
per second** `[estimate]`. The ceiling ignores prefill and attention, so measure it. Against that,
a dense 70B on the same hardware reads 35 GB per token and tops out near 50.

Add the MIT licence and native image input and it's the obvious default for everyday development,
with the H200 node behind it for anything that needs more.

## Modalities

Molecular work involves figures, plots and structure renders, so image input matters.

**Three of the five take images**: GLM 5.3, GLM 5.3 Flash and MiniMax M3. MiniMax M3 and Kimi K3
carry 1M context, which is worth having when an agent is reading a codebase.

DeepSeek V4.1 Flash leads the coding benchmarks and is text-only, so if it becomes the default for
code then something else needs to sit alongside it for anything visual.

## What to settle before the event

| | |
| --- | --- |
| Serving stack on the dev workspaces, and one model known to answer | unresolved |
| H200 node scheduling — agent serving competes with benchmark runs for the same node | unresolved |
| Whether the **dual-GB10 ConnectX pairing** gives one 256 GB pool or two 128 GB boxes `[verify]` | unresolved |
| Which themes need image input | ask the themes |
| A serving stack that builds for `aarch64` as well as `x86_64` ([the usual trap](compute.md)) | unresolved |

Nobody should be choosing a model on day 1. One working setup per theme, known to run, is the whole
pre-work list.
