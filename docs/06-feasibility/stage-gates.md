# Stage gates

Six gates, from the origin document, with thresholds and owners added. `[source-doc]` for gate
and evidence; thresholds are proposals to argue about **before** the hackathon, not after results
exist.

**Pre-specifying thresholds is the whole point.** A gate assessed after seeing the data is not a
gate.

---

| Gate | Minimum evidence required | Proposed threshold | Scale-up implication | Owner |
| --- | --- | --- | --- | --- |
| **1. Technical reproducibility** | Same manifest produces repeatable artifacts and metrics | Clean clone → integrated run reproduces headline metrics within Monte-Carlo error; `provenance.json` complete | Safe to expand candidate count | F |
| **2. Ranking signal** | Known actives and selective compounds rank above decoys/non-selectives more often than baseline | Selectivity Spearman ρ exceeds the 2D baseline, **bootstrap 95% CI on the difference excludes 0** | Proceed to 50–100 ligand pilot | A + D |
| **3. Motion value** | Dynamic/surrogate states improve stability, contact persistence, or explain failure cases | Ranking stability (cross-seed rank correlation) improves over static, CI excludes 0 — **or** a documented failure-case explanation | Include ensembles in pilot; otherwise stay static | C |
| **4. Quantum value** | cuEST labels separate known edge cases or improve calibration | Convergence check passes **and** labels separate known selective from non-selective on the discriminating subset | Use targeted labelling in active learning | E |
| **5. Acquisition value** | High-uncertainty selection outperforms random labelling on error reduction per label | Uncertainty-guided error reduction per label exceeds random control, CI excludes 0 | Scale labels from tens → hundreds → thousands | D |
| **6. Operational cost** | Runtime and failure rate predictable enough for scheduling | GPU-h per label and per complex measured with <2× spread; stage failure rate <10% | Move from exploration to managed campaign | F |

---

## Dependencies between gates

```
Gate 1 (reproducibility) ──► everything. If runs aren't reproducible, no other gate means anything
Gate 4 (quantum value)   ──► Gate 5 (acquisition value). Bad labels make acquisition unmeasurable
Gate 2 (ranking signal)  ──► the scale-up decision. The others are conditional on it
```

Gate 4's convergence sub-check runs on **day 1** because gate 5 cannot be assessed without it.

## Reading the outcomes

| Pattern | Reading | Action |
| --- | --- | --- |
| 1, 2, 6 green; 3, 4, 5 amber | The static 3D pipeline works; the expensive layers are unproven | Phase 2 focused on motion and quantum, not a scale-up |
| 1, 2, 4, 5 green; 3 red | Motion-awareness does not pay for itself on this target class | Drop S3/S4 for kinases. **A genuinely useful, publishable negative** |
| 2 red | The pipeline does not beat 2D on selectivity | Stop. Investigate whether it's the benchmark ([C2](../02-scope/open-questions.md)) or the method |
| 1 red | Not assessable | Fix reproducibility before drawing any conclusion. Do not report results from an unreproducible run |
| 5 red, 4 green | Quantum labels are good; uncertainty-guided selection isn't better than random | Keep quantum, drop active learning. Cheaper and simpler — a real result |
| All green | Proceed to the useful pilot | Phase 3 |

## The failure mode these gates exist to prevent

Not failure — **ambiguity**. The characteristic ending of an exercise like this is "promising
results, more work needed", which is compatible with any underlying reality and licenses
indefinite continuation.

Three habits prevent it:

1. **Thresholds fixed before data.** Argue about them now; they are cheap to change now and
   impossible to change honestly later.
2. **Confidence intervals on every gate metric.** "Better" without an interval, at n≈20, is not
   evidence.
3. **A pre-agreed stop condition.** Gate 2 red means stop. Write down now what we will do if it
   happens, so that the decision is not made by whoever is most invested on day 5.

## Amber

A gate can legitimately be amber: the evidence points the right way but the interval includes
zero. That is the expected outcome for several gates at n≈20, and it is honest.

**Amber means "answerable at the next tier", not "probably fine".** An amber gate produces a
specific, costed experiment for Phase 2 — the sample size needed to resolve it — not a shrug.
