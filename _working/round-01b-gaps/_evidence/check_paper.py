"""Check the decision paper against the listed questions and its sources (A2 to A5).

usage: check_paper.py <estate root> <QUESTIONS.md> <GAPS-PAPER.md>
Paths in the paper's passages are relative to the estate root.
"""
import os
import re
import sys

root, qpath, ppath = sys.argv[1], sys.argv[2], sys.argv[3]
qs = []
for line in open(qpath, encoding="utf-8"):
    m = re.match(r"^- `docs/REQUIREMENTS\.md:(\d+)` (\*\*(G-\d\d)\*\* .*)$", line.rstrip("\n"))
    if m:
        qs.append((m.group(3), m.group(2)))
paper = open(ppath, encoding="utf-8").read()
plines = paper.split("\n")

# A2 - coverage both ways
sections = {}
cur = None
for line in plines:
    m = re.match(r"^## (G-\d\d) ", line)
    if m:
        cur = m.group(1)
        sections[cur] = []
        continue
    if line.startswith("## "):
        cur = None
    if cur:
        sections[cur].append(line)
qids = [g for g, _ in qs]
unanswered = []
for g, text in qs:
    body = sections.get(g)
    if body is None or ("> " + text) not in body:
        unanswered.append(g)
extra = [g for g in sections if g not in qids]
print("A2: questions listed %d, sections in the paper %d" % (len(qs), len(sections)))
for g in unanswered:
    print("  UNANSWERED " + g)
for g in extra:
    print("  EXTRA " + g)
print("A2: %d unanswered, %d extra" % (len(unanswered), len(extra)))

# A3 - every passage at its line
cache = {}
def lines_of(rel):
    if rel not in cache:
        cache[rel] = open(os.path.normpath(os.path.join(root, rel)), encoding="utf-8").read().split("\n")
    return cache[rel]
pat = re.compile(r"`((?:\.\./brief/MINI-REGISTRY-BRIEF\.md)|(?:docs/REQUIREMENTS\.md)):(\d+)` «([^»]*)»")
n = nf = wl = 0
for no, line in enumerate(plines, 1):
    for m in pat.finditer(line):
        n += 1
        rel, ln, text = m.group(1), int(m.group(2)), m.group(3)
        src = lines_of(rel)
        if 1 <= ln <= len(src) and text in src[ln - 1]:
            continue
        hits = [i + 1 for i, s in enumerate(src) if text in s]
        if hits:
            wl += 1
            print("  WRONG LINE paper:%d %s:%d, found at %s" % (no, rel, ln, hits))
        else:
            nf += 1
            print("  NOT FOUND paper:%d %s:%d %r" % (no, rel, ln, text[:60]))
print("A3: passages quoted %d" % n)
print("A3: %d not found, %d wrong line" % (nf, wl))

# A4 - positions, table rows, recommendations, per question
REC = "**Recommendation — a proposal for the owner's ruling, not a decision.**"
bad = 0
print("A4: question positions table-rows recommendations")
for g in qids:
    body = sections.get(g, [])
    pos = sum(1 for l in body if re.match(r"^\*\*Position [A-Z] — ", l))
    rows = sorted(set(re.match(r"^\| \(([a-d])\) ", l).group(1) for l in body if re.match(r"^\| \([a-d]\) ", l)))
    cols_ok = all(l.count("|") == pos + 2 for l in body if re.match(r"^\| \([a-d]\) ", l))
    recs = sum(1 for l in body if l.startswith(REC) and "We recommend" in l)
    flag = "" if (pos >= 2 and len(rows) == 4 and recs == 1 and cols_ok) else "  <-- short"
    if flag:
        bad += 1
    print("  %s %d %d %d%s%s" % (g, pos, len(rows), recs, "" if cols_ok else " (a row's cells do not match the positions)", flag))
print("A4: questions short of 2 positions, 4 rows (a)-(d) or 1 recommendation: %d" % bad)

# A5 - G-14 closed in one line quoting line 13; what the recommendations forgive
g14 = [l for l in plines if l.startswith("**G-14") and "`../brief/MINI-REGISTRY-BRIEF.md:13` «(capitals ignored)»" in l]
print("A5: lines closing G-14 with the brief's line 13 quoted: %d" % len(g14))
print("A5: sections headed G-14: %d" % (1 if "G-14" in sections else 0))
words = re.compile(r"space|accent|spelling|spelt|similar|fuzzy|forgiv|sound|nickname|initial|normalis|normaliz|trim", re.I)
print("A5: recommendation sentences naming anything a search could forgive (read each):")
for g in qids:
    for l in sections.get(g, []):
        if l.startswith(REC):
            for w in sorted(set(x.group(0).lower() for x in words.finditer(l))):
                print("  %s: %r" % (g, w))
decided = len(re.findall(r"the registry will|we decide|is decided", paper, re.I))
print("decision wording ('the registry will', 'we decide', 'is decided'): %d" % decided)
