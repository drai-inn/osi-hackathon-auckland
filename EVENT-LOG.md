# 📡 Live event log — Auckland Hub

**This file lives on the `live-log` branch and its pull request stays open until the final
presentations and reports are done.**

**To follow:** open the PR and click **Subscribe**. Every update lands here as a commit and as a
comment on the PR, so you can read it without opening a diff. **When the PR closes, the work is
finished.**

Updates are weekly through to October, then daily on 19–20 October. Each one has to earn its place:
if it wouldn't change what you do, it isn't here.

| | |
| --- | --- |
| **Event** | Mon 19 Oct, 10am – Tue 20 Oct, 4pm · Digital Research Innovation & AI Lab, Level 10, 70 Symonds Street |
| **Register** | Two free steps — the [Auckland RSVP](https://forms.cloud.microsoft/r/JQCAFqHdZ4), then [the global event's](https://luma.com/ku88xh92) |
| **Read first** | [drai-inn.github.io/osi-hackathon-auckland](https://drai-inn.github.io/osi-hackathon-auckland/) |
| **Propose a theme** | [Open an issue](https://github.com/drai-inn/osi-hackathon-auckland/issues/new) |

---

## Status board

Updated with each entry. The honest version.

| | |
| --- | --- |
| **Week** | 28 Sep – 4 Oct |
| **Shape** | Four themes to start from, and room for any others people bring |
| **🔴 Blocking** | Who we're inviting · no team has committed yet |
| **Hardware** | Goal is at least one model per theme known to start before anyone arrives. Not there yet |
| **Teams** | 0 committed. That's the number that matters now |

---

## 2026-09-28 · Registering takes two steps now, and we have start times

**Registering changed, and the old instruction was wrong.** There are two steps and you need both:

1. **[RSVP for Auckland](https://forms.cloud.microsoft/r/JQCAFqHdZ4)** — name, email, what you work
   on, which days you're coming, and whether you'd rather join remotely.
2. **[Register with the global event](https://luma.com/ku88xh92)** — the one that makes your project
   visible to the judges.

Both are free. If you signed up before today you did step 2 only, so the Auckland RSVP is still
outstanding. It takes a minute.

**Start and finish times.** **10am Monday 19 October to 4pm Tuesday 20 October**, Level 10, 70
Symonds Street. Come for one day or both. Joining remotely is fine, and the RSVP asks which.

**How submitting works, now confirmed with the organisers.** Judging is the global event's, and so
is the submission: you submit through their site and their judges see it there. Nothing gets handed
to us. Plan for a video of two minutes or less posted somewhere public, one form for the team, and
a public repo with a real description. In 2025, **32 of 120** submissions were left out of the
community paper for incomplete documentation `[literature]` — the write-up deserves the last hour
of day two rather than the last ten minutes.

**The submission deadline is not set yet.** It falls at the end of the global day 2, 22 October,
after our two days are done, which is deliberate: you finish on the 20th with the write-up still
ahead of you. The organisers say the date goes to their Slack first. Their submission page still
shows last year's date, so don't take it from there.

**Nobody has committed a team yet.** Four themes to start from and two open slots beside them, so
the shape of the room is still yours to change. If what you want to work on doesn't fit any of the
four, [propose a theme](https://github.com/drai-inn/osi-hackathon-auckland/issues/new) and we'll
make space for it.

**What we don't know yet.** The submission deadline, and whether every theme has a model known to
start on our hardware — dual GB10 is `aarch64` and the H200 is `x86_64`, and getting at least one
model per theme running before anyone arrives is the pre-work we're doing now. Both will be in the
next update.

---

## 2026-09-22 · Public, and open for teams

**[The site is live.](https://drai-inn.github.io/osi-hackathon-auckland/)** The repo is public under
CC BY 4.0 for the writing and MIT for the code in `tools/`. Everything a group needs to decide
whether to come is in it.

> **Superseded on 28 Sep:** registration is now **two steps**, an Auckland RSVP and the global
> event's. The paragraph below described one step, which was right at the time and is wrong now.

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

**Open, and honest about it.** No team has committed yet. That's the number that matters between now
and October, and it's the one this log will keep reporting.

---

## Template for an entry

Before posting, answer this: **would someone deciding whether to come, or working out what to
bring, do anything differently for having read it?** If not, it doesn't belong here. Releases,
build fixes, tooling and our own process are backstage.

```markdown
## YYYY-MM-DD · Headline

**What changed for you.**

**What to do about it.** Nothing is a fine answer.

**What we don't know yet.** And when we expect to know.
```

Numbers carry a provenance tag: `[measured]` · `[source-doc]` · `[literature]` · `[estimate]`.
