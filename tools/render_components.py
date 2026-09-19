#!/usr/bin/env python3
"""Component-scale views of the CDK9 site, from deposited coordinates.

    python3 tools/render_components.py

Writes  docs/03-pipeline/figures/zoom-ladder.svg
        docs/03-pipeline/figures/pocket-anatomy.svg
        data/pocket-anatomy.json

Why these and not another ribbon. A whole-protein picture says nothing about
what the pipeline actually operates on, because every stage works at a different
scale. S2 crops a shell. S5 scores contacts. S6 sends a few dozen atoms to a
quantum code. Those are different objects and they cost different amounts, so
they get drawn separately with their atom counts attached.

The second figure is the selectivity question at residue resolution: the twenty
residues lining the CDK9 site, and what sits at the same place in the three
counter-targets. Equivalence here is by structural superposition (CEalign), not
sequence alignment, which is the caveat on docs/03-pipeline/figures/protein-space.svg.

Needs: biopython, numpy. Network on first run; structures cache under .cache/pdb.
"""
from __future__ import annotations

import json
import math
import urllib.request
from datetime import date
from pathlib import Path

import numpy as np
from Bio.PDB import MMCIFParser, Model, Structure
from Bio.PDB.cealign import CEAligner

ROOT = Path(__file__).resolve().parent.parent
FIGS = ROOT / "docs/03-pipeline/figures"
DATA = ROOT / "data/pocket-anatomy.json"
CACHE = ROOT / ".cache" / "pdb"

VOID, PANEL, ON, SOFT = "#141C36", "#1D2A4F", "#EEF1FB", "#9AA7CD"
SOUTH, GOLD, ACTION = "#00D3F6", "#C79A4D", "#3F5FBC"

REF = ("CDK9", "3blr", "2.8 Å")
OTHERS = [("CDK7", "1ua2", "3.0 Å"), ("CDK12", "4nst", "2.2 Å"), ("CDK13", "5efq", "2.0 Å")]
LIGAND = "CPB"                       # flavopiridol, as deposited in 3BLR
PHOSPHO = {"TPO", "SEP", "PTR"}

# Roles are the standard kinase anatomy, assigned from the structure rather than
# from a sequence motif. Colour follows the role, not the residue.
ROLES = {
    "roof":    ("#8AA0E6", "G-loop and β-sheet roof"),
    "cat":     ("#B8C4E8", "β3 lysine and αC"),
    "gate":    (GOLD,      "gatekeeper"),
    "hinge":   (SOUTH,     "hinge"),
    "floor":   ("#8B7CF6", "floor and catalytic loop"),
    "dfg":     ("#E0A96D", "DFG"),
}
ROLE_OF = {25: "roof", 26: "roof", 30: "roof", 33: "roof",
           46: "cat", 48: "cat", 79: "cat",
           103: "gate",
           104: "hinge", 105: "hinge", 106: "hinge", 107: "hinge", 108: "hinge", 109: "hinge",
           151: "floor", 153: "floor", 154: "floor", 156: "floor",
           166: "dfg", 167: "dfg"}

ELEMENT = {"C": "#C7D0EA", "N": "#6FA8FF", "O": "#FF8A7A", "S": "#F2D06B",
           "CL": "#7FE6A6", "F": "#7FE6A6", "P": "#F2A65A"}

ONE = {"ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q",
       "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K",
       "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W",
       "TYR": "Y", "VAL": "V", "TPO": "T", "SEP": "S", "PTR": "Y"}


def fetch(pdb: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{pdb}.cif"
    if not f.exists():
        url = f"https://files.rcsb.org/download/{pdb.upper()}.cif"
        with urllib.request.urlopen(url, timeout=60) as r:
            f.write_bytes(r.read())
    return f


def model_of(pdb: str):
    return MMCIFParser(QUIET=True).get_structure(pdb, fetch(pdb))[0]


def kinase_chain(model):
    """The longest protein chain, which is the kinase rather than the cyclin."""
    best, n = None, 0
    for ch in model:
        cas = [r for r in ch if "CA" in r and r.id[0] == " "]
        if len(cas) > n:
            best, n = ch, len(cas)
    return best


def residues(chain):
    """Protein residues, counting phosphorylated ones as part of the chain."""
    return [r for r in chain if r.id[0] == " " or r.resname.strip() in PHOSPHO]


def heavy(res):
    return [a for a in res if a.element != "H"]


def lone(chain) -> Structure.Structure:
    """A one-chain structure, so CEalign superposes kinase onto kinase."""
    s = Structure.Structure("x")
    m = Model.Model(0)
    s.add(m)
    m.add(chain.copy())
    return s


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------- measurement

def shell(prot, lig_xyz, cutoff):
    """Whole residues with any heavy atom inside `cutoff` of any ligand atom.

    Whole residues, because a crop that cuts a sidechain in half hands the next
    stage a radical. S2 has to decide how to cap; this is the count before capping.
    """
    keep = []
    for cid, r in prot:
        C = np.array([a.coord for a in heavy(r)])
        if not len(C):
            continue
        if np.linalg.norm(C[:, None, :] - lig_xyz[None, :, :], axis=2).min() < cutoff:
            keep.append((cid, r))
    return keep


def measure():
    """Atom counts at every scale the pipeline works at. All [measured]."""
    m = model_of(REF[1])
    kin = kinase_chain(m)
    lig = [r for ch in m for r in ch if r.resname.strip() == LIGAND][0]
    lig_atoms = heavy(lig)
    lig_xyz = np.array([a.coord for a in lig_atoms])

    prot_all = [(ch.id, r) for ch in m for r in residues(ch)]
    prot_kin = [(kin.id, r) for r in residues(kin)]

    levels = []
    levels.append(dict(key="complex", label="Complex", radius=None, stage="S1",
                       caption="what co-folding hands us",
                       residues=len(prot_all),
                       atoms=sum(len(heavy(r)) for _, r in prot_all) + len(lig_atoms),
                       chains=sorted({c for c, _ in prot_all})))
    for cut, stage, cap in ((15, "S2", "outer crop"), (10, "S2", "the value we sweep"),
                            (6, "S5", "what scoring sees"), (4, "S6", "what quantum gets")):
        keep = shell(prot_all, lig_xyz, cut)
        levels.append(dict(key=f"crop{cut}", label=f"Crop {cut} Å", radius=cut, stage=stage,
                           caption=cap, residues=len(keep),
                           atoms=sum(len(heavy(r)) for _, r in keep) + len(lig_atoms),
                           chains=sorted({c for c, _ in keep})))
    levels.append(dict(key="ligand", label="Ligand", radius=0, stage="S7",
                       caption="the thing being labelled", residues=1,
                       atoms=len(lig_atoms), chains=[]))

    # the pocket lining, and what sits at the same place in the counter-targets
    ref_res = {r.id[1]: r for r in residues(kin)}
    al = CEAligner()
    al.set_reference(lone(kin))
    equiv, rms = {}, {}
    for name, pdb, _ in OTHERS:
        s = lone(kinase_chain(model_of(pdb)))
        al.align(s)
        rms[name] = round(float(al.rms), 2)
        moved = [r for r in next(s[0].get_chains()) if "CA" in r and r.id[0] == " "]
        ca = np.array([r["CA"].coord for r in moved])
        row = {}
        for pos in ROLE_OF:
            if pos not in ref_res or "CA" not in ref_res[pos]:
                continue
            d = np.linalg.norm(ca - ref_res[pos]["CA"].coord, axis=1)
            j = int(d.argmin())
            row[pos] = dict(resname=moved[j].resname.strip(), number=moved[j].id[1],
                            ca_offset_A=round(float(d[j]), 2))
        equiv[name] = row

    pocket = []
    for pos in sorted(ROLE_OF):
        if pos not in ref_res:
            continue
        r = ref_res[pos]
        C = np.array([a.coord for a in heavy(r)])
        pocket.append(dict(
            position=pos, resname=r.resname.strip(), role=ROLE_OF[pos],
            min_dist_A=round(float(np.linalg.norm(C[:, None, :] - lig_xyz[None, :, :],
                                                  axis=2).min()), 2),
            equivalents={n: equiv[n].get(pos) for n, _, _ in OTHERS}))

    # A wider sweep than the figure shows, because WP-B needs the curve and the
    # figure only has room for six panels.
    sweep = []
    for cut in (4, 5, 6, 8, 10, 12, 15, 18, 20):
        keep = shell(prot_all, lig_xyz, cut)
        n = sum(len(heavy(r)) for _, r in keep) + len(lig_atoms)
        sweep.append(dict(radius_A=cut, residues=len(keep), heavy_atoms=n,
                          chains=sorted({c for c, _ in keep})))
    base = next(x["heavy_atoms"] for x in sweep if x["radius_A"] == 4)
    for x in sweep:
        x["relative_cost_n3"] = round((x["heavy_atoms"] / base) ** 3, 1)

    return dict(
        generated=str(date.today()),
        tool="tools/render_components.py",
        reference=dict(target=REF[0], pdb=REF[1].upper(), resolution=REF[2], ligand=LIGAND,
                       ligand_name="flavopiridol", ligand_heavy_atoms=len(lig_atoms)),
        counter_targets=[dict(target=n, pdb=p.upper(), resolution=r,
                              cealign_rms_A=rms[n]) for n, p, r in OTHERS],
        method=("Whole residues with any heavy atom within the cutoff of any ligand heavy atom. "
                "Hydrogens excluded throughout; deposited structures at this resolution do not "
                "have them. Cross-target equivalence by CEalign superposition, nearest Cα."),
        levels=levels, radius_sweep=sweep, pocket=pocket)


# ------------------------------------------------------------- the zoom ladder

def bands(segs, colour, width, opacity, n=6):
    """Depth-cued segments as a handful of grouped paths rather than thousands of
    lines. Same picture, an order of magnitude less SVG."""
    if not segs:
        return []
    zs = [s[0] for s in segs]
    lo, hi = min(zs), max(zs)
    out, buckets = [], [[] for _ in range(n)]
    for z, x1, y1, x2, y2 in segs:
        t = (z - lo) / (hi - lo) if hi > lo else 0.5
        buckets[min(int(t * n), n - 1)].append((x1, y1, x2, y2))
    for k, b in enumerate(buckets):
        if not b:
            continue
        t = (k + 0.5) / n
        d = " ".join(f"M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" for x1, y1, x2, y2 in b)
        out.append(f'<g stroke="{colour}" stroke-width="{width(t):.2f}" '
                   f'opacity="{opacity(t):.2f}" stroke-linecap="round" fill="none">'
                   f'<path d="{d}"/></g>')
    return out


def trace(X, Y, Z, colour, width, opacity, gap):
    """gap is the pixel distance above which two consecutive Cα are treated as a
    chain break. It scales with the zoom — a fixed value eats the whole trace the
    moment you magnify past about 9 px per Å."""
    segs = [((Z[k] + Z[k+1]) / 2, X[k], Y[k], X[k+1], Y[k+1]) for k in range(len(X) - 1)
            if math.dist((X[k], Y[k]), (X[k+1], Y[k+1])) < gap]
    return bands(segs, colour, width, opacity)


def bonds(atoms, cut=1.95):
    xyz = np.array([a.coord for a in atoms])
    d = np.linalg.norm(xyz[:, None, :] - xyz[None, :, :], axis=2)
    return [(i, j) for i in range(len(atoms)) for j in range(i + 1, len(atoms))
            if d[i, j] < cut]


def zoom_ladder(meas) -> str:
    m = model_of(REF[1])
    lig = [r for ch in m for r in ch if r.resname.strip() == LIGAND][0]
    lig_atoms = heavy(lig)
    lig_xyz = np.array([a.coord for a in lig_atoms])
    prot = [(ch.id, r) for ch in m for r in residues(ch)]
    kin_id = kinase_chain(m).id

    # one orientation for every panel, set by the pocket, so this reads as a zoom
    pocket_xyz = np.vstack([np.array([a.coord for a in heavy(r)])
                            for _, r in shell(prot, lig_xyz, 10)])
    centre = lig_xyz.mean(axis=0)
    _, _, vt = np.linalg.svd(pocket_xyz - pocket_xyz.mean(axis=0))
    basis = vt[:3]

    def proj(xyz):
        p = (np.atleast_2d(xyz) - centre) @ basis.T
        return p[:, 0], p[:, 1], p[:, 2]

    PW, PH, GAP, TOP = 248, 290, 12, 132
    W = 34 * 2 + 6 * PW + 5 * GAP
    H = TOP + PH + 292

    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Inter,Helvetica Neue,Arial,sans-serif" role="img" aria-label="Six scales '
         f'of the CDK9 site, from the whole complex down to the quantum region, with heavy-atom '
         f'counts and the pipeline stage that works at each scale">',
         '<title>What each stage actually holds</title>',
         f'<rect width="{W}" height="{H}" fill="{VOID}"/>',
         f'<text x="34" y="52" fill="{ON}" font-size="27" font-weight="800" letter-spacing="-.5">'
         f'One site, six scales</text>',
         f'<text x="34" y="80" fill="{SOFT}" font-size="14">Every stage works on a different '
         f'object. Same camera, same centre, same structure — only the radius changes. '
         f'CDK9 with flavopiridol, 3BLR.</text>',
         f'<text x="34" y="102" fill="{SOFT}" font-size="14">Bright is kept, dim is discarded. '
         f'Counts are heavy atoms, measured, not estimated.</text>']

    qm = next(l for l in meas["levels"] if l["key"] == "crop4")["atoms"]

    for i, lev in enumerate(meas["levels"]):
        px, py = 34 + i * (PW + GAP), TOP
        keep_set = set()
        if lev["radius"] is None:
            keep = prot
        elif lev["radius"] == 0:
            keep = []
        else:
            keep = shell(prot, lig_xyz, lev["radius"])
        keep_set = {id(r) for _, r in keep}
        sticks = lev["radius"] is not None and lev["radius"] <= 6

        # frame on what survives, so each panel fills its box
        frame = np.vstack([lig_xyz] + ([np.array([a.coord for a in heavy(r)])
                                        for _, r in keep] if keep else []))
        fx, fy, _ = proj(frame)
        span = max(fx.max() - fx.min(), fy.max() - fy.min(), 6.0) * 1.12
        sc = min(PW - 30, PH - 96) / span
        mx, my = (fx.min() + fx.max()) / 2, (fy.min() + fy.max()) / 2

        def S(xyz):
            x, y, z = proj(xyz)
            return px + PW / 2 + (x - mx) * sc, py + 44 + (PH - 96) / 2 + (y - my) * sc, z

        o.append(f'<rect x="{px}" y="{py}" width="{PW}" height="{PH}" rx="8" fill="{PANEL}" '
                 f'opacity="{0.6 if lev["radius"] in (10, 4) else 0.34}"/>')
        brk = max(18.0, sc * 6.0)
        o.append(f'<clipPath id="clip{i}"><rect x="{px+1}" y="{py+34}" width="{PW-2}" '
                 f'height="{PH-76}"/></clipPath>')
        o.append(f'<g clip-path="url(#clip{i})">')

        # discarded material, faint, so the boundary is visible rather than asserted
        if lev["radius"] is not None:
            for cid in sorted({c for c, _ in prot}):
                drop = [r for c, r in prot if c == cid and id(r) not in keep_set and "CA" in r]
                if len(drop) < 2:
                    continue
                X, Y, Z = S(np.array([r["CA"].coord for r in drop]))
                o += trace(X, Y, Z, SOFT, lambda t: 1.0, lambda t: 0.10 + 0.06 * t, gap=brk)

        if keep and not sticks:
            # chains drawn separately, so the cyclin disappearing at the first crop
            # is something you can see rather than something the caption claims
            for cid in sorted({c for c, _ in keep}):
                ca = [r["CA"].coord for c, r in keep if c == cid and "CA" in r]
                if len(ca) < 2:
                    continue
                X, Y, Z = S(np.array(ca))
                o += trace(X, Y, Z, SOUTH if cid == kin_id else ACTION,
                           lambda t: 0.9 + 1.9 * t, lambda t: 0.20 + 0.50 * t, gap=brk)
        elif keep:
            at = [a for _, r in keep for a in heavy(r)]
            X, Y, Z = S(np.array([a.coord for a in at]))
            segs = [((Z[a] + Z[b]) / 2, X[a], Y[a], X[b], Y[b]) for a, b in bonds(at)]
            o += bands(segs, SOUTH, lambda t: 1.0 + 1.3 * t, lambda t: 0.24 + 0.44 * t)

        # the ligand, always, at every scale
        LX, LY, LZ = S(lig_xyz)
        lw = 4.2 if lev["radius"] == 0 else (2.6 if sticks else 2.0)
        for a, b in bonds(lig_atoms):
            o.append(f'<line x1="{LX[a]:.1f}" y1="{LY[a]:.1f}" x2="{LX[b]:.1f}" y2="{LY[b]:.1f}" '
                     f'stroke="{GOLD}" stroke-width="{lw}" stroke-linecap="round" opacity=".95"/>')
        for k, a in enumerate(lig_atoms):
            col = ELEMENT.get(a.element.upper(), GOLD) if lev["radius"] == 0 else GOLD
            o.append(f'<circle cx="{LX[k]:.1f}" cy="{LY[k]:.1f}" '
                     f'r="{3.4 if lev["radius"]==0 else 2.1}" fill="{col}"/>')
        o.append('</g>')

        # heading and the numbers
        o.append(f'<text x="{px+16}" y="{py+27}" font-size="15" font-weight="800" fill="{ON}">'
                 f'{esc(lev["label"])}</text>')
        o.append(f'<text x="{px+PW-16}" y="{py+27}" text-anchor="end" font-size="12" '
                 f'font-weight="800" fill="{SOUTH if lev["stage"] in ("S2","S5","S6") else SOFT}">'
                 f'{lev["stage"]}</text>')
        o.append(f'<text x="{px+16}" y="{py+PH-38}" font-size="20" font-weight="800" fill="{ON}">'
                 f'{lev["atoms"]:,}<tspan dx="5" font-size="11" font-weight="600" fill="{SOFT}">'
                 f'heavy atoms</tspan></text>')
        res = f'{lev["residues"]} residues' if lev["radius"] != 0 else '1 molecule'
        if lev["key"] == "complex":
            o.append(f'<text x="{px+16}" y="{py+PH-60}" font-size="11" fill="{ACTION}" '
                     f'font-weight="700">cyclin T1<tspan dx="8" fill="{SOUTH}">CDK9</tspan></text>')
        o.append(f'<text x="{px+16}" y="{py+PH-20}" font-size="11.5" fill="{SOFT}">'
                 f'{res} · {esc(lev["caption"])}</text>')

    return o, W, H, TOP + PH, qm


def zoom_ladder_svg(meas) -> str:
    o, W, H, y0, qm = zoom_ladder(meas)
    y = y0 + 44
    o.append(f'<line x1="34" y1="{y0+20}" x2="{W-34}" y2="{y0+20}" stroke="{SOFT}" opacity=".2"/>')
    o.append(f'<text x="34" y="{y}" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.4">WHAT THE RADIUS COSTS</text>')

    # Cost, relative to the 4 Å region, on an N^3 scaling. Cubic is the polite
    # end of the range for hybrid DFT; the point is the exponent, not the digit.
    bars = [l for l in meas["levels"] if l["key"].startswith("crop")]
    bw = W - 130 - 34 - 345
    top = max(l["atoms"] for l in bars)
    for k, l in enumerate(bars):
        by = y + 24 + k * 30
        frac = l["atoms"] / top
        o.append(f'<text x="34" y="{by+12}" fill="{ON}" font-size="12.5" font-weight="700">'
                 f'{esc(l["label"])}</text>')
        o.append(f'<rect x="130" y="{by}" width="{bw*frac:.0f}" height="15" rx="3" '
                 f'fill="{SOUTH}" opacity="{0.28+0.5*frac:.2f}"/>')
        o.append(f'<text x="{130+bw*frac+10:.0f}" y="{by+12}" fill="{SOFT}" font-size="12">'
                 f'{l["atoms"]:,} atoms<tspan dx="12" fill="{GOLD}" font-weight="700">'
                 f'≈{(l["atoms"]/qm)**3:,.0f}×</tspan>'
                 f'<tspan dx="6" fill="{SOFT}">quantum cost</tspan></text>')

    yb = y + 24 + len(bars) * 30 + 24
    for k, line in enumerate([
        "Crop radius is not a setting to be guessed. Between 4 and 15 Å the quantum cost moves by "
        "more than two orders of magnitude, and nobody has told us where the accuracy stops improving.",
        "That is why s2.crop_radius_A is swept rather than chosen. See docs/04-experiments/hpo-microtopic.md.",
        "Cost is a cubic scaling on atom count, relative to the 4 Å region. Indicative, not a benchmark — "
        "day 1 replaces it with wall-clock. Hydrogens are absent at this resolution and roughly double every count.",
        "No cyclin T1 residue falls inside 15 Å — the first one appears at 18. Every radius we are "
        "considering drops the cyclin, and the cyclin is what holds the αC helix in place.",
    ]):
        o.append(f'<text x="34" y="{yb+k*19}" fill="{ON if k < 2 else SOFT}" font-size="12.5" '
                 f'opacity="{0.85 if k < 2 else 0.62}">{esc(line)}</text>')
    o.append('</svg>')
    return "\n".join(o)


# ---------------------------------------------------------- the pocket anatomy

def pocket_anatomy_svg(meas) -> str:
    m = model_of(REF[1])
    kin = kinase_chain(m)
    lig = [r for ch in m for r in ch if r.resname.strip() == LIGAND][0]
    lig_atoms = heavy(lig)
    lig_xyz = np.array([a.coord for a in lig_atoms])
    ref_res = {r.id[1]: r for r in residues(kin)}

    rows = meas["pocket"]
    uniq = [p for p in rows
            if all(e and e["resname"] != p["resname"] for e in p["equivalents"].values())]

    pk_xyz = np.vstack([np.array([a.coord for a in heavy(ref_res[p["position"]])]) for p in rows])
    centre = np.vstack([pk_xyz, lig_xyz]).mean(axis=0)
    _, _, vt = np.linalg.svd(np.vstack([pk_xyz, lig_xyz]) - centre)
    basis = vt[:3]

    def proj(xyz):
        p = (np.atleast_2d(xyz) - centre) @ basis.T
        return p[:, 0], p[:, 1], p[:, 2]

    PX, PY, PWD, PHT = 48, 130, 666, 496
    fx, fy, _ = proj(np.vstack([pk_xyz, lig_xyz]))
    span = max(fx.max() - fx.min(), fy.max() - fy.min()) * 1.06
    sc = min(300, PHT - 120) / span
    mx, my = (fx.min() + fx.max()) / 2, (fy.min() + fy.max()) / 2
    ox, oy = PX + PWD / 2, PY + 46 + (PHT - 90) / 2

    def S(xyz):
        x, y, z = proj(xyz)
        return ox + (x - mx) * sc, oy + (y - my) * sc, z

    W, H = 1432, 980
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Inter,Helvetica Neue,Arial,sans-serif" role="img" aria-label="The twenty '
         f'residues lining the CDK9 ATP site, and the structurally equivalent residue in CDK7, '
         f'CDK12 and CDK13">',
         '<title>The pocket, residue by residue</title>',
         f'<rect width="{W}" height="{H}" fill="{VOID}"/>',
         f'<text x="34" y="52" fill="{ON}" font-size="27" font-weight="800" letter-spacing="-.5">'
         f'The pocket, residue by residue</text>',
         f'<text x="34" y="80" fill="{SOFT}" font-size="14">Twenty residues line the CDK9 site '
         f'within 5 Å of flavopiridol. Selectivity is decided here, not across the domain.</text>',
         f'<text x="34" y="102" fill="{SOFT}" font-size="14">Equivalence across targets is by '
         f'structural superposition, nearest Cα after CEalign — not by sequence alignment.</text>',
         f'<rect x="{PX}" y="{PY}" width="{PWD}" height="{PHT}" rx="8" fill="{PANEL}" opacity=".45"/>']

    # The chain running through, clipped to a disc. Two jobs: the pocket gets
    # somewhere to sit, and the panel reads as a magnification of the structure
    # figure rather than a diagram invented next to it.
    lens_r = 236
    o.append(f'<clipPath id="lens"><circle cx="{ox:.0f}" cy="{oy:.0f}" r="{lens_r}"/></clipPath>')
    o.append('<g clip-path="url(#lens)">')
    ctx = [r for r in residues(kinase_chain(m)) if "CA" in r]
    X, Y, Z = S(np.array([r["CA"].coord for r in ctx]))
    o += trace(X, Y, Z, SOFT, lambda t: 1.5, lambda t: 0.20 + 0.20 * t, gap=sc * 6.0)
    o.append('</g>')
    o.append(f'<circle cx="{ox:.0f}" cy="{oy:.0f}" r="{lens_r}" fill="none" stroke="{SOFT}" '
             f'stroke-width="1" opacity=".22"/>')

    # ligand next, it is the thing everything else is measured against
    LX, LY, _ = S(lig_xyz)
    for a, b in bonds(lig_atoms):
        o.append(f'<line x1="{LX[a]:.1f}" y1="{LY[a]:.1f}" x2="{LX[b]:.1f}" y2="{LY[b]:.1f}" '
                 f'stroke="{GOLD}" stroke-width="3.2" stroke-linecap="round" opacity=".95"/>')
    for k, a in enumerate(lig_atoms):
        o.append(f'<circle cx="{LX[k]:.1f}" cy="{LY[k]:.1f}" r="2.6" '
                 f'fill="{ELEMENT.get(a.element.upper(), GOLD)}"/>')

    # each residue as a stub from Cα to sidechain centroid, dotted at the business end
    nodes = []
    for p in rows:
        r = ref_res[p["position"]]
        side = [a for a in heavy(r) if a.name not in ("N", "C", "O")] or heavy(r)
        cx, cy, cz = S(np.array([np.array([a.coord for a in side]).mean(axis=0)]))
        ax, ay, _ = S(np.array([r["CA"].coord])) if "CA" in r else (cx, cy, cz)
        nodes.append(dict(p=p, x=float(cx[0]), y=float(cy[0]), z=float(cz[0]),
                          ax=float(ax[0]), ay=float(ay[0]),
                          col=ROLES[p["role"]][0], unique=p in uniq))
    for n in sorted(nodes, key=lambda n: n["z"]):
        o.append(f'<line x1="{n["ax"]:.1f}" y1="{n["ay"]:.1f}" x2="{n["x"]:.1f}" y2="{n["y"]:.1f}" '
                 f'stroke="{n["col"]}" stroke-width="2" stroke-linecap="round" opacity=".5"/>')
        rr = 7.5 if n["unique"] else 5.5
        o.append(f'<circle cx="{n["x"]:.1f}" cy="{n["y"]:.1f}" r="{rr}" fill="{n["col"]}" '
                 f'opacity="{0.95 if n["unique"] else 0.7}"/>')
        if n["unique"]:
            o.append(f'<circle cx="{n["x"]:.1f}" cy="{n["y"]:.1f}" r="12" fill="none" '
                     f'stroke="{n["col"]}" stroke-width="1.5" opacity=".6"/>')

    # labels in two columns, leader-lined, so nothing collides with the structure
    left = sorted(sorted(nodes, key=lambda n: n["x"])[:10], key=lambda n: n["y"])
    right = sorted(sorted(nodes, key=lambda n: n["x"])[10:], key=lambda n: n["y"])
    for col, xs, anchor in ((left, PX + 14, "start"), (right, PX + PWD - 14, "end")):
        step = (PHT - 130) / max(len(col) - 1, 1)
        for k, n in enumerate(col):
            ly = PY + 74 + k * step
            lx = xs + (54 if anchor == "start" else -54)
            o.append(f'<line x1="{lx:.0f}" y1="{ly:.0f}" x2="{n["x"]:.1f}" y2="{n["y"]:.1f}" '
                     f'stroke="{n["col"]}" stroke-width="1" opacity=".28"/>')
            nm = f'{n["p"]["resname"].title()}{n["p"]["position"]}'
            o.append(f'<text x="{xs}" y="{ly+4:.0f}" text-anchor="{anchor}" font-size="12.5" '
                     f'font-weight="{800 if n["unique"] else 600}" fill="{n["col"]}">{nm}'
                     f'<tspan dx="6" font-size="10.5" font-weight="500" fill="{SOFT}" '
                     f'opacity=".8">{n["p"]["min_dist_A"]:.1f} Å</tspan></text>')
            if n["unique"]:
                ux = xs - 13 if anchor == "start" else xs + 13
                o.append(f'<circle cx="{ux}" cy="{ly-4:.0f}" r="4" fill="none" '
                         f'stroke="{n["col"]}" stroke-width="1.6"/>')

    o.append(f'<text x="{PX+16}" y="{PY+28}" fill="{ON}" font-size="14" font-weight="800">'
             f'CDK9 · 3BLR · flavopiridol</text>')
    o.append(f'<text x="{PX+PWD-16}" y="{PY+28}" text-anchor="end" fill="{SOFT}" font-size="11.5">'
             f'distance to the nearest ligand atom</text>')
    return o, W, H, uniq, rows, (PX, PY, PWD, PHT)


def pocket_anatomy(meas) -> str:
    o, W, H, uniq, rows, (PX, PY, PWD, PHT) = pocket_anatomy_svg(meas)
    QX, QW = PX + PWD + 20, W - (PX + PWD + 20) - 34

    # the callout: one residue, and it is the whole selectivity argument
    o.append(f'<rect x="{QX}" y="{PY}" width="{QW}" height="250" rx="8" fill="{PANEL}" '
             f'opacity=".62"/>')
    o.append(f'<rect x="{QX}" y="{PY}" width="4" height="250" rx="2" fill="{SOUTH}"/>')
    o.append(f'<text x="{QX+24}" y="{PY+40}" fill="{SOUTH}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.4">THE ONE THAT MATTERS</text>')
    o.append(f'<text x="{QX+24}" y="{PY+80}" fill="{ON}" font-size="23" font-weight="800" '
             f'letter-spacing="-.3">Cys106 sits at the hinge. The other three have Met.</text>')
    for k, line in enumerate([
        "CDK9 Asp104-Phe105-Cys106-Glu107. CDK7 has Met94, CDK12 Met816, CDK13 Met794.",
        "Cys106 is 3.2 Å from flavopiridol. It is the only position in the twenty where CDK9 differs",
        "from all three counter-targets and sits directly on the ligand.",
        "This came out of the sequence pass as a guess. The structures confirm it.",
    ]):
        o.append(f'<text x="{QX+24}" y="{PY+112+k*22}" fill="{ON if k < 3 else SOFT}" '
                 f'font-size="13.5" opacity="{0.88 if k < 3 else 0.7}">{esc(line)}</text>')
    o.append(f'<text x="{QX+24}" y="{PY+222}" fill="{SOFT}" font-size="12.5" opacity=".7">'
             f'{esc("Ala153 is the other one, on the floor: Asn in CDK7, Ser in CDK12 and CDK13.")}</text>')

    # roles
    ly = PY + 282
    o.append(f'<text x="{QX}" y="{ly}" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.4">ANATOMY</text>')
    for k, (key, (col, desc)) in enumerate(ROLES.items()):
        yy = ly + 28 + k * 26
        o.append(f'<circle cx="{QX+8}" cy="{yy-4}" r="5.5" fill="{col}"/>')
        o.append(f'<text x="{QX+24}" y="{yy}" fill="{ON}" font-size="13" opacity=".85">'
                 f'{esc(desc)}</text>')

    yy = ly + 28 + len(ROLES) * 26 + 18
    o.append(f'<text x="{QX}" y="{yy}" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.4">SUPERPOSITION QUALITY</text>')
    for k, c in enumerate(meas["counter_targets"]):
        o.append(f'<text x="{QX}" y="{yy+24+k*20}" fill="{SOFT}" font-size="12.5">'
                 f'<tspan fill="{ON}" font-weight="700">{c["target"]}</tspan>'
                 f'<tspan dx="8">{c["pdb"]} · {c["resolution"]} · CEalign RMSD '
                 f'{c["cealign_rms_A"]} Å</tspan></text>')

    # ------------------------------------------------ the grid, all four targets
    GY = PY + PHT + 56
    o.append(f'<line x1="34" y1="{GY-32}" x2="{W-34}" y2="{GY-32}" stroke="{SOFT}" opacity=".2"/>')
    o.append(f'<text x="34" y="{GY-10}" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.4">SAME PLACE, FOUR TARGETS</text>')

    LBL = 74
    cw = (W - 68 - LBL) / len(rows)
    names = [REF[0]] + [n for n, _, _ in OTHERS]
    for ci, p in enumerate(rows):
        x = 34 + LBL + ci * cw
        col = ROLES[p["role"]][0]
        o.append(f'<rect x="{x+1:.1f}" y="{GY+6}" width="{cw-2:.1f}" height="3" rx="1.5" '
                 f'fill="{col}" opacity=".8"/>')
        if p in uniq:
            o.append(f'<rect x="{x+1:.1f}" y="{GY+14}" width="{cw-2:.1f}" height="{4+4*26+6}" '
                     f'rx="4" fill="{SOUTH}" opacity=".10"/>')
    for ri, name in enumerate(names):
        y = GY + 36 + ri * 26
        o.append(f'<text x="34" y="{y}" fill="{ON if ri == 0 else SOFT}" font-size="12.5" '
                 f'font-weight="{800 if ri == 0 else 600}">{name}</text>')
        for ci, p in enumerate(rows):
            x = 34 + LBL + ci * cw + cw / 2
            if ri == 0:
                txt, diff = f'{ONE.get(p["resname"], "?")}{p["position"]}', False
            else:
                e = p["equivalents"][name]
                if not e:
                    txt, diff = "–", False
                else:
                    txt = f'{ONE.get(e["resname"], "?")}{e["number"]}'
                    diff = e["resname"] != p["resname"]
                    if e["ca_offset_A"] > 2.5:
                        txt += "*"
            col = ROLES[p["role"]][0] if (ri == 0 or diff) else SOFT
            o.append(f'<text x="{x:.1f}" y="{y}" text-anchor="middle" font-size="11.5" '
                     f'font-weight="{700 if (ri == 0 or diff) else 500}" fill="{col}" '
                     f'opacity="{1 if (ri == 0 or diff) else .6}">{txt}</text>')

    fy = GY + 36 + 4 * 26 + 26
    for k, line in enumerate([
        "Coloured and bold where the counter-target differs from CDK9. Shaded columns are the two "
        "positions where CDK9 differs from all three.",
        "An asterisk means the nearest Cα after superposition is more than 2.5 Å away, so read that "
        "one as approximate. CDK7 is the worst case at 3.9 Å RMSD, which is what a 3.0 Å structure buys you.",
        "tools/render_components.py → this file and data/pocket-anatomy.json. Every number regenerates.",
    ]):
        o.append(f'<text x="34" y="{fy+k*19}" fill="{ON if k == 0 else SOFT}" font-size="12.5" '
                 f'opacity="{0.85 if k == 0 else 0.62}">{esc(line)}</text>')
    o.append('</svg>')
    return "\n".join(o)


def main() -> None:
    meas = measure()
    FIGS.mkdir(parents=True, exist_ok=True)
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(meas, indent=2) + "\n")
    for path, svg in ((FIGS / "zoom-ladder.svg", zoom_ladder_svg(meas)),
                      (FIGS / "pocket-anatomy.svg", pocket_anatomy(meas))):
        path.write_text(svg)
        print(f"wrote {path.relative_to(ROOT)}  ({path.stat().st_size:,} bytes)")
    print(f"wrote {DATA.relative_to(ROOT)}  ({DATA.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
