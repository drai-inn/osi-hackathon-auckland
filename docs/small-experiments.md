# Small experiments

A thread that runs through all four [themes](themes.md), and the reason the two days can produce
something real.

## The situation

Every theme has a model with settings, an evaluation that costs real time, and no way to
grid-search. Crop radius, microstate count, graph cutoff, model class, theory level. Pick any two
and you already have more combinations than you can run.

This is the same problem as tuning a neural network, with two differences that matter.

1. Several of the settings change **the problem**, not just the search. A 10 Å crop is a different
   physical system from a 15 Å crop.
2. The evaluation is often a **small-sample ranking statistic**. Noisy, bounded, and not smooth in
   the parameters.

## What the literature gives us

From Lourie et al. 2026 `[literature]`:

- **Tuning budget dominates every other methodological choice.** 4 configurations give no signal.
  16 give none. 64 give a visible one. 256 give an accurate one.
- **Small scales are *more* hyperparameter-sensitive than large ones.** This is the counterintuitive
  part, and the reason small-scale results get dismissed as unreliable. They were usually
  undertuned.
- **The mechanism is geometric.** As scale grows, the intrinsic dimension of the loss surface falls,
  so good configurations fill more of the space and become easy to find.
- **The prescription:** explore thoroughly where it's cheap, then carry up with simple rules.

## Why it matters here

Most published model comparisons tune one arm properly and the other hardly at all. That favours
whichever model needed less tuning. **Equal tuning budget per arm** is the cheapest way to make a
comparison mean something, and it's within reach at the scale we're working at.

It also applies to model class. Whether a small well-tuned graph model matches a large pretrained
one is an open question at this scale, and answering it is a couple of days of work rather than a
couple of months.

## What a group can do with it in two days

- Pick two or three settings that matter and sample them randomly rather than in a grid
- Give every arm the same tuning budget, and say what it was
- Report intervals, not point estimates
- Note which settings changed the answer and which didn't

Any group that does this has a result worth presenting, whatever the model did.
