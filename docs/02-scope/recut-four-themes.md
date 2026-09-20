# Recut — four themes, four communities

**Status:** top-level cut, for reaction. Nothing else in the repo has been changed yet.
**If adopted:** ADR-0007 plus a restructure of `docs/05-delivery/` and the outreach copy.

---

## What changes

We had one pipeline, six work packages, and four adjacent activities bolted alongside for
engagement. The work was the pipeline; engagement was something we did next to it.

The recut makes them the same thing. **Four themes, each owned by a different research community,
each a real piece of work in its own right.**

| | Before | After |
| --- | --- | --- |
| Top-level unit | 8 stages, S0–S8 | 4 themes |
| Who a unit belongs to | A work package, internal | A research community, named |
| Engagement | 4 activities alongside the work | The themes *are* the engagement |
| Integration | One chain, 8 links | One chain, 3 links, plus one parallel track |
| Testbed | CDK9 vs CDK7 | CDK9 vs CDK7 for T1–T3; T4 brings its own |

The stages do not disappear. They become the interior of themes 1 and 2, where they belong.

## The question, recut

Before: *how far can a chain of surrogates get us?*

That still holds, but it only describes two of the four themes. The generalisation:

> ### Where does a learned model earn the right to replace physics?
>
> Four groups, four scales, one question. Every theme swaps an expensive physical calculation for a
> model that is supposed to stay physically honest. In all four the interesting part is the same:
> **where does it stop being honest, and would you notice?**

The four themes are four answers at four scales — 10⁹ molecules, 10⁴ atoms in motion, one binding
event to a whole system, and a few thousand approved drugs across many genotypes.

---

## Theme 1 · Filter before you dock

**From data-driven screening of ultra-large libraries to physically aware pre-filters ahead of
physics-based docking.**

> **Owns:** *At the top of a ten-billion-compound library, what does a physically aware filter throw
> away — and how would you ever know?*

| | |
| --- | --- |
| **Communities** | Cheminformatics · virtual screening · ML · industrial medicinal chemistry |
| **Contributes** | The shortlist everything downstream runs on |
| **Takes home** | A protocol for measuring recall at the top of a funnel, which nobody can currently do |
| **Compute** | Embarrassingly parallel, GPU-hungry. The best fit for GB10 pre-computation in the month |
| **On-ramp** | Excellent. A newcomer can own a filter and see what it kept and dropped inside an hour |
| **Interior** | S0, S1, S2, S5 |

**The honest failure mode.** A filter trained on docking scores inherits docking's errors, and you
never look at the discards, so the error is invisible by construction. Recall at 10⁹ is not
measurable the usual way.

**The trick that makes it measurable.** Spike a known set into a large library and measure recall
directly. Cheap, honest, and rarely done — which makes it a result rather than a demo.

---

## Theme 2 · Machine-learned potentials in the loop

**Enhanced MD through ML interatomic potentials.**

> **Owns:** *Does an MLIP-driven ensemble change the answer, and where does the potential leave its
> training distribution?*

| | |
| --- | --- |
| **Communities** | Molecular dynamics · computational chemistry · **materials science**, where most of the MLIP community actually lives · quantum chemistry |
| **Contributes** | Ensembles and a refined ranking into Theme 3 |
| **Takes home** | An out-of-distribution protocol for protein–ligand interfaces, which the materials-trained potentials do not have |
| **Compute** | The heaviest of the four. GB10 unified memory is genuinely interesting for larger systems; H200 for throughput |
| **On-ramp** | Moderate. Setup cost is real, but watching a pocket move is a good first hour |
| **Interior** | S3, S4, S6, S7 |

**The honest failure mode.** Foundation MLIPs are trained mostly on small molecules or on materials.
A protein–ligand interface with charged residues, structured water and sometimes a metal is out of
distribution, **and the potential will not tell you that.** It returns a confident number either way.

Our quantum stage is already the instrument for detecting it. That connection is the strongest
piece of continuity between the old plan and this one.

---

## Theme 3 · From a binding event to a system

**Multi-scale modelling with physics-aware ML, from protein–ligand interaction to systems-level
change.**

> **Owns:** *A compound hits CDK9 and partly hits CDK7. What actually happens downstream, and can a
> physics-aware model carry the signal up?*

| | |
| --- | --- |
| **Communities** | Systems biology · quantitative systems pharmacology · mathematical and physiological modelling · toxicology · clinical pharmacology |
| **Contributes** | The reason selectivity matters at all |
| **Takes home** | A worked attempt at the missing link between an affinity number and a phenotype |
| **Compute** | Light. Data- and model-hungry, not FLOP-hungry |
| **On-ramp** | Very good, including for people who do not code |
| **Interior** | New. Nothing in the repo covers this today |

**Why this theme earns its place.** Without it, selectivity is an abstract ranking exercise. CDK9
versus CDK7 matters because of what happens in a normal cell when you hit the wrong one. Theme 3 is
where that becomes a claim instead of an assumption.

**The honest failure mode.** Almost nothing validated connects a binding affinity to a systems
response. It is easy to build a plausible multi-scale model that predicts nothing, and hard to tell
the difference in two days. This theme needs a retrospective anchor — a known on-target/off-target
pair with a documented phenotype — chosen before the event, or it produces a diagram.

**Local fit.** The Auckland Bioengineering Institute does multi-scale physiological modelling as its
core business. That is the obvious first conversation, and it is a group that would not otherwise
come to a drug-discovery event.

---

## Theme 4 · Repurposing on a laptop

**Genotype plus protein structure plus approved drugs, with deliberately lightweight models.**

> **Owns:** *Given a variant, a structure and a few thousand approved drugs, can a lightweight model
> find a plausible repurposing candidate that survives a retrospective hold-out?*

| | |
| --- | --- |
| **Communities** | Bioinformatics · clinical genetics · pharmacy · precision medicine · health data science |
| **Contributes** | Runs alongside. Shares structure preparation with T1 and T2, and shares T2's question — *does a small change in the pocket change the answer?* |
| **Takes home** | A variant-aware repurposing baseline and a hold-out protocol the field mostly skips |
| **Compute** | A laptop. **Deliberately** |
| **On-ramp** | The best in the programme |
| **Interior** | New |

**Why the constraint is the point.** This is the only theme certain to finish inside two days.
Bounded search space — roughly three thousand approved drugs — known structures, and a question a
newcomer can state. If everything else slips, this still produces a result, which is
[design rule 1](../05-delivery/adjacent-activities.md#design-rules-for-these-tracks) working as
intended.

**The honest failure mode.** The repurposing literature is full of predictions that never validated.
Without a time-split retrospective hold-out, this theme produces a story. With one, it produces a
number.

**⚠️ Flag before anyone starts.** If real human genotype data is in scope, data governance and Māori
data sovereignty obligations have to be settled first, in partnership and properly — not as a
compliance step at the end. That is not a two-day conversation and it should not be squeezed into
one. **Recommendation: public and synthetic variant data only for the event**, and treat any real-data
extension as a separate, properly-resourced follow-on.

---

## What holds it together

Four themes is a conference unless something makes it one experiment. Four things do.

**1. Every theme is a surrogate, so every theme owes a
[fidelity contract](../03-pipeline/fidelity-contracts.md).** Stated ground truth, a validation set
containing close calls, an agreement metric, and a **trust region**. This is already our discipline
and it generalises without modification.

**2. Every theme has an unmeasured error at its handoff.** T1 discards without measuring recall. T2
extrapolates without knowing it. T3 has no validated link. T4 has no hold-out. Naming that in all
four is the shared methodological contribution.

**3. Start small, explore properly, then scale.** The
[HPO microtopic](../04-experiments/hpo-microtopic.md) applies unchanged to all four, and it is still
the thread that interests people who will never care about CDK9.

**4. A shared testbed.** CDK9 vs CDK7 for T1–T3. Theme 4 brings its own, and can include CDK
inhibitors so the two halves can still talk.

## The chain, and the risk that comes with it

```
T1 ──shortlist──► T2 ──perturbation profile──► T3
                                                     T4 ──runs alongside──
```

The old claim was that nobody had run the whole 8-stage chain. The recut makes the chain coarser —
three links instead of eight — so **the differentiating claim now lives entirely in those two
handoffs.** If T1 → T2 → T3 does not actually run end to end, we have four good demos and no result.

Mitigation is the same discipline as before: freeze both handoff formats early, the way
[interfaces.md](../03-pipeline/interfaces.md) freezes the current ones. A shortlist schema and a
perturbation-profile schema, agreed in week 2, not on the day.

## What survives, what moves, what is missing

| Asset | Fate |
| --- | --- |
| Fidelity contracts · trust region | **Survives, promoted.** Now the top-level framing across all four |
| Start small / HPO microtopic | **Survives unchanged.** Cuts across all four |
| Provenance tags | **Survives unchanged** |
| Compute plan, GB10/H200 split, budget tooling | **Survives unchanged.** The architecture split is theme-independent |
| CDK9/CDK7 case, the structural figures, `pocket-anatomy.json` | **Survives.** Shared testbed for T1–T3 |
| Stages S0–S8 | **Moves.** Becomes the interior of T1 and T2, not the top-level structure |
| WP A–F | **Recut.** A (benchmark) and F (workflow) become shared foundations serving all four; B/D fold into T1; C/E fold into T2 |
| Stage gates | **Needs recutting.** Six gates were written for one chain. Each theme needs its own, plus two for the handoffs |
| Adjacent activities 1–4 | **Dissolve into the themes.** Activity 2 (small-data HPO) survives as the cross-cutting thread; Activity 4's agentic and reproducibility content attaches to the shared foundation |
| Narrative, outreach copy, onboarding ladders | **Needs re-cutting** from a rewritten `narrative.md`, which is where all recruitment copy comes from |
| **Themes 3 and 4** | **Missing entirely.** No stage page, no work package, no contacts, no compute estimate |

That last row is the real cost of the recut. Half the programme now has nothing written behind it,
four weeks out.

## The honest risks

**People.** Six packages needed 13–20. Four themes plus two shared foundations is not fewer people,
it is the same people spread across more surface. At the low end that is three per theme, which is
one illness away from a theme not happening. Either recruit harder or run two as tracks and two as
clinics.

**Timing.** Invitations were going out Wednesday against the old framing. The recut changes who we
are inviting and what we are inviting them to. Themes 3 and 4 open genuinely new doors — ABI,
clinical genetics, pharmacy — and those are cold contacts with four weeks' notice.

**The sharp question gets blunter.** One sentence is what made the old framing travel. *Where does a
learned model earn the right to replace physics?* is broader and therefore weaker as a recruitment
line. It needs testing on a real person before it goes in an email.

**Scope.** Four themes is more ambitious than one pipeline, not less, and the two days did not get
longer.

## Decisions this needs

| # | Decision | Recommendation |
| --- | --- | --- |
| **R1** | Is the surrogate-chain headline retired or generalised? | **Generalised.** T1→T2→T3 is still a chain of surrogates. Keep the continuity |
| **R2** | Four full tracks, or two tracks and two clinics? | **Depends only on headcount.** Set a floor of three people per theme and decide against the actual list |
| **R3** | Does CDK9/CDK7 stay the shared testbed for T1–T3? | **Yes.** It is the only thing preventing four unrelated projects |
| **R4** | Are the T1→T2 and T2→T3 handoffs mandatory or best-effort? | **Mandatory, and schema-frozen in week 2.** Otherwise the recut has no integrated result |
| **R5** | Real genotype data in T4? | **No for the event.** Public and synthetic only. Real data is a separate, properly-partnered piece of work |
| **R6** | Does WP A–F retire? | **A and F survive as shared foundations. B–E retire** into T1 and T2 |

## What I have not done

Only this file. The README, narrative, outreach copy, onboarding ladders, work packages, stage gates
and critical path all still describe the old structure. **Nothing should be re-cut from
`narrative.md` until R1–R6 are settled**, or we will rewrite the recruitment copy twice.
