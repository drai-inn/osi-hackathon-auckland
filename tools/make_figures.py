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




# =============================================================================
# Figure 2 — objects of study
# What each phase actually holds in its hands, and what gets measured on it.
# Deliberately not isometric: this one is about the matter, not the machinery.
# =============================================================================

OUT2 = OUT.parent / "objects-of-study.svg"

OBJECTS = [
    ("S0", "Benchmark",  "a table of compounds",
     "activity, assay, decoy class", "glyph_table"),
    ("S1", "Complex",    "a predicted protein-ligand pose",
     "RMSD to crystal, confidence", "glyph_complex"),
    ("S2", "Pocket",     "a cropped binding-site shell",
     "contacts retained, net charge", "glyph_pocket"),
    ("S3", "Ensemble",   "the same pocket, many ways",
     "contact persistence, RMSF", "glyph_ensemble"),
    ("S4", "Microstates", "a few states, with weights",
     "cluster stability under bootstrap", "glyph_states"),
    ("S5", "Graph",      "the pocket as a 3D graph",
     "score, uncertainty, rank", "glyph_graph"),
    ("S6", "Density",    "the electrons, properly",
     "interaction energy, ESP", "glyph_density"),
    ("S7", "Correction", "cheap score against expensive truth",
     "error reduction per label", "glyph_correction"),
]


def hexring(cx, cy, r, **kw):
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
           for a in range(0, 360, 60)]
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    attrs = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in kw.items())
    return f'<polygon points="{d}" {attrs}/>'


def glyph_table(x, y):
    """A curated set: some actives, some decoys, some unknown."""
    g = [f'<g transform="translate({x},{y})">']
    fills = [SOUTH, "none", SOUTH, "none", "none", SOUTH, "none", "none", SOUTH, "none", "none", "none"]
    for i, f in enumerate(fills):
        cx, cy = 20 + (i % 4) * 34, 18 + (i // 4) * 34
        g.append(hexring(cx, cy, 11, fill=(f if f != "none" else "none"),
                         stroke=(SOFT if f == "none" else SOUTH), stroke_width=1.5,
                         opacity=(".55" if f == "none" else ".9")))
        g.append(f'<line x1="{cx+11:.0f}" y1="{cy}" x2="{cx+16:.0f}" y2="{cy}" '
                 f'stroke="{SOFT}" stroke-width="1.3" opacity=".5"/>')
    g.append(f'<text x="0" y="152" fill="{SOFT}" font-size="10.5" opacity=".75">'
             f'actives · decoys · non-selectives</text>')
    return "\n".join(g) + "</g>"


def protein_blob(op=".5", sw=1.7):
    """A rough protein silhouette with two helices."""
    return (f'<path d="M14 62 q-6 -32 20 -44 q26 -12 50 -2 q26 10 24 38 q-2 28 -26 36 '
            f'q-26 8 -46 0 q-20 -8 -22 -28 z" fill="none" stroke="{ON}" stroke-width="{sw}" '
            f'opacity="{op}"/>'
            f'<path d="M30 40 q8 -8 16 0 q8 8 16 0 q8 -8 16 0" fill="none" stroke="{ON}" '
            f'stroke-width="1.4" opacity="{op}"/>'
            f'<path d="M28 82 q8 -8 16 0 q8 8 16 0" fill="none" stroke="{ON}" stroke-width="1.4" '
            f'opacity="{op}"/>')


def glyph_complex(x, y):
    g = [f'<g transform="translate({x},{y})">', protein_blob()]
    g.append(f'<circle cx="60" cy="62" r="24" fill="none" stroke="{SOUTH}" stroke-width="1.1" '
             f'stroke-dasharray="3 3" opacity=".55"/>')
    g.append(hexring(60, 62, 11, fill=SOUTH, opacity=".9"))
    g.append(f'<text x="0" y="152" fill="{SOFT}" font-size="10.5" opacity=".75">'
             f'co-folded, with a confidence halo</text>')
    return "\n".join(g) + "</g>"


def glyph_pocket(x, y):
    """A wedge cut out of the protein, residues pointing in."""
    g = [f'<g transform="translate({x},{y})">', protein_blob(op=".16", sw=1.3)]
    g.append(f'<path d="M60 62 m-38 0 a38 38 0 0 1 76 0 a38 38 0 0 1 -76 0" fill="none" '
             f'stroke="{SOUTH}" stroke-width="1.6" stroke-dasharray="5 4" opacity=".8"/>')
    for a in range(0, 360, 45):
        r = math.radians(a)
        x1, y1 = 60 + 36 * math.cos(r), 62 + 36 * math.sin(r)
        x2, y2 = 60 + 20 * math.cos(r), 62 + 20 * math.sin(r)
        g.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{ON}" stroke-width="1.5" opacity=".6"/>')
        g.append(f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="2.4" fill="{ON}" opacity=".6"/>')
    g.append(hexring(60, 62, 9, fill=SOUTH, opacity=".85"))
    g.append(f'<line x1="60" y1="62" x2="{60+36*math.cos(math.radians(-60)):.1f}" '
             f'y2="{62+36*math.sin(math.radians(-60)):.1f}" stroke="{GOLD}" stroke-width="1.2" '
             f'opacity=".85"/>')
    g.append(f'<text x="86" y="34" fill="{GOLD}" font-size="10.5" font-weight="700">r</text>')
    g.append(f'<text x="0" y="152" fill="{SOFT}" font-size="10.5" opacity=".75">'
             f'10, 12 or 15 Å of protein</text>')
    return "\n".join(g) + "</g>"


def glyph_ensemble(x, y):
    g = [f'<g transform="translate({x},{y})">']
    for k, dx in enumerate((-9, -4.5, 0, 4.5, 9)):
        op = ".9" if k == 2 else ".22"
        col = SOUTH if k == 2 else ON
        g.append(f'<g transform="translate({dx},{dx*0.4:.1f})">'
                 f'<circle cx="60" cy="62" r="34" fill="none" stroke="{col}" stroke-width="1.5" '
                 f'opacity="{op}"/></g>')
    for a in (20, 110, 200, 290):
        r = math.radians(a)
        g.append(f'<line x1="{60+34*math.cos(r):.1f}" y1="{62+34*math.sin(r):.1f}" '
                 f'x2="{60+19*math.cos(r):.1f}" y2="{62+19*math.sin(r):.1f}" stroke="{ON}" '
                 f'stroke-width="1.4" opacity=".45"/>')
    g.append(hexring(60, 62, 9, fill=SOUTH, opacity=".8"))
    g.append(f'<text x="0" y="152" fill="{SOFT}" font-size="10.5" opacity=".75">'
             f'static, relaxed or learned</text>')
    return "\n".join(g) + "</g>"


def glyph_states(x, y):
    g = [f'<g transform="translate({x},{y})">']
    for i, (w, lab) in enumerate([(0.58, "0.58"), (0.29, "0.29"), (0.13, "0.13")]):
        cx = 24 + i * 40
        g.append(f'<circle cx="{cx}" cy="46" r="17" fill="none" stroke="{SOUTH if i==0 else ON}" '
                 f'stroke-width="1.6" opacity="{.9 if i==0 else .5}"/>')
        g.append(hexring(cx, 46, 6, fill=(SOUTH if i == 0 else ON),
                         opacity=(".8" if i == 0 else ".45")))
        g.append(f'<rect x="{cx-13}" y="74" width="26" height="{34*w:.0f}" rx="2" '
                 f'fill="{SOUTH if i==0 else ON}" opacity="{.75 if i==0 else .35}" '
                 f'transform="translate(0,{34-34*w:.0f})"/>')
        g.append(f'<text x="{cx}" y="120" fill="{SOFT}" font-size="9.5" text-anchor="middle" '
                 f'opacity=".7">{lab}</text>')
    g.append(f'<text x="0" y="152" fill="{SOFT}" font-size="10.5" opacity=".75">'
             f'weights, and do they hold up</text>')
    return "\n".join(g) + "</g>"


def glyph_graph(x, y):
    g = [f'<g transform="translate({x},{y})">']
    nodes = [(60, 26), (92, 46), (92, 80), (60, 98), (28, 80), (28, 46), (60, 62)]
    for i, (ax, ay) in enumerate(nodes):
        for bx, by in nodes[i + 1:]:
            if math.hypot(ax - bx, ay - by) < 45:
                g.append(f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{ON}" '
                         f'stroke-width="1" opacity=".3"/>')
    for ax, ay in nodes:
        g.append(f'<circle cx="{ax}" cy="{ay}" r="4.5" fill="{ON}" opacity=".65"/>')
    g.append(f'<circle cx="60" cy="62" r="6.5" fill="{SOUTH}"/>')
    g.append(f'<rect x="20" y="116" width="80" height="6" rx="3" fill="{ON}" opacity=".2"/>')
    g.append(f'<rect x="20" y="116" width="52" height="6" rx="3" fill="{SOUTH}" opacity=".85"/>')
    g.append(f'<line x1="44" y1="119" x2="82" y2="119" stroke="{GOLD}" stroke-width="1.4"/>')
    g.append(f'<line x1="44" y1="114" x2="44" y2="124" stroke="{GOLD}" stroke-width="1.4"/>')
    g.append(f'<line x1="82" y1="114" x2="82" y2="124" stroke="{GOLD}" stroke-width="1.4"/>')
    g.append(f'<text x="0" y="152" fill="{SOFT}" font-size="10.5" opacity=".75">'
             f'a score, with an interval on it</text>')
    return "\n".join(g) + "</g>"


def glyph_density(x, y):
    g = [f'<g transform="translate({x},{y})">']
    for i, rr in enumerate((30, 23, 16, 9)):
        g.append(f'<ellipse cx="42" cy="58" rx="{rr}" ry="{rr*0.78:.0f}" fill="none" '
                 f'stroke="{ACTION}" stroke-width="1.3" opacity="{.25 + i*0.17:.2f}"/>')
    for i, rr in enumerate((26, 19, 12)):
        g.append(f'<ellipse cx="86" cy="70" rx="{rr}" ry="{rr*0.8:.0f}" fill="none" '
                 f'stroke="#C0603A" stroke-width="1.3" opacity="{.28 + i*0.2:.2f}"/>')
    g.append(f'<text x="38" y="62" fill="{ACTION}" font-size="15" font-weight="800">−</text>')
    g.append(f'<text x="82" y="75" fill="#C0603A" font-size="15" font-weight="800">+</text>')
    g.append(hexring(64, 100, 8, fill="none", stroke=SOUTH, stroke_width=1.6, opacity=".8"))
    g.append(f'<text x="0" y="152" fill="{SOFT}" font-size="10.5" opacity=".75">'
             f'ΔE, partial charges, ESP</text>')
    return "\n".join(g) + "</g>"


def glyph_correction(x, y):
    g = [f'<g transform="translate({x},{y})">']
    g.append(f'<line x1="18" y1="104" x2="18" y2="20" stroke="{SOFT}" stroke-width="1.2" opacity=".5"/>')
    g.append(f'<line x1="18" y1="104" x2="112" y2="104" stroke="{SOFT}" stroke-width="1.2" opacity=".5"/>')
    g.append(f'<line x1="22" y1="100" x2="108" y2="26" stroke="{SOFT}" stroke-width="1.2" '
             f'stroke-dasharray="4 3" opacity=".45"/>')
    pts = [(36, 78), (52, 74), (66, 56), (82, 52), (96, 38)]
    for px, py in pts:
        tx, ty = 22 + (100 - py) * (86 / 74), py
        g.append(f'<circle cx="{px}" cy="{py}" r="3.4" fill="{ON}" opacity=".4"/>')
        g.append(f'<line x1="{px}" y1="{py}" x2="{min(tx,108):.0f}" y2="{py}" stroke="{SOUTH}" '
                 f'stroke-width="1.7" opacity=".9" marker-end="url(#ar3)"/>')
    g.append(f'<text x="0" y="152" fill="{SOFT}" font-size="10.5" opacity=".75">'
             f'gain per expensive label</text>')
    return "\n".join(g) + "</g>"


def build_objects() -> str:
    W, H = 1340, 830
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Inter,Helvetica Neue,Arial,sans-serif" role="img" '
         f'aria-label="What each phase of the pipeline actually holds, and what is measured on it">',
         '<title>Objects of study, phase by phase</title>',
         f'<rect width="{W}" height="{H}" fill="{VOID}"/>',
         '<defs><marker id="ar3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" '
         f'markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{SOUTH}"/>'
         '</marker></defs>']

    o.append(f'<text x="48" y="58" fill="{ON}" font-size="28" font-weight="800" '
             f'letter-spacing="-.5">Objects of study</text>')
    o.append(f'<text x="48" y="86" fill="{SOFT}" font-size="14.5">Each phase holds a different '
             f'kind of thing. What it is, and what we measure on it.</text>')

    # the targets, across the top
    o.append(f'<line x1="48" y1="112" x2="{W-48}" y2="112" stroke="{SOFT}" opacity=".2"/>')
    o.append(f'<text x="48" y="140" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.6">THE TARGETS</text>')
    for i, (name, primary) in enumerate([("CDK9", True), ("CDK7", False),
                                         ("CDK12", False), ("CDK13", False)]):
        cx = 210 + i * 108
        col = SOUTH if primary else "#5A6B9C"
        o.append(f'<circle cx="{cx}" cy="150" r="27" fill="none" stroke="{col}" '
                 f'stroke-width="{2 if primary else 1.4}" opacity="{.95 if primary else .55}"/>')
        for a in range(0, 360, 60):
            r = math.radians(a)
            o.append(f'<line x1="{cx+27*math.cos(r):.1f}" y1="{150+27*math.sin(r):.1f}" '
                     f'x2="{cx+16*math.cos(r):.1f}" y2="{150+16*math.sin(r):.1f}" stroke="{col}" '
                     f'stroke-width="1.3" opacity="{.7 if primary else .4}"/>')
        o.append(hexring(cx, 150, 8, fill=col, opacity=(".85" if primary else ".3")))
        o.append(f'<text x="{cx}" y="196" fill="{ON if primary else SOFT}" font-size="12.5" '
                 f'font-weight="{800 if primary else 600}" text-anchor="middle">{name}</text>')
    o.append(f'<text x="672" y="146" fill="{ON}" font-size="15" font-weight="700">'
             f'Same fold. Same ligand. Different answer.</text>')
    o.append(f'<text x="672" y="168" fill="{SOFT}" font-size="13.5">Bind the first one and not the '
             f'others, and the whole chain has to see</text>')
    o.append(f'<text x="672" y="186" fill="{SOFT}" font-size="13.5">a difference that a 2D '
             f'fingerprint throws away.</text>')
    o.append(f'<line x1="48" y1="224" x2="{W-48}" y2="224" stroke="{SOFT}" opacity=".2"/>')

    # eight panels, 4 x 2
    glyphs = {f.__name__: f for f in (glyph_table, glyph_complex, glyph_pocket, glyph_ensemble,
                                      glyph_states, glyph_graph, glyph_density, glyph_correction)}
    for i, (sid, name, obj, measured, gname) in enumerate(OBJECTS):
        col, row = i % 4, i // 4
        px, py = 48 + col * 322, 254 + row * 286
        o.append(f'<rect x="{px}" y="{py}" width="296" height="258" rx="8" fill="{PANEL}" '
                 f'opacity=".38"/>')
        o.append(f'<text x="{px+20}" y="{py+28}" font-size="13" font-weight="800">'
                 f'<tspan fill="{SOUTH}">{sid}</tspan>'
                 f'<tspan dx="9" fill="{ON}">{name}</tspan></text>')
        o.append(glyphs[gname](px + 24, py + 42))
        o.append(f'<text x="{px+20}" y="{py+222}" fill="{ON}" font-size="12.5" opacity=".9">'
                 f'{obj}</text>')
        o.append(f'<text x="{px+20}" y="{py+242}" fill="{GOLD}" font-size="11.5" opacity=".9">'
                 f'measured: {measured}</text>')
        if col < 3:
            o.append(f'<text x="{px+306}" y="{py+134}" fill="{SOFT}" font-size="17" '
                     f'opacity=".45">›</text>')

    o.append('</svg>')
    return "\n".join(o)


# =============================================================================
# Figure 3 — the scale trajectory
# Start small, explore the parameter space, scale only what survives.
# =============================================================================

OUT3 = OUT.parent / "scale-trajectory.svg"

TIERS = [
    ("Smoke test", "5 ligands · 2 targets · 1 pose",
     ["10–30 complexes", "5–10 quantum labels", "1–3 h on 8× H200"],
     "Do the containers run, do the formats line up", 0.30),
    ("Hackathon minimum", "12–20 ligands · 2 targets · 3 poses",
     ["72–120 complexes", "20–50 quantum labels", "~290 H200-hours"],
     "Do parameter changes move the ranking, is each stage feasible", 0.52),
    ("Useful pilot", "50–100 ligands · 4 targets · 3–5 states",
     ["600–2,000 complexes", "200–1,000 labels", "~1,600 H200-hours"],
     "Ranking stability, selectivity trend, cost per label", 0.75),
    ("Scale-up", "1k–10k candidates after filtering",
     ["5k–50k complexes", "5k–50k labels", "campaign scale"],
     "Operational throughput and candidate prioritisation", 1.00),
]

GATE_TEXT = [
    "Reproducible? Costs measured?",
    "Ranking beats 2D baseline?\nMotion and quantum earning their cost?",
    "Predictable enough to schedule?",
]


def build_trajectory() -> str:
    W, H = 1340, 790
    BASE, TOP = 556, 232
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Inter,Helvetica Neue,Arial,sans-serif" role="img" '
         f'aria-label="The scale trajectory from smoke test to scale-up, with gates between tiers">',
         '<title>Start small, then scale what survives</title>',
         f'<rect width="{W}" height="{H}" fill="{VOID}"/>']

    o.append(f'<text x="48" y="56" fill="{ON}" font-size="28" font-weight="800" '
             f'letter-spacing="-.5">Start small. Then scale what survives.</text>')
    o.append(f'<text x="48" y="84" fill="{SOFT}" font-size="14.5">Explore the parameter space where '
             f'it is cheap. Move up a tier only when the gate below it is green.</text>')

    cw = (W - 150) / len(TIERS)
    for i, (name, scope, nums, asks, h) in enumerate(TIERS):
        x = 80 + i * cw
        top = BASE - (BASE - TOP) * h
        surro = i < 2
        col = SOUTH if surro else "#4A5C8C"
        o.append(f'<rect x="{x:.0f}" y="{top:.0f}" width="{cw-42:.0f}" height="{BASE-top:.0f}" '
                 f'rx="5" fill="{col}" opacity="{.20 if not surro else .30}"/>')
        o.append(f'<rect x="{x:.0f}" y="{top:.0f}" width="{cw-42:.0f}" height="4" rx="2" '
                 f'fill="{col}"/>')
        o.append(f'<text x="{x+14:.0f}" y="{top-34:.0f}" fill="{ON}" font-size="16.5" '
                 f'font-weight="800">{name}</text>')
        o.append(f'<text x="{x+14:.0f}" y="{top-14:.0f}" fill="{SOUTH if surro else SOFT}" '
                 f'font-size="12">{scope}</text>')
        for k, n in enumerate(nums):
            o.append(f'<text x="{x+14:.0f}" y="{top+30+k*20:.0f}" fill="{ON}" font-size="12.5" '
                     f'opacity=".85">{n}</text>')
        o.append(f'<text x="{x+14:.0f}" y="{BASE+26:.0f}" fill="{SOFT}" font-size="11.5" '
                 f'font-weight="700" letter-spacing="1.2">WHAT IT ANSWERS</text>')
        for k, line in enumerate(_wrap(asks, 34)):
            o.append(f'<text x="{x+14:.0f}" y="{BASE+46+k*17:.0f}" fill="{SOFT}" '
                     f'font-size="12">{line}</text>')

        if i < len(TIERS) - 1:
            gx = x + cw - 34
            o.append(f'<line x1="{gx:.0f}" y1="{TOP-70:.0f}" x2="{gx:.0f}" y2="{BASE+16:.0f}" '
                     f'stroke="{GOLD}" stroke-width="1.2" stroke-dasharray="5 5" opacity=".55"/>')
            o.append(f'<circle cx="{gx:.0f}" cy="{TOP-82:.0f}" r="13" fill="{VOID}" '
                     f'stroke="{GOLD}" stroke-width="1.4"/>')
            o.append(f'<text x="{gx:.0f}" y="{TOP-77:.0f}" fill="{GOLD}" font-size="12" '
                     f'font-weight="800" text-anchor="middle">{i+1}</text>')
            for k, line in enumerate(GATE_TEXT[i].split("\n")):
                o.append(f'<text x="{gx:.0f}" y="{TOP-52+k*15:.0f}" fill="{GOLD}" font-size="11" '
                         f'text-anchor="middle" opacity=".85">{line}</text>')

    o.append(f'<text x="48" y="{BASE+120:.0f}" fill="{SOFT}" font-size="12.5" font-weight="700" '
             f'letter-spacing="1.4">THE POINT OF STARTING SMALL</text>')
    for k, line in enumerate([
            "Four configurations tell you nothing. Sixteen tell you nothing. A couple of hundred give a clean answer.",
            "Small experiments fail to transfer because they are under-explored, not because they are small.",
            "So the cheap tiers are where we search hard, and the expensive ones inherit what survived."]):
        o.append(f'<text x="48" y="{BASE+144+k*19:.0f}" fill="{ON}" font-size="13" opacity=".8">'
                 f'{line}</text>')
    o.append('</svg>')
    return "\n".join(o)


def _wrap(text: str, n: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines



# =============================================================================
# Figure 4 — the protein space
# Where our targets sit in the CDK family, and why whole-domain identity
# understates the problem. Numbers from data/protein-space.json, which
# tools/fetch_protein_space.py produces.
# =============================================================================

OUT4 = OUT.parent / "protein-space.svg"
DATA = Path(__file__).resolve().parent.parent / "data" / "protein-space.json"


def _ramp(v, lo=35.0, hi=100.0):
    """Identity to a colour on the panel-to-cyan ramp."""
    t = max(0.0, min(1.0, (v - lo) / (hi - lo)))
    a = (0x1D, 0x2A, 0x4F)
    b = (0x00, 0xD3, 0xF6)
    return "#%02X%02X%02X" % tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def build_protein_space() -> str:
    import json
    d = json.loads(DATA.read_text())
    order, reg, sid = d["order"], d["region_identity"], d["site_identity"]
    sres, spos = d["site_residues"], d["site_positions"]
    ours = {"CDK9", "CDK7", "CDK12", "CDK13"}

    W, H = 1340, 1040
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Inter,Helvetica Neue,Arial,sans-serif" role="img" '
         f'aria-label="Where CDK9 and its counter-targets sit in the CDK family">',
         '<title>The protein space</title>',
         f'<rect width="{W}" height="{H}" fill="{VOID}"/>']
    o.append(f'<text x="48" y="56" fill="{ON}" font-size="28" font-weight="800" '
             f'letter-spacing="-.5">The protein space</text>')
    o.append(f'<text x="48" y="84" fill="{SOFT}" font-size="14.5">Sequence identity across the CDK '
             f'family. Whole kinase region on the left, the 18 ATP-site positions on the right.</text>')

    # ---- heatmap -------------------------------------------------------------
    cell, hx, hy = 44, 150, 190
    o.append(f'<text x="48" y="{hy-40}" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.5">WHOLE KINASE REGION</text>')
    for j, b in enumerate(order):
        o.append(f'<text x="{hx+j*cell+cell/2:.0f}" y="{hy-10}" fill="{SOUTH if b in ours else SOFT}" '
                 f'font-size="10.5" font-weight="{800 if b in ours else 600}" '
                 f'text-anchor="middle" transform="rotate(-50 {hx+j*cell+cell/2:.0f} {hy-10})">{b}</text>')
    for i, a in enumerate(order):
        o.append(f'<text x="{hx-10}" y="{hy+i*cell+cell/2+4:.0f}" '
                 f'fill="{SOUTH if a in ours else SOFT}" font-size="10.5" '
                 f'font-weight="{800 if a in ours else 600}" text-anchor="end">{a}</text>')
        for j, b in enumerate(order):
            v = 100.0 if a == b else reg[f"{a}|{b}"]
            x, y = hx + j * cell, hy + i * cell
            o.append(f'<rect x="{x}" y="{y}" width="{cell-2}" height="{cell-2}" rx="2" '
                     f'fill="{_ramp(v)}" opacity="{0.35 if a==b else 0.95}"/>')
            if v >= 60 and a != b:
                o.append(f'<text x="{x+(cell-2)/2:.0f}" y="{y+(cell-2)/2+4:.0f}" fill="#062430" '
                         f'font-size="10.5" font-weight="800" text-anchor="middle">{v:.0f}</text>')
    # ring our four
    for i, a in enumerate(order):
        for j, b in enumerate(order):
            if a in ours and b in ours and a != b:
                o.append(f'<rect x="{hx+j*cell-1}" y="{hy+i*cell-1}" width="{cell}" height="{cell}" '
                         f'rx="3" fill="none" stroke="{GOLD}" stroke-width="1.6" opacity=".8"/>')
    o.append(f'<text x="{hx}" y="{hy+len(order)*cell+30}" fill="{GOLD}" font-size="12">'
             f'gold: our four targets</text>')

    # ---- paired bars ---------------------------------------------------------
    bx, by = 660, 190
    o.append(f'<text x="{bx}" y="{by-40}" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.5">CDK9 AGAINST EACH COUNTER-TARGET</text>')
    for k, b in enumerate(["CDK7", "CDK12", "CDK13"]):
        y = by + k * 74
        o.append(f'<text x="{bx}" y="{y+4}" fill="{ON}" font-size="13.5" font-weight="700">{b}</text>')
        for m, (lab, v, col) in enumerate([("region", reg[f"CDK9|{b}"], "#4A5C8C"),
                                           ("ATP site", sid[f"CDK9|{b}"], SOUTH)]):
            yy = y + 18 + m * 22
            o.append(f'<text x="{bx+80}" y="{yy+9}" fill="{SOFT}" font-size="11" '
                     f'text-anchor="end">{lab}</text>')
            o.append(f'<rect x="{bx+90}" y="{yy}" width="380" height="13" rx="3" fill="{PANEL}"/>')
            o.append(f'<rect x="{bx+90}" y="{yy}" width="{380*v/100:.0f}" height="13" rx="3" '
                     f'fill="{col}" opacity=".95"/>')
            o.append(f'<text x="{bx+480}" y="{yy+11}" fill="{ON}" font-size="11.5" '
                     f'font-weight="700">{v:.0f}%</text>')
    o.append(f'<text x="{bx}" y="{by+232}" fill="{ON}" font-size="13.5" opacity=".9">'
             f'The pocket is far more conserved than the domain around it.</text>')
    o.append(f'<text x="{bx}" y="{by+252}" fill="{SOFT}" font-size="13">'
             f'Whole-region identity understates how hard this is.</text>')

    # ---- ATP-site residue strip ---------------------------------------------
    sy = 800
    o.append(f'<text x="48" y="{sy-52}" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.5">THE 18 ATP-SITE POSITIONS</text>')
    keys = sorted(spos, key=int)
    cw2, sx = 46, 160
    for j, p in enumerate(keys):
        x = sx + j * cw2
        role = spos[p]
        o.append(f'<text x="{x+cw2/2:.0f}" y="{sy+2}" fill="{SOFT}" font-size="9" '
                 f'text-anchor="middle" opacity=".7">{p}</text>')
        if role not in ("—",):
            o.append(f'<text x="{x+cw2/2:.0f}" y="{sy-14}" fill="{GOLD if "hinge" in role or "gate" in role else SOFT}" '
                     f'font-size="8.5" text-anchor="middle" opacity=".8" '
                     f'transform="rotate(-45 {x+cw2/2:.0f} {sy-14})">{role}</text>')
    for i, n in enumerate(["CDK9", "CDK7", "CDK12", "CDK13"]):
        y = sy + 18 + i * 30
        o.append(f'<text x="{sx-12}" y="{y+16}" fill="{SOUTH if n=="CDK9" else ON}" '
                 f'font-size="12" font-weight="{800 if n=="CDK9" else 600}" '
                 f'text-anchor="end">{n}</text>')
        for j, p in enumerate(keys):
            x = sx + j * cw2
            r = sres[n].get(p, "?")
            same = (r == sres["CDK9"].get(p))
            fill = SOUTH if (n == "CDK9") else (PANEL if same else "#8A5A2B")
            op = ".85" if n == "CDK9" else (".5" if same else ".95")
            o.append(f'<rect x="{x}" y="{y}" width="{cw2-4}" height="24" rx="3" fill="{fill}" '
                     f'opacity="{op}"/>')
            o.append(f'<text x="{x+(cw2-4)/2:.0f}" y="{y+17}" '
                     f'fill="{"#062430" if n=="CDK9" else ON}" font-size="12.5" '
                     f'font-weight="{800 if not same and n!="CDK9" else 600}" '
                     f'text-anchor="middle">{r}</text>')
    o.append(f'<text x="{sx}" y="{sy+160}" fill="{SOFT}" font-size="12">'
             f'orange: differs from CDK9. The hinge is where CDK12 and CDK13 diverge; '
             f'CDK7 matches CDK9 there and differs elsewhere.</text>')

    # ---- the harder pair -----------------------------------------------------
    o.append(f'<rect x="{bx}" y="{by+282}" width="622" height="86" rx="6" fill="{PANEL}" opacity=".5"/>')
    o.append(f'<text x="{bx+20}" y="{by+310}" fill="{GOLD}" font-size="13.5" font-weight="800">'
             f'A harder pair sits in the same family</text>')
    o.append(f'<text x="{bx+20}" y="{by+332}" fill="{ON}" font-size="13">'
             f'CDK8 and CDK19 are identical at all 18 ATP-site positions '
             f'({sid["CDK8|CDK19"]:.0f}%).</text>')
    o.append(f'<text x="{bx+20}" y="{by+352}" fill="{SOFT}" font-size="12.5">'
             f'CDK4 / CDK6 sit at {sid["CDK4|CDK6"]:.0f}%. Natural scale-up targets once the '
             f'chain holds on ours.</text>')

    o.append(f'<text x="48" y="{H-26}" fill="{SOFT}" font-size="11" opacity=".65">'
             f'UniProt sequences. ATP-site positions mapped from CDK2 by sequence alignment, not '
             f'structural superposition, so treat as indicative. '
             f'tools/fetch_protein_space.py → data/protein-space.json</text>')
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    for path, fn in ((OUT, build), (OUT2, build_objects), (OUT3, build_trajectory),
                     (OUT4, build_protein_space)):
        path.write_text(fn())
        print(f"wrote {path.relative_to(Path.cwd())}  ({path.stat().st_size:,} bytes)")
