#!/usr/bin/env python3
"""Generate collateral imagery with Qwen-Image on a GPU workspace.

    python3 tools/generate_imagery.py "a prompt" out.png [steps] [seed]

Runs on the Coder sandbox, not on a laptop. It needs a whole RTX PRO 6000 and
about 54 GB of weights. See docs/compute.md for the workspace profile and the
measured numbers.

    gpu=1 cpu=8 memory=32, image quay.io/jupyter/pytorch-notebook:cuda12-pytorch-2.11.0
    pip install diffusers transformers accelerate sentencepiece protobuf

Qwen-Image is Apache-2.0 and ungated. FLUX and Stable Diffusion 3.5 need a
HuggingFace token even where the licence is permissive.

**This is for event collateral, never for figures.** Diffusion output cannot be
regenerated deterministically across setups, and it will happily draw chemistry
that looks right and is not. Figures come from data — see tools/make_cards.py
and tools/render_components.py.
"""
from __future__ import annotations

import sys
import time

import torch
from diffusers import DiffusionPipeline

MODEL = "Qwen/Qwen-Image"

# What has been generated so far, so the repo can say where an image came from.
# Reproducible in intent rather than byte-for-byte: a different diffusers or
# driver version will shift the output even on the same seed.
PROVENANCE = {
    # Round 2, 21 Sep 2026. Qwen-Image, bfloat16, 1328x1328, 30 steps,
    # true_cfg_scale 4.0, seed 11, ~41 s each once the model is resident.
    "outreach/imagery/folding-basin.png": dict(
        prompt="minimal techno-futurist poster art, one smooth undulating folding energy landscape "
               "surface, a single glowing cyan sphere settling into the basin, deep navy void, "
               "violet rim light, vast negative space, flat vector, elegant, playful"),
    "outreach/imagery/through-the-membrane.png": dict(
        prompt="minimal techno-futurist illustration, a lipid membrane as a rhythmic row of round "
               "heads with tails, one bright cyan molecule slipping through the gap, deep navy, "
               "violet accents, flat geometric, spacious, witty"),
    # Round 3, 21 Sep 2026. Seed 23. Dropping "flat vector" for "soft gradients"
    # is what produced the organic feel; the colour ramp is what carries meaning.
    "outreach/imagery/energy-surface.png": dict(
        prompt="organic undulating free energy surface seen at a low grazing angle, smooth viscous "
               "swelling forms, fine topographic contour bands following every peak and trough, "
               + "RAMP" + ", minimal, techno-futurist, generous negative space, soft gradients, "
               "elegant"),
    "outreach/imagery/stacked-isosurfaces.png": dict(
        prompt="stacked translucent iso-surfaces sliced through a molecular potential field, "
               "organic rounded layers offset in depth, each layer a band of " + "RAMP" + ", strong "
               "sense of dimension and cross-section, minimal, airy, techno-futurist, soft gradients"),
    "outreach/imagery/drip.png": dict(
        prompt="a glossy organic droplet stretching and dripping through a soft membrane gap, "
               "viscous gooey surface tension, the droplet shaded by " + "RAMP" + " to show its "
               "energy, deep navy background, playful, wet, techno-futurist, generous space, "
               "soft gradients"),

    # Round 4, 21 Sep 2026. Seeds 31, 47 and 89 of one prompt, at 1664x928 and
    # 34 steps. The 16:9 frame does much of the work of making it feel expansive,
    # and "deep black navy void" plus the pale-background negatives fixed the
    # washed-out sky that round 3 produced.
    "outreach/imagery/terrain-{31,47,89}.png": dict(
        prompt="a vast expansive undulating free energy surface receding to a distant horizon, seen "
               "from above and far back, fine topographic contour bands following every peak and "
               "trough, " + "RAMP" + ", set against a deep black navy void, dark background, glossy "
               "organic droplets resting on the surface, some half sunk with a meniscus where they "
               "meet it, one fully engulfed and glowing beneath, translucent isosurface buckyball "
               "cages and fullerene lattices floating above and partly embedded in the ridges, fine "
               "whispery biological filaments and threads drifting across, around and through the "
               "surface, soft gradients, luminous, techno-futurist, expansive, minimal, elegant",
        size=(1664, 928), steps=34, seeds=(31, 47, 89)),

    "outreach/imagery/field-lines.png": dict(
        prompt="minimal biophysics art, smooth electrostatic field lines curving around an unseen "
               "molecule, thin cyan contours on deep navy, one violet node, techno-futurist, airy, "
               "flat vector"),
}

# Deep navy -> violet -> cyan -> pale is both perceptually ordered, so it reads
# as a scientific colourmap, and close to the brand. Substituted for "RAMP" above.
RAMP = ("a perceptually uniform colour ramp running deep navy in the troughs through violet "
        "to bright cyan on the peaks and pale highlights at the crests")

# Shared across rounds 2 and 3. Keeping the negatives is most of what moved the output
# away from stock-illustration science.
NEGATIVE = ("text, words, letters, numbers, watermark, signature, logo, cluttered, busy, "
            "stock illustration, bohr atom, staircase, bar chart, arrow, infographic, "
            "gemstone, cut crystal, double helix, photorealistic, harsh edges, "
            "pale sky, white background, bright background, washed out, daylight")

DEFAULTS = dict(steps=30, seed=11, size=(1328, 1328), true_cfg_scale=4.0,
                dtype="bfloat16", model=MODEL, date="2026-09-21")


def main() -> None:
    prompt = sys.argv[1]
    out = sys.argv[2]
    steps = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 7

    t0 = time.time()
    pipe = DiffusionPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16).to("cuda")
    print(f"loaded in {time.time()-t0:.0f}s | {torch.cuda.memory_allocated()/2**30:.1f} GiB",
          flush=True)

    t1 = time.time()
    img = pipe(prompt=prompt, negative_prompt=NEGATIVE, width=1328, height=1328,
               num_inference_steps=steps, true_cfg_scale=4.0,
               generator=torch.Generator("cuda").manual_seed(seed)).images[0]
    img.save(out)
    print(f"generated in {time.time()-t1:.1f}s -> {out} | "
          f"peak {torch.cuda.max_memory_allocated()/2**30:.1f} GiB")


if __name__ == "__main__":
    main()
