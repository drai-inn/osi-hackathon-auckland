# ADR-0005 — Develop on GB10, benchmark on H200, pre-compute the month

**Status:** accepted · **Date:** 2026-09-19 · **Deciders:** Nick Jones

## Context

Two facts arrived together and reshape the plan:

1. **The event is two days** (19–20 Oct), not five.
2. **Dual GB10 boxes are available continuously** from now to the end, and HGX H200 is bookable in
   blocks.

Two days cannot absorb a build. The five-day plan put containers, stage implementations, cost
measurement and the quantum convergence study on "day 1"; there is no such day any more.

The two machines have very different characters. GB10 is capacity-rich and bandwidth-poor
(~128 GB unified, ~273 GB/s `[verify]`); H200 is the reverse (141 GB HBM3e, ~4.8 TB/s). GB10 is
uncontended and ours; H200 is queued and booked.

## Decision

**Three commitments:**

1. **Development targets GB10 and is validated on H200 weekly.** Not the other way round —
   iterating behind an H200 queue wastes the month.
2. **The month runs a pre-computation campaign**, so the event starts with complexes, ensembles,
   reference MD, baselines and the quantum convergence study already done. Only work that needs
   people present happens in the room ([plan.md](../05-delivery/plan.md#what-genuinely-needs-people-in-a-room)).
3. **During the event, GB10 is the participant-facing resource and H200 is the batch resource.** A
   newcomer's first run must not queue behind a sweep.

Corollary, and the reason this ADR exists rather than being a scheduling note: **every container
must build for both `aarch64` and `x86_64`.** Multi-arch manifests are the default; per-arch images
the fallback. Any stage that cannot build for `aarch64` develops on H200 and forfeits the month's
compute dividend — we need that list by Fri 25 Sep.

## Alternatives considered

| Option | Why not |
| --- | --- |
| Develop on H200 only | Queue latency turns a 5-minute edit cycle into 40 minutes. Wastes the month, and leaves the GB10s idle |
| Use GB10 only | Quantum chemistry is bandwidth-bound and cuEST may be `x86_64`-only. Throughput sweeps would take weeks |
| Keep the 5-day plan and compress it | Two days is 40% of five. Compression is not a plan, it is a hope |
| Pick one architecture and stick to it | We do not get to choose: the boxes we have are `aarch64`, the cluster we need is `x86_64` |

## Consequences

**Good:** ~1,200 GB10-hours over the month ≈ ~180 H200-equivalent hours `[estimate]`, roughly
half to two-thirds of the whole hackathon-minimum workload, obtained for free by using time we
would otherwise spend waiting. The event becomes two days of science. Interactive on-ramps get a
dedicated, uncontended machine, which is what makes a sub-30-minute first result plausible.

**Bad:** every container is built twice, and every dependency needs an `aarch64` story. The
GB10:H200 ratio is currently an `[estimate]` with wide error bars, so all month-capacity planning
is soft until [W2.7](../05-delivery/critical-path.md) measures it. Artifacts may need copying
between architectures, which nobody has budgeted time for yet.

**Revisit if:** the week-1 spike finds that a material fraction of the stack has no `aarch64`
build. Then GB10 becomes a development box for the ML stages only, the month's dividend shrinks,
and the event scope must be cut accordingly — a decision we want to make on 25 Sep with four weeks
in hand, not in week 3 with one.
