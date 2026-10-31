#!/usr/bin/env python3
"""The review's own reading of docs/GOAL-QUESTIONS-PAPER.md, written from the paper's and the goal's
words, not from the round's programs. Prints: the questions listed from GOAL.md and compared both
ways; every citation beside its whole source line; every range's first and last line; per-section
counts; every declared dependency both ways; the rows of "Taken together" against the goal's headings."""
import re, sys, os, hashlib

ROOT = "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry"
PAPER = os.path.join(ROOT, "docs/GOAL-QUESTIONS-PAPER.md")
GOAL = os.path.join(ROOT, "docs/GOAL.md")

def lines(p):
    with open(p, encoding="utf-8") as f:
        return f.read().split("\n")

P = lines(PAPER)
G = lines(GOAL)

print("== paper", PAPER, os.path.getsize(PAPER), "bytes sha256",
      hashlib.sha256(open(PAPER, "rb").read()).hexdigest())

# 1. The questions, listed from GOAL.md's closing section by its own numbering.
start = next(i for i, l in enumerate(G) if l.startswith("## Gaps against the sources"))
goalq = {}
for i in range(start, len(G)):
    m = re.match(r"^(\d+)\. \*\*(.+?)\*\*", G[i])
    if m:
        goalq[int(m.group(1))] = (i + 1, G[i])
print("\n== 1. questions in GOAL.md (numbered items after line %d): %d %s" % (start + 1, len(goalq), sorted(goalq)))

# sections of the paper
secs = {}
cur = None
for i, l in enumerate(P):
    m = re.match(r"^## Q-(\d+) ", l)
    if m:
        if cur is not None and secs[cur][1] is None:
            secs[cur][1] = i
        cur = int(m.group(1)); secs[cur] = [i + 1, None]
    elif (l.startswith("## ") or l.startswith("---")) and cur is not None:
        secs[cur][1] = i; cur = None
if cur is not None:
    secs[cur][1] = len(P)
print("sections Q-n in the paper: %d %s" % (len(secs), sorted(secs)))
print("in GOAL, not in the paper:", sorted(set(goalq) - set(secs)))
print("in the paper, not in GOAL:", sorted(set(secs) - set(goalq)))
bad = 0
for n, (a, b) in sorted(secs.items()):
    block = [l for l in P[a - 1:b] if l.startswith("> ")]
    q = block[0] if block else ""
    m = re.match(r"^> `docs/GOAL\.md:(\d+)` (.*)$", q)
    ok = bool(m) and n in goalq and int(m.group(1)) == goalq[n][0] and m.group(2) == goalq[n][1]
    if not ok:
        bad += 1
    print("  Q-%d paper line %d quotes GOAL.md:%s word for word at its line: %s" % (n, a, m.group(1) if m else "?", ok))
print("questions quoted not word for word or at another line:", bad)

# 2. Every citation `path:line` «words» (and `path:a-b` ranges).
print("\n== 2. citations")
cit = re.compile(r"`([^`\s]+?):(\d+)(?:-(\d+))?`((?:\s*«[^»]*»(?:\s*·\s*«[^»]*»)*)?)")
nq = nr = nb = 0
for i, l in enumerate(P):
    if l.startswith("> "):
        continue  # the quoted questions, checked in part 1
    for m in cit.finditer(l):
        path, a, b, words = m.group(1), int(m.group(2)), m.group(3), m.group(4)
        if path.startswith("<"):
            continue
        full = os.path.normpath(os.path.join(ROOT, path))
        if not os.path.exists(full):
            print("  paper:%d %s:%s  FILE NOT FOUND" % (i + 1, path, a)); nb += 1; continue
        S = lines(full)
        if b:
            nr += 1
            b = int(b)
            print("  paper:%d RANGE %s:%d-%d (file has %d lines)\n      first: %s\n      last:  %s\n      next:  %s" % (
                i + 1, path, a, b, len(S), S[a - 1][:110], S[b - 1][:110] if b <= len(S) else "BEYOND END",
                S[b][:110] if b < len(S) else "(end of file)"))
            if b > len(S): nb += 1
            continue
        qs = re.findall(r"«([^»]*)»", words or "")
        src = S[a - 1] if a <= len(S) else ""
        if not qs:
            nr += 1
            print("  paper:%d LINE %s:%d (no words quoted) -> %s" % (i + 1, path, a, src[:160]))
            continue
        for q in qs:
            nq += 1
            ok = q in src
            if not ok: nb += 1
            print("  paper:%d %s:%d «%s» %s\n      source: %s" % (i + 1, path, a, q, "HOLDS" if ok else "NOT AT THIS LINE", src))
print("quoted passages: %d; ranges or bare lines: %d; not holding: %d" % (nq, nr, nb))

# 3. Per section: positions, tables, proposals, dependencies
print("\n== 3. per section")
dep = {}; depby = {}
for n, (a, b) in sorted(secs.items()):
    body = P[a - 1:b]
    pos = sum(1 for l in body if re.match(r"^\*\*Position [AB]\b", l))
    tables = sum(1 for l in body if l.startswith("| Test"))
    props = sum(1 for l in body if l.startswith("**Proposal — not a decision.**"))
    dl = next((l for l in body if l.startswith("**Depends on:**")), "")
    m1 = re.search(r"\*\*Depends on:\*\* (.*?)\. \*\*Depended on by:\*\* (.*?)\.$", dl)
    d1 = sorted(int(x) for x in re.findall(r"Q-(\d+)", m1.group(1))) if m1 else None
    d2 = sorted(int(x) for x in re.findall(r"Q-(\d+)", m1.group(2))) if m1 else None
    dep[n] = d1; depby[n] = d2
    named = set()
    for l in body:
        if l.startswith("> ") or l.startswith("**Depends on:**"):
            continue
        named |= set(int(x) for x in re.findall(r"\bQ-(\d+)", l))
    named.discard(n)
    rows = [l for l in body if l.startswith("| ") and not l.startswith("| Test") and not l.startswith("|---")]
    both = sum(1 for r in rows if r.rstrip().endswith("both meet |"))
    div = sum(1 for r in rows if r.rstrip().endswith("divides |"))
    print("  Q-%d positions %d tables %d proposals %d | depends on %s | depended on by %s | Q-n named in body %s | rows %d both meet %d divides %d" % (
        n, pos, tables, props, d1, d2, sorted(named), len(rows), both, div))
one_way = []
for n in dep:
    for k in dep[n] or []:
        if n not in (depby.get(k) or []):
            one_way.append("Q-%d depends on Q-%d but Q-%d does not list Q-%d as depended on by" % (n, k, k, n))
    for k in depby[n] or []:
        if n not in (dep.get(k) or []):
            one_way.append("Q-%d says depended on by Q-%d but Q-%d does not list Q-%d" % (n, k, k, n))
print("declared pairs (B depends on A):", sum(len(v or []) for v in dep.values()))
print("one-way between sections:", len(one_way))
for x in one_way: print("  ", x)

ti = next(i for i, l in enumerate(P) if l.startswith("## The dependencies"))
tpairs = set()
for l in P[ti:ti + 20]:
    if l.startswith("| ") and "←" in l:
        cell = l.split("|")[1].strip()
        for b_, as_ in re.findall(r"(\d+) ← ([\d, ]+?)(?=, \d+ ←|$)", cell):
            for a_ in re.findall(r"\d+", as_):
                tpairs.add((int(b_), int(a_)))
secpairs = set((n, k) for n in dep for k in dep[n] or [])
print("pairs in the dependency table:", len(tpairs))
print("in table, not in sections:", sorted(tpairs - secpairs))
print("in sections, not in table:", sorted(secpairs - tpairs))

print("\n== 4. Taken together")
gh = [re.match(r"^### ((?:S|F|SC)-\d+)", l).group(1) for l in G if re.match(r"^### (?:S|F|SC)-\d+", l)]
tt = next(i for i, l in enumerate(P) if l.startswith("## Taken together"))
rows = [l.split("|")[1].strip() for l in P[tt:] if re.match(r"^\| (?:S|F|SC)-\d+ \|", l)]
print("goal headings:", len(gh), gh)
print("rows of Taken together:", len(rows), rows)
print("missing:", [h for h in gh if h not in rows], "extra:", [r for r in rows if r not in gh])
scr = [l for l in P[tt:] if l.startswith("- SC-")]
print("screens in the final list:", len(scr))
for s in scr:
    print("  ", s, "| R-17 line:", '"Invented data, Progressa is fictional"' in s)
