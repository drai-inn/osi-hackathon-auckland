# ADR-0001 — Staged multi-fidelity funnel over a single model

**Status:** accepted · **Date:** 2026-09-19 · **Deciders:** Nick Jones

## Context

The obvious alternative to this whole architecture is: take the best available 3D binding-affinity
model, fine-tune it on selectivity data, and use it. Simpler, fewer moving parts, one thing to
debug.

The origin document argues against it: the discriminating signal for paralog selectivity lives in
local geometry, induced fit, electrostatics and conformational ensembles, and no single model
available today captures all four at a cost that permits screening. `[source-doc]`

## Decision

A **staged funnel** with monotonically increasing cost per candidate: cheap AI surrogates handle
volume, expensive physics is spent only where it buys information. Each stage is permitted to be
wrong in a characterised way; the next stage corrects the errors the previous one is known to make.

Corollaries:
- Roles are the design; model choices are implementation. Boltz-2, Nesso-1, MACE and cuEST occupy
  roles and are swappable behind interfaces.
- Every surrogate carries a [fidelity contract](../03-pipeline/fidelity-contracts.md).

## Alternatives considered

| Option | Why not |
| --- | --- |
| Single fine-tuned 3D affinity model | Cannot express ensemble or electronic effects; no mechanism for targeted high-fidelity enrichment |
| Physics-first (FEP on everything) | Orders of magnitude too expensive; different question (absolute affinity, not selectivity ranking) |
| 2D/QSAR with selectivity labels | This is our **baseline**, not our method. If it wins, that is the result |

## Consequences

**Good:** expensive methods used where they pay. Stages developed in parallel. Each stage
independently measurable and swappable. Negative results are localisable to a stage.

**Bad:** integration risk (→ [R5](../06-feasibility/risks.md)). Errors compound across stages.
More people needed. Six interfaces to maintain.

**Revisit if:** the static baseline ([S1](../03-pipeline/stages/S1-complex-generation.md) →
[S2](../03-pipeline/stages/S2-pocket-extraction.md) → [S5](../03-pipeline/stages/S5-equivariant-scoring.md))
captures essentially all the signal. Then the funnel's extra stages are unjustified complexity and
we should say so.
