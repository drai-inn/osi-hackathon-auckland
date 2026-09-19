# Open Scientific Intelligence Hackathon — Auckland Hub

### Can AI tell two near-identical drug targets apart?
**{{DATES}} · {{VENUE}} · University of Auckland · Free**
*Part of the 4th annual global OSI Hackathon — 16 hubs, 4 continents, 1000+ participants*

---

## The problem

Most drugs fail on **selectivity**, not potency. A compound designed for one protein hits its close
relatives too, and the programme dies late and expensively. Conventional screening cannot separate
them, because it flattens a 3D pocket into a fingerprint and throws away exactly what makes two
pockets different: geometry, motion, electrostatics.

## What we're building

A staged pipeline where **fast AI models do the volume work** — predicting structures, sampling how
pockets move, scoring geometry — and **GPU quantum chemistry is spent only where it changes the
answer**. Four times in that chain a learned model stands in for something expensive, and every one
of them has to declare where it may be trusted.

Driving case: **CDK9 against CDK7** — two kinases so similar that telling them apart is the whole
problem.

## The question underneath

A pipeline like this has eight configurable choices and nobody can afford to explore them at scale.
So everyone guesses. Recent work suggests that is precisely the mistake — that small experiments
fail to transfer not because they are small but because they are **undertuned**.

> **When does what you learn from a small experiment actually predict the large one?**

Ecology with one field season. Clinical work with small cohorts. Materials with slow synthesis.
That question is not ours alone, which is why this is a cross-disciplinary event.

## Who we need

| | What you'd do |
| --- | --- |
| **Medicinal chemistry / pharmacology** | Break our benchmark. Find the compounds our baseline gets wrong for chemically obvious reasons |
| **Structural biology** | Triage predicted poses. Tell us which are nonsense — we cannot do this without you |
| **Quantum chemistry / physics** | When is a cheap approximation good enough, and how would you know? |
| **Statistics / ML** | Bring your own small-data problem. Twenty samples, eight parameters, no budget |
| **Research software engineering** | Make a multi-stage GPU pipeline someone else can actually run |
| **New to all of this** | Own one configuration. One command, twenty minutes, your name on a data point in the final analysis |

## What you get

- **Two days on real hardware.** Dual GB10 boxes and HGX H200 access, and a pipeline that already
  works when you walk in — we spend the month beforehand building it so you don't spend the event
  installing things
- **A result with your name on it.** Every participant's contribution lands in an artifact
- **A route to publication.** The 2025 event produced a 120-project paper crediting every team
- **Prize eligibility** and the global showcase
- **A room full of people from other disciplines** who have the piece you're missing

## Why Auckland

New Zealand is the first time zone. **We are the first hub in the world to start** — sixteen hours
before the US sites wake up. What we build goes into the global event's first morning.

## Commit as much or as little as you like

1. **Full participant** — both days, embedded in a team
2. **Clinic participant** — 90 minutes on day 1, plus the day-2 presentations
3. **Reviewer** — read the plan, tell us what's wrong with it, come to the closing session

---

**Register:** {{REGISTER}} · **Details:** {{LINK}} · **Contact:** Nick Jones, njon001@aucklanduni.ac.nz

*A clean "no" is a successful outcome. We have six gates written before any data exists, and if the
method doesn't work we would like to find that out in two days rather than two years.*
