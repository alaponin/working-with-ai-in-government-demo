"""A2, A4, A5: the count, both ways, from a count CSV and the two sets.

Usage: count.py <estate root> <count.csv> <REQUIREMENTS_SET.txt> <GOAL_SET.txt>
Prints the rows read, the unknown rows and the absent requirements; then requirements -> goal and
goal -> requirements, each total and every member unreached by name, with its ground or its source.
"""
import csv, re, sys

root, csvp, rsetp, gsetp = sys.argv[1:5]


def read_set(p):
    out = []
    for row in open(p, encoding="utf-8").read().split("\n"):
        if row:
            k, place, text = row.split("\t", 2)
            out.append((k, place))
    return out


rset = read_set(rsetp)
gset = read_set(gsetp)
rkeys = [k for k, _ in rset]
gkeys = [k for k, _ in gset]

rows = list(csv.DictReader(open(csvp, encoding="utf-8", newline="")))
print("rows read: %d (%s)" % (len(rows), csvp))

unknown = [r for r in rows if r["requirement"] not in rkeys
           or (r["element"] not in gkeys and r["element"] != "none")]
for r in unknown:
    print("unknown row: %s,%s" % (r["requirement"], r["element"]))
seen = set(r["requirement"] for r in rows)
absent = [k for k in rkeys if k not in seen]
for k in absent:
    print("absent requirement: %s" % k)
mixed = [k for k in rkeys if any(r["requirement"] == k and r["element"] == "none" for r in rows)
         and any(r["requirement"] == k and r["element"] != "none" for r in rows)]
for k in mixed:
    print("requirement both with none and with elements: %s" % k)
pairs = [(r["requirement"], r["element"]) for r in rows]
dups = sorted(set(p for p in pairs if pairs.count(p) > 1))
for p in dups:
    print("pair written twice: %s,%s" % p)
print("%d unknown, %d absent" % (len(unknown), len(absent)))

good = [r for r in rows if r not in unknown]

print()
print("== Requirements -> goal (%d requirements)" % len(rkeys))
reach = {k: sorted(set(r["element"] for r in good if r["requirement"] == k and r["element"] != "none"),
                   key=gkeys.index) for k in rkeys}
some = [k for k in rkeys if reach[k]]
none = [k for k in rkeys if not reach[k]]
for k in rkeys:
    print("  %s -> %s" % (k, " ".join(reach[k]) if reach[k] else "none"))
print("reach at least one element: %d" % len(some))
print("reach none: %d" % len(none))
for k in none:
    g = [r["ground"] for r in good if r["requirement"] == k and r["element"] == "none"]
    print("  %s — %s" % (k, g[0] if g else "(no ground: absent from the CSV)"))

# the source of each element of the goal
goal = open(root + "/docs/GOAL.md", encoding="utf-8").read().split("\n")
paper = open(root + "/docs/GOAL-QUESTIONS-PAPER.md", encoding="utf-8").read().split("\n")
tt = next(i for i, l in enumerate(paper) if l.strip() == "## Taken together")


def source_of(k, place):
    p, n = place.rsplit(":", 1)
    n = int(n)
    out = []
    if p == "docs/GOAL.md":
        for i in range(n, len(goal)):
            if i > n and goal[i].startswith("#"):
                break
            if goal[i].startswith("- **Source:**") or goal[i].startswith("- **Named by:**"):
                out.append("docs/GOAL.md:%d %s" % (i + 1, goal[i][2:]))
    else:
        out.append("%s:%d %s" % (p, n, paper[n - 1]))
    for i in range(tt, len(paper)):
        if paper[i].startswith("| %s |" % k):
            out.append("docs/GOAL-QUESTIONS-PAPER.md:%d %s" % (i + 1, paper[i]))
    return out


print()
print("== Goal -> requirements (%d elements)" % len(gkeys))
by = {k: sorted(set(r["requirement"] for r in good if r["element"] == k), key=rkeys.index) for k in gkeys}
for k in gkeys:
    print("  %s <- %s" % (k, " ".join(by[k]) if by[k] else "none"))
reached = [k for k in gkeys if by[k]]
unreached = [k for k in gkeys if not by[k]]
print("reached by at least one requirement: %d" % len(reached))
print("reached by none: %d" % len(unreached))
place = dict(gset)
for k in unreached:
    print("  %s" % k)
    for s in source_of(k, place[k]):
        print("      %s" % s)
