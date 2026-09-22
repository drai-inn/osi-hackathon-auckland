# Working notes for AI agents in this repo

## What this is

The team repo for the **Auckland site of the Open Scientific Intelligence Hackathon 2026**, a
global, multi-site event now in its fourth year.

**Mon 19 – Tue 20 Oct 2026.** The global event runs 21–22 October.

The question: **how far can a chain of surrogates take us in biomolecular interactions?** Systems,
proteins, ligand binding, drug discovery, pharmacology. Four themes to start from, each taking one
rung of that ladder, plus two open slots on the site and in the README for anything that belongs
somewhere else. See [ADR-0007](docs/adr/0007-four-themes-invited-teams.md) for the shape and why.

Registration is the **global event's** — one free sign-up covers every site, ours included. There is
no local registration and no local email address anywhere in the public assets; questions go to
issues. Don't reintroduce a personal contact address.

This is an invitation, not a project specification. We deliberately do not define the work in
advance, because the groups who turn up bring their own problems and their own expertise. **Resist
the urge to specify.** If something reads like it is closing down a choice a participant should
make, it is probably wrong for this repo.

## Structure

Flat on purpose.

| | |
| --- | --- |
| `README.md` | The front door |
| `docs/narrative.md` | The pitch. **All recruitment copy is cut from here** — rewrite it there and re-cut |
| `docs/themes.md` | The themes, the open-weight models worth a look in each, and how to propose one |
| `docs/taking-part.md` | What the two days are like, and the four questions every group answers |
| `docs/worked-example.md` | A CDK selectivity problem, ready to pick up |
| `docs/compute.md` | Dual GB10 and an HGX H200 |
| `docs/small-experiments.md` | Learning a parameter space when every run is expensive |
| `docs/figures/` | **Data.** Drawn from deposited coordinates by a script, and regenerable. Never hand-edit an SVG |
| `docs/cards/`, `outreach/imagery/` | **Collateral.** Generated backgrounds, mood rather than measurement |
| `docs/adr/` | Decisions |
| `outreach/` | The collateral, and the brand |
| `tools/` | Generators and the link checker |

## Hardware, which affects everything

**Dual GB10 is `aarch64`. The HGX H200 is `x86_64`.** Anything containerised has to build for both.
This is the most commonly missed constraint here, and the one piece of pre-work that agents cannot
fix on the day: at least one model per theme has to be known to start on our hardware before anyone
arrives. See [compute.md](docs/compute.md).

## Conventions

**Provenance tags on every number.** `[measured]` someone ran it · `[source-doc]` from the origin
documents · `[literature]` published, cited · `[estimate]` a guess, flagged as one. An untagged
number is a bug.

**Every figure regenerates from a script.** No screenshots, no hand-posed renders. Structural
figures carry their PDB ID, the date fetched and the command.

**Collateral is held to a different standard, and the line matters.** Theme-card backgrounds and
`outreach/imagery/` come from a diffusion model, so they cannot be regenerated deterministically and
they will draw chemistry that looks right and is not. They carry mood. Anything a reader could take
as a measurement belongs in `docs/figures/` and comes from data. Do not move an image across that
line without saying so.

**Run `make check` before committing.** It checks every relative link and anchor, and it has a
self-test because GitHub's anchor rule is easy to get subtly wrong.

## Tone

Written for a mixed-discipline audience: chemists, physicists, statisticians, systems biologists,
clinicians, RSEs. Assume intelligence, not shared vocabulary.

Keep the language plain and positive. Say the thing once and move on. **Avoid the contrastive
construction** — "not X, it's Y", "that sounds like A and it's the opposite", "the point isn't P,
it's Q". It reads as sales and it is the main thing to watch for in drafts.

Be concrete about what is not known. This repo is more useful for being honest about its gaps than
it would be for sounding confident.

## History

There was a pre-pivot version of this repo built around an eight-stage pipeline, six work packages
and named owners. It was removed on 21 Sep. It is in the git history and in
[PR #15](https://github.com/drai-inn/osi-hackathon-auckland/pull/15) if anything needs pulling
back. Do not reintroduce work packages, owners, hosts, stage gates or a central benchmark team.
