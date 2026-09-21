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

FRAME = ("composition weighted to the right with a calm uncluttered upper left, falling away to "
         "near black at the top and bottom edges, wide cinematic depth, soft gradients, "
         "techno-futurist, minimal, elegant, no subject in the lower third")

NEG = ("text, words, letters, numbers, watermark, signature, logo, cluttered, busy, "
       "stock illustration, bohr atom, staircase, bar chart, arrow, infographic, "
       "gemstone, cut crystal, double helix, photorealistic, harsh edges, "
       "pale sky, white background, bright background, washed out, daylight, "
       "centred composition, symmetrical")

PROMPTS = {
    1: ("screening at scale — an immense dark plain scattered with countless faint particles "
        "receding to a horizon, a small handful of them lit bright cyan and standing out from "
        f"the rest, {RAMP}, {FRAME}"),
    2: ("molecules in motion — a single luminous organic form caught mid-movement, its trajectory "
        "smeared into soft overlapping echoes behind it, viscous and fluid, "
        f"{RAMP}, {FRAME}"),
    3: ("binding to a whole system — nested translucent shells opening outward from one small "
        "bright core, each shell a wider scale than the last, layered depth, "
        f"{RAMP}, {FRAME}"),
    4: ("repurposing what we have — a dark field of many identical small rounded forms in loose "
        "rows, three of them lit bright cyan and connected by a fine thread, the rest dim, "
        f"{RAMP}, {FRAME}"),
}

SEED = 53


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
