"""Reviewer's own check (not the round's): every `<path>:<line>` «words» in the paper,
read at its source line; every 'register line N' a section names, against the register
lines quoted in that same section; every register line naming a gap, against its section."""
import re, sys
ROOT = "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/"
paper = open(ROOT + "docs/GAPS-PAPER.md", encoding="utf-8").read().split("\n")
files = {"docs/REQUIREMENTS.md": open(ROOT + "docs/REQUIREMENTS.md", encoding="utf-8").read().split("\n"),
         "../brief/MINI-REGISTRY-BRIEF.md": open(ROOT + "../brief/MINI-REGISTRY-BRIEF.md", encoding="utf-8").read().split("\n")}
pat = re.compile(r"`([^`]+?):(\d+)`\s*«(.+?)»")
total = at = elsewhere = nowhere = 0
section = None
quoted_reg = {}      # section -> set of register lines quoted
named_reg = {}       # section -> set of 'register line N' mentioned
print("## 1. passages")
for i, line in enumerate(paper, 1):
    m = re.match(r"## (G-\d\d)", line)
    if m:
        section = m.group(1)
    elif line.startswith("## "):
        section = None
    for path, n, words in pat.findall(line):
        n = int(n); total += 1
        src = files[path]
        if words in src[n - 1]:
            at += 1
        else:
            hits = [k + 1 for k, l in enumerate(src) if words in l]
            if hits: elsewhere += 1; print(f"paper:{i} {path}:{n} ELSEWHERE {hits}: {words}")
            else: nowhere += 1; print(f"paper:{i} {path}:{n} NOWHERE: {words}")
        if path == "docs/REQUIREMENTS.md" and section:
            quoted_reg.setdefault(section, set()).add(n)
    if section:
        for n in re.findall(r"register lines? (\d+)", line):
            named_reg.setdefault(section, set()).add(int(n))
print(f"passages {total}: at the named line {at}, elsewhere {elsewhere}, nowhere {nowhere}")
print("## 2. 'register line N' named in a section, not quoted in that section")
miss = 0
for s in sorted(named_reg):
    d = sorted(named_reg[s] - quoted_reg.get(s, set()))
    print(f"{s} named {sorted(named_reg[s])} unquoted {d}")
    miss += len(d)
print(f"unquoted register lines named: {miss}")
print("## 3. register lines (1-323) naming 'gap G-xx', against the section's quotations")
reg = files["docs/REQUIREMENTS.md"]
unq = 0; pairs = 0
for k, l in enumerate(reg[:323], 1):
    for g in re.findall(r"gap (G-\d\d)", l):
        pairs += 1
        ok = k in quoted_reg.get(g, set())
        unq += (not ok)
        print(f"{g} register:{k} {'quoted' if ok else 'UNQUOTED'}")
print(f"gap-line pairs {pairs}; unquoted {unq}")
print("## 4. bare 'line N' (the brief) in the paper, each with the brief's line")
for i, line in enumerate(paper, 1):
    for n in re.findall(r"(?<!register )(?<!register lines )\b[Ll]ines? (\d+)", line):
        n = int(n)
        if n <= len(files["../brief/MINI-REGISTRY-BRIEF.md"]):
            print(f"paper:{i} line {n}: {files['../brief/MINI-REGISTRY-BRIEF.md'][n-1][:90]}")
