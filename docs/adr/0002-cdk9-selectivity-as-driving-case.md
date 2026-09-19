# ADR-0002 — CDK9 paralog selectivity as the driving case

**Status:** accepted · **Date:** 2026-09-19 · **Deciders:** Nick Jones

## Context

A scoping exercise needs one concrete problem. Too easy and the pipeline's value is invisible; too
hard and everything is within noise; too obscure and there is no data to build a benchmark from.

## Decision

**CDK9 vs. CDK7 / CDK12 / CDK13.** `[source-doc]` Minimum viable: CDK9 + one close counter-target.

Reasons:
- **Genuinely hard.** Highly similar ATP sites — exactly the regime where 2D methods fail and 3D
  should help. If our method cannot beat 2D here, the thesis is wrong.
- **Data exists** for all four across ChEMBL/BindingDB and the PDB — a benchmark is buildable in
  the time available.
- **Known selective and known pan-CDK compounds exist**, giving real discriminating cases rather
  than actives-vs-random-decoys.
- **Real consequences.** Selectivity failure in this family has therapeutic-window implications,
  so the question is not a toy.

## Alternatives considered

| Option | Why not |
| --- | --- |
| A cryptic or allosteric pocket | Closer to the method's unique strength, but too little data for a benchmark in a week |
| A PROTAC ternary system | Very high scientific interest; far more moving parts than a hackathon supports |
| A standard public benchmark (DUD-E, LIT-PCBA) | Measures hit-finding, not selectivity. Wrong question |
| A broader kinase panel | More data, but the discrimination becomes easy and the result uninformative |

## Consequences

**Good:** data available; a real and recognised problem; discriminating negatives exist; results
are interpretable to medicinal chemists.

**Bad:** kinase-specific conclusions may not generalise to the cryptic/allosteric cases that
motivated the approach. **State this limitation explicitly in every write-up.** Also: these
structures are well-represented in every model's training data, so memorisation is a live concern
(→ [R7](../05-feasibility/risks.md)).

**Revisit if:** the CDK family turns out to be separable by 2D methods alone (→ gate 2 red for a
benchmark reason rather than a method reason), or a partner brings a target with better
characteristics.
