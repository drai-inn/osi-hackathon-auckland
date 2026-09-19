# Ladder D · Builder. RSE, HPC, infrastructure, pipeline code

**For you if:** you want to build the thing. Research software engineering, HPC, MLOps, or you're
simply the person who ends up making other people's code run.

**There is real work available from this week**, not just on the day. The month before the event is
where this project is won or lost, and most of it is yours.

---

## Rung 0 · Orient, 20 minutes

1. Clone, and run the two tools. Standard library only, no environment needed:
   ```bash
   make validate && make budget TIER=hackathon_minimum
   ```
2. Read **[architecture.md](../../03-pipeline/architecture.md)**, nine stages, four surrogates,
   what each is for
3. Read **[interfaces.md](../../03-pipeline/interfaces.md)**, the data contracts. This is the
   document that decides whether six groups integrate on day 2 or produce six demos

**You now know:** the shape of the system and where the seams are.

## Rung 1 · First contact, 30 minutes

**Read [S8 Orchestration](../../03-pipeline/stages/S8-orchestration.md) and
[the Snakefile sketch](../../../workflow/Snakefile.sketch), and tell us what's wrong with them.**

The sketch is deliberately not runnable. It exists to make the DAG shape, artifact layout and config
namespace concrete enough to argue about. Known soft spots:

- The checkpoint machinery around `s1_complexes` is the fiddliest part and is hand-waved
- Snakemake on Kubernetes is less well-trodden than on Slurm, and nobody has validated the executor
- Cost telemetry is asserted, not designed

Or go straight to the thing that actually worries us:

**[The architecture spike](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/2).** GB10 is
`aarch64`; H200 is `x86_64`. Everything will work beautifully on GB10 through weeks 2 and 3 and then
the H200 run won't start. One day of spike work this week eliminates it entirely. It is the most
under-appreciated risk in the project and it is sitting unclaimed.

## Rung 2 · Contribute, a week in the month

Claim one. Each is a real deliverable with a date:

| Task | By | Issue |
| --- | --- | --- |
| **Architecture spike**, what builds for `aarch64` and `x86_64` | Fri 25 Sep | [#2](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/2) |
| Multi-arch base images, published and digest-pinned | Fri 2 Oct | [#8](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/8) |
| **`make smoke` green on GB10** with every stage stubbed | Fri 2 Oct | [#8](https://github.com/drai-inn/drugs-surrogate-pipeline/issues/8) |
| Cost telemetry. GPU-seconds per item per stage, to disk and MLflow | Fri 9 Oct |, |
| **The live dashboard**, runs appear with the runner's name | Fri 9 Oct |, |
| Pre-computation campaign, unattended overnight jobs | Fri 16 Oct |, |

**The dashboard is worth calling out.** It is the thing that makes
[on-ramp A](../engagement.md#a-your-run-your-parameter--anyone-including-non-coders--20-min) work,
and on-ramp A is the promise the entire newcomer experience rests on. It's a small piece of software
with a disproportionate effect on whether fifteen people have a good two days.

## Rung 3 · Own, the event

Own **WP-F**. On the day that means:

- Keeping the DAG and dashboard alive while fifteen people hammer them
- The **GPU-hour burn-down board**, visible in the room. Nothing concentrates minds like watching
  the quantum budget disappear
- Day 2's **integrated run**, and the 15:00–16:30 window reserved for it failing and being re-run
- The **reproducibility report**, which is [gate 1](../../06-feasibility/stage-gates.md), and
  without it no other gate means anything

## Rung 4 · Carry, afterwards

- **The template.** A reusable pattern for GPU research pipelines at UoA: Snakemake, multi-arch
  containers, provenance that survives, cost telemetry as a first-class output. That generalises to
  every GPU-using group on campus and is
  [Activity 4](../../05-delivery/adjacent-activities.md#activity-4-alternate--reproducible-gpu-research-workflows)
- **The eResearch conversation.** Phase 3 exceeds one department's capacity
- **Upstream.** No other hub appears to have solved reproducible multi-arch GPU orchestration for
  this kind of workflow. It's worth offering

---

## The constraint, so you don't have to guess

**Snakemake + containers + whole-GPU Kubernetes jobs + MLflow. Nothing else.**
([ADR-0004](../../adr/0004-snakemake-containers-no-new-infra.md))

If that proves insufficient the answer is a smaller run, not more machinery. This is a scope
boundary rather than a preference, and WP-F owns enforcing it, including against your own good
ideas. Multi-stage GPU pipelines attract infrastructure, and infrastructure is how a two-day event
becomes a two-day installation.
