#!/usr/bin/env python3
"""Four theme cards, one SVG each.

    python3 tools/make_cards.py

Writes docs/cards/theme-{1..4}.svg

Each card carries its own generated imagery, drawn procedurally from a fixed
seed so the output is identical on every run. Standard library only.
"""
from __future__ import annotations

import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/cards"
GEOM = ROOT / "data/card-geometry.json"

VOID, PANEL, ON, SOFT = "#141C36", "#1D2A4F", "#EEF1FB", "#9AA7CD"
SOUTH, GOLD, ACTION, VIOLET = "#00D3F6", "#C79A4D", "#3F5FBC", "#8B7CF6"

# CPK-ish, tuned for the dark panel
ELEMENT = {"C": "#C7D0EA", "N": "#6FA8FF", "O": "#FF8A7A", "S": "#F2D06B",
           "CL": "#7FE6A6", "F": "#7FE6A6", "P": "#F2A65A"}

W, H = 600, 406
ART_Y, ART_H = 112, 176
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


# ------------------------------------------------------------------ artwork

def art_screening(rng) -> list[str]:
    """A wide field of candidates narrowing to a few."""
    o, cy = [], ART_Y + ART_H / 2
    for _ in range(320):
        t = rng.random() ** 0.6
        x = 40 + t * 470
        spread = (1 - t) ** 1.5 * 78 + 5
        y = cy + rng.gauss(0, spread / 2.2)
        if not ART_Y + 8 < y < ART_Y + ART_H - 8:
            continue
        keep = t > 0.72 and abs(y - cy) < 16
        r = 2.4 if keep else 1.5
        col = SOUTH if keep else SOFT
        op = 0.95 if keep else 0.13 + 0.16 * (1 - t)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" opacity="{op:.2f}"/>')
    o.append(f'<path d="M40 {cy-88:.0f} Q300 {cy-58:.0f} 512 {cy-13:.0f}" fill="none" '
             f'stroke="{SOFT}" stroke-width="1" opacity=".22"/>')
    o.append(f'<path d="M40 {cy+88:.0f} Q300 {cy+58:.0f} 512 {cy+13:.0f}" fill="none" '
             f'stroke="{SOFT}" stroke-width="1" opacity=".22"/>')
    return o


def art_motion_real(rng) -> list[str]:
    """Flavopiridol as deposited, inside four superposed CDK pockets.

    Real coordinates rather than a drawn squiggle. The spread between the four
    backbones is genuine structural variation, which is the theme.
    """
    g = json.loads(GEOM.read_text())
    lig, traces = g["ligand"], g["traces"]
    # Frame on the ligand, not the whole crop, so the molecule is legible and the
    # backbone reads as the pocket around it. Everything else clips.
    lx = [p[0] for p in lig["atoms"]]; ly = [p[1] for p in lig["atoms"]]
    cx, cy = (min(lx) + max(lx)) / 2, (min(ly) + max(ly)) / 2
    span = max(max(lx) - min(lx), max(ly) - min(ly)) * 2.15
    sc = (ART_H - 14) / span
    ox = W / 2 - cx * sc
    oy = ART_Y + ART_H / 2 - cy * sc
    # drop the outer shell, which is tangle at this zoom
    traces = [[q for q in t if abs(q[0] - cx) < span and abs(q[1] - cy) < span * 0.8]
              for t in traces]
    def S(p):
        return ox + p[0] * sc, oy + p[1] * sc, p[2]

    o = []
    # the four backbones. CDK9 lit, the counter-targets behind it.
    for k, t in enumerate(traces):
        pr = [S(q) for q in t]
        d = ""
        pen = False
        for a, b in zip(pr, pr[1:]):
            if math.dist(a[:2], b[:2]) > sc * 6.0:      # chain break
                pen = False
                continue
            if not pen:
                d += f"M{a[0]:.1f} {a[1]:.1f}"
                pen = True
            d += f"L{b[0]:.1f} {b[1]:.1f}"
        o.append(f'<path d="{d}" fill="none" stroke="{SOUTH if k == 0 else SOFT}" '
                 f'stroke-width="{3.0 if k == 0 else 1.9}" stroke-linecap="round" '
                 f'stroke-linejoin="round" opacity="{0.50 if k == 0 else 0.17}"/>')

    # the ligand, drawn properly
    lp = [S(p) for p in lig["atoms"]]
    for i, j in lig["bonds"]:
        o.append(f'<line x1="{lp[i][0]:.1f}" y1="{lp[i][1]:.1f}" x2="{lp[j][0]:.1f}" '
                 f'y2="{lp[j][1]:.1f}" stroke="{GOLD}" stroke-width="4.0" '
                 f'stroke-linecap="round" opacity=".95"/>')
    for k, (x, y, _) in enumerate(lp):
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.6" '
                 f'fill="{ELEMENT.get(lig["elements"][k], GOLD)}"/>')
    return o


def art_motion(rng) -> list[str]:
    """One chain, sampled several times. The spread is the point."""
    o, cy = [], ART_Y + ART_H / 2
    # an irregular chain rather than a wave, so it reads as a molecule
    base, x, y, ang = [], 66.0, cy + 18, -0.5
    for _ in range(13):
        base.append((x, y))
        ang += rng.uniform(-1.15, 1.15)
        x += math.cos(ang) * 14 + 24
        y = max(ART_Y + 34, min(ART_Y + ART_H - 34, y + math.sin(ang) * 30))
    branch = rng.sample(range(2, 11), 3)

    for k in range(6, -1, -1):
        amp = k * 4.2
        pts = [(px + rng.gauss(0, amp * 0.55), py + rng.gauss(0, amp)) for px, py in base]
        d = " ".join(f"{'M' if i == 0 else 'L'}{px:.1f} {py:.1f}" for i, (px, py) in enumerate(pts))
        live = k == 0
        op = 0.95 if live else 0.26 - k * 0.028
        o.append(f'<path d="{d}" fill="none" stroke="{SOUTH if live else SOFT}" '
                 f'stroke-width="{3.0 if live else 1.6}" stroke-linecap="round" '
                 f'stroke-linejoin="round" opacity="{op:.2f}"/>')
        for i in branch:
            bx, by = pts[i]
            o.append(f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{bx+7:.1f}" y2="{by-19:.1f}" '
                     f'stroke="{SOUTH if live else SOFT}" stroke-width="{2.4 if live else 1.3}" '
                     f'stroke-linecap="round" opacity="{op:.2f}"/>')
            if live:
                o.append(f'<circle cx="{bx+7:.1f}" cy="{by-19:.1f}" r="4.4" fill="{GOLD}"/>')
        if live:
            for px, py in pts:
                o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.6" fill="{SOUTH}"/>')
    return o


def art_scales(rng) -> list[str]:
    """One binding event, opening out into the system around it."""
    o, cx, cy = [], 150.0, ART_Y + ART_H / 2
    for k, r in enumerate((44, 96, 158, 226)):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{SOFT}" '
                 f'stroke-width="1" opacity="{0.26 - k*0.045:.2f}"/>')
        n = 3 + k * 4
        for i in range(n):
            a = -1.05 + i * (2.1 / max(n - 1, 1)) + rng.uniform(-0.06, 0.06)
            x, y = cx + math.cos(a) * r, cy + math.sin(a) * r
            if not (ART_Y + 6 < y < ART_Y + ART_H - 6 and x < 560):
                continue
            col = (SOUTH, ACTION, VIOLET, SOFT)[k]
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5.0 - k*0.7:.1f}" fill="{col}" '
                     f'opacity="{0.9 - k*0.14:.2f}"/>')
            o.append(f'<line x1="{cx + math.cos(a)*(r-46):.1f}" y1="{cy + math.sin(a)*(r-46):.1f}" '
                     f'x2="{x:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width=".9" opacity=".2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{GOLD}"/>')
    return o


def art_repurposing(rng) -> list[str]:
    """A shelf of approved compounds, matched against a few targets."""
    o = []
    lx, rx = 96.0, 452.0
    rows, cols = 7, 3
    shelf = []
    for r in range(rows):
        for c in range(cols):
            x = lx + c * 34
            y = ART_Y + 22 + r * 22
            shelf.append((x, y))
            o.append(f'<rect x="{x-9:.1f}" y="{y-5:.1f}" width="18" height="10" rx="5" '
                     f'fill="{SOFT}" opacity=".24"/>')
    targets = [(rx, ART_Y + 40), (rx, ART_Y + 88), (rx, ART_Y + 136)]
    for i, (tx, ty) in enumerate(targets):
        o.append(f'<circle cx="{tx}" cy="{ty}" r="17" fill="none" stroke="{SOFT}" '
                 f'stroke-width="1.4" opacity=".4"/>')
        o.append(f'<path d="M{tx-9} {ty+3} q9 -13 18 0" fill="none" stroke="{VIOLET}" '
                 f'stroke-width="2" opacity=".75"/>')
    picks = rng.sample(shelf, 4)
    for i, (x, y) in enumerate(picks):
        tx, ty = targets[i % 3]
        hit = i == 0
        o.append(f'<path d="M{x+11:.1f} {y:.1f} C{(x+tx)/2:.0f} {y:.1f} {(x+tx)/2:.0f} {ty} '
                 f'{tx-19:.0f} {ty}" fill="none" stroke="{SOUTH if hit else SOFT}" '
                 f'stroke-width="{1.8 if hit else 1}" opacity="{0.9 if hit else 0.28}"/>')
        o.append(f'<rect x="{x-9:.1f}" y="{y-5:.1f}" width="18" height="10" rx="5" '
                 f'fill="{SOUTH if hit else SOFT}" opacity="{1 if hit else .55}"/>')
    return o


CARDS = [
    (1, "Screening at scale", SOUTH, art_screening,
     "Models that know something about shape, used to filter before you pay for docking.",
     "Boltz-2 · OpenFold3 · IntFold · ChemBERTa-2 · ESM-2"),
    (2, "Molecules in motion", SOUTH, art_motion_real,
     "Machine-learned interatomic potentials in MD. Near-quantum forces you can afford to run.",
     "MACE · UMA · eSEN · Orb-v3 · NequIP"),
    (3, "Binding to whole system", VIOLET, art_scales,
     "Carrying a molecular signal up to functional and physiological change.",
     "STATE · scGPT · Geneformer · scFoundation"),
    (4, "Repurposing what we have", VIOLET, art_repurposing,
     "Genotype, structure and approved drugs, with deliberately small models.",
     "Evo 2 · Nucleotide Transformer · TxGNN · PrimeKG"),
]


def build(n, title, accent, art, blurb, models) -> str:
    rng = random.Random(1000 + n)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="{FONT}" role="img" aria-label="Theme {n}, {esc(title)}. {esc(blurb)}">',
         f'<title>Theme {n} — {esc(title)}</title>',
         f'<rect width="{W}" height="{H}" rx="10" fill="{PANEL}"/>',
         f'<rect width="{W}" height="4" rx="2" fill="{accent}"/>',
         f'<clipPath id="a{n}"><rect x="1" y="{ART_Y}" width="{W-2}" height="{ART_H}"/></clipPath>',
         f'<g clip-path="url(#a{n})">'] + art(rng) + ['</g>']
    o.append(f'<text x="34" y="52" fill="{accent}" font-size="12" font-weight="800" '
             f'letter-spacing="1.8">THEME {n}</text>')
    o.append(f'<text x="34" y="86" fill="{ON}" font-size="26" font-weight="800" '
             f'letter-spacing="-.4">{esc(title)}</text>')
    for i, line in enumerate(wrap(blurb, 58)):
        o.append(f'<text x="34" y="{ART_Y + ART_H + 32 + i*22}" fill="{ON}" font-size="15" '
                 f'opacity=".82">{esc(line)}</text>')
    o.append(f'<line x1="34" y1="{H-48}" x2="{W-34}" y2="{H-48}" stroke="{SOFT}" opacity=".18"/>')
    o.append(f'<text x="34" y="{H-22}" fill="{SOFT}" font-size="12.5">{esc(models)}</text>')
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for n, title, accent, art, blurb, models in CARDS:
        p = OUT / f"theme-{n}.svg"
        p.write_text(build(n, title, accent, art, blurb, models))
        print(f"wrote {p.relative_to(OUT.parent.parent.parent)}  ({p.stat().st_size:,} bytes)")
