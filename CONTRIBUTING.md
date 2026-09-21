# Contributing

## What this repo is for

Inviting people to the Auckland site of the [Open Scientific Intelligence Hackathon](docs/the-global-event.md),
and holding the small amount of shared material the two days need.

It is deliberately light. The work gets defined by the groups who turn up.

## The nature of the thing

A hackathon. Two days, four [themes](docs/themes.md), project teams bringing their own problems.
People work in ones, twos and threes on whatever they have taken on. Nobody is assigned.

A few things we hold to:

- **No stupid questions.** Most of us are new to most of this.
- **It's safe to experiment.** Breaking something is a result.
- **A negative is a result.** "We tried it, here's where it fell over" is useful to everyone.
- **Show the thing, not the slides.**

## Before you send a pull request

```bash
make check
```

Checks every relative link and anchor in the markdown. It has a self-test, because GitHub's anchor
rule is easy to get subtly wrong.

## House rules

**Numbers carry a provenance tag.** `[measured]`, `[source-doc]`, `[literature]` or `[estimate]`.
An untagged number is a bug.

**Figures regenerate from a script.** `make cards` and `make figures`. Never hand-edit an SVG.
Structural figures carry their PDB ID, the date fetched and the command that made them.

**Recruitment copy is cut from [narrative.md](docs/narrative.md).** Rewrite the pitch there and
re-cut, so the versions stay together.

**Decisions that change scope get an [ADR](docs/adr/).** Use `0000-template.md`.

**Keep it plain.** Say the thing once. Watch for the contrastive construction — "not X, it's Y" —
which creeps into drafts and reads as sales.

## The live log

[EVENT-LOG.md](EVENT-LOG.md) lives on the `event-log` branch as a single open pull request. Anyone
can subscribe to it and get every update and nothing else. It closes when the final presentations
and reports are done.

To post: commit to `event-log`. Newest at the top, dated, short, honest, including what broke.

## Licence

Contributions are accepted under the repository's licences: [CC BY 4.0](LICENSE) for documentation,
copy and imagery, MIT for code in `tools/`. If you contribute something you did not write, say where
it came from.

## Questions

Nick Jones · njon001@aucklanduni.ac.nz · or open an issue.
