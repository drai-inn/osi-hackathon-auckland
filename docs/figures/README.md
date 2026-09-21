# Figures

All generated from a script. Nothing hand-posed, no screenshots.

| Figure | From | Shows |
| --- | --- | --- |
| [structures-cdk-family.svg](structures-cdk-family.svg) | `tools/render_structures.py` | Four CDK targets from deposited coordinates, superposed onto CDK9 |
| [pocket-anatomy.svg](pocket-anatomy.svg) | `tools/render_components.py` + `data/pocket-anatomy.json` | The twenty residues lining the CDK9 site, and the equivalent residue in the three counter-targets |
| [zoom-ladder.svg](zoom-ladder.svg) | `tools/render_components.py` | One site at six scales, complex down to a quantum region, with heavy-atom counts |

The four [theme cards](../cards/) are a different thing and live by different rules. They come
from `tools/make_cards.py`, which composites a generated background from `docs/cards/bg/` with a
scrim and the theme's text. **Those backgrounds are collateral, not data** — mood for a recruitment
card. Everything on this page comes from deposited coordinates.

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
