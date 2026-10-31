"""Rebuild the first edition of the paper from version 1's planted copy (undoing its five plants,
proved by its sha256), then list, per question, every table cell, position statement and ground
that version 2 changed, with its line in the new paper (tests A11 and A12).

usage: cells_diff.py <planted copy of version 1> <GAPS-PAPER.md now> <rebuilt v1 out>
"""
import hashlib
import re
import sys

planted, now_path, out_v1 = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(planted, encoding="utf-8").read()
for old, new in [
    ("## G-13 — the note's one page", "## G-15 — the note's one page"),
    ("«if it finds none, it gives the child a new learner number and saves the record;»",
     "«if it finds none, it gives the pupil a new learner number and saves the record;»"),
    ("`../brief/MINI-REGISTRY-BRIEF.md:27` «| Ages | 6 to 12 |»",
     "`../brief/MINI-REGISTRY-BRIEF.md:26` «| Ages | 6 to 12 |»"),
    ("**Position B — the pages only.**", "Position B, the pages only."),
    ("**G-14 — closed, not reopened.**", "G-14 closed."),
]:
    s = s.replace(new, old, 1)
open(out_v1, "w", encoding="utf-8").write(s)
print("v1 rebuilt sha256 %s" % hashlib.sha256(s.encode("utf-8")).hexdigest())

def parts(text):
    out = {}
    cur = None
    for no, line in enumerate(text.split("\n"), 1):
        m = re.match(r"^## (G-\d\d) ", line)
        if m:
            cur = m.group(1)
            continue
        if line.startswith("## "):
            cur = None
        if not cur:
            continue
        m = re.match(r"^\| \(([a-d])\) [^|]*\|(.*)\|$", line)
        if m:
            for i, cell in enumerate(m.group(2).split("|")):
                out[(cur, "(%s) %s" % (m.group(1), "ABC"[i]))] = (cell.strip(), no)
        m = re.match(r"^\*\*Position ([A-Z]) — ", line)
        if m:
            out[(cur, "Position %s" % m.group(1))] = (line, no)
        if line.startswith("*Ground:*"):
            out[(cur, "Ground")] = (line, no)
        if line.startswith("**Given to every position"):
            out[(cur, "Given to every position")] = (line, no)
    return out

old, new = parts(s), parts(open(now_path, encoding="utf-8").read())
gs = sorted(set(k[0] for k in new))
tot_cells = 0
for g in gs:
    changed = [(k[1], new[k][1]) for k in sorted(new, key=lambda k: new[k][1]) if k[0] == g and (k not in old or old[k][0] != new[k][0])]
    cells = [c for c in changed if c[0].startswith("(")]
    tot_cells += len(cells)
    print("%s: %d table cells changed; %s" % (g, len(cells), ", ".join("%s paper:%d" % c for c in changed) or "nothing changed"))
print("table cells changed in all: %d, in %d sections" % (tot_cells, sum(1 for g in gs if any(k[0] == g and k[1].startswith("(") and (k not in old or old[k][0] != new[k][0]) for k in new))))
