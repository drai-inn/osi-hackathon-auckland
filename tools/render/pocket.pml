# Same view as pocket.cxc, for PyMOL.
#
#   pymol -cq tools/render/pocket.pml

fetch 3BLR, async=0
fetch 1UA2, async=0

hide everything
bg_color grey10

show cartoon, 3BLR and chain A
color slate, 3BLR and chain A
set cartoon_transparency, 0.6, 3BLR

select lig9, 3BLR and not polymer and not solvent and not inorganic
show sticks, lig9
color cyan, lig9

# the crop radius we sweep: 10, 12, 15
select shell12, byres (3BLR and polymer within 12 of lig9)
show sticks, shell12
util.cbaw shell12

show cartoon, 1UA2
color purple, 1UA2
set cartoon_transparency, 0.6, 1UA2

set ray_opaque_background, 1
set ray_shadows, 0
orient lig9
ray 1600, 1200
png docs/03-pipeline/figures/pocket-cdk9-pymol.png, dpi=150
