# Ladder B · Domain expert — chemistry, pharmacology, structural biology

**For you if:** you know molecules, assays or structures. You may or may not code, and it doesn't
much matter — **your judgement is the input, not your code.**

The honest framing: there are two or three points in this project where a wrong call by the
computational team would invalidate everything downstream, silently, and nobody would notice until
the write-up. Those calls are yours.

---

## Rung 0 · Orient — 15 minutes

Read the **[problem statement](../../01-context/problem-statement.md)** — one page on why
selectivity is the hard part and why 2D methods fail at it.

Then skim **[S0 Benchmark](../../03-pipeline/stages/S0-benchmark.md)**, and specifically its
**failure modes** section. If your reaction is "yes, and also…", write that down. It is exactly
what we need.

**You now know:** what we're claiming and where it could go wrong chemically.

## Rung 1 · First contact — 30 minutes · *before the event, by email, or day 1*

Pick whichever you'd rather:

- **Five poses.** We show you five predicted CDK9 complexes. Plausible, implausible, uncertain, and
  a line on why. That's it. See
  [on-ramp B](../engagement.md#b--pose-triage--structural-biology-medicinal-chemistry--zero-code)
- **The harmonisation question.** We have CDK9 and CDK7 activity data from multiple sources at
  different ATP concentrations. Tell us what can legitimately be compared. See
  [C1](../../02-scope/open-questions.md) and
  [data-sources.md](../../06-feasibility/data-sources.md)

**Why this is not busywork:** the pose annotations become the ground truth for
[fidelity contract 1](../../03-pipeline/fidelity-contracts.md#1-co-folding-s1--replaces-experimental-structure-determination),
which we cannot produce computationally. The harmonisation answer determines whether our headline
metric means anything at all.

## Rung 2 · Contribute — half a day · *day 1*

**[Break the benchmark](../engagement.md#c--break-the-benchmark--medicinal-chemistry-pharmacology--60-min).**
We hand you the 2D baseline's predictions. You find the compounds it gets wrong for reasons a
chemist would call obvious.

Every hit is a benchmark improvement and a slide. This directly attacks
[R2](../../06-feasibility/risks.md) — the highest probability-times-impact risk in the register,
and the one most likely to go unnoticed until after the write-up.

Also at this rung:
- **Decoy strategy.** Property-matched, DUD-E-style, or literature non-selectives? The easy choice
  makes the benchmark meaningless ([C2](../../02-scope/open-questions.md))
- **Activity cliffs.** Which of our pairs are real cliffs and which are assay noise? Those are the
  discriminating cases and they look like errors

## Rung 3 · Own — day 2

- **Own the benchmark's limitations statement.** One page: what this benchmark can and cannot
  support. It goes in the write-up and it is the difference between a citable asset and a CSV
- **Sit on the gate assessment.** [Gate 2](../../06-feasibility/stage-gates.md) is "does the ranking
  mean anything?" and it needs someone who can say whether the compounds that moved should have
- **Sanity-check the result.** If the pipeline ranks something highly that you know is wrong, that
  is the most valuable sentence spoken on day 2

## Rung 4 · Carry — afterwards

- **Co-author the benchmark release.** There is a real gap here: a curated, documented,
  honestly-caveated CDK selectivity benchmark. Other groups would use it
- **Bring your own target.** The pipeline is target-agnostic. If you have a selectivity problem
  that matters more than CDK9, phase 2 could be yours
  ([C-series questions](../../02-scope/open-questions.md))
- **Stay as the chemistry reviewer.** Ongoing, low-commitment, and the project is materially worse
  without one

---

## What we will get wrong without you

Stated plainly, because it's the reason to come:

1. **Comparing incomparable assays.** Two IC50 values at different ATP concentrations don't form a
   valid selectivity ratio. Get this wrong and we spend a week optimising against an artefact
2. **Trivially separable decoys.** If our negatives differ in molecular weight, a 2D model scores
   0.95 and the whole 3D apparatus has proved nothing
3. **Treating activity cliffs as noise** when they are the discriminating cases
4. **Believing predicted poses** because the model reports high confidence and most of these
   structures are in its training data
