# FAQ

For the micro-repo, and for the six questions you will otherwise answer individually forty times.

---

**Do I need to know anything about drug discovery?**
No. Several roles need the opposite — someone who will ask why we are doing it that way. Only
Activity 1 (benchmark curation) assumes chemistry.

**Do I need to be able to code?**
No. Pose triage and benchmark critique involve no code at all. The "own a configuration" on-ramp is
one command, and someone will be sitting next to you.

**I've never done anything with AI. Is this for me?**
Yes, and we have designed for it specifically. Within the first hour you will own one configuration
of the pipeline — one command, about twenty minutes, and your run appears on the shared dashboard as
a data point in the final analysis. Not a training exercise; the actual experiment, which needs
many configurations and is better with a room of people each running one.

**What do I need to bring?**
A laptop. Everything runs on our hardware. We spend the month beforehand making sure nothing needs
installing on the day — that is the whole reason the month exists.

**Two days is a lot. Is there a smaller version?**
Three levels:
1. **Full participant** — both days, embedded in a team
2. **Clinic participant** — 90 minutes on day 1 plus the day-2 closing session
3. **Reviewer** — read the plan, tell us what is wrong with it, come to the close

Level 3 costs an hour and is how several of the most useful contributions will arrive.

**What's the actual science?**
Most drugs fail on selectivity, not potency. We are building a staged pipeline where fast AI models
do the volume work and GPU quantum chemistry is spent only where it changes the answer, and testing
it on CDK9 versus CDK7 — two kinases similar enough that conventional methods cannot separate them.
Full version: [narrative.md](../docs/00-event/narrative.md).

**What if it doesn't work?**
Then we will know in two days rather than two years, which is the point. Six gates were written
before any data existed. **A clean "no" is a successful outcome.** The result we are actually trying
to avoid is the ambiguous one that lets a project drift forward on optimism.

**What hardware?**
Dual NVIDIA GB10 boxes, ours continuously for the month beforehand and during the event, plus HGX
H200 access for benchmarks and batch work. GB10 is the participant-facing machine on the day, so
your first run will not queue behind someone's sweep.

**Is this part of something bigger?**
Yes — the 4th annual global Open Scientific Intelligence Hackathon runs 21–22 October. 16 hubs
across 4 continents, 1000+ participants in 2025, 120 projects, and a paper each year crediting
every team.

**We run two days ahead of it, on 19–20 October.** That is deliberate: we finish sixteen hours
before the earliest hub in the world opens, so what we build is available to every other hub from
the moment they start. If you want to keep going, Wednesday the 21st is the global event's opening
day and you can roll straight into it.

**Will I be an author on anything?**
If we submit a project, the global write-up credits every team member. The 2025 paper documented 88
projects and listed every contributor. No promises about journals, but the track record is there.

**Who owns what we build?**
Open source by default. See {{LINK}} for specifics — and if IP matters to you, ask before the event
rather than after.

**Can I join remotely?**
The global event has an online hub, and yes. But the Auckland-specific value is the room: the
conversations between a medicinal chemist and an ML person are most of the point and do not happen
over chat.

**Can I bring a student / a colleague / my own problem?**
Yes to all three. The small-data clinic is explicitly a bring-your-own-problem session — if you have
an expensive experiment and a pile of parameters you cannot afford to explore, that is the session.

**I'm not at the University of Auckland.**
Still welcome. Email njon001@aucklanduni.ac.nz.
