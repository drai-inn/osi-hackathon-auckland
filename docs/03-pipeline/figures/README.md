# Figures

All generated. None hand-made, none screenshots. If a figure can't be regenerated it won't survive
the third revision of the thing it describes.

| Figure | From | Shows |
| --- | --- | --- |
| [pipeline-isometric.svg](pipeline-isometric.svg) | `tools/make_figures.py` | The eight steps, what passes between them, where the gates sit. Slab width is candidates, height is cost each, cyan is a surrogate |
| [objects-of-study.svg](objects-of-study.svg) | `tools/make_figures.py` | What each phase actually holds, and what is measured on it. Headed by the four targets |
| [scale-trajectory.svg](scale-trajectory.svg) | `tools/make_figures.py` | Four tiers from smoke test to scale-up, with a gate between each |
| [protein-space.svg](protein-space.svg) | `tools/make_figures.py` + `data/protein-space.json` | Identity across the CDK family, whole region against the ATP site |
| [structures-cdk-family.svg](structures-cdk-family.svg) | `tools/render_structures.py` | The four targets from deposited coordinates, superposed onto CDK9 |

## Regenerate

```bash
python3 tools/make_figures.py          # the four schematics, no network needed
python3 tools/render_structures.py     # the structures, needs biopython + network on first run
python3 tools/fetch_protein_space.py   # refresh the CDK identity numbers
```

## Where they appear

| | README | narrative | architecture | problem statement | visualisation | landing page |
| --- | :-: | :-: | :-: | :-: | :-: | :-: |
| pipeline-isometric | ● | ● | ● | | | ● |
| objects-of-study | ● | ● | ● | | | |
| scale-trajectory | ● | ● | | | | ● |
| protein-space | ● | | | ● | ● | |
| structures-cdk-family | ● | | | | ● | ● |

Keep this table honest. A figure nobody links to is dead weight.

## Interactive

[`tools/render/viewer.html`](../../../tools/render/viewer.html) is the live version: all four
structures plus a superposed view, rotatable, with the crop radius as a button. GitHub can't run
JavaScript in a README, so the SVGs are the static equivalent. Both come from the same PDB entries.
