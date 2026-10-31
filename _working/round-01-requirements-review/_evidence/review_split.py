#!/usr/bin/env python3
"""The reviewer's own route to the brief's requirement units (review of C-2026-10-31-01).

A route the round did not use:
- the five sections are found by scanning for the line "## " that opens each and the next "## ";
- headings are NOT units; the table's header row and separator are NOT units;
- EVERY sentence is a unit, inside list items too (a list item of two sentences gives two units);
- the disposition is the reviewer's own, written in HAND below, keyed by line and the unit's first words,
  read from the brief line by line by the reviewer, not from the round's dispositions.tsv.
Then: compares row by row with the round's inventory (SENTENCES.md) and register (REQUIREMENTS.md),
both ways, and looks every requirement's quote up at the line it cites.

Usage: python3 review_split.py <brief> <SENTENCES.md> <REQUIREMENTS.md>
"""
import re
import sys

brief_path, sent_path, reg_path = sys.argv[1:4]
lines = open(brief_path, encoding="utf-8").read().split("\n")
FIVE = ["What it is for", "What it must do", "The made-up data, in known numbers",
        "What it must not do", "What it delivers"]

# the reviewer's own dispositions: (line, first words) -> R (requirement) or N (not), with reason
HAND = {
    (7, "Progressa's Ministry"): ("N", "context: the ministry's wish for the real registry"),
    (7, "Before anyone builds"): ("R", "the prototype: clerk enrols, no child registered twice"),
    (7, "The prototype is for agreement"): ("N", "purpose"),
    (7, "It is not the registry"): ("N", "scope statement; nothing the prototype does"),
    (11, "One goal"): ("R", "the one goal"),
    (11, "A school clerk enters"): ("R", "the four entries"),
    (11, "The registry searches"): ("R", "search first"),
    (13, "if it finds exactly one"): ("R", "the match rule, capitals ignored"),
    (14, "if it finds none"): ("R", "new number, saved"),
    (15, "the clerk sees"): ("R", "outcome shown"),
    (19, "The prototype starts with"): ("R", "data over three lists"),
    (23, "| Children"): ("R", "60"),
    (24, "| Schools"): ("R", "3"),
    (25, "| Children on more"): ("R", "8"),
    (26, "| Of those"): ("R", "4"),
    (27, "| Ages"): ("R", "6 to 12"),
    (29, "The numbers are fixed"): ("R", "numbers fixed"),
    (29, "The data is made the same way"): ("R", "reset reproducible"),
    (33, "Hold any real"): ("R", "must not: real data"),
    (33, "Every screen says"): ("R", "banner on every screen"),
    (34, "Connect to anything"): ("R", "must not: outside connection"),
    (34, "Other bodies"): ("R", "other bodies simulated"),
    (35, "Open a window"): ("R", "must not: window"),
    (35, "Every check of the screens"): ("R", "windowless checks"),
    (39, "The working prototype"): ("R", "deliverable 1"),
    (40, "A one-page note"): ("R", "deliverable 2"),
}


def sentences(t):
    # split after . ? ! (with an optional closing ** or ") followed by whitespace
    parts = re.split(r'(?<=[.?!])(?:\*\*|")?\s+(?=[A-Z"*])', t)
    # re-attach a closing ** or " lost by the split
    out = []
    for p in parts:
        p = p.strip()
        if p:
            out.append(p)
    return out


units = []  # (line, text)
sec = None
for i, l in enumerate(lines, 1):
    if l.startswith("## "):
        sec = l[3:].strip() if l[3:].strip() in FIVE else None
        continue
    if sec is None or not l.strip():
        continue
    s = l.strip()
    if s.startswith("|"):
        if set(s) <= set("|- "):
            continue
        if s.startswith("| Setting |"):
            continue
        units.append((i, s))
        continue
    s = re.sub(r"^(- |\d+\. )", "", s)
    for x in sentences(s):
        units.append((i, x))

print("reviewer's units (sentences, list-item sentences, data rows; no headings): %d" % len(units))
disp = []
for (i, t) in units:
    key = [k for k in HAND if k[0] == i and t.startswith(k[1])]
    if len(key) != 1:
        sys.exit("NO HAND DISPOSITION for line %d: %s" % (i, t))
    disp.append((i, t, HAND[key[0]][0], HAND[key[0]][1]))
unused = [k for k in HAND if not any(k[0] == i and t.startswith(k[1]) for i, t in units)]
if unused:
    sys.exit("HAND entries matching no unit: %s" % unused)
nreq = sum(1 for d in disp if d[2] == "R")
print("reviewer's units marked requirement: %d; not: %d" % (nreq, len(disp) - nreq))

# the round's inventory
inv = {}
cur = None
for l in open(sent_path, encoding="utf-8"):
    m = re.match(r"^### (U-\d+) · line (\d+) · ([^·]+) · (.+)$", l.rstrip("\n"))
    if m:
        cur = m.group(1)
        inv[cur] = [int(m.group(2)), m.group(3).strip(), m.group(4).strip(), None]
        continue
    if cur and l.startswith("> ") and inv[cur][3] is None:
        inv[cur][3] = l[2:].rstrip("\n")
# the register
reg = {}
cur = None
for l in open(reg_path, encoding="utf-8"):
    l = l.rstrip("\n")
    m = re.match(r"^### (R-\d+)$", l)
    if m:
        cur = m.group(1); reg[cur] = {"unit": None, "line": None, "quote": None, "req": None}; continue
    if l.startswith("## "):
        cur = None; continue
    if not cur:
        continue
    m = re.match(r"^\*\*Cites:\*\* (U-\d+), brief line (\d+)$", l)
    if m:
        reg[cur]["unit"], reg[cur]["line"] = m.group(1), int(m.group(2))
    elif l.startswith("> ") and reg[cur]["quote"] is None:
        reg[cur]["quote"] = l[2:]
    elif l.startswith("**Requirement.**"):
        reg[cur]["req"] = l[len("**Requirement.** "):]

print("round's inventory units: %d; marked requirement: %d" % (len(inv), sum(1 for v in inv.values() if v[2] == "requirement")))
print("round's register requirements: %d" % len(reg))
print()
print("== reviewer's units, row by row, against the inventory and the register ==")
miss_inv = miss_reg = disagree = 0
for (i, t, d, why) in disp:
    us = [u for u, v in inv.items() if v[0] == i and v[3] and (t in v[3] or v[3] in t)]
    rs = [r for r, v in reg.items() if v["unit"] in us]
    invd = ",".join(inv[u][2] for u in us) if us else "-"
    flag = ""
    if not us:
        flag += " MISSING-FROM-INVENTORY"; miss_inv += 1
    if d == "R" and not rs:
        flag += " MISSING-FROM-REGISTER"; miss_reg += 1
    if us and ((d == "R") != all(inv[u][2] == "requirement" for u in us)):
        flag += " DISPOSITION-DIFFERS"; disagree += 1
    print("L%-3d %s | %-40.40s | inv %s (%s) | reg %s%s" % (i, d, t, ",".join(us) or "-", invd, ",".join(rs) or "-", flag))
print("reviewer's units missing from the inventory: %d" % miss_inv)
print("reviewer's requirement units with no R-: %d" % miss_reg)
print("dispositions differing: %d" % disagree)
print()
print("== the other way: inventory units and R- numbers not matched by a reviewer's unit ==")
matched_u = set()
for (i, t, d, why) in disp:
    for u, v in inv.items():
        if v[0] == i and v[3] and (t in v[3] or v[3] in t):
            matched_u.add(u)
extra_u = [u for u in inv if u not in matched_u]
for u in extra_u:
    print("  inventory %s line %d %s (%s): no reviewer's unit — %s" % (u, inv[u][0], inv[u][1], inv[u][2], inv[u][3]))
print("inventory units with no reviewer's unit: %d (of which marked requirement: %d)" % (
    len(extra_u), sum(1 for u in extra_u if inv[u][2] == "requirement")))
r_no = [r for r, v in reg.items() if v["unit"] not in matched_u or inv[v["unit"]][2] != "requirement"]
print("R- numbers resting on no reviewer's requirement unit: %d %s" % (len(r_no), r_no))
print()
print("== every requirement looked up at its line in the brief ==")
bad = 0
for r, v in sorted(reg.items()):
    ok = v["quote"] is not None and v["quote"] in lines[v["line"] - 1]
    if not ok:
        bad += 1
    print("  %s line %d quote at that line: %s" % (r, v["line"], "yes" if ok else "NO"))
print("quotes not at their cited line: %d" % bad)
