"""Check QUESTIONS-PAPER.md against the listed questions and its sources (A2, A3, A4).

usage: check_paper.py <estate root> <QUESTIONS.md> <QUESTIONS-PAPER.md>
Paths in the paper's passages are relative to the estate root.
"""
import os
import re
import sys

root, qpath, ppath = sys.argv[1], sys.argv[2], sys.argv[3]
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
for n in unanswered:
    print("  UNANSWERED Q-%d" % n)
for n in extra:
    print("  EXTRA Q-%d" % n)
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
# the questions quoted in the sections, as `docs/GROUNDWORK.md:N` <text> (no guillemets)
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
print("A3: passages quoted %d, by file %s; questions quoted %d" % (n, sorted(files.items()), qn))
print("A3: %d not found, %d wrong line" % (nf + qbad, wl))

# A4
PROP = "**Proposal — not a decision.**"
bad = 0
print("A4: question positions tables proposals")
for q, _ in qs:
    body = sections.get(q, [])
    pos = sum(1 for l in body if re.match(r"^\*\*Position [A-Z] — ", l))
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
deps = {q: re.findall(r"Depends on ([^.:]*)", "\n".join(sections.get(q, []))) for q, _ in qs}
print("depends lines: %s" % {q: d for q, d in deps.items() if d})
