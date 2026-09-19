#!/usr/bin/env python3
"""Render the CDK targets from real PDB coordinates into brand-styled SVG.

    python3 tools/render_structures.py

Writes docs/03-pipeline/figures/structures-cdk-family.svg

Why not ChimeraX or PyMOL: neither is installed everywhere, neither renders SVG,
and a PNG in the README can't be diffed. This reads the actual deposited
coordinates, superposes the four targets onto CDK9 with CEalign, and draws a
depth-cued CA ribbon. It regenerates anywhere Python and biopython run, including
the GB10 boxes, and the output is text.

It is a schematic, not a replacement for a real renderer. For publication figures
use tools/render/pocket.cxc. See docs/03-pipeline/visualisation.md.

Needs: biopython, numpy. Network on first run; structures cache under .cache/pdb.
"""
from __future__ import annotations

import math
import urllib.request
from pathlib import Path

import numpy as np
from Bio.PDB import MMCIFParser, Select
from Bio.PDB.cealign import CEAligner

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/03-pipeline/figures/structures-cdk-family.svg"
CACHE = ROOT / ".cache" / "pdb"

VOID, PANEL, ON, SOFT = "#141C36", "#1D2A4F", "#EEF1FB", "#9AA7CD"
SOUTH, GOLD = "#00D3F6", "#C79A4D"

# Verified against the RCSB entry API on 2026-09-19.
TARGETS = [
    ("CDK9",  "3blr", "2.8 Å", "flavopiridol, with cyclin T1", "#00D3F6", True),
    ("CDK7",  "1ua2", "3.0 Å", "ATP",                          "#8AA0E6", False),
    ("CDK12", "4nst", "2.2 Å", "ADP-AlF, with cyclin K",       "#8B7CF6", False),
    ("CDK13", "5efq", "2.0 Å", "ADP-AlF, with cyclin K",       "#A58BF0", False),
]

# Crystallisation additives and ions. Not what anyone came to see.
JUNK = {"HOH", "SO4", "GOL", "EDO", "CL", "NA", "MG", "ACT", "PO4", "ZN", "CA",
        "DMS", "PEG", "TRS", "MPD", "AF3", "IOD", "BR", "K", "FMT", "NO3"}

# Phosphorylated residues. These are part of the chain, not ligands, and the
# activation-loop phosphothreonine is worth marking rather than hiding.
PHOSPHO = {"TPO", "SEP", "PTR"}


def fetch(pdb: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{pdb}.cif"
    if not f.exists():
        url = f"https://files.rcsb.org/download/{pdb.upper()}.cif"
        with urllib.request.urlopen(url, timeout=60) as r:
            f.write_bytes(r.read())
    return f


def kinase_chain(model):
    """The longest protein chain, which is the kinase rather than the cyclin."""
    best, n = None, 0
    for ch in model:
        cas = [r["CA"] for r in ch if "CA" in r and r.id[0] == " "]
        if len(cas) > n:
            best, n = ch, len(cas)
    return best


def _near(coords, ref_ca, cutoff=10.0):
    """Is this residue actually touching the chain we are drawing?

    Entries often hold several crystallographic copies. Without this, a second
    copy's ADP floats in the panel looking like it means something.
    """
    if not len(coords):
        return False
    d = np.linalg.norm(ref_ca[None, :, :] - np.asarray(coords)[:, None, :], axis=2)
    return bool(d.min() < cutoff)


def ligand_atoms(model, ref_ca):
    """Whatever sits in this chain's ATP site. Not additives, not modified residues."""
    out = []
    for ch in model:
        for res in ch:
            n = res.resname.strip()
            if res.id[0] == " " or n in JUNK or n in PHOSPHO:
                continue
            atoms = [a for a in res if a.element != "H"]
            if len(atoms) >= 8 and _near([a.coord for a in atoms], ref_ca):
                out.extend(atoms)
    return out


def phospho_sites(model, ref_ca):
    """Activation-loop phosphothreonine and friends. Marked, not drawn as ligand."""
    out = []
    for ch in model:
        for res in ch:
            if res.resname.strip() not in PHOSPHO:
                continue
            p = [a for a in res if a.element == "P"] or [a for a in res if a.name == "CA"]
            if p and _near([a.coord for a in p], ref_ca, 6.0):
                out.extend(p)
    return out


def load(pdb: str):
    st = MMCIFParser(QUIET=True).get_structure(pdb, fetch(pdb))
    m = st[0]
    ch = kinase_chain(m)
    return st, m, ch


def main() -> None:
    structures = {}
    ref_struct = None
    for name, pdb, *_ in TARGETS:
        st, m, ch = load(pdb)
        if ref_struct is None:
            ref_struct = st
        else:
            try:
                CEAligner().set_reference(ref_struct) or None
            except Exception:
                pass
        structures[name] = (st, m, ch, pdb)

    # superpose everything onto CDK9
    al = CEAligner()
    al.set_reference(structures["CDK9"][0])
    for name in list(structures):
        if name == "CDK9":
            continue
        try:
            al.align(structures[name][0])
        except Exception as e:                       # pragma: no cover
            print(f"  ! CEalign failed for {name}: {e}")

    # shared camera from the CDK9 kinase domain
    ref_ca = np.array([r["CA"].coord for r in structures["CDK9"][2]
                       if "CA" in r and r.id[0] == " "])
    centre = ref_ca.mean(axis=0)
    u, s, vt = np.linalg.svd(ref_ca - centre)
    basis = vt[:3]                                   # rows: widest, next, depth

    def project(xyz):
        p = (np.atleast_2d(xyz) - centre) @ basis.T
        return p[:, 0], p[:, 1], p[:, 2]

    # panel scale
    allx, ally = [], []
    for name, (st, m, ch, pdb) in structures.items():
        ca = np.array([r["CA"].coord for r in ch if "CA" in r and r.id[0] == " "])
        x, y, _ = project(ca)
        allx += [x.min(), x.max()]; ally += [y.min(), y.max()]
    span = max(max(allx) - min(allx), max(ally) - min(ally)) * 1.06
    PW, PH = 316, 300
    scale = min(PW - 40, PH - 76) / span
    cx0, cy0 = (min(allx) + max(allx)) / 2, (min(ally) + max(ally)) / 2

    W, H = 4 * PW + 60, PH + 190
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Inter,Helvetica Neue,Arial,sans-serif" role="img" '
         f'aria-label="CDK9, CDK7, CDK12 and CDK13 backbones superposed and drawn from deposited coordinates">',
         '<title>The four targets, from deposited coordinates</title>',
         f'<rect width="{W}" height="{H}" fill="{VOID}"/>']
    o.append(f'<text x="34" y="52" fill="{ON}" font-size="27" font-weight="800" '
             f'letter-spacing="-.5">The four targets</text>')
    o.append(f'<text x="34" y="80" fill="{SOFT}" font-size="14">Deposited coordinates, superposed '
             f'onto CDK9 with CEalign and drawn in one shared view. Same fold, same place, '
             f'different answer.</text>')

    for i, (name, pdb, res, note, colour, is_primary) in enumerate(TARGETS):
        st, m, ch, _ = structures[name]
        px, py = 30 + i * PW, 118
        o.append(f'<rect x="{px}" y="{py}" width="{PW-24}" height="{PH}" rx="8" fill="{PANEL}" '
                 f'opacity="{0.55 if is_primary else 0.34}"/>')

        def S(xyz):
            x, y, z = project(xyz)
            return (px + (PW - 24) / 2 + (x - cx0) * scale,
                    py + PH / 2 + (y - cy0) * scale, z)

        ca = np.array([r["CA"].coord for r in ch if "CA" in r and r.id[0] == " "])
        X, Y, Z = S(ca)
        zmin, zmax = Z.min(), Z.max()

        # depth-sorted backbone segments: far segments thin and dim, near ones solid
        segs = []
        for k in range(len(X) - 1):
            if math.dist((X[k], Y[k]), (X[k+1], Y[k+1])) > 26:
                continue                              # chain break
            zm = (Z[k] + Z[k+1]) / 2
            t = (zm - zmin) / (zmax - zmin) if zmax > zmin else 0.5
            segs.append((zm, X[k], Y[k], X[k+1], Y[k+1], t))
        segs.sort(key=lambda s: s[0])
        for zm, x1, y1, x2, y2, t in segs:
            o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                     f'stroke="{colour}" stroke-width="{1.1 + 2.6*t:.2f}" '
                     f'stroke-linecap="round" opacity="{0.22 + 0.62*t:.2f}"/>')

        # ligand, if the entry has one
        lig = ligand_atoms(m, ca)
        if lig:
            lx, ly, lz = S(np.array([a.coord for a in lig]))
            for a in range(len(lx)):
                for b in range(a + 1, len(lx)):
                    if np.linalg.norm(lig[a].coord - lig[b].coord) < 1.8:
                        o.append(f'<line x1="{lx[a]:.1f}" y1="{ly[a]:.1f}" x2="{lx[b]:.1f}" '
                                 f'y2="{ly[b]:.1f}" stroke="{GOLD}" stroke-width="2.4" '
                                 f'stroke-linecap="round" opacity=".95"/>')
            for a in range(len(lx)):
                o.append(f'<circle cx="{lx[a]:.1f}" cy="{ly[a]:.1f}" r="2.6" fill="{GOLD}"/>')

        # activation-loop phosphate, if the construct carries one
        for a in phospho_sites(m, ca):
            sx, sy, _ = S(np.array([a.coord]))
            o.append(f'<circle cx="{sx[0]:.1f}" cy="{sy[0]:.1f}" r="4.6" fill="none" '
                     f'stroke="{ON}" stroke-width="1.4" opacity=".55"/>')
            o.append(f'<circle cx="{sx[0]:.1f}" cy="{sy[0]:.1f}" r="1.8" fill="{ON}" opacity=".7"/>')

        o.append(f'<text x="{px+18}" y="{py+28}" font-size="15" font-weight="800">'
                 f'<tspan fill="{colour}">{name}</tspan>'
                 f'<tspan dx="8" fill="{SOFT}" font-size="12" font-weight="600">'
                 f'{pdb.upper()} · {res}</tspan></text>')
        o.append(f'<text x="{px+18}" y="{py+PH-16}" fill="{SOFT}" font-size="11.5">{note}</text>')
        o.append(f'<text x="{px+18}" y="{py+PH-34}" fill="{SOFT}" font-size="11.5" opacity=".8">'
                 f'{len(ca)} residues traced</text>')

    ly0 = 118 + PH + 34
    o.append(f'<line x1="34" y1="{ly0-16}" x2="{W-34}" y2="{ly0-16}" stroke="{SOFT}" opacity=".2"/>')
    o.append(f'<text x="34" y="{ly0+8}" fill="{SOFT}" font-size="11.5" font-weight="700" '
             f'letter-spacing="1.4">READING IT</text>')
    for k, line in enumerate([
        "Cα trace only, depth-cued: nearer segments are thicker and brighter. Gold is what sits in the ATP site. Open circles mark the activation-loop phosphate.",
        "All four superposed onto CDK9 and drawn through one camera, so what differs between panels is the protein, not the pose.",
        "Schematic, not a replacement for a renderer. tools/render_structures.py → this file. For publication figures use tools/render/pocket.cxc."]):
        o.append(f'<text x="34" y="{ly0+30+k*19}" fill="{ON if k<2 else SOFT}" font-size="12.5" '
                 f'opacity="{0.85 if k<2 else 0.65}">{line}</text>')
    o.append('</svg>')

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(o))
    print(f"wrote {OUT.relative_to(ROOT)}  ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
