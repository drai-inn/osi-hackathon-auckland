# 📡 Live event log — Auckland Hub

**This file lives on the `live-log` branch and its pull request stays open until the final
presentations and reports are done.**

**To follow:** open the PR and click **Subscribe**. Every update is a commit here — you get those
and nothing else. No issue noise, no CI. **When the PR closes, the work is finished.**

**To post:** commit to `live-log`. Newest at the top. Short, dated, and including what broke. A log
that records only progress isn't worth following.

Cadence: weekly through to October, daily during 19-20 October.

| | |
| --- | --- |
| **Event** | Mon 19 – Tue 20 Oct 2026 · Digital Research Innovation & AI Lab, Level 10, 70 Symonds Street |
| **Register** | Free, through the global event — [luma.com/ku88xh92](https://luma.com/ku88xh92). One registration covers every site |
| **Read first** | [drai-inn.github.io/osi-hackathon-auckland](https://drai-inn.github.io/osi-hackathon-auckland/) |
| **Propose a theme** | [Open an issue](https://github.com/drai-inn/osi-hackathon-auckland/issues/new) |

---

## Status board

Updated with each entry. The honest version.

| | |
| --- | --- |
| **Week** | 22–28 Sep |
| **Shape** | Four themes to start from, and room for any others people bring |
| **🔴 Blocking** | Who we're inviting · no team has committed yet |
| **Hardware** | Goal is at least one model per theme known to start before anyone arrives. Not there yet |
| **Teams** | 0 committed. That's the number that matters now |

---

## 2026-09-22 · Public, and open for teams

**[The site is live.](https://drai-inn.github.io/osi-hackathon-auckland/)** The repo is public under
CC BY 4.0 for the writing and MIT for the code in `tools/`, and
[v26.9.0](https://github.com/drai-inn/osi-hackathon-auckland/releases/tag/v26.9.0) is the first
release. Everything a group needs to decide whether to come is in it.

**Registration is the global event's.** Ben Blaiszik is supportive of our dates and our approach, so
there's no separate local list to join: [one free registration](https://luma.com/ku88xh92) covers
Auckland on 19–20 October and the global days on 21–22 October.

**Four themes, and room for more.** Screening at scale · molecules in motion · binding to whole
system · repurposing what we have. Those four come from where we happen to sit, and the site now
carries two open slots beside them. A group bringing something that belongs elsewhere on the ladder
can [propose a theme](https://github.com/drai-inn/osi-hackathon-auckland/issues/new) and we'll make
space for it. We're creating a room for people to gather; the shape of the room is still open.

**What a group does, in three moves.** Find out what open-weight models exist in your area. Get one
or two running on our hardware. Work out what to measure, and report it back at the end of day one.
The third move is the one we care most about, and it's the one nobody has settled — a recent
benchmark put single-cell foundation models level with a simple linear baseline, and another found
the choice of metric changes which model comes out on top.

**Each group sources its own data and picks its own benchmark.** What keeps groups comparable is
that everyone answers the same four questions about whatever they picked: what's your ground truth ·
what are you comparing against, and is there a simple baseline in there · what would change your
mind · where would it break.

**What this log replaces.** The previous log PR was opened before the event was recut and carried
the old shape with it. It's closed. This one starts where the work actually is. Nothing is lost —
the history is in the repo.

**Open, and honest about it.** No team has committed yet. That's the number that matters between now
and October, and it's the one this log will keep reporting.

---

## Template for an entry

```markdown
## YYYY-MM-DD · Headline

**What landed.**

**What slipped, and why.**

**What we learned.** Including the things that didn't work.

**Numbers.** With a provenance tag: [measured] · [source-doc] · [literature] · [estimate]

**Next.**
```
