#!/usr/bin/env python3
"""Fail on missing relative targets in tracked Markdown files."""

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^]\n]*\]\(([^)\n]+)\)")


def links(text):
    fenced = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        if not fenced:
            for match in LINK.finditer(line):
                yield number, match.group(1).strip().split(maxsplit=1)[0].strip("<>")


if "--self-test" in sys.argv:
    assert list(links("[ok](README.md)\n")) == [(1, "README.md")]
    assert not list(links("```md\n[ignored](missing.md)\n```\n"))
    sys.exit(0)

tracked = subprocess.check_output(["git", "ls-files", "-z", "--", "*.md"], cwd=ROOT)
missing = []
for name in filter(None, tracked.decode().split("\0")):
    page = ROOT / name
    for number, target in links(page.read_text(encoding="utf-8")):
        if not target or target.startswith(("#", "/")):
            continue
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        destination = (page.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(ROOT) or not destination.exists():
            missing.append(f"{name}:{number}: {target}")

if missing:
    print("Missing relative Markdown targets:\n" + "\n".join(missing))
    sys.exit(1)
print("Tracked relative Markdown links resolve.")
