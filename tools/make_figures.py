#!/usr/bin/env python3
"""Generate the isometric pipeline figure.

    python3 tools/make_figures.py

Writes docs/03-pipeline/figures/pipeline-isometric.svg. Standard library only.

The figure encodes three things in geometry rather than only in labels:
  slab width      candidates reaching that step   (wide early, narrow late)
  slab thickness  cost per candidate              (thin early, thick late)
  slab colour     whether the step is a surrogate standing in for something
                  expensive, or plain machinery

Edit STAGES and re-run. Keep it honest: if the pipeline changes, the picture
should change with it rather than drifting into decoration.
"""
from __future__ import annotations
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "docs/03-pipeline/figures/pipeline-isometric.svg"

# --- brand -------------------------------------------------------------------
VOID, PANEL = "#141C36", "#1D2A4F"
ON, SOFT = "#EEF1FB", "#9AA7CD"
ACTION, SOUTH, GOLD = "#3F5FBC", "#00D3F6", "#C79A4D"
LINE = "rgba(154,167,205,.30)"

# --- the pipeline ------------------------------------------------------------
# id, name, what happens, what passes on, gate (or None), surrogate?, candidates, cost
STAGES = [
    ("S0", "Benchmark",            "Curate ligands, targets, decoys;\nharmonise activity labels",
     "manifest.csv",                None,                       False, 1.00, 0.02),
    ("S1", "Complex generation",   "Co-fold target-ligand complexes\nwhere no crystal exists",
     "predicted complexes + confidence", None,                  True,  0.86, 0.10),
    ("S2", "Pocket extraction",    "Crop the binding-site shell,\nassign protonation",
     "cropped pockets",             None,                       False, 0.86, 0.02),
    ("S3", "Ensemble generation",  "Sample how the pocket moves:\nstatic, relaxation or learned",
     "conformer ensembles",         "Motion value",             True,  0.86, 0.26),
    ("S4", "Ensemble reduction",   "Cluster to a few representative\nmicrostates with weights",
     "microstates + weights",       None,                       False, 0.74, 0.03),
    ("S5", "Equivariant scoring",  "Score the local 3D graph;\nrank, and estimate uncertainty",
     "scores + acquisition list",   "Ranking signal",           True,  0.60, 0.08),
    ("S6", "Quantum labelling",    "DFT on the genuinely uncertain\ncases only",
     "electronic-structure labels", "Quantum value",            False, 0.20, 1.00),
    ("S7", "Feedback learning",    "Correct the cheap scorer from\nexpensive labels",
     "improved scorer  →  back to S5", "Acquisition value",     True,  0.14, 0.09),
]

# --- isometric helpers -------------------------------------------------------
# Stages step along +x and +y together. Moving both keeps the horizontal drift
# small while giving each stage a full label row of vertical space, so the
# staircase stays clear of the text column on the right.
C = 31.0                       # grid unit in px
AX, AY = 4.21, 3.39            # per-stage step in grid x and y
OX, OY = 330.0, 150.0
COS, SIN = math.cos(math.radians(30)), 0.5

def iso(x: float, y: float, z: float) -> tuple[float, float]:
    return OX + (x - y) * COS * C, OY + (x + y) * SIN * C - z

def shade(hex_colour: str, factor: float) -> str:
    h = hex_colour.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02X%02X%02X" % tuple(max(0, min(255, int(v * factor))) for v in (r, g, b))

def poly(pts, fill, extra="") -> str:
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{d}" fill="{fill}" {extra}/>'

def slab(x0, y0, x1, y1, h, colour):
    """An isometric box. Returns svg, plus the screen point at its top-right corner."""
    top   = [iso(x0, y0, h), iso(x1, y0, h), iso(x1, y1, h), iso(x0, y1, h)]
    right = [iso(x1, y0, h), iso(x1, y1, h), iso(x1, y1, 0), iso(x1, y0, 0)]
    left  = [iso(x0, y1, h), iso(x1, y1, h), iso(x1, y1, 0), iso(x0, y1, 0)]
    svg = (poly(left,  shade(colour, .55)) + poly(right, shade(colour, .74))
           + poly(top, colour, 'stroke="rgba(255,255,255,.18)" stroke-width="1"'))
    return svg, iso(x1, y0, h)

# --- build -------------------------------------------------------------------
def build() -> str:
    W, H = 1320, 1230
    o: list[str] = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
             f'height="{H}" font-family="Inter,Helvetica Neue,Arial,sans-serif" '
             f'role="img" aria-label="Isometric diagram of the eight-stage surrogate pipeline">')
    o.append('<title>The surrogate pipeline, stage by stage</title>')
    o.append(f'<rect width="{W}" height="{H}" fill="{VOID}"/>')
    o.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
             f'markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{SOFT}"/>'
             '</marker>'
             '<marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
             f'markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{SOUTH}"/>'
             '</marker></defs>')

    # heading
    o.append(f'<text x="56" y="62" fill="{ON}" font-size="30" font-weight="800" '
             f'letter-spacing="-.5">How far can a chain of surrogates get us?</text>')
    o.append(f'<text x="56" y="92" fill="{SOFT}" font-size="15">Eight steps. Four of them hand an '
             f'expensive calculation to a learned model. Quantum chemistry is kept for the cases '
             f'where it changes the answer.</text>')

    TEXT_X = 660
    label_y: list[float] = []

    for i, (sid, name, does, passes, gate, surro, cand, cost) in enumerate(STAGES):
        x0, y0 = i * AX, i * AY
        x1 = x0 + 2.55
        y1 = y0 + 0.45 + 1.25 * cand           # candidates reaching this step
        height = 9 + 54 * cost                 # cost per candidate
        colour = SOUTH if surro else "#4A5C8C"

        svg, corner = slab(x0, y0, x1, y1, height, colour)
        o.append(svg)

        # stage id on the slab's top face
        cx, cy = iso((x0 + x1) / 2, (y0 + y1) / 2, height)
        o.append(f'<text x="{cx:.0f}" y="{cy + 5:.0f}" fill="{"#062430" if surro else ON}" '
                 f'font-size="15" font-weight="800" text-anchor="middle">{sid}</text>')

        # connector down to the next slab
        if i < len(STAGES) - 1:
            ax, ay = iso(x1 * .55 + x0 * .45, y1, height * .45)
            bx, by = iso(x0 + AX + 1.0, y0 + AY - .1, height * .45)
            o.append(f'<line x1="{ax:.0f}" y1="{ay:.0f}" x2="{bx:.0f}" y2="{by:.0f}" '
                     f'stroke="{SOFT}" stroke-width="1.5" opacity=".45" marker-end="url(#ar)"/>')

        # label block, right-hand column, leader line back to the slab
        ly = 152 + i * 118
        label_y.append(ly)
        o.append(f'<path d="M{corner[0]:.0f} {corner[1]:.0f} L{TEXT_X - 26} {ly - 4}" '
                 f'fill="none" stroke="{SOFT}" stroke-width="1" opacity=".28"/>')
        o.append(f'<circle cx="{corner[0]:.0f}" cy="{corner[1]:.0f}" r="3" fill="{SOFT}" opacity=".6"/>')

        o.append(f'<text x="{TEXT_X}" y="{ly}" font-size="17" font-weight="800" fill="{ON}">'
                 f'<tspan fill="{SOUTH if surro else SOFT}">{sid}</tspan>'
                 f'<tspan dx="10">{name}</tspan>'
                 + (f'<tspan dx="12" font-size="10.5" font-weight="700" fill="{SOUTH}" '
                    f'letter-spacing="1.2">SURROGATE</tspan>' if surro else '')
                 + '</text>')
        for j, line in enumerate(does.split("\n")):
            o.append(f'<text x="{TEXT_X}" y="{ly + 22 + j * 17:.0f}" font-size="13.5" '
                     f'fill="{SOFT}">{line}</text>')
        o.append(f'<text x="{TEXT_X}" y="{ly + 22 + len(does.split(chr(10))) * 17 + 3:.0f}" '
                 f'font-size="12.5" fill="{ON}" opacity=".62">→ {passes}</text>')
        if gate:
            gy = ly + 22 + len(does.split("\n")) * 17 + 3
            o.append(f'<rect x="{TEXT_X + 332}" y="{gy - 15:.0f}" width="150" height="21" rx="4" '
                     f'fill="none" stroke="{GOLD}" stroke-width="1" opacity=".75"/>')
            o.append(f'<text x="{TEXT_X + 407}" y="{gy:.0f}" font-size="11" font-weight="700" '
                     f'fill="{GOLD}" text-anchor="middle" letter-spacing=".6">GATE · {gate}</text>')

    # axis annotations along the staircase
    o.append(f'<text x="56" y="{OY + 250:.0f}" fill="{SOFT}" font-size="12" font-weight="700" '
             f'letter-spacing="1.6" opacity=".8">CANDIDATES</text>')
    o.append(f'<text x="56" y="{OY + 268:.0f}" fill="{SOFT}" font-size="12" opacity=".6">'
             f'slab width, falling</text>')
    o.append(f'<text x="56" y="{OY + 306:.0f}" fill="{SOFT}" font-size="12" font-weight="700" '
             f'letter-spacing="1.6" opacity=".8">COST EACH</text>')
    o.append(f'<text x="56" y="{OY + 324:.0f}" fill="{SOFT}" font-size="12" opacity=".6">'
             f'slab height, rising</text>')
    o.append(f'<text x="56" y="{OY + 368:.0f}" fill="{SOUTH}" font-size="12" font-weight="700" '
             f'letter-spacing="1.6" opacity=".9">CYAN</text>')
    o.append(f'<text x="56" y="{OY + 386:.0f}" fill="{SOFT}" font-size="12" opacity=".6">'
             f'a surrogate stands in</text>')
    o.append(f'<text x="56" y="{OY + 404:.0f}" fill="{SOFT}" font-size="12" opacity=".6">'
             f'for something expensive</text>')

    # feedback loop, S7 back to S5
    fy, gx = label_y[7] + 58, TEXT_X + 492
    o.append(f'<path d="M{gx} {fy} L{gx + 34} {fy} L{gx + 34} {label_y[5] - 8} '
             f'L{gx} {label_y[5] - 8}" fill="none" stroke="{SOUTH}" stroke-width="1.6" '
             f'stroke-dasharray="4 4" marker-end="url(#ar2)" opacity=".8"/>')
    o.append(f'<text x="{gx + 38}" y="{(fy + label_y[5]) / 2 + 4:.0f}" fill="{SOUTH}" '
             f'font-size="11.5" font-weight="700">retrain</text>')

    # footer: the two gates that sit across the whole run
    o.append(f'<line x1="56" y1="{H - 96}" x2="{W - 56}" y2="{H - 96}" stroke="{SOFT}" '
             f'opacity=".22"/>')
    o.append(f'<text x="56" y="{H - 66}" fill="{SOFT}" font-size="12.5" font-weight="700" '
             f'letter-spacing="1.4">ACROSS THE WHOLE RUN</text>')
    for k, (g, d) in enumerate([("Technical reproducibility", "same manifest, same artifacts"),
                                ("Operational cost", "GPU-hours per informative label")]):
        x = 56 + k * 380
        o.append(f'<rect x="{x}" y="{H - 54}" width="16" height="16" rx="3" fill="none" '
                 f'stroke="{GOLD}" stroke-width="1.2" opacity=".75"/>')
        o.append(f'<text x="{x + 26}" y="{H - 48}" fill="{ON}" font-size="13" '
                 f'font-weight="700">{g}</text>')
        o.append(f'<text x="{x + 26}" y="{H - 31}" fill="{SOFT}" font-size="12">{d}</text>')
    o.append(f'<text x="{W - 56}" y="{H - 38}" fill="{SOFT}" font-size="11.5" text-anchor="end" '
             f'opacity=".7">Every surrogate carries a fidelity contract: ground truth, validation '
             f'set, trust region.</text>')

    o.append('</svg>')
    return "\n".join(o)

if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build())
    print(f"wrote {OUT.relative_to(Path.cwd())}  ({OUT.stat().st_size:,} bytes)")
