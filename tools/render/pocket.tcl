# Same view as pocket.cxc, for VMD.
#
#   vmd -dispdev text -e tools/render/pocket.tcl
#
# NOTE: no official arm64 build of VMD, so this will not run on the GB10 boxes.
# See docs/03-pipeline/visualisation.md.

mol new 3BLR.pdb type pdb waitfor all
mol delrep 0 top

# protein cartoon
mol representation NewCartoon 0.30 12.0 4.1 0
mol selection {chain A and protein}
mol color ColorID 23
mol addrep top
mol modmaterial 0 top Transparent

# ligand
mol representation Licorice 0.22 24.0 24.0
mol selection {not protein and not water and not ions}
mol color ColorID 10
mol addrep top

# the 12 A shell we crop to
mol representation Licorice 0.12 18.0 18.0
mol selection {protein and same residue as (within 12 of (not protein and not water and not ions))}
mol color Name
mol addrep top

color Display Background black
display projection Orthographic
display depthcue off
display rendermode GLSL
axes location Off

render TachyonLOptiXInternal docs/03-pipeline/figures/pocket-cdk9-vmd.png
quit
