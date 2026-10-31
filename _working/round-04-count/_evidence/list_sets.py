"""A1: list the two sets from their sources, then check each line at the place it names.

The requirements: every heading "### R-nn" of docs/REQUIREMENTS.md.
The goal as ruled: every heading "### S-n", "### F-n", "### SC-n" of docs/GOAL.md, and F-6 and F-7
from the line beginning "**Added:**" in the section "Taken together" of docs/GOAL-QUESTIONS-PAPER.md.
Usage: list_sets.py <estate root> <evidence folder>
"""
import re, sys

root, ev = sys.argv[1], sys.argv[2]


def lines_of(rel):
    return open(root + "/" + rel, encoding="utf-8").read().split("\n")


req = lines_of("docs/REQUIREMENTS.md")
goal = lines_of("docs/GOAL.md")
paper = lines_of("docs/GOAL-QUESTIONS-PAPER.md")

rset = [("R-%s" % m.group(1), "docs/REQUIREMENTS.md", i + 1, l)
        for i, l in enumerate(req) for m in [re.match(r"^### R-(\d\d)\s*$", l)] if m]

gset = [(m.group(1), "docs/GOAL.md", i + 1, l)
        for i, l in enumerate(goal) for m in [re.match(r"^### ((?:S|F|SC)-\d+) — ", l)] if m]
tt = next(i for i, l in enumerate(paper) if l.strip() == "## Taken together")
for i, l in enumerate(paper):
    if i > tt and l.startswith("**Added:**"):
        for e in re.findall(r"\b(F-\d+), ", l):
            gset.append((e, "docs/GOAL-QUESTIONS-PAPER.md", i + 1, l))

order = {"S": 0, "F": 1, "SC": 2}
gset.sort(key=lambda t: (order[t[0].split("-")[0]], int(t[0].split("-")[1])))

with open(ev + "/REQUIREMENTS_SET.txt", "w", encoding="utf-8") as f:
    for k, p, n, l in rset:
        f.write("%s\t%s:%d\t%s\n" % (k, p, n, l))
with open(ev + "/GOAL_SET.txt", "w", encoding="utf-8") as f:
    for k, p, n, l in gset:
        f.write("%s\t%s:%d\t%s\n" % (k, p, n, l))

# read back and check every line at the place it names
for name in ("REQUIREMENTS_SET.txt", "GOAL_SET.txt"):
    count = nf = 0
    keys = []
    for row in open(ev + "/" + name, encoding="utf-8").read().split("\n"):
        if not row:
            continue
        k, place, text = row.split("\t", 2)
        p, n = place.rsplit(":", 1)
        count += 1
        keys.append(k)
        at = lines_of(p)[int(n) - 1]
        if text != at or k not in at:
            nf += 1
            print("not found at its place:", row[:90])
    print("%s: %d lines, %d distinct, %d not found at its place" % (name, count, len(set(keys)), nf))
    print("  " + " ".join(keys))
