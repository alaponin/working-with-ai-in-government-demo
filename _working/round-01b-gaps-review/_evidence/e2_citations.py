"""The reviewer's own reading of every citation in the decision paper (not the round's check_paper.py).

usage: e2_citations.py <estate root>
Prints: (1) every quoted passage with the source line it names, for reading against the sentence that
cites it; (2) every bare 'line N' in the paper beside the brief's line N; (3) per question, the register
lines outside the gaps section that name the question ('gap G-xx'), and whether the paper's section
quotes any register line at all.
"""
import os
import sys

root = sys.argv[1]
brief = open(os.path.join(root, "..", "brief", "MINI-REGISTRY-BRIEF.md"), encoding="utf-8").read().split("\n")
reg = open(os.path.join(root, "docs", "REQUIREMENTS.md"), encoding="utf-8").read().split("\n")
paper = open(os.path.join(root, "docs", "GAPS-PAPER.md"), encoding="utf-8").read().split("\n")
src = {"../brief/MINI-REGISTRY-BRIEF.md": brief, "docs/REQUIREMENTS.md": reg}

# (1) passages: scan by string search, not by regex
n = found = wrong = missing = 0
section = "head"
per_section_reg = {}
print("## 1. passages: paper line | section | source:line | found at named line")
for pno, line in enumerate(paper, 1):
    if line.startswith("## G-"):
        section = line[3:7]
    elif line.startswith("## "):
        section = "head"
    i = 0
    while True:
        a = line.find("`", i)
        if a < 0:
            break
        b = line.find("`", a + 1)
        if b < 0:
            break
        ref = line[a + 1:b]
        i = b + 1
        if ":" not in ref or not (ref.startswith("../brief/") or ref.startswith("docs/REQ")):
            continue
        path, ln = ref.rsplit(":", 1)
        rest = line[b + 1:]
        if not rest.startswith(" «"):
            continue
        q = rest[2:rest.find("»")]
        n += 1
        ln = int(ln)
        s = src[path]
        ok = q in s[ln - 1]
        if path.startswith("docs/"):
            per_section_reg[section] = per_section_reg.get(section, 0) + 1
        if ok:
            found += 1
        else:
            hits = [k + 1 for k, t in enumerate(s) if q in t]
            if hits:
                wrong += 1
            else:
                missing += 1
        print("paper:%d | %s | %s:%d | %s" % (pno, section, "brief" if path.startswith("..") else "register", ln, "yes" if ok else "NO"))
print("passages %d: at the named line %d, elsewhere %d, nowhere %d" % (n, found, wrong, missing))

# (2) bare line references
print("\n## 2. bare 'line N' references, with the brief's line N")
import re
for pno, line in enumerate(paper, 1):
    for m in re.finditer(r"\bline (\d+)", line):
        ln = int(m.group(1))
        print("paper:%d line %d -> %s" % (pno, ln, brief[ln - 1][:110]))

# (3) register lines naming each question
print("\n## 3. register lines (outside the gaps section) naming each question, and register passages the paper's section quotes")
gaps_at = reg.index("## Gaps against the brief")
for k in range(1, 14):
    g = "G-%02d" % k
    names = [i + 1 for i, t in enumerate(reg[:gaps_at]) if ("gap " + g) in t]
    print("%s: register lines naming it %s; register passages quoted in its section: %d" % (g, names, per_section_reg.get(g, 0)))
q0 = sum(1 for k in range(1, 14) if per_section_reg.get("G-%02d" % k, 0) == 0)
print("questions whose section quotes no register passage: %d of 13" % q0)
