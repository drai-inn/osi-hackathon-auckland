#!/usr/bin/env python3
"""The theme cards, one SVG each.

    python3 tools/make_cards.py

Writes docs/cards/theme-{1..4}.svg and docs/cards/theme-open-{1,2}.svg

The four named cards say what we happen to be interested in. The two open ones
are deliberately empty slots, dashed rather than filled, and on the site they
link out to an issue. Somebody arriving with a problem that sits somewhere else
should be able to see that there is room for it before they read a word.

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

# A four-step ramp rather than two colours, so the four read as one set. It
# orders the cards, nothing more — the themes are not a fidelity ladder in this
# order, and the scale label on each card is where the real claim is made.
RUNG = ["#8B7CF6", "#7C8DF0", "#4FB6EE", "#00D3F6"]


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

# The scale is the extra piece of context: it is what makes the four read as one
# ladder rather than four unrelated tiles, and it is the thing a visitor uses to
# work out which theme is theirs.
CARDS = [
    (1, "Screening at scale", "MANY MOLECULES, COARSE",
     "Models that know something about shape, used to filter before you pay for docking.",
     "Boltz-2 · OpenFold3 · IntFold · ChemBERTa-2 · ESM-2"),
    (2, "Molecules in motion", "ATOMS, IN MOTION",
     "Machine-learned interatomic potentials in MD. Near-quantum forces you can afford to run.",
     "MACE · UMA · eSEN · Orb-v3 · NequIP"),
    (3, "Binding to whole system", "ONE EVENT, WHOLE CELL",
     "Carrying a molecular signal up to functional and physiological change.",
     "STATE · scGPT · Geneformer · scFoundation"),
    (4, "Repurposing what we have", "EVERY APPROVED DRUG",
     "Genotype, structure and approved drugs, with deliberately small models.",
     "Evo 2 · Nucleotide Transformer · TxGNN · PrimeKG"),
]


def data_uri(path: Path) -> str:
    return "data:image/webp;base64," + base64.b64encode(path.read_bytes()).decode()


def build(n, title, scale, blurb, models) -> str:
    accent = RUNG[n - 1]
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

    # Four ticks with this theme's one filled: the set reads as a ladder, and a
    # card seen on its own still says where it sits.
    for k in range(4):
        on = k == n - 1
        o.append(f'<rect x="{34 + k*13}" y="{40 if on else 43}" width="9" '
                 f'height="{10 if on else 4}" rx="2" fill="{RUNG[k]}" '
                 f'opacity="{1 if on else 0.33}"/>')
    o.append(f'<text x="{34 + 4*13 + 8}" y="52" fill="{accent}" font-size="12" '
             f'font-weight="800" letter-spacing="1.8">THEME {n}</text>')
    o.append(f'<text x="{W-34}" y="52" text-anchor="end" fill="{ON}" font-size="11.5" '
             f'font-weight="700" letter-spacing="1.4" opacity=".62">{esc(scale)}</text>')
    # Light and large. The words are the thing being foregrounded, not the picture
    # behind them, so the weight comes off and the size goes up.
    o.append(f'<text x="34" y="92" fill="{ON}" font-size="37" font-weight="300" '
             f'letter-spacing="-.6">{esc(title)}</text>')
    for i, line in enumerate(wrap(blurb, 56)):
        o.append(f'<text x="34" y="{H - 96 + i*23}" fill="{ON}" font-size="15.5" '
                 f'opacity=".92">{esc(line)}</text>')
    o.append(f'<line x1="34" y1="{H-48}" x2="{W-34}" y2="{H-48}" stroke="{ON}" opacity=".22"/>')
    o.append(f'<text x="34" y="{H-22}" fill="{ON}" font-size="12.5" opacity=".72">'
             f'{esc(models)}</text>')
    o.append('</svg>')
    return "\n".join(o)


# An empty slot. Same frame, same type, no background and no filled rung — the
# card should look like the others with the contents not yet decided.
OPEN = [
    (1, "Your theme", "SOMEWHERE ELSE ON THE LADDER",
     "Bring a problem that doesn't sit in the four. Open an issue and we'll make room for it."),
    (2, "Your theme", "OR A METHOD, OR A BENCHMARK",
     "A dataset, an evaluation or a comparison you think ought to exist and doesn't."),
]


def build_open(k, title, scale, blurb) -> str:
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
         f'height="{H}" font-family="{FONT}" role="img" '
         f'aria-label="An open theme. {esc(blurb)}">',
         f'<title>{esc(title)} — {esc(blurb)}</title>',
         '<defs>',
         f'<linearGradient id="open{k}" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{PANEL}"/><stop offset="1" stop-color="{VOID}"/>'
         f'</linearGradient>',
         '</defs>',
         f'<rect width="{W}" height="{H}" rx="10" fill="url(#open{k})"/>',
         f'<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="9" fill="none" '
         f'stroke="{SOFT}" stroke-width="3" stroke-dasharray="9 8" opacity=".72"/>']

    # Four hollow ticks: none of them is this card's.
    for i in range(4):
        o.append(f'<rect x="{34 + i*13}" y="43" width="9" height="4" rx="2" fill="none" '
                 f'stroke="{SOFT}" stroke-width="1.2" opacity=".5"/>')
    o.append(f'<text x="{34 + 4*13 + 8}" y="52" fill="{SOFT}" font-size="12" '
             f'font-weight="800" letter-spacing="1.8">OPEN</text>')
    o.append(f'<text x="{W-34}" y="52" text-anchor="end" fill="{ON}" font-size="11.5" '
             f'font-weight="700" letter-spacing="1.4" opacity=".45">{esc(scale)}</text>')
    o.append(f'<text x="34" y="92" fill="{ON}" font-size="37" font-weight="300" '
             f'letter-spacing="-.6" opacity=".9">{esc(title)}</text>')
    o.append(f'<g stroke="{SOUTH}" stroke-width="3" stroke-linecap="round" opacity=".85">'
             f'<path d="M{W/2-19} {H/2+4} h38 M{W/2} {H/2-15} v38"/></g>')
    for i, line in enumerate(wrap(blurb, 56)):
        o.append(f'<text x="34" y="{H - 96 + i*23}" fill="{ON}" font-size="15.5" '
                 f'opacity=".78">{esc(line)}</text>')
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    written = [(OUT / f"theme-{n}.svg", build(n, *rest)) for n, *rest in CARDS]
    written += [(OUT / f"theme-open-{k}.svg", build_open(k, *rest)) for k, *rest in OPEN]
    for p, svg in written:
        p.write_text(svg)
        print(f"wrote {p.relative_to(OUT.parent.parent.parent)}  ({p.stat().st_size:,} bytes)")
