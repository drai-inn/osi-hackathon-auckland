# Structure render scripts

Same view, three tools, so whoever has one installed can produce it. Plus a browser viewer that
needs nothing installed at all.

| File | Tool | Run it |
| --- | --- | --- |
| [`pocket.cxc`](pocket.cxc) | ChimeraX | `chimerax --nogui --script tools/render/pocket.cxc` |
| [`pocket.pml`](pocket.pml) | PyMOL | `pymol -cq tools/render/pocket.pml` |
| [`pocket.tcl`](pocket.tcl) | VMD | `vmd -dispdev text -e tools/render/pocket.tcl` |
| [`viewer.html`](viewer.html) | 3Dmol.js in a browser | open it, or embed the two `<div>`s |

**ChimeraX is the one to keep working**, because it's native on Apple Silicon and runs headless
cleanly. The others are there so nobody has to install a new tool to contribute a figure.

**VMD has no official arm64 build.** It won't run on the GB10 boxes. Don't let a figure pipeline
depend on it.

## What they draw

CDK9 (3BLR, 2.8 Å, with cyclin T1 and flavopiridol) beside CDK7 (1UA2, 3.0 Å). The ligand in cyan,
and the residue shell inside the crop radius shown as sticks, because that radius is a parameter we
sweep and it helps to see what 10 versus 15 Å actually includes.

`viewer.html` makes the radius a button, which is the version worth sharing when we post an update.

## The rule

Every committed structural figure carries, in the script that made it: the **PDB ID**, the **date
fetched**, the **exact command**, and the **tool version**. Same discipline as the provenance tags
on numbers. See [visualisation.md](../../docs/03-pipeline/visualisation.md).

No hand-posed screenshots. If it can't be regenerated it won't survive the third revision.
