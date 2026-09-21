# Compute plan — GB10 for the month, H200 for the benchmarks

> Serving open-weight models for agentic development is sized separately in
> [agentic-models.md](agentic-models.md), and it competes for the same hardware.

Two resources with very different characters, available on different timescales. Using each for
what it is good at is most of the feasibility argument for a two-day event.

For GPU-hour arithmetic per run tier see compute-budget.md; this page is about
*which machine* and *when*.

---

## The two resources

### A third tier

Development happens on **Coder dev workspaces** carrying **2× RTX PRO 6000 Blackwell Max-Q**, 96 GB
GDDR7 each at ~1.79 TB/s `[literature]`. Fast memory in a small amount, and the right place for
everyday work and for serving an agent model that fits in 192 GB. See
[agentic-models.md](agentic-models.md).

**The GB10s are for the domain models** — Boltz, Nesso-1, MLIPs — where 128 GB is plenty and the
models are small. The large agent LLMs belong on the H200 node or the workspaces.

**The HGX H200 is a whole node**, so roughly 1.1 TB across eight GPUs. That takes any open-weight
model we are likely to want, and agent serving competes with benchmark runs for it.

| | **Dual GB10** | **HGX H200** |
| --- | --- | --- |
| Availability | **Now through the end** — ours, uncontended | Bookable blocks; benchmarks + the event |
| Architecture | `aarch64` (Grace Arm) + Blackwell | `x86_64` + Hopper |
| Memory | 128 GB unified per box; 256 GB across the pair via ConnectX-7 `[verify]` | 141 GB HBM3e per GPU |
| Memory bandwidth | ~273 GB/s `[verify]` | ~4.8 TB/s |
| Character | **Big models fit; they run slowly.** Capacity-rich, bandwidth-poor | **Throughput.** ~18× the bandwidth |
| Good for | Development, correctness, unattended overnight work, small-N exploration, the day-1 on-ramps | Sweeps, quantum labelling, anything bandwidth-bound, timing benchmarks |
| Bad for | Quantum chemistry, large batch inference, anything latency-sensitive | Iterating on code. Queue waits make a 5-minute edit cycle a 40-minute one |

Specifications are from public material and marked `[verify]` — WP-F confirms against the actual
boxes in week 1.

### The GB10:H200 ratio

Per-unit costs in compute-budget.md are quoted in **H200-hours**. To plan GB10
work we need a conversion, and the honest answer is that it depends heavily on the workload:

- **Compute-bound** (co-folding, scorer training): GB10 ≈ **0.2–0.3×** an H200 `[estimate]`
- **Bandwidth-bound** (batch inference, MD integration, DFT): GB10 ≈ **0.05–0.1×** `[estimate]`

Planning figure: **1 GB10-hour ≈ 0.15 H200-hours**, with wide error bars.
W2.7 measures the real ratio by
running the same S1 job on both. Until then every GB10 estimate on this page is soft.

### What the month on GB10 is worth

2 boxes × 30 days × ~20 usable hours = **~1,200 GB10-hours ≈ 180 H200-equivalent hours** `[estimate]`.

For comparison, the whole hackathon-minimum workload is ~286 H200-hours. So **the month of GB10
time can pre-compute roughly half to two-thirds of it** — excluding the quantum stage, which almost
certainly needs H200.

That is the feasibility argument for a two-day event in one sentence.

---

## The architecture split

🔴 **This is the most under-appreciated risk in the project.** GB10 is `aarch64`; H200 is `x86_64`. A
container built on one will not run on the other unless it is built for both.

It fails silently in the worst way: everything works beautifully on GB10 all through weeks 2 and 3,
and then the H200 run in week 3 or — worse — on the day, doesn't start.

**What to do, in week 1** (W1.1):

1. Inventory every dependency for an `aarch64` build. PyTorch, CUDA, OpenMM and RDKit are generally
   fine on Grace; specialist cheminformatics and quantum packages frequently are not.
2. Decide the build strategy — multi-arch manifests (`docker buildx --platform linux/amd64,linux/arm64`)
   are the clean answer, cross-compilation or per-arch images the fallback.
3. **Run something non-trivial on both** before week 2. Not a hello-world: the real S1 container.
4. Write the answer down as a table of works / needs-building / impossible, and re-scope anything in
   the third column immediately.

If a stage cannot be built for `aarch64`, that stage develops on H200 and does not benefit from the
month of GB10 time. Know which stages those are by Friday 25 Sep, not in week 3.

---

## Allocation

### GB10 — continuous, now to 18 Oct

| Period | Use |
| --- | --- |
| Week 1 | The architecture spike. Nothing else matters until it is answered |
| Week 2 | Smoke test, stage skeletons, S1 first real complexes |
| Week 3 | Stages real; start overnight pre-computation |
| Week 4 | **Unattended pre-computation campaign** — all complexes, ensembles, reference MD, baselines. This is what the boxes are for |
| 19–20 Oct | **The on-ramps.** Interactive, low-latency, uncontended — exactly right for a room of people each launching their own run |

**During the event, GB10 is the participant-facing resource and H200 is the batch resource.** A
newcomer's first run must not sit in a queue behind a sweep.

### H200 — booked blocks

| When | What | Why it must be H200 |
| --- | --- | --- |
| Week 2, ~half a day | Benchmark the same S1 job run on GB10 | Measures the ratio everything else is planned against |
| Week 3, **1–2 days** | **Quantum convergence study** ([S6](worked-example.md)) | DFT is bandwidth-bound and cuEST may be `x86_64`-only. Also the load-bearing check of the whole project |
| Week 4, ~half a day | Rehearsal: the integrated pipeline, end to end | Proves the event-day path works before the event |
| **19–20 Oct** | Production sweeps, quantum labelling, the integrated run | Throughput |

**Book the week-3 block now.** It is the one with no slack: if the convergence study fails, we need
time to change the approach, and it cannot start until S1–S4 produce real pockets.

---

## Consequences for the plan

- **Development targets GB10 and is validated on H200 weekly.** Not the other way round: iterating
  behind an H200 queue wastes the month.
- **Pre-computation is scheduled like a campaign, not run ad hoc.** WP-F owns a queue of unattended
  overnight jobs from week 3.
- **Anything that cannot run on GB10 is a scheduling constraint**, so we need the list in week 1.
- **The event's interactive load lives on GB10.** Sizing for the on-ramps: ~15 people × a few runs
  each × ~20 min ≈ well within two boxes, *if* the runs are the cheap S5 configurations. Confirm in
  the week-4 dry run.

## Open

- Exact GB10 specification and whether the pair presents as one 256 GB device or two (W1.1)
- Whether cuEST has an `aarch64` build at all (W1.3)
- H200 queue policy: reservation or fair-share? Determines whether "book a block" means anything (W1.2)
- Shared storage between GB10 and H200 — if artifacts must be copied between them, budget the time
  and the bandwidth. An unglamorous detail that has eaten whole days on projects like this
