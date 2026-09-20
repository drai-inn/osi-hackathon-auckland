# Agentic development and operations of the pipeline

**Reviewed:** 21 Sep 2026 · **Settled by:** D9 at [today's session](../monday-session.md) ·
**Touches:** WP-D, WP-F, [Activity 4](../adjacent-activities.md#activity-4-alternate--reproducible-gpu-research-workflows)

**The proposal, as we understood it.** Put LLM agents to work on two halves of this project:
*development*, meaning agents help build the stage implementations during the month, and
*operations*, meaning agents drive the pipeline — launching sweeps, triaging failures, deciding what
to run next.

**Recommendation in one line:** take the development half now, take exactly one narrow operations
experiment, and decline agent-driven orchestration until after the event.

---

## Why this deserves a serious answer rather than a polite one

Agentic systems were the dominant theme of the 2025 event. Six of the projects we catalogued are
agentic, and four of them sit directly on our stages —
[DynaAgent](../../00-event/interested-parties.md) on S3, LARA-HPC on S6 and S8, F.A.D.E across the
whole funnel, Agent Learn on S7. The global event's own taxonomy files us as an **Action System**
tagged *Agentic Workflows*. Going in with nothing agentic is a position, and it should be a chosen
one.

It also fits our existing framing more neatly than anything else we have been offered.
**An agent at a decision point is another surrogate.** It replaces human judgement the way our
co-folding model replaces structure determination. Our repo already says what a surrogate owes:
[a fidelity contract](../../03-pipeline/fidelity-contracts.md) — stated ground truth, a validation
set containing close calls, an agreement metric, and a trust region.

That is the gap. In the agentic-science work we reviewed, **nobody states a trust region for the
agent.** They report that it worked on a handful of systems. It is the same criticism we already
make of the field's surrogates, pointed at a new object, and it costs us no new machinery to make.

## Why the obvious version does not work

**The arithmetic.** Our pipeline is eight stages. Reliability research this year puts the compounding
cost plainly: at 95% per-step success over 20 dependent steps, end-to-end success is about 36%, and
at 85% over 8 steps it is about 27% `[literature]`. Degradation with horizon is super-linear, and it
is invisible to benchmarks that report single-shot success on short tasks. An agent driving the
whole chain is the worst possible place to put one.

**It collides with a scope boundary we set deliberately.** [ADR-0004](../../adr/0004-snakemake-containers-no-new-infra.md)
and [S8](../../03-pipeline/stages/S8-orchestration.md) say Snakemake plus containers, no additional
distributed systems, and — verbatim — *"If that is insufficient, the correct response is a smaller
run, not more machinery. This is a scope boundary, not a preference."* An agentic orchestration
layer is more machinery. Proposing it is fine; proposing it without amending the ADR is not.

**Irreversible actions on a facility we have not booked yet.** DOE facilities spent this year on
exactly this problem — Oak Ridge ran a session on securing and evaluating agentic AI at scientific
facilities in August `[literature]`. The named hazard is that submitted jobs and instrument actions
cannot be undone, and that generic filters cannot read the semantics of a batch script. Our H200
access is [A2](../../02-scope/open-questions.md), still open, still red. An agent with submit rights
on a shared quota we do not yet have is not a risk we are in a position to take.

**Low differentiation.** If the contribution is "we built an agent that runs a drug discovery
pipeline", it is the fifth one at the event. The trust region is what makes it ours.

## The OSS landscape, and what is actually worth betting on

Judged on fit to *this* programme, utility inside four weeks, and momentum that will outlast the
hackathon.

| Option | Momentum | Fit here | Call |
| --- | --- | --- | --- |
| **MCP** (Model Context Protocol) | Donated to the Linux Foundation's Agentic AI Foundation in Dec 2025; the 2026-07-28 spec is the largest revision since launch, with a stateless core and a Tasks extension for long-running work; ~9.7k servers in the official registry as of May `[literature]` | The interop layer, not a framework. The Tasks extension is the piece that matters for anything queued | **Adopt** for tool exposure. Cheap, reversible, vendor-neutral |
| **AGENTS.md** | Same foundation; 60k+ repositories and 20+ tools as of Dec 2025 `[literature]` | One hand-written file. Nothing to install | **Adopt, but see the caveat below** |
| **OpenTelemetry GenAI semantic conventions** + Langfuse or Phoenix | CNCF SIG; instrument once, route to any backend | Same spine as WP-F's cost telemetry obligation. Agent traces and GPU-seconds in one place | **Adopt** if we do the narrow experiment |
| **Academy** (Globus Labs / Argonne) | Federated agents across HPC, experimental facilities and data repositories; IPDPS 2026 paper; Parsl and Globus Compute underneath `[literature]` | The best *intellectual* fit in the field, and the right constituency — this is the Argonne orbit the event runs in | **Defer, and open a conversation.** It is a distributed system, so it is an ADR-0004 amendment, not a four-week adoption |
| General agent frameworks (LangGraph, CrewAI, AutoGen and successors) | High churn | Nothing here needs a graph runtime that Snakemake does not already give us | **Decline** for the event |

**The AGENTS.md caveat, because it is the most useful finding in this review.** A 2026 study across
138 real-world repositories found that *LLM-generated* context files **reduce** agent task success
while adding over 20% inference cost, and that developer-written files gave only about +4%, and only
when minimal and precise `[literature]`.

Our [CLAUDE.md](../../../CLAUDE.md) is agent-written and long. On that evidence it is more likely to
be costing us than helping us. Worth a measurement before we write another one.

## What to accept

### 1. Agentic development — accept, starts now, no new dependencies

Agents help implement stages during the month, against the frozen interfaces and the contract tests.
This is the safe half and we are already doing it informally.

The guardrail is one we built for other reasons: **the contract tests.** An agent writing code
against a failing test has a ground truth and a stopping condition. That is the whole difference
between this and agentic operations.

Concretely: a short hand-written `AGENTS.md`, and WP-F ships the stub DAG and `make smoke` on the
schedule it already has. Nothing changes in the plan. Cost: zero.

### 2. One operations experiment — accept, narrowly, as an experiment and not as infrastructure

**The acquisition decision at S5 → S6.** Which microstates get sent to the quantum stage.

It is the only genuine judgement call in the pipeline, and it is *already framed as a comparison* —
[S6](../../03-pipeline/stages/S6-quantum-labelling.md) takes top-ranked, high-uncertainty and a
**random control**. Adding an agent makes it a fourth acquisition source measured against the same
control. That is an experiment we know how to run and report.

**Run it on paper first, and spend no labels.** The agent produces a ranked list; we measure its
overlap with the three existing arms and with the control, and we look at where it disagrees. Zero
GPU cost, zero facility risk, and it answers the interesting question — *does it pick differently,
and is the difference informative?* — before anything is committed.

This matters for a boring reason: the label budget is **20–50, a hard ceiling**
`[source-doc]`. Split three ways that is roughly 7–17 per arm. A fourth arm takes it to 5–12, which
is not enough to say anything. **Do not split the budget four ways.** Only if the paper exercise
shows genuine divergence, and only if the budget allows, does the agent arm get labels of its own.

**And it owes a fidelity contract like everything else:**

| | |
| --- | --- |
| **Ground truth** | The acquisition set a competent human picks, plus the random control |
| **Validation set** | The close calls — microstates where the three existing arms disagree |
| **Agreement metric** | Rank overlap with each arm, and label informativeness per selection |
| **Trust region** | Stated explicitly: where it may propose, where it may not, and what it may never do unsupervised |

That last row is the contribution. It is what nobody else writes down.

### 3. Decline, for now

- Agent-driven orchestration of the DAG
- Any agent with job-submission rights on the H200, or on the GB10 boxes during the event
- Academy, or any new agent middleware, inside the four weeks

None of these are bad ideas. They are Phase 2, and two of them need [ADR-0004](../../adr/0004-snakemake-containers-no-new-infra.md)
reopened first.

## How it ties back into the programme

**It belongs in [Activity 4](../adjacent-activities.md#activity-4-alternate--reproducible-gpu-research-workflows),
and it improves that activity's case.** Activity 4 is the RSE and e-research clinic — reproducible
GPU research workflows — currently the alternate, recommended as a half-day. *What does it take to
let an agent operate a research pipeline safely?* is the 2026 form of that clinic's question, it is
the question the RSE community on this campus is being asked right now, and it makes Activity 4 a
genuinely current draw instead of a worthy one. **That is a live input to D2.**

**It gives WP-D a reason to exist for someone who is not a chemist.** WP-D owns S5 and S7 and has no
owner. The acquisition experiment is a statistics-and-ML problem, which widens who we can credibly
ask.

**It does not touch the critical path.** Nothing here is a week-1 item, nothing blocks the three
spikes, and the paper exercise cannot start until the scorer produces rankings in week 3.

**It is a plausible output, but not at the venue you would expect.** The NeurIPS ML4Molecules
workshop in Paris, 13 Dec 2026, explicitly asks for *negative results, careful baselines and
benchmark contributions* — our framing almost exactly. **Its deadline was 29 Aug 2026 and has
passed** `[literature]`. So it is a 2027 target, not an output of this event, and nobody should
plan around it.

## The honest risk

This is exactly the kind of proposal that eats a hackathon. It is interesting, it is current, it
demos well, and it is not the thing we said we would measure. Our own working notes say not to
scaffold code that freezes decisions still open, and the same discipline applies here.

The narrow version survives that test because it spends no GPU time, adds no dependency, and
produces a number either way. **If it starts to need infrastructure, it has stopped being the thing
we approved.**

## D9, for the agenda

> **Do we take agentic development and operations, and at what scope?**
>
> **Recommendation:** yes to agentic development immediately, with a short hand-written `AGENTS.md`.
> Yes to one operations experiment — the S5→S6 acquisition agent, run on paper, owed a fidelity
> contract like every other surrogate. No to agentic orchestration, no to job-submission rights, no
> to new middleware before the event. Fold the topic into Activity 4 and let it argue for itself
> under D2.
>
> **Why:** the pipeline is eight stages and compounding error makes full autonomy arithmetic we
> cannot win. One decision point, measured against a control we already run, is an experiment. The
> trust region is the part nobody else states, and it is the only version of this that is ours.

## Sources

Search-derived, September 2026. Verify before any of this is quoted outwards.

- [Empowering Scientific Workflows with Federated Agents](https://arxiv.org/abs/2505.05428) (Academy; IPDPS 2026) · [project page](https://academy-agents.org/)
- [MCP 2026-07-28 specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/) · [2026 roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) · [adoption figures](https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol)
- [AGENTS.md specification](https://asdlc.io/practices/agents-md-spec/) · [context-file effectiveness](https://aaif.io/blog/measuring-agents-md-what-five-runs-show-that-one-doesn-t)
- [Beyond pass@1: a reliability science framework for long-horizon LLM agents](https://arxiv.org/pdf/2603.29231) · [The long-horizon task mirage](https://arxiv.org/html/2604.11978v1)
- [Securing and Evaluating Agentic AI at Scientific Facilities](https://www.olcf.ornl.gov/calendar/securing-and-evaluating-agentic-ai-at-scientific-facilities-aug-2026/) (OLCF, Aug 2026)
- [Agentic Systems for Molecular Sciences, NeurIPS 2026 workshop](https://moleculediscovery.github.io/workshop2026/)
- [Exploring modularity of agentic systems for drug discovery](https://arxiv.org/pdf/2506.22189) · [OpenFF agentic workflows roadmap item](https://openforcefield.org/about/roadmap/projects/agentic-workflows-drug-discovery/)
