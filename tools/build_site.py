#!/usr/bin/env python3
"""Assemble the GitHub Pages site into _site/.

    python3 tools/build_site.py

Takes outreach/site/index.html, flattens what it references into _site/assets/,
rewrites the paths, and fills the placeholders that need public URLs. Publish
with `make pages`, which pushes _site/ to the gh-pages branch.

The source page keeps its relative paths so it still opens from the filesystem
during editing. Only the built copy is rewritten.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"

REPO = "https://github.com/drai-inn/osi-hackathon-auckland"
PAGES = "https://drai-inn.github.io/osi-hackathon-auckland/"

FILL = {
    "{{REPO}}": REPO,
    "{{EVENT_LOG_PR}}": f"{REPO}/pull/14",
    # No local registration exists yet. Until one does, the honest call to
    # action is to get in touch; the global event's own registration is linked
    # separately further down the page.
    "{{REGISTER}}": "mailto:njon001@aucklanduni.ac.nz?subject=OSI%20Hackathon%20Auckland",
    "{{LINK}}": PAGES,
}

ASSETS = [
    ("outreach/imagery/terrain.webp", "assets/terrain.webp"),
    ("outreach/imagery/stacked-isosurfaces.webp", "assets/stacked-isosurfaces.webp"),
    ("outreach/imagery/drip.webp", "assets/drip.webp"),
    ("outreach/imagery/energy-surface.webp", "assets/energy-surface.webp"),
    ("outreach/imagery/through-the-membrane.webp", "assets/through-the-membrane.webp"),
    ("outreach/brand/readme-banner.png", "assets/banner.png"),
    ("outreach/poster-A3.pdf", "poster.pdf"),
] + [(f"docs/cards/theme-{n}.svg", f"assets/theme-{n}.svg") for n in (1, 2, 3, 4)]

REWRITE = [
    (r"\.\./imagery/", "assets/"),
    (r"\.\./\.\./docs/cards/", "assets/"),
    (r"\.\./poster-A3\.pdf", "poster.pdf"),
]


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets").mkdir(parents=True)

    for src, dst in ASSETS:
        shutil.copy2(ROOT / src, SITE / dst)

    html = (ROOT / "outreach/site/index.html").read_text()
    for pat, rep in REWRITE:
        html = re.sub(pat, rep, html)
    for k, v in FILL.items():
        html = html.replace(k, v)

    left = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if left:
        raise SystemExit(f"unfilled placeholders in the built page: {sorted(set(left))}")

    (SITE / "index.html").write_text(html)
    (SITE / ".nojekyll").write_text("")          # assets/ is fine, but be explicit

    n = sum(1 for _ in SITE.rglob("*") if _.is_file())
    size = sum(f.stat().st_size for f in SITE.rglob("*") if f.is_file())
    print(f"built _site/  {n} files, {size/1024:.0f} KB  ->  {PAGES}")


if __name__ == "__main__":
    main()
