#!/usr/bin/env python3
"""Four theme cards, one SVG each.

    python3 tools/make_cards.py

Writes docs/cards/theme-{1..4}.svg

Each card is a generated background from docs/cards/bg/, a dark scrim so the
text reads, and the theme's name, line and models. The backgrounds are mood
rather than measurement — they are collateral, and nothing in them should be
read as a depiction of anything. The figures that do carry data live in
docs/figures/ and come from deposited coordinates.

Backgrounds are embedded as data URIs so each SVG is self-contained. An SVG
loaded through <img>, which is how GitHub renders it, cannot fetch anything
external.

Standard library only.
"""
from __future__ import annotations

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/cards"
BG = OUT / "bg"

VOID, PANEL, ON, SOFT = "#141C36", "#1D2A4F", "#EEF1FB", "#9AA7CD"
SOUTH, GOLD, ACTION, VIOLET = "#00D3F6", "#C79A4D", "#3F5FBC", "#8B7CF6"


W, H = 600, 406
FONT = "Inter,Helvetica Neue,Arial,sans-serif"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(text: str, width: int) -> list[str]:
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if len(trial) > width and line:
            lines.append(line)
            line = word
        else:
            line = trial
    if line:
        lines.append(line)
    return lines

CARDS = [
    (1, "Screening at scale", SOUTH,
     "Models that know something about shape, used to filter before you pay for docking.",
     "Boltz-2 · OpenFold3 · IntFold · ChemBERTa-2 · ESM-2"),
    (2, "Molecules in motion", SOUTH,
     "Machine-learned interatomic potentials in MD. Near-quantum forces you can afford to run.",
     "MACE · UMA · eSEN · Orb-v3 · NequIP"),
    (3, "Binding to whole system", VIOLET,
     "Carrying a molecular signal up to functional and physiological change.",
     "STATE · scGPT · Geneformer · scFoundation"),
    (4, "Repurposing what we have", VIOLET,
     "Genotype, structure and approved drugs, with deliberately small models.",
     "Evo 2 · Nucleotide Transformer · TxGNN · PrimeKG"),
]


def data_uri(path: Path) -> str:
    return "data:image/webp;base64," + base64.b64encode(path.read_bytes()).decode()


def build(n, title, accent, blurb, models) -> str:
    bg = data_uri(BG / f"theme-{n}.webp")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
         f'viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}" role="img" '
         f'aria-label="Theme {n}, {esc(title)}. {esc(blurb)}">',
         f'<title>Theme {n} — {esc(title)}</title>',
         '<defs>',
         # Dark at both ends and open in the middle: the title needs a ground at
         # the top and the copy needs one at the foot, but the image should still
         # read between them. Some backgrounds go pale up top, so the top band
         # has to be there even where it looks unnecessary.
         f'<linearGradient id="scrim{n}" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{VOID}" stop-opacity=".82"/>'
         f'<stop offset=".17" stop-color="{VOID}" stop-opacity=".62"/>'
         f'<stop offset=".34" stop-color="{VOID}" stop-opacity=".34"/>'
         f'<stop offset=".55" stop-color="{VOID}" stop-opacity=".58"/>'
         f'<stop offset=".7" stop-color="{VOID}" stop-opacity=".9"/>'
         f'<stop offset="1" stop-color="{VOID}" stop-opacity=".97"/></linearGradient>',
         f'<clipPath id="round{n}"><rect width="{W}" height="{H}" rx="10"/></clipPath>',
         '</defs>',
         f'<g clip-path="url(#round{n})">',
         f'<image href="{bg}" xlink:href="{bg}" x="0" y="0" width="{W}" height="{H}" '
         f'preserveAspectRatio="xMidYMid slice"/>',
         f'<rect width="{W}" height="{H}" fill="url(#scrim{n})"/>',
         f'<rect width="{W}" height="4" fill="{accent}"/>',
         '</g>']

    o.append(f'<text x="34" y="52" fill="{accent}" font-size="12" font-weight="800" '
             f'letter-spacing="1.8">THEME {n}</text>')
    o.append(f'<text x="34" y="86" fill="{ON}" font-size="27" font-weight="800" '
             f'letter-spacing="-.4">{esc(title)}</text>')
    for i, line in enumerate(wrap(blurb, 56)):
        o.append(f'<text x="34" y="{H - 96 + i*23}" fill="{ON}" font-size="15.5" '
                 f'opacity=".92">{esc(line)}</text>')
    o.append(f'<line x1="34" y1="{H-48}" x2="{W-34}" y2="{H-48}" stroke="{ON}" opacity=".22"/>')
    o.append(f'<text x="34" y="{H-22}" fill="{ON}" font-size="12.5" opacity=".72">'
             f'{esc(models)}</text>')
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for n, title, accent, blurb, models in CARDS:
        p = OUT / f"theme-{n}.svg"
        p.write_text(build(n, title, accent, blurb, models))
        print(f"wrote {p.relative_to(OUT.parent.parent.parent)}  ({p.stat().st_size:,} bytes)")
