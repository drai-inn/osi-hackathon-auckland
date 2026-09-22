#!/usr/bin/env python3
"""Raster fallbacks for the favicon.

    python3 tools/make_icons.py

Writes outreach/brand/favicon-{16,32}.png and apple-touch-icon.png from
outreach/brand/favicon.svg.

The SVG is the real icon and carries its own light/dark switch. These are for
the browsers that will not take an SVG favicon, and for iOS, which wants a
square tile it can round off itself. Those get the reversed crest on the brand
navy rather than a transparent one, because a fallback has no way to know what
colour the strip behind it is.

Rendered through headless Chrome, the same as every other image in outreach/,
so there is no image library to install. Standard library only.
"""
from __future__ import annotations

import base64
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "outreach/brand"

VOID = "#141C36"

# name, px, background, crest colour, inset as a fraction of the tile
ICONS = [
    ("favicon-32.png", 32, VOID, "#EEF1FB", 0.10),
    ("favicon-16.png", 16, VOID, "#EEF1FB", 0.06),
    ("apple-touch-icon.png", 180, VOID, "#EEF1FB", 0.20),
]


def chrome() -> str:
    for c in ("chrome", "google-chrome", "chromium"):
        if shutil.which(c):
            return c
    mac = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if Path(mac).exists():
        return mac
    raise SystemExit("no chrome on PATH, and not at the usual macOS location")


def main() -> None:
    svg = (BRAND / "favicon.svg").read_text()

    for name, px, bg, fg, inset in ICONS:
        # Recolour for the tile and drop the media query: these are flat.
        art = svg.replace(".crest{fill:#0C0C48}", f".crest{{fill:{fg}}}")
        art = art.replace(
            "@media (prefers-color-scheme: dark){ .crest{fill:#EEF1FB} }", "")
        uri = "data:image/svg+xml;base64," + base64.b64encode(art.encode()).decode()
        pad = round(px * inset)
        html = (
            f'<!DOCTYPE html><html><body style="margin:0;width:{px}px;height:{px}px;'
            f'background:{bg};display:flex;align-items:center;justify-content:center">'
            f'<img src="{uri}" style="height:{px - 2 * pad}px;width:auto"></body></html>'
        )
        with tempfile.TemporaryDirectory() as tmp:
            page = Path(tmp) / "icon.html"
            page.write_text(html)
            subprocess.run(
                [chrome(), "--headless", "--disable-gpu", "--hide-scrollbars",
                 f"--window-size={px},{px}",
                 f"--screenshot={BRAND / name}", f"file://{page}"],
                check=True, capture_output=True,
            )
        print(f"wrote {(BRAND / name).relative_to(ROOT)}  "
              f"{px}x{px}  {(BRAND / name).stat().st_size:,} bytes")


if __name__ == "__main__":
    sys.exit(main())
