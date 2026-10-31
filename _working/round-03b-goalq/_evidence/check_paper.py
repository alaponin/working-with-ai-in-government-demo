"""A2 to A6 over docs/GOAL-QUESTIONS-PAPER.md."""
import re, sys, os
root = sys.argv[1]
which = sys.argv[2]
P = open(root + "/docs/GOAL-QUESTIONS-PAPER.md", encoding="utf-8").read()
PL = P.split("\n")
QL = open(root + "/_working/round-03b-goalq/_evidence/QUESTIONS.md", encoding="utf-8").read().split("\n")
questions = {}
for l in QL:
    m = re.match(r"^- `docs/GOAL.md:(\d+)` (\d+)\. (.*)$", l)
    if m:
        questions[int(m.group(2))] = (int(m.group(1)), m.group(2) + ". " + m.group(3))

# sections
sec = {}
cur = None
for i, l in enumerate(PL):
    m = re.match(r"^## Q-(\d+) — ", l)
    if m:
        cur = int(m.group(1)); sec[cur] = []
        continue
    if l.startswith("## ") or l.strip() == "---":
        cur = None
    if cur is not None:
        sec[cur].append(l)

def a2():
    un = [q for q in questions if q not in sec]
    ex = [s for s in sec if s not in questions]
    bad = []
    for q, body in sec.items():
        if q in questions:
            n, text = questions[q]
            want = "> `docs/GOAL.md:%d` %s" % (n, text)
            if want not in body:
                bad.append(q)
    print("questions listed:", len(questions), "sections:", len(sec))
    print("%d unanswered, %d extra" % (len(un), len(ex)))
    print("sections whose quoted question differs from QUESTIONS.md:", bad if bad else 0)

def a3():
    nf = wl = 0; n = 0; rng = 0
    for i, l in enumerate(PL):
        for m in re.finditer(r"`([^`\s]+?):(\d+)` «([^»]+)»", l):
            n += 1
            path, ln, words = m.group(1), int(m.group(2)), m.group(3)
            fl = open(os.path.normpath(os.path.join(root, path)), encoding="utf-8").read().split("\n")
            if words in fl[ln - 1]:
                continue
            others = [j + 1 for j, x in enumerate(fl) if words in x]
            if others:
                wl += 1; print("wrong line: paper:%d %s:%d, found at %s" % (i + 1, path, ln, others))
            else:
                nf += 1; print("not found: paper:%d %s:%d «%s»" % (i + 1, path, ln, words[:60]))
        m = re.match(r"^> `([^`\s]+?):(\d+)` (.*)$", l)
        if m:
            n += 1
            fl = open(os.path.normpath(os.path.join(root, m.group(1))), encoding="utf-8").read().split("\n")
            if m.group(3) not in fl[int(m.group(2)) - 1]:
                nf += 1; print("not found (blockquote): paper:%d" % (i + 1))
        for m in re.finditer(r"`([^`\s]+?):(\d+)-(\d+)`", l):
            rng += 1
            fl = open(os.path.normpath(os.path.join(root, m.group(1))), encoding="utf-8").read().split("\n")
            if int(m.group(3)) > len(fl):
                nf += 1; print("range past end: paper:%d %s" % (i + 1, m.group(0)))
    print("quoted passages checked:", n, "line ranges checked:", rng)
    print("%d not found, %d wrong line" % (nf, wl))

def a4():
    print("section | positions | tables | proposals")
    for q in sorted(sec):
        b = sec[q]
        pos = sum(1 for l in b if l.startswith("**Position "))
        tab = sum(1 for l in b if l.startswith("| Test |"))
        pro = sum(1 for l in b if l.startswith("**Proposal — not a decision.**"))
        print("Q-%d | %d | %d | %d" % (q, pos, tab, pro))

def nums(t):
    return [int(x) for x in re.findall(r"Q-(\d+)", t)]

def a5():
    # the table of dependencies
    pairs = set()
    tl = P.split("## The dependencies")[1].split("\n---\n")[0].split("\n")
    for l in tl:
        if l.startswith("| ") and "←" in l and not l.startswith("| Pair"):
            cell = l.split("|")[1]
            for part in re.finditer(r"(\d+) ← ([\d, ]+?)(?=,\s*\d+ ←|$)", cell.strip()):
                b = int(part.group(1))
                for a in re.findall(r"\d+", part.group(2)):
                    pairs.add((b, int(a)))
    on = {}; by = {}
    for q, body in sec.items():
        d = next(l for l in body if l.startswith("**Depends on:**"))
        m = re.match(r"\*\*Depends on:\*\* (.*?)\. \*\*Depended on by:\*\* (.*?)\.$", d)
        on[q] = set(nums(m.group(1))); by[q] = set(nums(m.group(2)))
    print("pairs in the table:", len(pairs))
    oneway = 0
    for (b, a) in sorted(pairs):
        ok = a in on[b] and b in by[a]
        if not ok:
            oneway += 1; print("one-way: %d <- %d" % (b, a))
    # declarations not in the table
    for q in sec:
        for a in on[q]:
            if (q, a) not in pairs: oneway += 1; print("declared, not in table: %d <- %d" % (q, a))
        for b in by[q]:
            if (b, q) not in pairs: oneway += 1; print("declared, not in table: %d <- %d" % (b, q))
    print("%d one-way" % oneway)
    print("per section: other questions named in its positions and table, against its Depends on")
    outside = 0
    for q in sorted(sec):
        named = set()
        for l in sec[q]:
            if l.startswith("**Position ") or l.startswith("| ") or l.startswith("**Passages:**"):
                named |= set(nums(l))
        named.discard(q)
        extra = named - on[q]
        outside += len(extra)
        print("Q-%d depends on %s; judged under the recommendations of %s; named outside its dependencies: %s"
              % (q, sorted(on[q]) or "none", sorted(named) or "none", sorted(extra) or "none"))
    print("%d judged under an answer it does not depend on" % outside)

def a6():
    G = open(root + "/docs/GOAL.md", encoding="utf-8").read().split("\n")
    goal = [re.match(r"^### ((?:S|F|SC)-\d+) ", l).group(1) for l in G if re.match(r"^### (S|F|SC)-\d+ ", l)]
    tt = P.split("## Taken together")[1].split("\n")
    rows = [l.split("|")[1].strip() for l in tt if re.match(r"^\| (S|F|SC)-\d+ \|", l)]
    miss = [g for g in goal if g not in rows]; extra = [r for r in rows if r not in goal]
    print("goal's steps, failures, screens:", len(goal), goal)
    print("rows of Taken together:", len(rows))
    print("%d missing, %d extra" % (len(miss), len(extra)))
    after = P.split("**The screens the goal then has**")[1].split("\n")
    sc = [l for l in after if l.startswith("- SC-")]
    without = [l for l in sc if '"Invented data, Progressa is fictional"' not in l]
    print("screens in the final list:", len(sc), "; without R-17's line:", len(without))

{"A2": a2, "A3": a3, "A4": a4, "A5": a5, "A6": a6}[which]()
