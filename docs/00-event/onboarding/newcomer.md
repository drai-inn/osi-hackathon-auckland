# Ladder A · New to AI for science

**For you if:** you're good at something else, you're curious about this, and you've never built
anything with AI. Possibly you're not sure you belong here.

You do. The event is designed around that fact, not in spite of it, see
[engagement.md](../engagement.md). Everything below assumes no prior experience, and every rung
has a named person whose job is to unstick you.

---

## Rung 0 · Orient, 10 minutes

Read **[the short versions](../narrative.md#the-short-versions)** at the foot of the narrative.
Three paragraphs. If the one-sentence version makes sense to you, you have enough.

Then skim the **[glossary](../../02-scope/glossary.md)**, not to learn it, just so you know it
exists when someone says "equivariant" at you.

**You now know:** what we're doing and why anyone cares.
**Stop here if:** it turns out not to be for you. That's a real outcome and it cost you ten minutes.

## Rung 1 · First contact, 30 minutes · *before the event or in the first hour*

**Run one configuration of the pipeline.**

Your host gives you a config ID. One command on a GB10 box. About twenty minutes later your run
appears on the shared dashboard with your name on it.

That run is **a data point in the day-2 analysis**. It is not an exercise, the experiment genuinely
needs many configurations, and a room of people each owning one is a better use of the room than a
queue script. See
[on-ramp A](../engagement.md#a-your-run-your-parameter--anyone-including-non-coders--20-min).

**You need:** a laptop. Nothing installed.
**Someone is beside you:** your work package's host.
**If it takes more than 30 minutes**, that's a broken on-ramp, not you. Say so, we test this in
[week 4](../../05-delivery/critical-path.md) precisely so it doesn't happen.

**You now have:** a result with your name on it, and a working mental model of what the pipeline does.

## Rung 2 · Contribute, half a day · *day 1*

Pick one:

- **Run a small sweep.** Three or four configurations instead of one, varying one parameter. You
  now have an opinion about whether that parameter matters, which is
  [the whole question](../../04-experiments/hpo-microtopic.md)
- **Take a second on-ramp** that uses what you already know:
  [pose triage](../engagement.md#b-pose-triage--structural-biology-medicinal-chemistry--zero-code)
  if you have any structural intuition,
  [break the benchmark](../engagement.md#c-break-the-benchmark--medicinal-chemistry-pharmacology--60-min) if you have any chemistry
- **Be the person who asks.** Sit in on a work package's explainer and write your questions on the
  surprises board. Assumptions survive inside a subfield because everyone shares them; the useful
  questions come from outside

All three land in the output. None require you to write code.

## Rung 3 · Own, day 2

Own a slice of the analysis. Concretely, one of:

- **Present your parameter.** Two minutes in the day-2 session: what you varied, what happened,
  what the interval was. You will be the person in the room who knows that parameter best
- **Own a figure.** One plot in the final write-up, with your name on it
- **Run the sealed-forecast reveal.** Collect the day-1 predictions, score them, present who called
  it. Ten minutes of prep, and it's the most enjoyable slot of the day

## Rung 4 · Carry, afterwards

- **Your name is in the artifacts**, and if we submit to the global event's write-up, in the paper
- **Take the method home.** The [small-data protocol](../../04-experiments/hpo-microtopic.md) is
  discipline-agnostic. If your own research has an expensive experiment and too many settings, it
  applies directly, that's [Ladder C](ml-stats.md)
- **Come back for phase 2**, if the [gates](../../06-feasibility/stage-gates.md) go green
- **Wednesday 21 Oct** is the global hackathon's opening day. You can keep going

---

## Things that are true and worth saying

**You will not be the only person who doesn't know what's going on.** Six disciplines are in the
room and nobody understands more than two of them. The medicinal chemist doesn't know what an
equivariant network is; the ML person doesn't know what a gatekeeper residue is. Asking is the
normal state.

**No one debugs alone.** Fifteen minutes stuck is a host's failure. Say something at minute
fourteen.

**The two-minute rule.** At standup, explain yesterday to someone outside your discipline in two
minutes. If you can't, that's a finding about the work, not about you.

**A clean "no" is a successful outcome.** If the method doesn't work we want to know in two days.
You are not here to make it succeed; you're here to help find out.
