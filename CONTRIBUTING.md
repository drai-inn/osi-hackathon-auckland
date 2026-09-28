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

[EVENT-LOG.md](EVENT-LOG.md) lives on the `live-log` branch as a single open pull request. Anyone
can subscribe to it and get every update and nothing else. It closes when the final presentations
and reports are done.

**A sync never travels alone.** People subscribed to that pull request get a notification for every
commit on the branch, so a bare "bring the live log up to date with main" spends their attention
and tells them nothing. Three things make an update, and they happen together or not at all:

1. the branch is synced with `main`, which keeps the pull request's diff honest
2. a dated entry goes into `EVENT-LOG.md`, which is the record
3. the same text is posted as a pull request comment, which is what reaches a subscriber as prose
   rather than as a commit subject

**A release is the unit.** Cut the tag, write the entry, then run it in one pass:

```
make update ENTRY=entry.md RELEASE=v26.9.6 ROW='Week=28 Sep – 4 Oct'
```

`ROW` updates any `| **Name** | value |` row, which is how the status board and the header table
stay current instead of drifting. `DRY=1` shows you what would be pushed and posted without doing
either. For more than one row, call [tools/post_update.py](tools/post_update.py) directly — `--row`
is repeatable there.

**The bar: would a participant act differently for having read it?** Someone deciding whether to
come, or working out what to bring, or planning their two days. If the answer is no, it doesn't go
in the log. Releases, build fixes, tooling, repo mechanics and our own process are all invisible to
the people subscribed — they are backstage, and the log is not.

Newest at the top, dated, short, honest. A log that records only progress isn't worth following,
so say what isn't known and what has slipped **where that affects a participant** — whether a model
will be running on the hardware, whether a deadline has moved. Not whether a build passed.

The shape of an entry follows from the bar:

```markdown
## YYYY-MM-DD · Headline

**What changed for you.**

**What to do about it.** Nothing is a fine answer.

**What we don't know yet.** And when we expect to know.
```

## Licence

Contributions are accepted under the repository's licences: [CC BY 4.0](LICENSE) for documentation,
copy and imagery, MIT for code in `tools/`. If you contribute something you did not write, say where
it came from.

## Questions

[Open an issue](https://github.com/drai-inn/osi-hackathon-auckland/issues/new).
