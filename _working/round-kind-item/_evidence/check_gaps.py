#!/usr/bin/env python3
"""Check every quotation in a gaps or quotes file against the line its Source names.

Usage: check_gaps.py <file.md> <root>
A block is a line `Source: `<path>:<line>`` followed by `> ` lines (joined by a space).
Prints one line per quotation and a closing `<n> not found`; exits 1 when n > 0.
"""
import re, sys, pathlib

src_re = re.compile(r"^Source: `([^`]+):(\d+)`\s*$")
text, root = pathlib.Path(sys.argv[1]).read_text().splitlines(), pathlib.Path(sys.argv[2])
blocks, cur = [], None
for ln in text:
    m = src_re.match(ln)
    if m:
        cur = [m.group(1), int(m.group(2)), []]
        blocks.append(cur)
    elif cur is not None and ln.startswith("> "):
        cur[2].append(ln[2:])
    elif cur is not None and ln.strip() == "":
        if cur[2]:
            cur = None
missing = 0
for path, no, q in blocks:
    quote = " ".join(q)
    lines = (root / path).read_text().splitlines()
    ok = 0 < no <= len(lines) and quote in lines[no - 1]
    missing += not ok
    print(f"{'found    ' if ok else 'NOT FOUND'} {path}:{no}  {quote[:70]}")
print(f"{len(blocks)} quotations, {missing} not found")
sys.exit(1 if missing else 0)
