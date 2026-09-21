# ADR-0007 — Four themes and invited teams

**Date:** 2026-09-21 · **Status:** accepted · **Supersedes:** ADR-0001 through ADR-0004

## Context

The repo was built around one pipeline of eight stages, six work packages with named owners, and
four adjacent activities alongside for engagement. Recruitment was going to ask individuals to fill
roles in a project that was already specified.

Two problems. The specification was detailed enough to turn away the people we most wanted, who have
their own problems and their own expertise. And the pipeline framing covered structure and
interaction but stopped short of systems and pharmacology, which is where the question gets
interesting.

## Decision

Four open themes, and we invite project teams.

The question widens to **how far can a chain of surrogates take us in biomolecular interactions** —
systems, proteins, ligand binding, drug discovery, pharmacology. Biology has a ladder of scales and
machine learning now has one alongside it. Each theme takes a rung.

Themes are notional. A group brings its own problem and its own data, or takes the worked example.
In each theme the work is the same three moves: find the open-weight models, get one or two running
on our hardware, work out what to measure and report it back.

No owners, no hosts, no work packages, no central benchmark or workflow team. Setup is agentic
support plus the core team.

## Consequences

Comparability comes from every group answering the same four questions about its own benchmark,
reported at the end of day one, rather than from a shared dataset.

Four loose themes produce a portfolio. That is a weaker scientific claim than one integrated chain,
and it is the trade we took: engagement and curiosity ahead of prescription, for a first year.

ADR-0001 through ADR-0004 described the pipeline architecture and are superseded. ADR-0005 (compute)
and ADR-0006 (dates) still hold.

The pre-pivot documents are removed rather than archived. They are in the git history and in
[PR #15](https://github.com/drai-inn/osi-hackathon-auckland/pull/15) if anything needs pulling
back.

One piece of pre-work survives: at least one model per theme has to be known to start on our
hardware before anyone arrives. That is architecture-dependent, so agents cannot fix it on the day.
