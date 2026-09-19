# Ladder C · Machine learning and statistics

**For you if:** you model things for a living. The chemistry is not the draw — the methodology is,
and you may have your own version of the same problem.

**The pitch in one line:** we're testing whether a claim about small-scale experiments, made this
August in the language-model literature, holds in a completely different domain.

---

## Rung 0 · Orient — 20 minutes

Read the **[source note on Lourie et al.](../../01-context/source-notes/small-scale-experiments.md)**
— our distillation, with a transfer table saying which of their claims we think carry over and
which don't.

The short version: thorough configuration search is the single ingredient that determines whether
small experiments transfer. Four configurations showed nothing. Sixteen showed nothing. 256 gave a
clean predictive answer. And counterintuitively, **small systems are more sensitive to their
configuration than large ones**, because the intrinsic dimension of the loss surface falls with
scale.

**You now know:** the claim we're testing, and our doubts about it.

## Rung 1 · First contact — 30 minutes · *before the event*

**Read [hpo-microtopic.md](../../04-experiments/hpo-microtopic.md) and tell us where it breaks.**

Genuinely. It is a design, not a result, and it has at least three weaknesses we know about
(listed at the foot under *Honest risks*) and probably more we don't:

- Our "scale" axes are benchmark size and label budget, not model capacity. The geometric argument
  may not transfer at all
- Several of our parameters change the *problem*, not just the search — a 10 Å crop is a different
  physical system, not a differently-tuned one
- Two scale tiers is thin for any claim about a trend, and three may not be affordable
- At n≈20 ligands, between-configuration variance may be dominated by resampling variance

Send us one paragraph. That is a real contribution and it costs half an hour.

## Rung 2 · Contribute — half a day · *day 1*

Pick one:

- **[Bring your own problem](../engagement.md#e--bring-your-own-small-data-problem--visiting-researchers-statisticians-any-empirical-field--90-min)**
  to the clinic. Map your expensive experiment onto our search-space spec. You leave with a protocol
  for your own work; we get a second domain to test the claim against. Both sides win and it takes
  90 minutes
- **Own the statistical protocol.** Bootstrap over ligands, paired comparisons on shared resamples,
  permutation tests against baseline, pre-registration. It's all specified in
  [metrics.md](../../04-experiments/metrics.md#statistical-protocol) and it needs someone who will
  actually enforce it when the results are exciting
- **Run the variance decomposition.** Functional ANOVA over the random search, with intervals. This
  is the answer to *which parameters actually matter*, which is question one of the three the event
  must answer

## Rung 3 · Own — day 2

**Own a diagnostic.** There are four
([methodology.md](../../04-experiments/methodology.md#4-diagnostics-over-extrapolation)):

| | Question | Instrument |
| --- | --- | --- |
| D1 | Have we searched enough? | Does the score distribution approach the noisy quadratic limit? |
| D2 | **Will scaling up be easy?** | Does sensitivity fall as the tier rises — the headline question |
| D3 | Does the cheap proxy track what we care about? | Correlation across configurations |
| D4 | Does it hold out of sample? | Fit on the small tier, validate the ordering on the next |

**D2 is the one to take** if you want the interesting problem. A negative — sensitivity does *not*
fall with scale in this pipeline — invalidates the "start small, scale up" strategy for this class
of problem, and is more publishable than a marginal enrichment improvement.

Also on day 2: be the person who says a difference of 0.05 on twenty compounds is nothing. Someone
has to, and it is easier for an outsider.

## Rung 4 · Carry — afterwards

- **The methods note.** A two-page, discipline-agnostic protocol: search-space spec, random-search
  driver, variance-decomposition report, four diagnostics. Nothing in it is chemistry-specific, and
  it is plausibly a paper on its own
- **Your own domain.** If the clinic worked, run it properly on your data. We'd like to know what
  happened
- **Phase 2 design.** Every amber gate becomes "what sample size would resolve this?", which is a
  question for you

---

## The caveats we already know about

We would rather you arrive knowing these than discover them and conclude we hadn't thought about it.

1. **Their regime is pretraining from scratch with fixed data.** Ours is fine-tuning and active
   learning on tiny, heterogeneous, partly-wrong data. The perplexity–capability correspondence
   breaks when the data changes — and our active-learning loop changes the data. That's the sharpest
   disanalogy in the whole design
2. **Our metric is a small-sample ranking statistic**, not a smooth loss. Noisy, bounded,
   non-differentiable in the parameters
3. **We will not afford 256 full-pipeline configurations.** We concentrate the budget on the cheapest
   stage (scoring) and accept weaker conclusions elsewhere. Whether stage effects are separable
   enough for that to work is itself an assumption, checked by the integrated run
