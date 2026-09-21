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
    "outreach/imagery/hero-surrogate-ladder.png": dict(
        prompt="abstract scientific editorial illustration, a ladder of scales rising from "
               "atoms to a protein pocket to a whole cell, deep navy background, cyan and "
               "violet line work, geometric, restrained, poster art",
        steps=30, seed=7, size=(1328, 1328), date="2026-09-21",
        model=MODEL, dtype="bfloat16", true_cfg_scale=4.0,
    ),
}


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
    img = pipe(prompt=prompt, negative_prompt=" ", width=1328, height=1328,
               num_inference_steps=steps, true_cfg_scale=4.0,
               generator=torch.Generator("cuda").manual_seed(seed)).images[0]
    img.save(out)
    print(f"generated in {time.time()-t1:.1f}s -> {out} | "
          f"peak {torch.cuda.max_memory_allocated()/2**30:.1f} GiB")


if __name__ == "__main__":
    main()
