#!/usr/bin/env python3
"""A2 and A3 for round 1: compare the register with the inventory, and check every quote against the brief.

Usage: python3 compare_register.py <SENTENCES.md> <REQUIREMENTS.md> <brief>

A2 — both ways: every unit marked requirement in the inventory is cited by at least one R- number
     (else "uncited"), and every R- number cites a unit marked requirement (else "unsupported").
     A requirement also counts as unsupported where its cited line or its quote differs from the
     inventory's for that unit.
A3 — every quoted unit in the register is a substring of the brief (else "not found").
Also prints, per R- number, whether its test has the three parts (Set up, Do, See).
"""
import re
import sys

sent_path, reg_path, brief_path = sys.argv[1:4]
brief = open(brief_path, encoding="utf-8").read()

inv = {}  # unit id -> (line, disposition, text)
cur = None
for line in open(sent_path, encoding="utf-8"):
    m = re.match(r"^### (U-\d+) · line (\d+) · [^·]+ · (.+)$", line.rstrip("\n"))
    if m:
        cur = m.group(1)
        inv[cur] = [int(m.group(2)), m.group(3), None]
        continue
    if cur and line.startswith("> ") and inv[cur][2] is None:
        inv[cur][2] = line[2:].rstrip("\n")

reg = {}  # R id -> dict
cur = None
for line in open(reg_path, encoding="utf-8"):
    line = line.rstrip("\n")
    m = re.match(r"^### (R-\d+)$", line)
    if m:
        cur = m.group(1)
        reg[cur] = {"unit": None, "line": None, "quote": None, "parts": set()}
        continue
    if line.startswith("## "):
        cur = None
        continue
    if not cur:
        continue
    m = re.match(r"^\*\*Cites:\*\* (U-\d+), brief line (\d+)$", line)
    if m:
        reg[cur]["unit"], reg[cur]["line"] = m.group(1), int(m.group(2))
    elif line.startswith("> ") and reg[cur]["quote"] is None:
        reg[cur]["quote"] = line[2:]
    for part in ("Set up", "Do", "See"):
        if line.startswith("- *%s:*" % part):
            reg[cur]["parts"].add(part)

req_units = sorted(u for u, v in inv.items() if v[1] == "requirement")
cited = {v["unit"] for v in reg.values()}
uncited = [u for u in req_units if u not in cited]
unsupported = []
for r, v in sorted(reg.items()):
    u = v["unit"]
    if u not in inv or inv[u][1] != "requirement":
        unsupported.append((r, "cites %s, not a unit marked requirement" % u))
    elif inv[u][0] != v["line"] or inv[u][2] != v["quote"]:
        unsupported.append((r, "line or quote differs from the inventory's %s" % u))

not_found = [r for r, v in sorted(reg.items()) if not v["quote"] or v["quote"] not in brief]
no_three = [r for r, v in sorted(reg.items()) if v["parts"] != {"Set up", "Do", "See"}]

print("inventory units: %d; marked requirement: %d" % (len(inv), len(req_units)))
print("register requirements: %d (R-%s to R-%s)" % (len(reg), min(reg)[2:], max(reg)[2:]))
for r, v in sorted(reg.items()):
    print("  %s cites %s line %d — test parts: %s" % (r, v["unit"], v["line"], ", ".join(sorted(v["parts"]))))
for u in req_units:
    print("  %s cited by %s" % (u, ", ".join(r for r, v in sorted(reg.items()) if v["unit"] == u) or "nothing"))
for u in uncited:
    print("UNCITED %s" % u)
for r, why in unsupported:
    print("UNSUPPORTED %s: %s" % (r, why))
for r in not_found:
    print("NOT FOUND %s" % r)
for r in no_three:
    print("TEST WITHOUT THREE PARTS %s" % r)
print("A2: %d uncited, %d unsupported" % (len(uncited), len(unsupported)))
print("A3: %d not found" % len(not_found))
print("tests without the three parts: %d" % len(no_three))
