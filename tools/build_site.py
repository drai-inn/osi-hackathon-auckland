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

PAGES = "https://drai-inn.github.io/osi-hackathon-auckland/"

# Nothing is substituted any more. Every URL the page needs is public and is
# written into the source, so what you open from the filesystem while editing is
# what ships. The check at the end of main() stays: a {{...}} reaching the built
# page would mean someone had reintroduced a substitution without a value.

ASSETS = [
    ("outreach/imagery/terrain.webp", "assets/terrain.webp"),
    ("outreach/imagery/stacked-isosurfaces.webp", "assets/stacked-isosurfaces.webp"),
    ("outreach/imagery/drip.webp", "assets/drip.webp"),
    ("outreach/imagery/energy-surface.webp", "assets/energy-surface.webp"),
    ("outreach/imagery/through-the-membrane.webp", "assets/through-the-membrane.webp"),
    ("outreach/brand/readme-banner.png", "assets/banner.png"),
    ("outreach/brand/uoa-logo-white.png", "assets/uoa-logo-white.png"),
    ("outreach/brand/uoa-logo-navy.png", "assets/uoa-logo-navy.png"),
    ("outreach/poster-A3.pdf", "poster.pdf"),
] + [(f"docs/cards/theme-{n}.svg", f"assets/theme-{n}.svg") for n in (1, 2, 3, 4)] \
  + [(f"docs/cards/theme-open-{k}.svg", f"assets/theme-open-{k}.svg") for k in (1, 2)]

REWRITE = [
    (r"\.\./imagery/", "assets/"),
    (r"\.\./brand/", "assets/"),
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
