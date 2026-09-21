#!/usr/bin/env python3
"""Extract real molecular geometry for the theme cards.

    python3 tools/extract_card_geometry.py     # needs biopython + numpy

Writes data/card-geometry.json: flavopiridol from 3BLR with its bonds and
elements, and the pocket-neighbourhood backbone of all four CDK structures
superposed onto CDK9.

The card generator reads that JSON and stays standard-library only, so anyone
can run `make cards` on day 1 without an environment. Same pattern as
data/protein-space.json.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from Bio.PDB import MMCIFParser, Model, Structure
from Bio.PDB.cealign import CEAligner

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/card-geometry.json"
CACHE = ROOT / ".cache/pdb"
ENTRIES = ("3blr", "1ua2", "4nst", "5efq")
LIGAND = "CPB"                      # flavopiridol, as deposited in 3BLR

P = MMCIFParser(QUIET=True)


def kinase(pdb):
    m = P.get_structure(pdb, CACHE / f"{pdb}.cif")[0]
    best, n = None, 0
    for ch in m:
        cas = [r for r in ch if "CA" in r and r.id[0] == " "]
        if len(cas) > n:
            best, n = ch, len(cas)
    return m, best


def lone(ch):
    s = Structure.Structure("x")
    mo = Model.Model(0)
    s.add(mo)
    mo.add(ch.copy())
    return s


def main() -> None:
    m, ref = kinase(ENTRIES[0])
    lig = [r for ch in m for r in ch if r.resname.strip() == LIGAND][0]
    atoms = [a for a in lig if a.element != "H"]
    L = np.array([a.coord for a in atoms])

    shell = []
    for r in ref:
        if r.id[0] != " ":
            continue
        C = np.array([a.coord for a in r if a.element != "H"])
        if len(C) and np.linalg.norm(C[:, None, :] - L[None, :, :], axis=2).min() < 9.0:
            shell.append(r)
    pk = np.vstack([np.array([a.coord for a in r if a.element != "H"]) for r in shell])

    centre = np.vstack([pk, L]).mean(axis=0)
    _, _, vt = np.linalg.svd(np.vstack([pk, L]) - centre)
    basis = vt[:3]

    def proj(xyz):
        p = (np.atleast_2d(xyz) - centre) @ basis.T
        return [[round(float(a), 2), round(float(b), 2), round(float(c), 2)] for a, b, c in p]

    bonds = [[i, j] for i in range(len(atoms)) for j in range(i + 1, len(atoms))
             if np.linalg.norm(atoms[i].coord - atoms[j].coord) < 1.95]

    al = CEAligner()
    al.set_reference(lone(ref))
    traces = []
    for pdb in ENTRIES:
        _, ch = kinase(pdb)
        s = lone(ch)
        if pdb != ENTRIES[0]:
            al.align(s)
        moved = next(s[0].get_chains())
        ca = np.array([r["CA"].coord for r in moved if "CA" in r and r.id[0] == " "])
        traces.append(proj(ca[np.linalg.norm(ca - centre, axis=1) < 17.0]))

    OUT.write_text(json.dumps({
        "source": f"RCSB {', '.join(e.upper() for e in ENTRIES)}, fetched 2026-09-19. "
                  f"CEalign onto CDK9.",
        "tool": "tools/extract_card_geometry.py",
        "ligand": {"name": "flavopiridol", "het": LIGAND,
                   "elements": [a.element.upper() for a in atoms],
                   "atoms": proj(L), "bonds": bonds},
        "traces": traces,
    }) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}  ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
