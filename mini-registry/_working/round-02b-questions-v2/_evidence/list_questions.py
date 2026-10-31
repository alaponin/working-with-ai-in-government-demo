"""List the groundwork's open questions into QUESTIONS.md and check each against GROUNDWORK.md (A1).

usage: list_questions.py <GROUNDWORK.md> <QUESTIONS.md to write>
"""
import re
import sys

gpath, qpath = sys.argv[1], sys.argv[2]
lines = open(gpath, encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(lines) if l.startswith("## Gaps against the sources"))
qs = []
for i in range(start + 1, len(lines)):
    if lines[i].startswith("## "):
        break
    if re.match(r"^\d+\. \*\*", lines[i]):
        qs.append((i + 1, lines[i]))
with open(qpath, "w", encoding="utf-8") as f:
    f.write("# The groundwork's open questions, listed by list_questions.py from docs/GROUNDWORK.md\n\n")
    for n, t in qs:
        f.write("- `docs/GROUNDWORK.md:%d` %s\n" % (n, t))
src = open(gpath, encoding="utf-8").read().split("\n")
listed = nf = 0
for l in open(qpath, encoding="utf-8"):
    m = re.match(r"^- `docs/GROUNDWORK\.md:(\d+)` (.*)$", l.rstrip("\n"))
    if not m:
        continue
    listed += 1
    n, t = int(m.group(1)), m.group(2)
    if not (1 <= n <= len(src) and t in src[n - 1]):
        nf += 1
        print("NOT FOUND line %d" % n)
print(listed)
print("%d not found" % nf)
