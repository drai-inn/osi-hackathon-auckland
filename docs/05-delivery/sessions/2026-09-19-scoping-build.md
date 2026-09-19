# 2026-09-19 — scoping build

From two source PDFs to a complete scoping repo, event collateral and the first measured numbers.
One month out from the hackathon.

## What got built

| | |
| --- | --- |
| **The science** | Eight stages S0–S8, one page each. Four fidelity contracts. Interfaces frozen enough to build against. Parameter space, metrics, the HPO microtopic |
| **The event** | Narrative, global-event context, engagement design, six onboarding ladders, the interested-parties table |
| **Feasibility** | Compute plan across two architectures, budget, risks, six stage gates, four scale tiers |
| **Collateral** | One-pager, invitations, short-form copy, FAQ, poster, landing page, brand tokens |
| **Tooling** | Manifest validator, compute budget, four schematic figures, three structural ones, four renderer scripts, a 3Dmol viewer |
| **Decisions** | Six ADRs. Thirty-odd open questions with owners and dates |

Six work packages A–F. Three of them — B, C and D — still have no owner and no issues, which is
the single biggest gap going into Monday.

## Framing: four things we tried and dropped

Recorded here because they will otherwise be re-proposed.

**"Two days ahead of the world."** We run 19–20 Oct, the global event runs 21–22. An early draft
made a feature of it. Dropped: we are one local site of sixteen, the offset is a local scheduling
artefact, and nobody outside the organising group will notice or care. We give the global event more
exposure, not less. All "first hub" and "ahead of" language is gone from the copy.

**Evolution shown in the copy.** Strikethroughs, "✅ Resolved", before-and-after narration. Dropped
from every outward-facing document. The reader wants the current state. This directory is where the
evolution lives instead.

**The purpose buried mid-document.** *How far can a chain of surrogates get us?* now leads the
README, the narrative, the one-pager and the poster, in that order, on three legs: hand every
expensive step to a surrogate; measure where that lands as a baseline; get there by starting small.

**The trajectory dropped.** "Start small, then scale" fell out during a rewrite and went back in as
the third leg. It is the methodological commitment ([ADR-0003](../../adr/0003-small-scale-search-before-scale-up.md)),
not a note about resourcing.

## Dates

19–20 October, locked in [ADR-0006](../../adr/0006-run-19-20-october-as-a-precursor.md). We cannot
run past the 21st, and the 21st already has overlapping agendas. Extending into it is a call made on
the day, not a plan.

## Numbers established

All reproducible. Nothing here is an estimate unless it says so.

| | |
| --- | --- |
| CDK9 vs CDK7 / CDK12 / CDK13, kinase region | 44.1 / 46.2 / 50.0 % identity |
| The same pair across 18 ATP-site positions | 72.2 / 72.2 / 66.7 % |
| CDK8 vs CDK19 at the ATP site | **100 %** — a harder pair, same family |
| Residues within 5 Å of flavopiridol in CDK9 | 20 |
| Positions where CDK9 differs from all three counter-targets | **2** — Cys106 at the hinge, Ala153 on the floor |
| Crop radius 4 → 15 Å | 153 → 1,067 heavy atoms, ≈339× on a cubic scaling `[estimate]` |
| First cyclin T1 residue inside the crop | 18 Å — outside every radius we are considering |

**Cys106 was predicted, then confirmed.** The sequence pass flagged a cysteine at the CDK2-Leu83
equivalent position, unique among the four, and noted that positions were mapped by sequence
alignment and were indicative only. The structural pass — CEalign, nearest Cα — put it at 3.2 Å from
flavopiridol with methionine in all three counter-targets. Guess first, then check. Worth repeating
for anything else that comes out of a sequence alignment.

**All four targets have structures, at better resolution than expected.** CDK12 at 2.2 Å and CDK13
at 2.0 Å beat CDK9's own 2.8 Å. Not guaranteed going in.

## Things the tooling got wrong before it got them right

Each of these would have put a wrong claim in front of people.

- **TPO drawn as a ligand.** It is the activation-loop phosphothreonine, part of the chain. In gold
  next to the real ligand it read as a second binding event
- **Crystallographic copies leaking.** A neighbouring copy's ADP floated in the CDK12 and CDK13
  panels looking meaningful. Fixed with a 10 Å proximity filter to the chain being drawn
- **1UA2 captioned "apo kinase".** It has ATP bound
- **A chain-break threshold that did not scale with zoom.** Fixed at 34 px, so past about 9 px/Å
  every backbone segment looked like a break and the trace silently vanished
- **Compute-budget tables drifting from the tool.** Reconciled to actual output. They are generated
  by hand and will drift again — see the note in [CLAUDE.md](../../../CLAUDE.md)
- **An emoji in a heading.** Broke the anchor, and the link checker that should have caught it was
  itself collapsing multiple spaces to one hyphen where GitHub emits one per space

## Positioning

Against 88 documented projects from the 2025 event: the pieces exist separately — UMADock,
DynaAgent, F.A.D.E, DFTPilot, LARA-HPC, ACME — but nobody assembled the cascade with budget
discipline. Not one states a trust region. Nobody reports parameter sensitivity with intervals.
"Selectivity" appears once in the whole paper.

A warm route to Valence Labs exists: Michael Craig was on the 2024 kickoff panel. Relevant to
unblocking B3.

## Open at the end of the session

- **WP-B, WP-C and WP-D have no owner and no issues.** Three of six parallel phases unrepresented
- Two board views still to add in the Projects UI — group by work package, group by gate week. Not
  settable from the CLI
- PDB files need caching locally before the event so the viewer works offline at the venue
- The email to Ben Blaiszik — our dates, what a site on other dates can still join, the Valence
  Labs introduction — drafted in outline, not sent
- [C7](../../02-scope/open-questions.md) opened late: the crop drops the cyclin, and the cyclin holds
  the αC helix. Nobody has checked whether that matters

## Conventions that got set here

Worth knowing because they are enforced by review, not by a linter.

- **Every number carries a provenance tag.** Untagged is a bug
- **Every figure regenerates from a script.** No screenshots, no hand-posed renders
- **Every structural figure carries a PDB ID, a fetch date and the command**
- **All recruitment copy is cut from [narrative.md](../../00-event/narrative.md)**, not written twice
- **The weave motif sits with clear air above and below**, never inline with other decoration
