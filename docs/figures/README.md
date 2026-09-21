# Figures

All generated from a script. Nothing hand-posed, no screenshots.

| Figure | From | Shows |
| --- | --- | --- |
| [structures-cdk-family.svg](structures-cdk-family.svg) | `tools/render_structures.py` | Four CDK targets from deposited coordinates, superposed onto CDK9 |
| [pocket-anatomy.svg](pocket-anatomy.svg) | `tools/render_components.py` + `data/pocket-anatomy.json` | The twenty residues lining the CDK9 site, and the equivalent residue in the three counter-targets |
| [zoom-ladder.svg](zoom-ladder.svg) | `tools/render_components.py` | One site at six scales, complex down to a quantum region, with heavy-atom counts |

The four [theme cards](../cards/) come from `tools/make_cards.py`, which is standard-library only.
Theme 2's artwork is real geometry — flavopiridol as deposited, inside four superposed CDK pockets —
read from `data/card-geometry.json`, which `tools/extract_card_geometry.py` writes from the cached
PDB entries.

## Regenerate

```bash
python3 tools/render_structures.py    # needs biopython + numpy, network on first run
python3 tools/render_components.py
python3 tools/make_cards.py           # standard library only
```

## Where they appear

All three are on [worked-example.md](../worked-example.md). The cards are on the
[README](../../README.md), [themes.md](../themes.md) and the
[landing page](../../outreach/site/index.html).

Every structural figure carries its PDB ID, the date fetched and the command that produced it, in
the script that generates it.

## Rotating them

[`tools/render/viewer.html`](../../tools/render/viewer.html) opens the structures in a browser with
no install. GitHub can't run JavaScript inline, so the SVGs are the static version. Both come from
the same PDB entries.
