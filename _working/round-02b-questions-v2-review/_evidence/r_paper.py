"""Review of QUESTIONS-PAPER.md v2, written by the reviewing session (C-2026-10-31-12 v2).
Reads only; writes nothing but stdout.
usage: r_paper.py <estate root: .../mini-registry>
Parts: the set (A1, A2) listed from GROUNDWORK.md by its own route; every citation printed beside its
source line (A3, page part 2); positions/tables/proposals per section (A4); the dependency lines, both
ways (A12); the whole-quote of GAPS-PAPER.md:196 (found-not-fixed item 1); every (c) row (A13).
"""
import os, re, sys
root = sys.argv[1]
def lines(rel):
    return open(os.path.normpath(os.path.join(root, rel)), encoding="utf-8").read().split("\n")
P = lines("docs/QUESTIONS-PAPER.md")
GW = lines("docs/GROUNDWORK.md")

print("== THE SET, from GROUNDWORK.md's section 'Gaps against the sources'")
start = [i for i, l in enumerate(GW) if l.strip() == "## Gaps against the sources"][0]
gw_q = {}
for i in range(start + 1, len(GW)):
    if GW[i].startswith("## "):
        break
    m = re.match(r"^(\d+)\. ", GW[i])
    if m:
        gw_q[int(m.group(1))] = (i + 1, GW[i])
print("numbered items:", len(gw_q), sorted(gw_q))
sec = {}
cur = None
for i, l in enumerate(P, 1):
    m = re.match(r"^## Q-(\d+) ", l)
    if m:
        cur = int(m.group(1)); sec[cur] = []; continue
    if l.startswith("## ") or l == "---":
        cur = None
    if cur is not None:
        sec[cur].append((i, l))
print("question sections in the paper:", len(sec), sorted(sec))
miss = [n for n in gw_q if n not in sec]
extra = [n for n in sec if n not in gw_q]
notword = []
for n, (ln, text) in gw_q.items():
    want = "> `docs/GROUNDWORK.md:%d` %s" % (ln, text)
    if n in sec and not any(l == want for _, l in sec[n]):
        notword.append(n)
print("in the groundwork, not answered: %d %s" % (len(miss), miss))
print("in the paper, not in the groundwork: %d %s" % (len(extra), extra))
print("question quoted not word for word or at another line: %d %s" % (len(notword), notword))

print("\n== EVERY CITATION, beside its source line")
pat = re.compile(r"`([^`\s]+\.(?:md|csv)):(\d+)(?:-(\d+))?`(?: «([^»]*)»)?")
n = bad = 0
for no, l in enumerate(P, 1):
    for m in pat.finditer(l):
        rel, a, b, q = m.group(1), int(m.group(2)), m.group(3), m.group(4)
        if rel.startswith("_working"):
            continue
        s = lines(rel)
        n += 1
        if b:
            ok = 1 <= a <= int(b) <= len(s)
            print("paper:%d %s:%d-%s RANGE first=%r | last=%r %s" % (no, rel, a, b, s[a-1][:70], s[int(b)-1][:70], "OK" if ok else "OUT"))
        elif q is None:
            print("paper:%d %s:%d NO QUOTE source=%r" % (no, rel, a, s[a-1][:120]))
        else:
            ok = q in s[a-1]
            whole = q == s[a-1]
            print("paper:%d %s:%d %s%s\n   quoted: %s\n   source: %s" % (no, rel, a, "OK" if ok else "NOT AT LINE", " (whole line)" if whole else "", q[:200], s[a-1][:400]))
        if (b and not ok) or (q is not None and not b and not ok):
            bad += 1
print("citations read: %d; not holding: %d" % (n, bad))
print("\n== prose references to a line of the brief or the paper")
for no, l in enumerate(P, 1):
    for m in re.finditer(r"(?<![:`])\b(?:line|lines) (\d+)(?: to (\d+))?", l):
        print("paper:%d %r" % (no, l[max(0, m.start()-40):m.end()+30]))

print("\n== GAPS-PAPER.md:196 quoted whole?")
g = lines("docs/GAPS-PAPER.md")[195]
m = re.search(r"`docs/GAPS-PAPER\.md:196` «(.*)»\s*$", P[10])
print("quoted == source line 196:", m is not None and m.group(1) == g)

print("\n== A4: positions, tables, proposals per section; table rows")
rows_all = []
for q in sorted(sec):
    body = [l for _, l in sec[q]]
    pos = sum(1 for l in body if l.startswith("**Position "))
    tab = sum(1 for l in body if l.startswith("| Test |"))
    prop = sum(1 for l in body if l.startswith("**Proposal — not a decision.**"))
    rows = [(i, l) for i, l in sec[q] if l.startswith("| (")]
    rows_all += [(q, i, l) for i, l in rows]
    print("Q-%d positions %d tables %d proposals %d rows %d" % (q, pos, tab, prop, len(rows)))
bm = sum(1 for _, _, l in rows_all if l.rstrip().endswith("| both meet |"))
dv = sum(1 for _, _, l in rows_all if l.rstrip().endswith("| divides |"))
print("rows %d both meet %d divides %d" % (len(rows_all), bm, dv))
print("rows marked 'divides' whose two cells both begin 'yes':")
for q, i, l in rows_all:
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if c[-1] == "divides" and c[1].startswith("yes") and c[2].startswith("yes"):
        print("  Q-%d paper:%d %s" % (q, i, l))

print("\n== A12: dependency lines, both ways")
dep, by = {}, {}
for q in sorted(sec):
    t = [l for _, l in sec[q] if l.startswith("**Depends on:**")]
    m = re.match(r"\*\*Depends on:\*\* (.*?)\. \*\*Depended on by:\*\* (.*?)\.$", t[0]) if len(t) == 1 else None
    f = lambda s: set(int(x) for x in re.findall(r"Q-(\d+)", s))
    dep[q], by[q] = (f(m.group(1)), f(m.group(2))) if m else (set(), set())
    print("Q-%d depends on %s; depended on by %s" % (q, sorted(dep[q]), sorted(by[q])))
oneway = []
for a in dep:
    for b in dep[a]:
        if a not in by.get(b, set()):
            oneway.append((a, b, "declared in Q-%d, not in Q-%d's 'depended on by'" % (a, b)))
for b in by:
    for a in by[b]:
        if b not in dep.get(a, set()):
            oneway.append((a, b, "declared in Q-%d's 'depended on by', not in Q-%d" % (b, a)))
print("pairs declared: %d; one-way: %d %s" % (sum(len(v) for v in dep.values()), len(oneway), oneway))
print("other questions named in a section but not in its dependency line:")
for q in sorted(sec):
    named = set(int(x) for _, l in sec[q] if not l.startswith("**Depends on:**") and not l.startswith(">") for x in re.findall(r"Q-(\d+)", l)) - {q}
    left = named - dep[q] - by[q]
    if left:
        print("  Q-%d names %s" % (q, sorted(left)))

print("\n== every row (c), A and B cells")
for q, i, l in rows_all:
    if l.startswith("| (c)"):
        print("Q-%d paper:%d %s" % (q, i, l))
