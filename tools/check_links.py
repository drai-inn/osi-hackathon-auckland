#!/usr/bin/env python3
"""Check every relative link, image and anchor in the repo's markdown.

    python3 tools/check_links.py          # whole repo
    python3 tools/check_links.py README.md docs/

Exits non-zero on the first broken thing, so it can sit in `make check`.

Standard library only. Anchors follow GitHub's rule, which is easy to get subtly
wrong and has bitten this repo twice: an emoji in a heading silently changed the
anchor, and a checker that collapsed runs of spaces disagreed with GitHub, which
emits one hyphen per space. Both are covered by the tests at the foot of the file.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", ".cache", "node_modules", ".venv"}

# Links out to GitHub's own UI, relative to the repo page rather than the tree.
# They resolve on github.com and nowhere else, so they are not ours to check.
GITHUB_UI = ("../../tree/", "../../pulls", "../../issues", "../../compare/", "../../projects")

LINK = re.compile(r"!?\[[^\]]*\]\(\s*([^)\s]+)")
MD_LINK_IN_HEADING = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def slug(heading: str) -> str:
    """GitHub's anchor for a heading.

    Inline markdown is unwrapped, everything that is not a word character, a space
    or a hyphen is dropped, and each remaining space becomes one hyphen. Emoji
    disappear but the space beside them does not, which is why an emoji in a
    heading shifts the anchor instead of leaving it alone.
    """
    h = MD_LINK_IN_HEADING.sub(r"\1", heading.strip())
    h = h.replace("`", "").replace("*", "")          # the parser eats these first
    h = re.sub(r"[^\w\s-]", "", h.lower(), flags=re.UNICODE)
    return h.replace(" ", "-")                        # no trim, and no collapsing


def anchors(path: Path) -> set[str]:
    out, fence = set(), False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            out.add(slug(m.group(2)))
    return out


def targets(paths: list[Path]) -> list[Path]:
    out = []
    for p in paths:
        if p.is_dir():
            out += [f for f in p.rglob("*.md") if not SKIP & set(f.parts)]
        elif p.suffix == ".md":
            out.append(p)
    return sorted(set(out))


def main(argv: list[str]) -> int:
    paths = [Path(a) for a in argv] or [ROOT]
    files = targets(paths)
    cache: dict[Path, set[str]] = {}
    bad, n = [], 0

    for p in files:
        text = p.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            if raw.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            if raw.startswith(GITHUB_UI):
                continue
            n += 1
            frag = ""
            target = raw
            if "#" in target:
                target, frag = target.split("#", 1)
            dest = (p.parent / unquote(target)).resolve() if target else p
            if not dest.exists():
                bad.append(f"{p.relative_to(ROOT)}  ->  {raw}   (no such file)")
                continue
            if frag and dest.suffix == ".md":
                if dest not in cache:
                    cache[dest] = anchors(dest)
                if unquote(frag).lower() not in cache[dest]:
                    bad.append(f"{p.relative_to(ROOT)}  ->  {raw}   (no such heading)")

    print(f"{len(files)} files, {n} relative links, {len(bad)} broken")
    for b in bad:
        print(f"  {b}")
    return 1 if bad else 0


def _self_test() -> None:
    cases = {
        "The architecture split": "the-architecture-split",
        "🔴 The architecture split": "-the-architecture-split",
        "1. Co-folding (S1) — replaces experimental structure determination":
            "1-co-folding-s1--replaces-experimental-structure-determination",
        "Q2 — does sensitivity fall as scale rises? *(the headline)*":
            "q2--does-sensitivity-fall-as-scale-rises-the-headline",
        "`make check`": "make-check",
        "See [the plan](plan.md) first": "see-the-plan-first",
    }
    for heading, want in cases.items():
        got = slug(heading)
        assert got == want, f"{heading!r}: got {got!r}, want {want!r}"
    print("slug self-test OK")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        _self_test()
        raise SystemExit(0)
    raise SystemExit(main([a for a in sys.argv[1:] if not a.startswith("-")]))
