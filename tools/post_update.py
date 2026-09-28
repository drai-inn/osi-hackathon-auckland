#!/usr/bin/env python3
"""Post an update to the live log: sync, entry, and PR comment, in one pass.

The live log is a pull request people subscribe to, and the promise made to
them is "every update and nothing else". A bare "bring the live log up to date
with main" commit breaks that promise in both directions: it spends a
subscriber's attention and tells them nothing, and it makes the real updates
harder to find among the noise.

So the three things that make an update happen together or not at all:

  1. the branch is synced with main, which keeps the pull request's diff honest
  2. a dated entry goes into EVENT-LOG.md, which is the record
  3. the same text is posted as a pull request comment, which is what actually
     reaches a subscriber's inbox as prose rather than as a subject line

A release is the natural unit of all this. Cut the tag, write the entry, run
this once.

    python3 tools/post_update.py --entry entry.md --release v26.9.6

Standard library, plus git and the gh CLI. --dry-run does everything except
push and comment, and prints what it would have sent.
"""

import argparse
import datetime
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRANCH = "live-log"
PR = "16"
LOG = "EVENT-LOG.md"
REPO = "drai-inn/osi-hackathon-auckland"

# An entry opens with this and nothing else, so the file is unambiguous about
# where one ends and the next begins.
HEADING = re.compile(r"^## (\d{4}-\d{2}-\d{2}) · .+$")


def run(*cmd, cwd=None, check=True):
    out = subprocess.run(cmd, cwd=cwd, check=check, text=True, capture_output=True)
    if check and out.returncode:
        sys.exit(f"{' '.join(cmd)}\n{out.stderr}")
    return out.stdout.strip()


def read_entry(path: Path, today: str) -> tuple[str, str]:
    text = path.read_text().strip()
    first = text.splitlines()[0] if text else ""
    m = HEADING.match(first)
    if not m:
        sys.exit(f"the entry has to open with '## YYYY-MM-DD · Headline', not:\n  {first}")
    if m.group(1) != today:
        sys.exit(f"the entry is dated {m.group(1)} and today is {today}. "
                 "A log people follow is worth dating honestly.")
    return text, m.group(1)


def insert(log: str, entry: str) -> str:
    """Newest entry at the top, under the status board and above the last one."""
    lines = log.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if HEADING.match(line.rstrip("\n")):
            return "".join(lines[:i]) + entry + "\n\n---\n\n" + "".join(lines[i:])
    sys.exit(f"found no existing entry in {LOG} to put this one above")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--entry", required=True, type=Path,
                    help="markdown file holding the entry, opening with '## YYYY-MM-DD · Headline'")
    ap.add_argument("--release", default=None,
                    help="tag this update covers, e.g. v26.9.6. Linked from the entry and the comment")
    ap.add_argument("--row", action="append", default=[], metavar="NAME=VALUE",
                    help="update a table row by name, repeatable. The status board and the header "
                         "both use '| **Name** | value |', so this reaches either. "
                         "e.g. --row 'Week=28 Sep – 4 Oct'")
    ap.add_argument("--dry-run", action="store_true",
                    help="do everything except push and comment")
    args = ap.parse_args()

    today = datetime.date.today().isoformat()
    entry, _ = read_entry(args.entry, today)

    if args.release:
        tags = run("git", "tag", "--list", args.release, cwd=ROOT)
        if not tags:
            sys.exit(f"no such tag: {args.release}. Cut it before you announce it.")
        entry += (f"\n\nReleased as **[{args.release}]"
                  f"(https://github.com/{REPO}/releases/tag/{args.release})**.")

    work = Path(tempfile.mkdtemp(prefix="live-log-"))
    try:
        run("git", "fetch", "-q", "origin", BRANCH, cwd=ROOT)
        # Detached on purpose. A worktree that checks out the branch moves the
        # real ref when it commits, which means a --dry-run leaves the branch
        # advanced and the next real run stacks a second entry on top of it.
        # That happened once; it is not allowed to happen twice.
        run("git", "worktree", "add", "--detach", "-q", str(work),
            f"origin/{BRANCH}", cwd=ROOT)

        # Sync. The log is ours on both sides of a conflict; main only ever
        # carries the pointer to this branch.
        merged = subprocess.run(["git", "merge", "main", "--no-edit", "-m",
                                 "Sync the live log with main"],
                                cwd=work, text=True, capture_output=True)
        if merged.returncode:
            if "EVENT-LOG.md" not in merged.stdout + merged.stderr:
                sys.exit(f"the merge failed on something other than the log:\n{merged.stdout}\n{merged.stderr}")
            run("git", "checkout", "--ours", LOG, cwd=work)
            run("git", "add", LOG, cwd=work)
            run("git", "commit", "-q", "--no-edit", cwd=work)

        path = work / LOG
        log = path.read_text()
        for row in args.row:
            if "=" not in row:
                sys.exit(f"--row wants NAME=VALUE, got: {row}")
            name, value = row.split("=", 1)
            log, n = re.subn(rf"(\| \*\*{re.escape(name.strip())}\*\* \| )[^|]*(\|)",
                             lambda m, v=value.strip(): m.group(1) + v + " " + m.group(2),
                             log, count=1)
            if not n:
                sys.exit(f"found no table row called '{name.strip()}' to update")
        updated = insert(log, entry)
        heading = entry.splitlines()[0]
        if updated.count(heading) != 1:
            sys.exit(f"that entry would appear {updated.count(heading)} times in {LOG}. "
                     "Something already put it there.")
        path.write_text(updated)

        run("git", "add", LOG, cwd=work)
        subject = entry.splitlines()[0].lstrip("# ").strip()
        run("git", "commit", "-q", "-m",
            f"Log: {subject}\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>", cwd=work)

        if args.dry_run:
            print("--- would push to", BRANCH, "---")
            print(run("git", "log", "--oneline", "-3", cwd=work))
            print(f"\n--- would comment on PR #{PR} ---\n{entry}")
            return

        run("git", "push", "-q", "origin", f"HEAD:{BRANCH}", cwd=work)
        body = work / ".comment.md"
        body.write_text(entry)
        run("gh", "pr", "comment", PR, "--repo", REPO, "--body-file", str(body), cwd=work)
        print(f"posted to {BRANCH} and commented on PR #{PR}")
    finally:
        run("git", "worktree", "remove", "--force", str(work), cwd=ROOT, check=False)
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
