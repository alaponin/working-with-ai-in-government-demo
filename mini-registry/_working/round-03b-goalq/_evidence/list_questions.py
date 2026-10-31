"""A1: list the goal's questions from GOAL.md, under its heading "Gaps against the sources"."""
import re, sys
root = sys.argv[1]
out = sys.argv[2]
lines = open(root + "/docs/GOAL.md", encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(lines) if l.strip() == "## Gaps against the sources")
qs = [(i + 1, l) for i, l in enumerate(lines) if i > start and re.match(r"^\d+\. \*\*", l)]
with open(out, "w", encoding="utf-8") as f:
    f.write("# The goal's questions, listed from docs/GOAL.md by list_questions.py\n\n")
    for n, l in qs:
        f.write("- `docs/GOAL.md:%d` %s\n" % (n, l))
# check each listed question is a substring of GOAL.md at its line
listed = open(out, encoding="utf-8").read().split("\n")
nf = 0
count = 0
for l in listed:
    m = re.match(r"^- `docs/GOAL.md:(\d+)` (.*)$", l)
    if not m:
        continue
    count += 1
    if m.group(2) not in lines[int(m.group(1)) - 1]:
        nf += 1
        print("not found:", l[:80])
print(count)
print("%d not found" % nf)
