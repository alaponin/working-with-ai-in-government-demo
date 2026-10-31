"""Review of C-2026-10-31-11: the 14 questions listed again and compared both ways, and every
citation of the paper printed beside the full source line it names, for reading by the reviewer.

usage: r_questions_and_citations.py <estate root>
Route: the questions are read from GROUNDWORK.md by their numbering 1. to 14. under the heading
"Gaps against the sources" (not by the round's QUESTIONS.md); the paper is read by its blockquotes
and its headings; QUESTIONS.md is then compared with this listing as a third party.
"""
import os
import re
import sys

root = sys.argv[1]
G = os.path.join(root, "docs/GROUNDWORK.md")
P = os.path.join(root, "docs/QUESTIONS-PAPER.md")
Q = os.path.join(root, "_working/round-02b-questions/_evidence/QUESTIONS.md")
g = open(G, encoding="utf-8").read().split("\n")
p = open(P, encoding="utf-8").read().split("\n")

# 1. the groundwork's set, from its own source
h = [i for i, l in enumerate(g) if l.strip() == "## Gaps against the sources"]
assert len(h) == 1, h
mine = {}
for i in range(h[0] + 1, len(g)):
    if g[i].startswith("## "):
        break
    m = re.match(r"^(\d+)\. \*\*(.+?)\*\* ", g[i])
    if m:
        mine[int(m.group(1))] = (i + 1, m.group(2), g[i])
print("groundwork: numbered items under 'Gaps against the sources': %d; numbers %s" % (len(mine), sorted(mine)))

# 2. the paper's set: headings and blockquotes
heads = {}
quotes = {}
cur = None
for no, l in enumerate(p, 1):
    m = re.match(r"^## Q-(\d+) — (.+)$", l)
    if m:
        cur = int(m.group(1))
        heads[cur] = (no, m.group(2))
        continue
    if l.startswith("## "):
        cur = None
    m = re.match(r"^> `docs/GROUNDWORK\.md:(\d+)` (.+)$", l)
    if m and cur is not None:
        quotes.setdefault(cur, []).append((no, int(m.group(1)), m.group(2)))
print("paper: Q- headings %d; blockquoted questions %d" % (len(heads), sum(len(v) for v in quotes.values())))

# 3. both ways
g_not_p, p_not_g, mism = [], [], []
for n, (ln, title, text) in mine.items():
    qs = quotes.get(n, [])
    if len(qs) != 1:
        g_not_p.append(n)
        continue
    pno, cl, qt = qs[0]
    if cl != ln or qt != text:
        mism.append((n, "line %d vs %d" % (cl, ln), qt == text))
    t = title.rstrip(".").lower()
    if heads[n][1].lower() != t:
        print("  title differs Q-%d: groundwork %r · paper heading %r" % (n, t, heads[n][1]))
for n in heads:
    if n not in mine:
        p_not_g.append(n)
print("in the groundwork, not answered in the paper: %d %s" % (len(g_not_p), g_not_p))
print("in the paper, not in the groundwork: %d %s" % (len(p_not_g), p_not_g))
print("quoted at another line or not word for word: %d %s" % (len(mism), mism))

# 4. QUESTIONS.md against this listing
ql = [l.rstrip("\n") for l in open(Q, encoding="utf-8") if l.startswith("- `docs/GROUNDWORK.md:")]
qset = set()
for l in ql:
    m = re.match(r"^- `docs/GROUNDWORK\.md:(\d+)` (.+)$", l)
    qset.add((int(m.group(1)), m.group(2)))
gset = {(ln, text) for (ln, title, text) in mine.values()}
print("QUESTIONS.md lines %d; same as this listing: %s; only in QUESTIONS.md %d; only here %d" % (
    len(ql), qset == gset, len(qset - gset), len(gset - qset)))

# 5. every citation `path:line` «words», printed with the full source line, for reading
pat = re.compile(r"`([^`\s]+\.(?:md|csv)):(\d+)` «([^»]*)»")
cache = {}
n = bad = 0
print("\n--- citations: paper line · cited path:line · substring found at that line · the full source line")
for no, l in enumerate(p, 1):
    for m in pat.finditer(l):
        n += 1
        rel, ln, words = m.group(1), int(m.group(2)), m.group(3)
        path = os.path.normpath(os.path.join(root, rel))
        if path not in cache:
            cache[path] = open(path, encoding="utf-8").read().split("\n")
        s = cache[path]
        line = s[ln - 1] if 1 <= ln <= len(s) else ""
        ok = words in line
        bad += 0 if ok else 1
        print("paper:%d · %s:%d · %s\n    quoted: %s\n    source: %s" % (no, rel, ln, "yes" if ok else "NO", words, line))
print("\ncitations %d; not found at their line %d" % (n, bad))
# prose references to a line of the brief, not in the quoted form
for no, l in enumerate(p, 1):
    for m in re.finditer(r"(?:brief's |)line (\d+)(?:'s)?", l):
        if "`" in l[max(0, m.start() - 40):m.start()]:
            continue
        print("prose reference paper:%d · %r" % (no, l[max(0, m.start() - 30):m.end() + 30]))
