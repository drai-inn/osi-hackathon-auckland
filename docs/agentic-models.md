# Open-weight models for agentic development

Agents write a lot of the code during the two days, so which model sits behind them is a platform
decision we make in advance. This page is the shortlist and, more usefully, what each one needs to
run.

**Everything here is search-derived as of 21 Sep 2026 and moves quickly. Verify before committing
budget or a booking.**

## The shortlist

| Model | Total / active | Context | Modalities | Reported | Released |
| --- | --- | --- | --- | --- | --- |
| **DeepSeek V4.1 Flash** | 552B / 8–16B | — | text, code | 90.6 Terminal-Bench 2.1 · 74.2 DeepSWE. Leads the board including closed models `[literature]` | 10 Sep 2026 |
| **Kimi K3** | 2.8T / 104B | 1M | text, code | 88.3 Terminal-Bench 2.1 `[literature]` | 27 Jul 2026 |
| **GLM 5.3** | 753B | — | text, code | 1769 GDPval-AA v2, ahead of Claude Fable 5 and GPT-5.6 Sol `[literature]` | 28 Aug 2026 |
| **MiniMax M3** | 428B / ~23B | 1M | **text, code, image, video** | 59.0 SWE-bench Pro · 66.0 Terminal-Bench 2.1 · 74.2 MCP Atlas `[literature]` | Jun 2026 |

**Kimi K3 is the one missing from the original three** and it's a serious contender on
Terminal-Bench. Qwen3 and the DeepSeek V4 Pro variant are also in the conversation and worth a look
if the shortlist needs widening.

## What actually fits

This is the part that decides it, and it's arithmetic rather than preference. Weights at 4-bit,
roughly half a byte per parameter, plus KV cache and overhead `[estimate]`:

| Model | Weights at 4-bit | Dual GB10 · 256 GB | One H200 · 141 GB |
| --- | --- | --- | --- |
| MiniMax M3 | ~214 GB | **fits**, with room for KV cache | no |
| DeepSeek V4.1 Flash | ~276 GB | marginal miss; needs ~3.5-bit or offload | no |
| GLM 5.3 | ~377 GB | no | no |
| Kimi K3 | ~1.4 TB | no | no |

An HGX H200 node is normally eight GPUs and about 1.1 TB, which changes every row. **How much of a
node we get is the question that settles the model choice**, and it's the same unresolved access
question as everything else on [compute.md](compute.md).

## Why mixture-of-experts suits the GB10s

GB10 is capacity-rich and bandwidth-poor: 128 GB per box, ~273 GB/s. A dense model reads all its
weights for every token, so bandwidth caps it hard. A sparse MoE reads only the active experts.

Rough ceilings at 4-bit `[estimate]`:

| | Active params | Read per token | Ceiling |
| --- | --- | --- | --- |
| DeepSeek V4.1 Flash | 8–16B | 4–8 GB | ~34–68 tok/s |
| MiniMax M3 | ~23B | ~11.5 GB | ~24 tok/s |
| A dense 70B, for contrast | 70B | 35 GB | ~8 tok/s |

So **low active-parameter MoE is the shape that makes local agentic work viable on GB10**, and the
two models that fit that description are the two at the top of the list. Measure it rather than
trusting the arithmetic — the ceiling ignores prefill, attention and everything else.

## Modalities, and why they need deciding early

Molecular work involves figures, plots and structure renders, so image input is not a nice-to-have.
**MiniMax M3 is the only one on the shortlist with native image and video input.** The rest are text
and code.

If a theme needs a model to look at a plot, that either picks the model or means a second one behind
a router. Either is fine, and it's a platform decision rather than something to discover on the day.

## What to settle before the event

| | |
| --- | --- |
| **How many H200 GPUs** we get, and for how long. Everything else follows from this | unresolved |
| Whether the **dual-GB10 ConnectX pairing** gives one 256 GB pool or two 128 GB boxes `[verify]` | unresolved |
| **Self-host or API** for the models that don't fit. A hosted endpoint is a legitimate answer | unresolved |
| Which models need **image input**, per theme | ask the themes |
| A **serving stack** that builds for `aarch64` as well as `x86_64` ([the usual trap](compute.md)) | unresolved |

Nobody should be choosing a model on day 1. One working setup per theme, known to run, is the whole
pre-work list.
