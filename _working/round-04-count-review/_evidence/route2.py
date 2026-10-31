"""The review's second route: the count from the goal's own citations.

For each step and failure of docs/GOAL.md, the R-<nn> its "Source" line names; for the screens, the
R-<nn> the prose of section 3 names for every screen (GOAL.md has no "Source" line on a screen);
for F-6, F-7 and the amended elements, every R-<nn> in the ruled parts of
docs/GOAL-QUESTIONS-PAPER.md: each "**Proposal" line and the section "Taken together" to its end.
Then both totals each way, and every pair in one route and not the other, set beside count.csv.
Usage: route2.py <estate root> <count.csv>
"""
import csv, re, sys

root, csvp = sys.argv[1], sys.argv[2]
goal = open(root + "/docs/GOAL.md", encoding="utf-8").read().split("\n")
paper = open(root + "/docs/GOAL-QUESTIONS-PAPER.md", encoding="utf-8").read().split("\n")
req = open(root + "/docs/REQUIREMENTS.md", encoding="utf-8").read().split("\n")

R = ["R-%02d" % i for i in range(1, 24)]
assert [l for l in req if re.match(r"^### R-\d\d\s*$", l)] == ["### " + r for r in R]
G = ["S-%d" % i for i in range(1, 8)] + ["F-%d" % i for i in range(1, 8)] + ["SC-%d" % i for i in range(1, 6)]

cites = {}   # element -> {R-nn: "path:line"}
heads = {}
for i, l in enumerate(goal):
    m = re.match(r"^### ((?:S|F|SC)-\d+) — ", l)
    if m:
        heads[m.group(1)] = i
print("elements with a heading in GOAL.md: %d  %s" % (len(heads), " ".join(heads)))
for k, i in heads.items():
    cites[k] = {}
    for j in range(i + 1, len(goal)):
        if goal[j].startswith("#"):
            break
        if goal[j].startswith("- **Source:**"):
            for r in re.findall(r"\bR-\d\d\b", goal[j]):
                cites[k][r] = "docs/GOAL.md:%d" % (j + 1)

# the screens: the prose of section 3 before the first screen heading
s3 = next(i for i, l in enumerate(goal) if l.startswith("## 3. The screens"))
first_sc = min(heads[k] for k in heads if k.startswith("SC-"))
for j in range(s3, first_sc):
    found = re.findall(r"\bR-\d\d\b", goal[j])
    if found:
        print("screens' prose, docs/GOAL.md:%d cites %s" % (j + 1, " ".join(found)))
        for k in heads:
            if k.startswith("SC-"):
                for r in found:
                    cites[k].setdefault(r, "docs/GOAL.md:%d (section 3 prose)" % (j + 1))

# the ruled parts of the paper
for k in ("F-6", "F-7"):
    cites.setdefault(k, {})
tt = next(i for i, l in enumerate(paper) if l.strip() == "## Taken together")
ruled = [(i, l) for i, l in enumerate(paper) if l.startswith("**Proposal")] + \
        [(i, l) for i, l in enumerate(paper) if i >= tt]
print("ruled lines read in the paper: %d (%d proposals, %d lines of 'Taken together' from line %d)"
      % (len(ruled), sum(1 for i, l in ruled if l.startswith("**Proposal")), len(paper) - tt, tt + 1))
nruled = 0
for i, l in ruled:
    found = re.findall(r"\bR-\d\d\b", l)
    if found:
        nruled += 1
        print("ruled line docs/GOAL-QUESTIONS-PAPER.md:%d cites %s :: %s" % (i + 1, " ".join(found), l[:100]))
        m = re.match(r"^\| ((?:S|F|SC)-\d+) \|", l)
        for r in found:
            if m:
                cites[m.group(1)].setdefault(r, "docs/GOAL-QUESTIONS-PAPER.md:%d" % (i + 1))
print("ruled lines citing a requirement: %d" % nruled)

c2 = set((r, k) for k in G for r in cites.get(k, {}))
print()
print("== route 2: pairs from the goal's citations: %d" % len(c2))
for k in G:
    print("  %s <- %s" % (k, " ".join("%s (%s)" % (r, cites[k][r]) for r in sorted(cites.get(k, {}))) or "none"))

rows = list(csv.DictReader(open(csvp, encoding="utf-8", newline="")))
c1 = set((r["requirement"], r["element"]) for r in rows if r["element"] != "none")
ground = {(r["requirement"], r["element"]): r["ground"] for r in rows}
print("== route 1: pairs of count.csv (element not none): %d" % len(c1))


def totals(pairs, name):
    rr = [r for r in R if any(p[0] == r for p in pairs)]
    gg = [k for k in G if any(p[1] == k for p in pairs)]
    print("%s: requirements reaching >=1 element %d, none %d; elements reached %d, none %d"
          % (name, len(rr), len(R) - len(rr), len(gg), len(G) - len(gg)))
    print("    requirements reaching none: %s" % " ".join(r for r in R if r not in rr))
    print("    elements reached by none:   %s" % " ".join(k for k in G if k not in gg))
    return set(rr), set(gg)


print()
r1, g1 = totals(c1, "route 1 (count.csv)")
r2, g2 = totals(c2, "route 2 (goal's citations)")
print()
print("requirements reached in route 1 only: %s" % " ".join(r for r in R if r in r1 and r not in r2))
print("requirements reached in route 2 only: %s" % (" ".join(r for r in R if r in r2 and r not in r1) or "none"))
print("elements reached in route 1 only: %s" % (" ".join(k for k in G if k in g1 and k not in g2) or "none"))
print("elements reached in route 2 only: %s" % (" ".join(k for k in G if k in g2 and k not in g1) or "none"))
print()
both = c1 & c2
print("pairs in both routes: %d" % len(both))
only2 = sorted(c2 - c1, key=lambda p: (G.index(p[1]), p[0]))
print("pairs in route 2 only (the goal cites, count.csv lacks): %d" % len(only2))
for r, k in only2:
    print("  %s,%s  cited at %s" % (r, k, cites[k][r]))
only1 = sorted(c1 - c2, key=lambda p: (p[0], G.index(p[1])))
print("pairs in route 1 only (count.csv has, the goal does not cite): %d" % len(only1))
for r, k in only1:
    print("  %s,%s  ground: %s" % (r, k, ground[(r, k)]))
