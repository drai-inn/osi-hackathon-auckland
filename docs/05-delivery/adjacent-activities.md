# Adjacent activities — the cross-disciplinary tracks

**Purpose:** give researchers from adjacent disciplines a genuine reason to be in the room — one
where their expertise is load-bearing, not decorative — and where they leave with something
useful to *their* field.

Four are described. **Pick three.** The choice depends on who we can actually get
([A3](../02-scope/open-questions.md), [A5](../02-scope/open-questions.md)) and should be made
before invitations go out, not after.

## Design rules for these tracks

1. **Each must be independently valuable.** If the pipeline fails on day 2, each track still has a
   deliverable worth the participants' time. Nobody's week should be contingent on our success.
2. **Each feeds a work package and is fed by one.** Parallel but not disconnected.
3. **Each has an artifact that outlives the hackathon** — a dataset, a protocol, a toolkit, a note.
4. **Each has a 90-minute "clinic" format** that a visiting research leader can attend without
   committing to the full event. This is the low-commitment door in.

---

## Activity 1 — Selectivity benchmark clinic

**Disciplines:** medicinal chemistry · pharmacology · structural biology · cheminformatics · research data management
**Feeds:** WP-A · **Fed by:** everyone who needs the manifest
**Central question:** *What does a defensible selectivity benchmark actually look like, and can
we build one in a week?*

The intellectual content is not data-wrangling, it is **measurement validity**. Kinase IC50s from
different labs at different ATP concentrations are not comparable; selectivity ratios computed
across them are artefacts. Deciding what *can* legitimately be compared is a genuine
medicinal-chemistry and pharmacology judgement, and it is the kind of judgement that computational
people routinely get wrong on their own.

**Sessions**
- Assay harmonisation clinic — what can be pooled, what corrections are defensible
- Decoy design — property-matched vs. DUD-E vs. literature non-selectives, and why the easy
  choice makes the benchmark meaningless
- Activity-cliff triage — the discriminating cases, not the noise
- FAIR/provenance — how this becomes a citable, reusable asset

**Artifact:** a curated, documented, publicly releasable CDK9-selectivity benchmark with an
explicit statement of what it can and cannot support. There is a real gap here; a good one would
be used by other groups.

**Hook for a visiting leader:** "Come and tell us why our benchmark is wrong, before we build a
week of results on top of it." That invitation is usually accepted.

---

## Activity 2 — Small-data hyperparameter science

**Disciplines:** statistics · machine learning · applied mathematics · *and any empirical field
with expensive experiments*
**Feeds:** all work packages · **Fed by:** all work packages
**Central question:** *When does what you learn from a small experiment transfer to the scale you
care about?*
**Detail:** [hpo-microtopic.md](../04-experiments/hpo-microtopic.md)

The widest net in the programme, because the question is not about chemistry. Ecologists with one
field season, clinical researchers with small cohorts, materials groups with slow synthesis,
education researchers with one cohort a year — all have a configurable pipeline, an expensive
evaluation, and no ability to grid-search. Our pipeline is a convenient testbed for a question
they all have.

**Sessions**
- Why small-scale experiments are *harder* to tune than large ones, and the geometry behind it
  ([Lourie et al.](../01-context/source-notes/small-scale-experiments.md))
- Random search vs. grids: why grids fail above three dimensions
- Bring-your-own-problem clinic — participants map their own pipeline onto the search-space spec
- Live sensitivity analysis on the hackathon's own results

**Artifact:** a discipline-agnostic protocol note + a small toolkit (search-space spec format,
random-search driver, variance-decomposition report, the four diagnostics). Plausibly a methods
paper.

**Hook:** "We will run the experiment that tells you whether your small pilot was informative."
This is the track most likely to bring in people who would never attend a drug-discovery event,
and therefore the most valuable for the stated goal of engaging other research leaders.

---

## Activity 3 — The fidelity ladder: quantum, surrogates, and knowing when to trust them

**Disciplines:** quantum chemistry · computational physics · numerical analysis · uncertainty quantification
**Feeds:** WP-C, WP-E · **Fed by:** WP-B, WP-D
**Central question:** *When is a cheap approximation good enough, and how would you know?*

Four surrogates sit in this pipeline, each replacing something expensive
([the cascade](../03-pipeline/architecture.md#the-surrogate-cascade)). The general problem —
multi-fidelity modelling with a validation obligation — is shared with climate modelling,
engineering simulation, astrophysics and numerical weather prediction. Everyone builds these
ladders; few write down the trust region.

**Sessions**
- The fidelity contract as a design pattern ([fidelity-contracts.md](../03-pipeline/fidelity-contracts.md))
- Multi-fidelity and delta-learning: theory and what actually works at n=30 labels
- Convergence and error cancellation in pocket-shell quantum calculations
- Trust regions and out-of-distribution detection for learned potentials

**Artifact:** a filled-in contract for each of the four surrogates, plus a reusable template. Plus,
concretely, the quantum convergence study — which is the load-bearing check of the whole hackathon
and a legitimate piece of computational chemistry in its own right.

**Hook:** "Your surrogate has a correlation coefficient. Does it have a trust region?" Lands with
anyone who has had a fast approximation fail in the one regime that mattered.

---

## Activity 4 *(alternate)* — Reproducible GPU research workflows

**Disciplines:** research software engineering · e-research / HPC · MLOps
**Feeds:** WP-F · **Fed by:** all
**Central question:** *What does it take to make a multi-stage GPU research pipeline that someone
else can actually run?*

The least glamorous, arguably the highest institutional value: the answer generalises to every
GPU-using group on campus, and the RSE/eResearch community is a real and underused constituency.

**Sessions**
- Snakemake + containers + Kubernetes GPU jobs: a working pattern, not a lecture
- Provenance that survives: image digests, weight hashes, config resolution
- Cost telemetry as a first-class output — measuring GPU-seconds per scientific unit
- Reproducibility clinic: clone-to-smoke-test on someone else's laptop

**Artifact:** a reusable template repo for GPU research pipelines at UoA, plus this project's
reproducibility report.

**Recommendation:** run this as a **half-day clinic rather than a full track** if team size is
tight. WP-F must happen regardless; the question is only whether it is also an engagement vehicle.

---

## Choosing three

| If the priority is… | Take |
| --- | --- |
| Scientific credibility of the result | 1, 3, and 2 |
| Breadth of disciplines engaged | 1, 2, and 4 |
| Building durable institutional capability | 2, 3, and 4 |
| **Default recommendation** | **1, 2, 3** — with 4 as a half-day clinic |

The default protects the two things most likely to invalidate the project (a bad benchmark,
untrustworthy surrogates) while giving the methodological thread the room to become something
publishable. Activity 4's work happens regardless under WP-F.

## Running them across two days

The event is **Mon 19 – Tue 20 Oct**, so the clinics compress and most of each activity's substance
has to be prepared during the month.

- **Day 1, 10:00–11:30:** the three clinics run in parallel as
  [on-ramps](../00-event/engagement.md#the-on-ramps). Activity 1 is on-ramp C, Activity 2 is on-ramp E,
  Activity 3 runs as a working session on the pre-computed convergence study.
- **Day 1 afternoon – Day 2 morning:** participants embed in their linked work package.
- **Day 2, 14:30:** each activity presents its artifact — **separately from the pipeline result**,
  so a disappointing pipeline result does not bury three good pieces of work.

**What this means for the month:** an activity whose material is prepared on the day will not
happen. Activity 1 needs the 2D baseline browsable (week 2); Activity 3 needs the convergence study
finished (week 3); Activity 2 needs the search-space spec and a worked example (week 3).

## Invitation framing

Do not invite people to "a drug discovery hackathon". Invite them to the question their discipline
owns:

> *"We are running a week-long experiment on whether small-scale computational experiments can
> predict what happens at scale. The testbed is drug selectivity prediction, but the question is
> yours as much as ours. We would like you to own the part that your field is better at than we
> are."*
