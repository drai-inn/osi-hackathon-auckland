# Source note — Lourie, Cho, Ullrich & Lotfi, *"Small-Scale Experiments: Are We There Yet?"*

**Source:** arXiv:2608.11859v1 [cs.LG], 12 Aug 2026. FAIR at MSL Meta + NYU.
**Role in this repo:** this is the *methodological* source. It is about language-model
pretraining, not chemistry. We are borrowing its **experimental discipline**, and we should be
honest about which parts transfer and which do not.

---

## What the paper claims

The promise of scaling laws was cheap experiments: work out what's better at small scale, then
scale up the winner. Six years on, that hasn't landed — the literature found small-scale laws
unreliable below ~100M parameters and concluded you simply need big models. The paper argues the
confounder is **hyperparameters**.

Their findings, in order of usefulness to us:

### 1. Hyperparameter tuning is *the* ingredient `[literature]`

They ablate the standard scaling-law recipe. Parameter-counting conventions barely matter.
Learning-rate decay and per-budget tuning refine the estimate. But tuning **budget** decides
whether there is anything to fit at all:

| Configurations searched per scale | Result |
| --- | --- |
| 4 | Scaling law completely absent |
| 16 | Not yet visible; suboptimal configs inject too much noise |
| 64 | Clearly visible, extrapolation weak |
| 256 | Accurate law |

Their phrasing: uncovering small-scale laws "demands a search far more extensive than most ever
run." **Common practice tunes over a small grid. You may need hundreds of configurations.**

### 2. Scaling laws reach much further down than believed

They observe them from ~4M effective parameters — models that train in under an hour on a single
GPU. The cost argument is compelling: when parameters and data scale together, compute is
quadratic in model size, so one 1B-parameter run costs the same as 64 runs at 134M, 1,024 at 34M,
or 65,536 at 4M.

### 3. Hyperparameter sensitivity *falls* with scale, for a geometric reason

As parameters and data grow, good configurations occupy a larger fraction of the space. The
mechanism is that the **intrinsic dimension of the hyperparameter loss surface goes down** — the
"effective number of hyperparameters" (γ) drops toward one. Parameters drive this more than data.

Consequence, and their central prescription: *small scales require extensive search; large scales
are easy to adapt.* **Explore thoroughly where it is cheap; carry up with simple rules.**

### 4. Extrapolation is statistically fragile

Scaling laws exist at small scale, but extrapolating far beyond the data mostly compares
*estimates of the irreducible error*, which vary wildly across samples. Laws are reliable **near
the data**. Prefer a few well-separated scales (they use three: two to fit, one to validate) over
many nearby ones. A holistic, diagnostic approach beats pure curve-fitting.

### 5. Four diagnostics (their case study: pre-norm vs. post-norm)

| # | Question | Instrument |
| --- | --- | --- |
| 1 | Have we tuned thoroughly? | Does the score distribution approach the **noisy quadratic limit**? A small asymptotic regime signals hyperparameter sensitivity |
| 2 | Will scaling up be easy? | Does the score distribution concentrate near the optimum as scale grows? |
| 3 | Does the cheap proxy still track what we care about? | **Perplexity–capability correspondence**: equal loss ⇒ equal downstream capability (holds across scale, HPs, architecture, tokeniser — breaks if you change the *data*) |
| 4 | Does the regularity emerge at all? | Fit on the small scales, validate on a held-out larger one |

Failure of any diagnostic is itself information — usually about hyperparameters, model, or
implementation.

---

## What transfers to our pipeline, and what does not

This is the part to argue about, not accept.

| Their concept | Our analogue | Transfer confidence |
| --- | --- | --- |
| Search hundreds of configs, not a grid of 4–16 | Random search over the *joint pipeline configuration* (crop radius, states, scorer, theory level, acquisition) | **High** — the argument is about search-space geometry, not about language |
| "Scale" axis = parameters + tokens | Multiple axes: ligand count, poses/states, label budget, scorer capacity. No single compute-optimal frontier | **Medium** — the concept survives, the 1-D frontier does not |
| Sensitivity falls as scale rises; γ → 1 | Open empirical question. Our "scale" is benchmark and label budget, not model capacity | **Untested — this is our headline microtopic** |
| Noisy quadratic limit as a tuning-completeness check | Applicable to any score distribution from random search; needs enough runs to see the tail | **Medium-high** |
| Perplexity–capability correspondence | Does a cheap proxy (pose-scoring loss, held-out ranking) track selectivity enrichment? | **Medium** — must be tested, not assumed; and our data *changes* between tiers, which is exactly what breaks the correspondence for them |
| Extrapolate loss curves to pick a design | Do **not** do this. Our scales span ~2 orders of magnitude at most and our metric is a ranking statistic on ~20 compounds | **Low — explicitly out of scope** |

### The three caveats to keep repeating

1. **Their regime is pretraining from scratch with fixed data.** Ours is fine-tuning and active
   learning on tiny, heterogeneous, partly-wrong data. The perplexity–capability correspondence
   breaks "after changing the pretraining data" — and changing the data is literally what our
   active-learning loop does.
2. **Our headline metrics are small-sample ranking statistics.** With 12–20 ligands, the standard
   error on an enrichment metric is large. Sensitivity analysis must be paired with
   bootstrap/permutation confidence intervals or we will chase noise. See
   [metrics.md](../../03-experiments/metrics.md).
3. **Most of our knobs are not optimiser hyperparameters.** Crop radius and microstate count
   change the *problem*, not just the search. Whether the low-intrinsic-dimension result extends
   to structural pipeline parameters is unknown and worth finding out — that finding would be
   publishable in its own right.

---

## The one sentence to carry into the hackathon

> Build a complete understanding at the small scale by thoroughly exploring the configuration
> space, then use simple rules to carry it up — and treat every assumption that enables this as
> a diagnostic you are obliged to check.
