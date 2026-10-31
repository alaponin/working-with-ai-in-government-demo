"""Check QUESTIONS-PAPER.md (A2, A3, A4, A12, A13).

usage: check_paper.py <estate root> <QUESTIONS.md> <QUESTIONS-PAPER.md> <DEPENDENCIES.csv> <A13 log>
Paths in the paper's passages are relative to the estate root.
"""
import csv
import os
import re
import sys

root, qpath, ppath, dpath, rlog = sys.argv[1:6]
qs = []
for line in open(qpath, encoding="utf-8"):
    m = re.match(r"^- (`docs/GROUNDWORK\.md:(\d+)` (\d+)\. .*)$", line.rstrip("\n"))
    if m:
        qs.append((int(m.group(3)), m.group(1)))
plines = open(ppath, encoding="utf-8").read().split("\n")
sections, cur = {}, None
for line in plines:
    m = re.match(r"^## Q-(\d+) ", line)
    if m:
        cur = int(m.group(1))
        sections[cur] = []
        continue
    if line.startswith("## ") or line == "---":
        cur = None
    if cur is not None:
        sections[cur].append(line)

# A2
unanswered = [n for n, t in qs if n not in sections or ("> " + t) not in sections[n]]
extra = [n for n in sections if n not in [q for q, _ in qs]]
print("A2: questions listed %d, question sections %d" % (len(qs), len(sections)))
print("A2: %d unanswered, %d extra" % (len(unanswered), len(extra)))

# A3
cache = {}
def src(rel):
    if rel not in cache:
        cache[rel] = open(os.path.normpath(os.path.join(root, rel)), encoding="utf-8").read().split("\n")
    return cache[rel]
pat = re.compile(r"`([^`\s]+\.(?:md|csv)):(\d+)` «([^»]*)»")
n = nf = wl = 0
files = {}
for no, line in enumerate(plines, 1):
    for m in pat.finditer(line):
        n += 1
        rel, ln, text = m.group(1), int(m.group(2)), m.group(3)
        files[rel] = files.get(rel, 0) + 1
        s = src(rel)
        if 1 <= ln <= len(s) and text in s[ln - 1]:
            continue
        hits = [i + 1 for i, x in enumerate(s) if text in x]
        if hits:
            wl += 1
            print("  WRONG LINE paper:%d %s:%d, found at %s" % (no, rel, ln, hits))
        else:
            nf += 1
            print("  NOT FOUND paper:%d %s:%d %r" % (no, rel, ln, text[:60]))
qn = qbad = 0
for no, line in enumerate(plines, 1):
    m = re.match(r"^> `docs/GROUNDWORK\.md:(\d+)` (.*)$", line)
    if m:
        qn += 1
        s = src("docs/GROUNDWORK.md")
        ln = int(m.group(1))
        if not (1 <= ln <= len(s) and m.group(2) in s[ln - 1]):
            qbad += 1
            print("  QUESTION NOT AT ITS LINE paper:%d" % no)
rng = re.findall(r"`([^`\s]+\.(?:md|csv)):(\d+)-(\d+)`", "\n".join(plines))
rbad = 0
for rel, a, b in rng:
    if not (1 <= int(a) <= int(b) <= len(src(rel))):
        rbad += 1
        print("  RANGE OUT OF FILE %s:%s-%s" % (rel, a, b))
print("A3: passages quoted %d, by file %s; questions quoted %d; ranges cited %d, out of their file %d" % (n, sorted(files.items()), qn, len(rng), rbad))
print("A3: %d not found, %d wrong line" % (nf + qbad, wl))

# A4
PROP = "**Proposal — not a decision.**"
bad = 0
print("A4: question positions tables proposals")
for q, _ in qs:
    body = sections.get(q, [])
    pos = sum(1 for l in body if re.match(r"^\*\*Position [A-Z][^*]* — ", l))
    tables = sum(1 for l in body if l.startswith("| Test |"))
    props = sum(1 for l in body if l.startswith(PROP))
    ok = (pos, tables, props) == (2, 1, 1)
    bad += 0 if ok else 1
    print("  Q-%d %d %d %d%s" % (q, pos, tables, props, "" if ok else "  <-- not 2, 1, 1"))
print("A4: sections not reading 2, 1, 1: %d" % bad)
rows = [(q, l) for q, _ in qs for l in sections.get(q, []) if re.match(r"^\| \(", l)]
both = sum(1 for _, l in rows if l.rstrip().endswith("| both meet |"))
div = sum(1 for _, l in rows if l.rstrip().endswith("| divides |"))
print("A4: table rows %d: both meet %d, divides %d, unmarked %d" % (len(rows), both, div, len(rows) - both - div))

# A12
def qlist(s):
    return set(int(x) for x in re.findall(r"Q-(\d+)", s))
dep, by = {}, {}
for q, _ in qs:
    t = "\n".join(sections.get(q, []))
    m = re.search(r"\*\*Depends on:\*\* ([^*]*?)\. \*\*Depended on by:\*\* ([^\n]*?)\.$", t, re.M)
    dep[q], by[q] = (qlist(m.group(1)), qlist(m.group(2))) if m else (None, None)
    if m is None:
        print("  NO DEPENDENCY LINE Q-%d" % q)
pairs = set()
for row in csv.DictReader(open(dpath, encoding="utf-8")):
    pairs.add((int(row["depends"][2:]), int(row["on"][2:])))
oneway = 0
for a, b in sorted(pairs):
    da = b in (dep.get(a) or set())
    db = a in (by.get(b) or set())
    print("  Q-%d depends on Q-%d: declared in Q-%d %s, in Q-%d %s" % (a, b, a, "yes" if da else "NO", b, "yes" if db else "NO"))
    oneway += 0 if (da and db) else 1
declared = {(a, b) for a in dep if dep[a] for b in dep[a]} | {(b, a) for a in by if by[a] for b in by[a]}
notintable = declared - pairs
for a, b in sorted(notintable):
    print("  DECLARED, NOT IN THE TABLE: Q-%d on Q-%d" % (a, b))
print("A12: pairs in the table %d; declared in the paper %d; %d one-way; %d not in the table" % (len(pairs), len(declared), oneway, len(notintable)))

# A13
verdict = {}
for line in open(rlog, encoding="utf-8"):
    m = re.match(r"^Q-(\d+) rival .*can be met: (yes|no)$", line.rstrip("\n"))
    if m:
        verdict[int(m.group(1))] = m.group(2)
dis = 0
print("A13: question, rival's (c) cell in the paper, the program's verdict")
for q, _ in qs:
    row = [l for l in sections.get(q, []) if l.startswith("| (c) known numbers")]
    if len(row) != 1:
        print("  Q-%d: rows '(c) known numbers' %d" % (q, len(row)))
        dis += 1
        continue
    cells = [c.strip() for c in row[0].strip("|").split("|")]
    a_cell, b_cell = cells[1], cells[2]
    pa = "yes" if a_cell.startswith("yes") else "no"
    pb = "yes" if b_cell.startswith("yes") else "no"
    ok = pb == verdict.get(q) and pa == "yes"
    dis += 0 if ok else 1
    print("  Q-%d paper A %s, B %s; program B %s%s" % (q, pa, pb, verdict.get(q), "" if ok else "  <-- DISAGREES"))
print("A13: %d disagreements" % dis)
