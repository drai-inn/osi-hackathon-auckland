# Invitation templates

Seven, by audience. Each opens with **the question that discipline owns**, not with ours, a
medicinal chemist has no reason to attend "a hackathon", and every reason to attend an argument
about whether your benchmark is valid.

Keep them short. The [one-pager](one-pager.md) carries the detail.

---

## 1 · Medicinal chemistry / pharmacology → [Activity 1](../docs/05-delivery/adjacent-activities.md#activity-1--selectivity-benchmark-clinic)

> **Subject: Come and tell us our selectivity benchmark is wrong**
>
> Dear {{NAME}},
>
> We're running the Auckland hub of the global Open Scientific Intelligence Hackathon on
> {{DATES}}, building a pipeline that tries to distinguish CDK9 from CDK7, two kinases similar
> enough that most computational methods can't.
>
> The whole thing rests on a benchmark, and we are acutely aware that we could get it wrong in a
> way that invalidates everything downstream without anyone noticing. Two IC50 values measured at
> different ATP concentrations don't form a valid selectivity ratio. Property-matched decoys are
> the honest choice and the harder one. If our negatives are trivially separable, a 2D model scores
> 0.95 and we've proved nothing.
>
> These are your judgements, not ours. We'd like you to make them before we build a week of results
> on top.
>
> Concretely: a 90-minute clinic on day 1, or both days if you're interested. There's also an
> hour-long session where we hand you our baseline's predictions and ask you to find the compounds
> it gets wrong for reasons a chemist would call obvious, every hit improves the benchmark.
>
> One-pager attached. Happy to talk it through.
>
> Nick

## 2 · Structural biology → on-ramp B

> **Subject: 200 predicted binding poses, and nobody qualified to judge them**
>
> Dear {{NAME}},
>
> At the Auckland OSI Hackathon ({{DATES}}) we'll be generating predicted protein–ligand complexes
> for CDK9 and CDK7 using open-weight co-folding models, then scoring them.
>
> The models are confident. That's the problem. We have no way to tell a memorised pose from a
> generalised one, and most CDK co-crystals are in these models' training data, so a good RMSD may
> mean nothing at all.
>
> We'd like you to look at them and tell us which are nonsense. No code: a viewer, a
> plausible/implausible/uncertain button, and a box for why. Your annotations become the ground
> truth for our validation, and they're something we genuinely cannot produce computationally.
>
> An afternoon, or the full two days if you'd like to stay.
>
> Nick

## 3 · Statistics / ML / any field with expensive experiments → [Activity 2](../docs/05-delivery/adjacent-activities.md#activity-2--small-data-hyperparameter-science)

*The widest net. Send this one broadly, the recipient needs no chemistry at all.*

> **Subject: When does a small experiment actually predict the large one?**
>
> Dear {{NAME}},
>
> A question you may recognise: you can afford the small version of your experiment. Under what
> conditions does what you learn from it transfer to the scale you actually care about?
>
> Work published this August argues the usual answer is wrong. Small-scale experiments fail to
> transfer not because they are small but because they are **undertuned**, and, counterintuitively,
> small systems are *more* sensitive to their configuration than large ones. Searching four
> configurations showed nothing; sixteen showed nothing; 256 gave a clean predictive answer. Most
> published small-scale results, on this account, are not wrong so much as under-explored.
>
> We're testing whether that holds in a completely different domain. Our testbed is a drug-target
> selectivity pipeline with eight configurable choices, an expensive evaluation, and no ability to
> grid-search, structurally the same problem as yours, whatever yours is.
>
> The Auckland hub of the global OSI Hackathon, {{DATES}}. There's a 90-minute clinic where you map
> your own pipeline onto our search-space format and leave with a protocol for your own work, and
> you're very welcome to stay for the two days and help us answer it properly.
>
> No chemistry required. If anything, an outside view is what the session is for.
>
> Nick

## 4 · Quantum chemistry / physics / UQ → [Activity 3](../docs/05-delivery/adjacent-activities.md#activity-3--the-fidelity-ladder-quantum-surrogates-and-knowing-when-to-trust-them)

> **Subject: Your surrogate has a correlation coefficient. Does it have a trust region?**
>
> Dear {{NAME}},
>
> We're building a multi-fidelity pipeline with four learned surrogates in it, one replacing
> structure determination, one replacing MD, one replacing physics-based scoring, one replacing
> running DFT on everything.
>
> Our concern is the failure mode where a surrogate correlates beautifully overall and is
> systematically wrong on precisely the close calls the pipeline exists to resolve. Everyone in
> multi-fidelity modelling has met this. Few of us write down where the approximation stops being
> allowed.
>
> At the Auckland OSI Hackathon ({{DATES}}) we're making that a hard rule, no surrogate enters
> without a stated ground truth, a validation set containing close calls, and an explicit trust
> region. We'd like your help making those honest rather than decorative.
>
> There's also a real piece of computational chemistry in it: a convergence study on pocket-shell
> DFT, does the *ordering* of known selective and non-selective pairs survive the cheap theory
> level, and do the energies plateau with shell size, or are we amputating real interactions?
>
> Nick

## 5 · RSE / eResearch / HPC → [Activity 4](../docs/05-delivery/adjacent-activities.md#activity-4-alternate--reproducible-gpu-research-workflows)

> **Subject: A GPU research pipeline someone else can actually run**
>
> Dear {{NAME}},
>
> Short version: we have dual GB10 boxes for a month and H200 access for benchmarks, a six-stage
> containerised GPU pipeline to build across both, and an `aarch64`/`x86_64` split between the two
> machines that will bite us in week three if we get it wrong.
>
> You have opinions about all of this. We'd like them.
>
> The Auckland hub of the global OSI Hackathon, {{DATES}}. The artifact is a reusable template for
> GPU research pipelines at UoA. Snakemake, multi-arch containers, provenance that survives, and
> cost telemetry as a first-class output. That generalises to every GPU-using group on campus.
>
> There's real work in the month beforehand too, if you want it.
>
> Nick

## 6 · Newcomer to AI for science → on-ramp A

*Warmer, shorter, and makes one concrete promise.*

> **Subject: Two days, real GPUs, and a result with your name on it**
>
> Hi {{NAME}},
>
> We're running Auckland's hub of a global AI-for-science hackathon on {{DATES}}, and I'd like you
> to come.
>
> You don't need to have done this before, that's rather the point. Within the first hour you'll
> own one configuration of our pipeline: one command, about twenty minutes, and your run appears on
> the shared dashboard as a data point in the final analysis. Not an exercise. The actual
> experiment, which needs many configurations and is better with a room of people each running one.
>
> If you'd rather use what you already know, there are other ways in, looking at predicted
> molecular structures and telling us which are wrong, or going through our benchmark for the
> things a chemist would spot.
>
> Everything will already be working when you arrive; we spend the month beforehand making sure of
> it. Bring a laptop, that's all.
>
> Nick
>
> *We're a local site for the global Open Scientific Intelligence Hackathon, which runs 21-22
> October with registration open to anyone. Worth signing up for that too.*

## 7 · Tier-1 cold email to a previous hackathon participant

*For the four people in [interested-parties.md](../docs/00-event/interested-parties.md#tier-1-directly-adjacent-work).
Send four of these, not forty. Read their project first, the specificity is the whole message.*

> **Subject: {{THEIR_PROJECT}}, we're building the next stage of it in Auckland**
>
> Dear {{NAME}},
>
> I've been reading {{THEIR_PROJECT}} from the 2025 OSI Hackathon, {{ONE_SPECIFIC_THING}}.
>
> We're running the Auckland hub this year, building {{OUR_OVERLAPPING_THING}}. {{THEIR_WORK}} is
> the closest existing thing to it that I've found, and we'd rather learn from what you hit than
> rediscover it.
>
> Would you spend 30 minutes with our team during the event? We're on {{DATES}} NZDT, which is
> {{THEIR_LOCAL_TIME}} for you, and a few days before the global event, so it might be a convenient
> slot.
>
> Happy to send our plan beforehand; it's fairly detailed and we're not precious about it.
>
> Nick Jones, University of Auckland

---

## Follow-up, one week later, once only

> Hi {{NAME}}, following up briefly on the hackathon on {{DATES}}. No pressure at all if it's not
> the right time; if it's the format rather than the topic, there's a 90-minute version and a
> read-the-plan-and-tell-us-what's-wrong version, both of which are genuinely useful to us.
>
> Nick

**One follow-up. Never two.**
