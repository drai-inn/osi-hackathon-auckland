#!/usr/bin/env python3
"""Generate the four theme-card backgrounds.

Run inside the GPU workspace, where Qwen-Image weights are already cached:

    coder ssh ndj-k8s-base-1 -- 'cd /home/coder/imagegen && python3 theme_backgrounds.py'

Writes out/bg-theme-{1..4}.png at 1584x1056. Crop and convert them with the
snippet at the foot of this file, which is what puts them in docs/cards/bg/.

These are backgrounds for recruitment cards. They carry mood, not measurement —
see the note in CLAUDE.md about which side of that line things sit on.

Composition matters more than subject here. The card puts its title at the upper
left and its copy along the foot, so each prompt asks for weight on the right and
a calm upper left, and for the frame to fall away dark at top and bottom so the
scrim has something to work with.
"""
from __future__ import annotations

import time

import torch
from diffusers import DiffusionPipeline

MODEL = "Qwen/Qwen-Image"

RAMP = ("a perceptually uniform colour ramp running deep navy in the shadows through violet "
        "to bright cyan in the highlights")

# "no subject in the lower third" emptied the frame rather than balancing it,
# and asking for a calm upper left compounded that. Weighting is enough.
FRAME = ("composition weighted to the right, falling away to near black at the top and bottom "
         "edges, wide cinematic depth, soft gradients, techno-futurist, elegant")

NEG = ("text, words, letters, numbers, watermark, signature, logo, cluttered, busy, "
       "stock illustration, bohr atom, staircase, bar chart, arrow, infographic, "
       "gemstone, cut crystal, double helix, photorealistic, harsh edges, "
       "pale sky, white background, bright background, washed out, daylight, "
       "centred composition, symmetrical")

PROMPTS = {
    1: ("screening at scale — an immense dark plain densely covered with many thousands of tiny "
        "points of light receding to a far horizon, a dense glittering field, a small cluster of "
        f"them lit bright cyan and standing out from the rest, {RAMP}, {FRAME}"),
    2: ("molecules in motion — a single luminous organic form caught mid-movement, its trajectory "
        "smeared into soft overlapping echoes behind it, viscous and fluid, "
        f"{RAMP}, {FRAME}"),
    # "shells" produced a mollusc. Concentric membranes, and say what they are.
    3: ("binding to a whole system — concentric translucent membranes expanding outward from one "
        "small bright core like ripples frozen in three dimensions, each layer a wider scale than "
        f"the last, layered depth, abstract, {RAMP}, {FRAME}"),
    4: ("repurposing what we have — a dark field of many identical small rounded forms in loose "
        "rows, three of them lit bright cyan and connected by a fine thread, the rest dim, "
        f"{RAMP}, {FRAME}"),
}

SEED = 53
RERUN_SEED = 77          # themes 1 and 3, which needed a second attempt

# Two things to know before changing these.
#
# Uploading a script to the workspace by piping into `coder ssh <ws> -- cmd`
# silently writes an empty file; stdin is not forwarded for a command. Embed the
# base64 in the command string instead. Backgrounding with nohup inside
# `coder ssh -- cmd` is also killed when the session tears down, so run in the
# foreground.
#
# "shells" produced a mollusc with a pearl in it, and over-constraining the
# composition ("no subject in the lower third", "calm uncluttered upper left")
# emptied the frame rather than balancing it. Both are fixed above.


def main() -> None:
    t0 = time.time()
    pipe = DiffusionPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16).to("cuda")
    print(f"loaded {time.time() - t0:.0f}s", flush=True)
    for n, prompt in PROMPTS.items():
        t = time.time()
        img = pipe(prompt=prompt, negative_prompt=NEG, width=1584, height=1056,
                   num_inference_steps=32, true_cfg_scale=4.0,
                   generator=torch.Generator("cuda").manual_seed(SEED)).images[0]
        img.save(f"out/bg-theme-{n}.png")
        print(f"theme {n}: {time.time() - t:.0f}s", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()

# Afterwards, locally:
#
#   for n in 1 2 3 4; do
#     coder ssh ndj-k8s-base-1 -- base64 -w0 /home/coder/imagegen/out/bg-theme-$n.png \
#       | base64 -d > /tmp/bg-$n.png
#   done
#
# then resize to 1200x812, save WEBP quality 80 into docs/cards/bg/theme-$n.webp,
# and run `make cards`.
