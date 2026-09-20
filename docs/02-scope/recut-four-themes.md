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
| Domain | One funnel, structure to ranking | Systems to pharmacology |
| What we ask of people | Come and take part; on-ramps for non-coders | **Come hands-on with agents and code, in your own area** |
| What it produces | A scoping answer plus a community | The same, framed as the **seed** of a UoA capability |
| Key measure of success | An integrated run, and newcomers who owned a result | **Both, plus group leaders who personally got hands-on** |

The stages do not disappear. They become the interior of themes 1 and 2, where they belong.

## The question

The headline does not change. The domain widens.

> ### How far can a chain of surrogates take us in biomolecular interactions?
>
> Systems · proteins · ligand binding · drug discovery · pharmacology

Same sentence we already argued for, now covering the whole span rather than one funnel. That
matters for continuity: nothing written in the last week has to be thrown away, and people who
already know the pitch still recognise it.

### Why those five words are one chain and not a list

Physiological outcomes come from molecules interacting. Those interactions produce functional
change. Function is driven by spatial and structural change. Pharmacology is the effect of drugs on
that system.

So it reads bottom-up — **structure → interaction → function → physiology** — with the drug entering
at the bottom and its effect read at the top. Selectivity is a structural question with a
physiological answer, and at the moment nobody can carry the signal from one end to the other.

### Two ladders, and they line up

Biology has a scale ladder. ML now has a fidelity ladder that runs alongside it:

| Biology | Model class that claims that rung |
| --- | --- |
| Sequence, phenotype, association | Statistical and association models, language models over sequence |
| Structure, pose, recognition | 3D-aware and equivariant models |
| Atoms, motion, energy | Machine-learned interatomic potentials |
| Cell, tissue, organism | Multi-scale and physics-aware system models |

**The question in every theme is where on the right-hand column you have to be to get an answer you
can trust on the left.** Higher is not automatically better — it is more expensive, and past some
point it stops buying accuracy. Nobody has measured where that point is for any of these rungs.

That is the unifying frame, and it is why the four themes are one experiment: each takes a rung and
asks the same question of it.

### What we are actually trying to build

The four themes let a group go deep in its own field. Linked, they are the start of something UoA
does not currently have.

**Be honest about the noun at each stage, or the promise outruns the result.**

| After | What exists | Call it |
| --- | --- | --- |
| The two days | A working chain across three themes, four worked examples, and a group who have built together | **A seed.** Not a platform |
| Six months | Frozen interfaces, a reusable benchmark, two or three groups still running it | **A capability** |
| Two years, with funding | Something other people at UoA use without us | **A platform** |

Using "platform" in a September invitation to senior people is how the whole thing loses
credibility in the first meeting. The honest recruitment line is the seed, plus a credible route to
the rest.

## What we are asking of people

This is new, and it changes the engagement design.

> **Come and explore the broader opportunity while being hands-on with AI in your own area.**
> Come prepared to work with AI agents and with code, to find out where your own methods are moving
> under the new models.

Two things at once, deliberately. Depth in your own field, and a link into something larger. The
ask is partly introspective — **come and find out what these models are doing to your discipline** —
which is a better reason for a senior person to give up two days than "help us with our pipeline".

### This raises the bar and lowers it at the same time, and we have to say which

Our existing [engagement design](../00-event/engagement.md#the-on-ramps) promises on-ramps for
non-coders and a novice reaching a first result in under 30 minutes. "Come prepared to work with
code" reads like a contradiction, and people will quietly self-select out of it.

The resolution is the point, not a fudge: **agents lower the code bar rather than raising it.** You
do not need to be a programmer. You need to be willing to sit with an agent that writes the code
while you supply the judgement about whether it is right. A pharmacologist who has never written
Python can now contribute working code, and their contribution is the part that was always scarce.

If that is the position, it has to be stated in the invitation in those words, because the default
reading of "come prepared to work with code" is "not for me".

It also promotes the
[agentic development review](../05-delivery/proposals/2026-09-21-agentic-dev-ops.md) from an internal
tooling choice to the **participation model**. That was D9's cautious half — agents for development,
guardrailed by tests — and it is now load-bearing for engagement, which raises its priority.

---

## The measure of success we had not been writing down

**The number of senior research leaders who personally get hands-on.** Not attendance, not the
pipeline result.

Methodological change needs champions. A PI who has produced something themselves becomes one. A PI
who watched a demo does not, however impressed they were on the day.

This also settles how the [seed becomes a capability](#what-we-are-actually-trying-to-build). PIs are
the people who can commit a postdoc, a dataset or a grant line to a follow-on. Every other measure
of success expires when the event ends; this one is the mechanism by which it does not.

### Why the agentic piece is the right door

Not a gimmick, and worth being precise about why it works on this particular audience.

**It removes the disadvantage.** A group leader who last wrote code fifteen years ago is not behind
in a room where an agent writes it. Twenty years of judgement about what a right answer looks like
is worth more than current fluency in a framework.

**The division of labour flatters them honestly.** What the agent lacks is exactly what they have.
That is not a courtesy, it is the actual state of the technology, and senior people can tell the
difference.

**Their real objection is ours too.** A PI's scepticism is not "can it write the code". It is
*"can I stand behind what it produced"*. That is a rigour question, and rigour is what this whole
project is organised around. **The trust region is the pitch.** Come and find out what these tools
can do, from the group that will also tell you where they break. To a senior scientist that is a
credible invitation in a way that enthusiasm is not.

### The barrier nobody names

**A PI will not risk looking incompetent in front of their own group.** Time, scepticism and
competing priorities are all real and all solvable. This one is not, unless it is designed for. Five
rules follow from it:

1. **Never a group leader's first attempt in front of their own students.** Separate session, or
   separate room
2. **Pair PI with PI, across disciplines.** Both equally out of their depth in the other's field and
   equally new to the tool. Nobody is the expert, so nobody loses face
3. **Their own question, prepared beforehand.** CDK9 will not move a physiologist. Their own data
   will. This has to be asked for at invitation time, which means **this week**
4. **Ninety minutes, bounded, with staying optional and clearly legitimate.** A group leader will not
   give two days, and treating the short version as a consolation prize guarantees a no
5. **Show a failure inside the first thirty minutes**

That last one runs against the instinct to make it impressive. A sceptical senior scientist buys
credibility from seeing the limits, not the highlight reel — and showing the limits is the only
version consistent with what we say everywhere else in this repo.

### What we would count

| Measure | Why it is the one to count |
| --- | --- |
| Group leaders hands-on for **an hour or more on their own question** | Hands on keys, not watching. The threshold is arbitrary; the distinction is not |
| How many produced something **in their own domain** | Transfer. A result on our testbed proves nothing about theirs |
| How many commit to a **named follow-on** — a person, a dataset, a date | The real signal. Everything else is a good afternoon |
| How many leave with a founded **"not yet for my problem, and here is why"** | **Counts as success** |

That last row is load-bearing. Without it the measure rewards hype and we end up doing the thing we
criticise every other group for. A PI who leaves with a well-grounded no is a champion of rigour and
will be believed by their peers next time.

### The failure mode

A room of senior people being shown impressive things. They have to type, on their own problem, and
watch it break at least once. If nobody's hands were on a keyboard, it did not happen — whatever the
feedback forms say.

It also changes who hosts. Our [host/owner split](../00-event/engagement.md#the-structural-fix-split-the-host-role)
assumed the newcomer is junior. **A group leader needs a peer-level host**, not a PhD student, and we
do not currently have that role written down.

## Theme 1 · Filter before you dock

**From data-driven screening of ultra-large libraries to physically aware pre-filters ahead of
physics-based docking.**

**Closest to what we already have.** S0–S2 and S5 carry over largely intact. Two things are new: we
run it small to learn the parameter space before scaling, and **model class becomes one of the
things we vary rather than something we pick at the start.**

> **Owns:** *At the top of a very large library, what does a physically aware filter throw away —
> and when does the class of model you chose actually matter?*

| | |
| --- | --- |
| **Communities** | Cheminformatics · virtual screening · ML · industrial medicinal chemistry |
| **Contributes** | The shortlist everything downstream runs on, and the model-class answer the other three themes need |
| **Takes home** | A protocol for measuring recall at the top of a funnel, and an equal-budget comparison across model classes that the field mostly runs unfairly |
| **Compute** | Embarrassingly parallel, GPU-hungry. The best fit for GB10 pre-computation in the month |
| **On-ramp** | Excellent. A newcomer can own one cell of the grid and see what it kept and dropped inside an hour |
| **Interior** | S0, S1, S2, S5 |

### Model class is a hyperparameter

We already argue that [the pipeline is the model and its configuration is the hyperparameter
vector](../04-experiments/hpo-microtopic.md). Model class belongs in that vector. Two axes, and they
are independent:

| | **Sequence / 2D** | **3D-aware** |
| --- | --- | --- |
| **Small, task-trained** | Fingerprint + GBM, small GCNN | Equivariant GNN on the pocket |
| **Large, pretrained** | Protein and molecular language models | Foundation 3D models, MLIP-derived features |

Four quadrants, two questions. **When does 3D earn its cost?** And **when does scale earn its
cost?** The received answer to the second is "the big pretrained model wins", and we have good
reason to think that answer is measured badly.

**Why it is measured badly, and why we are unusually well placed to say so.**
[Lourie et al.](../01-context/source-notes/small-scale-experiments.md) `[literature]`: small-scale
experiments are *more* hyperparameter-sensitive than large ones, and tuning budget dominates every
other methodological choice — 4 configurations give no signal, 64 give a visible one, 256 give an
accurate one. Most published model-class comparisons tune one arm properly and the other arm
hardly at all. That systematically favours whichever class needed less tuning, not whichever class
is better.

**So the experiment is equal tuning budget per quadrant, at two or three data scales, reported with
intervals.** If a well-tuned small GCNN matches a large pretrained model on this task, that is a
real and useful negative, it is cheap to establish, and it is directly actionable for every group
on campus deciding what to run. If it does not, we have quantified what the scale premium buys.

This is the same microtopic we already had, pointed at a more interesting knob. It is also the one
place in the programme where the comparison is cheap enough to run honestly.

*Terminology check: reading PILM as protein-informed / protein language models. If you meant
physics-informed, it lands in the right-hand column instead and the design is unchanged.*

### The honest failure modes

**The filter's error is invisible by construction.** A pre-filter trained on docking scores inherits
docking's errors, and nobody looks at the discards. Recall at the top of a very large library is not
measurable the usual way.

**The trick that makes it measurable.** Spike a known set into a large library and measure recall
directly. Cheap, honest, and rarely done — which is what turns this from a demo into a result.

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

**1. The two ladders.** Each theme takes one rung of the biology ladder and asks how far up the
model ladder it has to climb. Same question, four places. That is what makes it an experiment rather
than a programme of unrelated work.

**2. Every theme is a surrogate, so every theme owes a
[fidelity contract](../03-pipeline/fidelity-contracts.md).** Stated ground truth, a validation set
containing close calls, an agreement metric, and a **trust region**. This is already our discipline
and it generalises without modification.

**3. Every theme has an unmeasured error at its handoff.** T1 discards without measuring recall. T2
extrapolates without knowing it. T3 has no validated link. T4 has no hold-out. Naming that in all
four is the shared methodological contribution.

**4. Start small, explore properly, then scale.** The
[HPO microtopic](../04-experiments/hpo-microtopic.md) applies unchanged to all four, and it is still
the thread that interests people who will never care about CDK9.

**5. A shared testbed.** CDK9 vs CDK7 for T1–T3. Theme 4 brings its own, and can include CDK
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

**The participation bar is the biggest untested assumption.** "Come prepared to work with AI agents
and code" is either the most attractive line in the invitation or the one that halves the response
rate, and we will not know which until it is in front of someone. Test it on two people this week —
one who codes and one who does not — before Wednesday.

**The PI clinic is the most likely thing to quietly become a demo.** It is easier to present than to
facilitate, the room will be polite about it, and we will not find out until the follow-ons do not
happen. The only defence is the hands-on-hours count, taken honestly on the day.

**Two of the four themes are where the domain experts are, and neither is written.** T3 and T4 carry
the systems and pharmacology end of the framing. If they stay empty, the chain is structure and
interaction only, which is the old scope with a new sentence over it.

**Scope.** Four themes is more ambitious than one pipeline, not less, and the two days did not get
longer.

## Decisions this needs

| # | Decision | Recommendation |
| --- | --- | --- |
| ~~R1~~ | Headline retired or generalised? | **Settled.** Generalised — *how far can a chain of surrogates take us in biomolecular interactions?* Same sentence, wider domain |
| **R7** | Do we state the agent-assisted participation model explicitly in the invitation? | **Yes, in those words.** "Come prepared to work with code" without "the agent writes it, you judge it" will lose exactly the domain experts we most need |
| **R8** | What do we call the outcome in recruitment copy? | **A seed, with a route to a platform.** Not a platform. Over-promising to senior people costs more than it wins |
| **R9** | Does T1 run the model-class comparison, or just build the filter? | **Both.** The comparison is the methods result and it is nearly free once the filter exists. Equal tuning budget per quadrant or it is not worth running |
| **R10** | Do we run a dedicated group-leader clinic, separate from the newcomer on-ramps? | **Yes.** Ninety minutes, cross-discipline PI pairs, their own questions, a failure shown early. Mixing it into the general on-ramps loses them |
| **R11** | Do invitations ask each invited PI for one question or dataset from their own area? | **Yes, and it is the reason to delay Wednesday by a day if the copy is not ready.** Without it they arrive with nothing to be hands-on *about*, and the clinic becomes a demo |
| **R12** | Who hosts a group leader? | **A peer.** A senior person or an experienced facilitator from outside their group. This role does not exist in `roles.md` yet |
| **R2** | Four full tracks, or two tracks and two clinics? | **Depends only on headcount.** Set a floor of three people per theme and decide against the actual list |
| **R3** | Does CDK9/CDK7 stay the shared testbed for T1–T3? | **Yes.** It is the only thing preventing four unrelated projects |
| **R4** | Are the T1→T2 and T2→T3 handoffs mandatory or best-effort? | **Mandatory, and schema-frozen in week 2.** Otherwise the recut has no integrated result |
| **R5** | Real genotype data in T4? | **No for the event.** Public and synthetic only. Real data is a separate, properly-partnered piece of work |
| **R6** | Does WP A–F retire? | **A and F survive as shared foundations. B–E retire** into T1 and T2 |

## What I have not done

Only this file. The README, narrative, outreach copy, onboarding ladders, work packages, stage gates
and critical path all still describe the old structure. **Nothing should be re-cut from
`narrative.md` until R2–R9 are settled**, or we will rewrite the recruitment copy twice.

Two that will need real work rather than a find-and-replace:

- **[engagement.md](../00-event/engagement.md) and the six onboarding ladders.** They were designed
  around a promise of zero-code on-ramps. The agent-assisted model does not break that promise, but
  it does change every ladder's first rung, and the 30-minute novice dry run now has to be run with
  an agent in the loop or it tests the wrong thing
- **[hpo-microtopic.md](../04-experiments/hpo-microtopic.md).** Model class joins the hyperparameter
  vector, which is a genuine extension of the argument rather than an edit to it
