# Ladder F · Stage owner

**For you if:** you've agreed to own a work package. This is the shortest ladder and the steepest -
you're not being onboarded so much as handed a scope.

**Your first week matters more than your event days.** Two days cannot absorb a build
([ADR-0006](../../adr/0006-run-19-20-october-as-a-precursor.md),
[ADR-0005](../../adr/0005-two-tier-compute-gb10-h200.md)).

---

## Rung 0 · Orient, 30 minutes

1. **[Your stage page](../../03-pipeline/stages/)**, purpose, inputs, outputs, parameters, metrics,
   failure modes, candidate software, first-day task
2. **[interfaces.md](../../03-pipeline/interfaces.md)**, what you owe downstream and what you can
   assume from upstream. Frozen on 2 Oct; object before then
3. **[Your work package](../../05-delivery/work-packages.md)**, dependencies and dated obligations
4. **[critical-path.md](../../05-delivery/critical-path.md)**, which week we're in

**You now know:** your scope, your deadlines and your interfaces.

## Rung 1 · First contact, this week

**File three questions.** As issues, or on the surprises board. Not "is this right?", specifically:

- One thing on your stage page that is **wrong**
- One thing that is **missing**
- One number that is `[estimate]` and that **you could measure** this week

Every stage page was written without its owner. They are drafts with opinions, and the fastest way
to make yours real is to disagree with it in writing.

## Rung 2 · Contribute, weeks 1 to 3

Hit your dated obligations in
[work-packages.md](../../05-delivery/work-packages.md#these-were-day-1-obligations-now-they-are-month-obligations).
The recurring pattern is: **measure the real cost, replace an `[estimate]`, make the stage run once
on real data.**

Two things that are easy to defer and shouldn't be:

- **Your [fidelity contract](../../03-pipeline/fidelity-contracts.md)**, if your stage has a
  surrogate. Ground truth, validation set containing close calls, agreement metric, trust region.
  Complete it *before* your output is used downstream, not after
- **Your pre-registration page.** One page: primary question, primary metric, comparison, threshold.
  Before data. It's the difference between a finding and a story at n≈20

## Rung 3 · Own, the event

- Drive your package's work. **You are not the host**, someone else owns the newcomers attached to
  you, and that separation is deliberate
  ([why](../engagement.md#the-structural-fix-split-the-host-role)). In a two-day sprint you would
  choose the technical work every time, and nobody would have done anything wrong
- Post your score distributions at end of day 1 so the methodology lead can start the sensitivity
  analysis overnight
- Present your gate evidence on day 2, **with intervals**
- Write your section of the handoff package live, 15:30–16:30, with the room present

## Rung 4 · Carry, afterwards

- **Your stage's write-up section**, and co-authorship on whatever comes out
- **Phase 2 scope for your stage**, if your gate came back amber, what sample size would resolve it
  and what would it cost?
- **Hand your stage over cleanly** if you're not continuing. The stage page is the handover document;
  keep it current

---

## The five things that will trip you up

1. **Building before interfaces are frozen.** Integration happens once, on day 2
2. **Reporting a point estimate.** At n≈20 a metric without an interval is not a result
3. **Skipping the control** because it obviously won't win. The random-acquisition control sometimes
   wins, and when it does, that's the result
4. **Deferring your fidelity contract** until after the surrogate is in use
5. **Treating the month as optional.** It is the project
