# The pitch

**All recruitment copy is cut from this page.** Rewrite it here and re-cut, so the versions stay
together.

---

## The question

> ### How far can a chain of surrogates take us in biomolecular interactions?
>
> Systems · proteins · ligand binding · drug discovery · pharmacology

## Why those five words are one chain

Physiological outcomes come from molecules interacting. Those interactions produce functional
change. Function is driven by spatial and structural change. Pharmacology is the effect of drugs on
that system.

It reads bottom-up: structure, interaction, function, physiology, with the drug entering at the
bottom and its effect read at the top. Carrying a signal cleanly from one end to the other is still
an open problem.

## Why now

Biology has a ladder of scales. Machine learning now has a ladder that runs alongside it:
association models over sequence, 3D-aware and equivariant models over structure, interatomic
potentials over atoms and motion, and multi-scale models over cells and tissue.

**Language models sit at nearly every rung as well.** ESM and AMPLIFY over protein sequence, Evo 2
and Nucleotide Transformer over DNA, ChemBERTa and MolFormer over molecules written as text,
Geneformer and scGPT over gene expression, and general LLMs for reading the literature and driving
the tools. In several of these places the language model is the thing to beat: ChemBERTa-2 beat a
strong graph network on most of MoleculeNet, and Evo 2 embeddings reach 0.997 AUROC on ClinVar
variant classification.

Most are open-weight and most arrived recently. Most of us know our own rung.

**Every theme asks the same question: how far up that second ladder do you have to climb to get an
answer you can trust, and how would you know?** Climbing higher costs more, and somewhere along the
way it stops buying accuracy. Finding where that happens is the work.

## What we're actually doing

Four [themes](themes.md), each a different rung. In each one, three moves:

1. Find out what open-weight models exist in that area
2. Get one or two running on our hardware
3. Work out what to measure, and report it back at the end of day one

The third is the one we care most about. Each group sources its own data and picks its own
benchmark, because evaluation looks different at every rung and designing it is a good part of the
work. Groups stay comparable by answering the same four questions about whatever they chose.

A recent benchmark found single-cell foundation models level with a simple linear baseline at
predicting perturbation effects, and another found the choice of metric changes which model comes
out on top. How to evaluate these things is genuinely unsettled, and there's a lot of room to do
useful work there.

## The four themes, in a line each

| | |
| --- | --- |
| **Screening at scale, with physics in the loop** | Models that know something about shape, used to filter before you pay for docking |
| **Molecules in motion** | Machine-learned interatomic potentials in MD — near-quantum forces you can afford to run |
| **From a binding event to a whole system** | Carrying a molecular signal up to functional and physiological change |
| **Repurposing what we already have** | Genotype, structure and approved drugs, with deliberately small models |

Language models cut across all four, and the cheapest useful thing they do is build your dataset.
Each group sources its own, and schema-guided extraction from the literature gets you there in an
afternoon.

Four to start from. They describe the kind of work we're interested in, and they come from where we
happen to sit. Bring your problem and take a space. If none of them fit, add one — we're making room
for people to gather, and the shape of the room is still open.
[Propose a theme](https://github.com/drai-inn/osi-hackathon-auckland/issues/new?title=Theme%3A%20&body=Four%20themes%20are%20up%20on%20the%20site.%20This%20one%20is%20somewhere%20else.%0A%0A%2A%2AThe%20problem%2C%20and%20roughly%20what%20scale%20it%20sits%20at%2A%2A%0A%0A%0A%2A%2AModels%20or%20methods%20you%27d%20want%20to%20try%2A%2A%0A%0A%0A%2A%2AWho%27s%20coming%20with%20you%2A%2A%0A).

## What we're asking

**Come and explore the broader opportunity while getting hands-on with AI in your own area.** Come
prepared to work with agents and with code, to find out where your own methods are moving under the
new models.

Two things at once: depth in your own field, and a link into something larger.

We're inviting **project teams**. A group leader brings their team, their expertise, and a problem
or candidate. If you can only come for the opening, come for the opening and leave your team to it.
That's a completely normal way to take part.

## What you get out of it

A calibrated view of where these models currently stand in *your* field, which is what you need in
order to decide whether to put a student on it.

Two days with people who don't share your background. Compute you don't have to organise. Default
targets and chemistry already prepared, so nobody starts from a blank page.

And a shot at something bigger. Four themes that work on their own are also, linked, the start of a
drug discovery capability UoA doesn't have yet. We'd call it a seed for now.

## What we expect

We don't know how far this gets, and finding out is the work. Several of these models may land level
with much simpler things on the problems we care about. We'd like the number either way, because
every rung on that ladder is improving quickly, and knowing where it stands now tells us when that
changes.

A well-founded *"not yet, and here's why"* is a result we'd be happy to present.

## The global event

We're one local site of the [global hackathon](the-global-event.md), which runs 21–22 October with
registration open to anyone. Sign up for that too — it's the bigger room.
