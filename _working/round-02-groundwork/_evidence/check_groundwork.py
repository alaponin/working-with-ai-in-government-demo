#!/usr/bin/env python3
"""The checks of round 2, A1 to A5, over the three tables and GROUNDWORK.md.

  check_groundwork.py a1   the set of SETTINGS_SET.md against settings.csv: missing and extra
  check_groundwork.py a2   every row's source: form, brief line and number, R-nn, G-nn
  check_groundwork.py a3   the search rule compares the brief's three fields and forgives capitals only
  check_groundwork.py a4   the register's two sections covered by a row or named in GROUNDWORK.md
  check_groundwork.py a5   the gaps section: present, each a question, none answered in a table
Each prints its counts and exits 1 where a count it names is not 0.
"""
import csv, re, sys

ROOT = "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry"
BRIEF = "/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md"
REG = ROOT + "/docs/REQUIREMENTS.md"
GW = ROOT + "/docs/GROUNDWORK.md"
SET = ROOT + "/_working/round-02-groundwork/_evidence/SETTINGS_SET.md"
T = {"settings": ROOT + "/docs/groundwork/settings.csv",
     "lists": ROOT + "/docs/groundwork/lists.csv",
     "search_rule": ROOT + "/docs/groundwork/search_rule.csv"}
SRC_COL = {"settings": "value", "lists": "meaning", "search_rule": "rule"}

def rows(name):
    with open(T[name], encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def a1():
    text = open(SET, encoding="utf-8").read()
    sec = text.split("## 3.")[1].split("## 4.")[0]
    want = set()
    for line in sec.split("\n"):
        m = re.match(r"\| (\d+) \| ([^|]+) \| ([^|]+) \|", line)
        if m:
            want.add((m.group(2).strip(), m.group(3).strip()))
    have = set((r["setting"], r["value"]) for r in rows("settings"))
    missing, extra = sorted(want - have), sorted(have - want)
    for x in missing: print("missing:", x)
    for x in extra: print("extra:", x)
    print("set %d, settings.csv %d rows" % (len(want), len(have)))
    print("%d missing, %d extra" % (len(missing), len(extra)))
    return 1 if missing or extra else 0

def a2():
    brief = open(BRIEF, encoding="utf-8").read().split("\n")
    reg = set(re.findall(r"^### (R-\d\d)$", open(REG, encoding="utf-8").read(), re.M))
    ruled = set("G-%02d" % i for i in range(1, 14))
    without, unresolved = 0, 0
    for name in T:
        rs = rows(name)
        for i, r in enumerate(rs, 2):
            src = (r.get("source") or "").strip()
            if not src:
                without += 1; print("%s:%d no source" % (name, i)); continue
            nums = re.findall(r"\d+", r[SRC_COL[name]])
            for part in src.split(" · "):
                m = re.fullmatch(r"brief:(\d+)|(R-\d\d)|ruling:(G-\d\d)", part)
                if not m:
                    unresolved += 1; print("%s:%d bad form %r" % (name, i, part)); continue
                if m.group(1):
                    n = int(m.group(1))
                    if n < 1 or n > len(brief) or not brief[n - 1].strip():
                        unresolved += 1; print("%s:%d brief line %d absent or empty" % (name, i, n)); continue
                    if name == "settings":
                        for x in nums:
                            if not re.search(r"\b%s\b" % x, brief[n - 1]):
                                unresolved += 1
                                print("%s:%d number %s not on brief:%d" % (name, i, x, n))
                elif m.group(2):
                    if m.group(2) not in reg:
                        unresolved += 1; print("%s:%d %s not in the register" % (name, i, m.group(2)))
                else:
                    if m.group(3) not in ruled:
                        unresolved += 1; print("%s:%d %s not ruled" % (name, i, m.group(3)))
        print("%s.csv: %d rows" % (name, len(rs)))
    print("%d without source, %d unresolved" % (without, unresolved))
    return 1 if without or unresolved else 0

def a3():
    rs = rows("search_rule")
    brief13 = open(BRIEF, encoding="utf-8").read().split("\n")[12]
    print("brief:13 " + brief13)
    compares = [r["rule"] for r in rs if r["part"] == "compares"]
    forgives = [r["rule"] for r in rs if r["part"] == "forgives"]
    dnc = [r["rule"] for r in rs if r["part"] == "does_not_compare"]
    print("compares:", compares)
    print("forgives:", forgives)
    print("forgives_nothing_else:", [r["rule"] for r in rs if r["part"] == "forgives_nothing_else"])
    print("does_not_compare:", dnc)
    print("does_not_read:", [r["rule"] for r in rs if r["part"] == "does_not_read"])
    fails = 0
    if sorted(compares) != sorted(["family name", "given names", "date of birth"]):
        fails += 1; print("FAIL: compares is not the three fields of brief:13")
    for f in compares:
        if f not in brief13:
            fails += 1; print("FAIL: %r not on brief:13" % f)
    if len(forgives) != 1 or not forgives[0].startswith("capitals") or "(capitals ignored)" not in brief13:
        fails += 1; print("FAIL: forgives is not capitals alone")
    if not any(r.startswith("school") for r in dnc):
        fails += 1; print("FAIL: school not among does_not_compare")
    for r in rs:
        if r["part"] in ("compares", "forgives", "where", "at_reset") and re.search(r"school|key", r["rule"]):
            fails += 1; print("FAIL: %s row names %r" % (r["part"], r["rule"]))
    print("compared fields: %d; forgiven: %d; school compared: %s; key table read: %s; failures: %d" % (
        len(compares), len(forgives), "no" if not any("school" in c for c in compares) else "yes",
        "no" if not any("key" in r["rule"] for r in rs if r["part"] != "does_not_read") else "yes", fails))
    return 1 if fails else 0

def a4():
    reg = open(REG, encoding="utf-8").read()
    want = []
    for sec in ("## What it must do", "## The made-up data, in known numbers"):
        body = reg.split(sec + "\n")[1].split("\n## ")[0]
        want += re.findall(r"^### (R-\d\d)$", body, re.M)
    cited = set()
    for name in T:
        for r in rows(name):
            cited |= set(re.findall(r"R-\d\d", r["source"]))
    gw = open(GW, encoding="utf-8").read()
    named_sec = gw.split("## Requirements the tables do not bear on")[1].split("\n## ")[0]
    named = set(re.findall(r"\*\*(R-\d\d)\*\* — .+", named_sec))
    unc = [r for r in want if r not in cited and r not in named]
    print("requirements in the two sections: %d (%s)" % (len(want), ", ".join(want)))
    for r in want:
        print("  %s: %s" % (r, "cited by a row" if r in cited else ("named in GROUNDWORK.md" if r in named else "UNCOVERED")))
    print("%d uncovered" % len(unc))
    return 1 if unc else 0

def a5():
    gw = open(GW, encoding="utf-8").read()
    if "\n## Gaps against the sources\n" not in gw:
        print("section absent"); return 1
    sec = gw.split("\n## Gaps against the sources\n")[1].split("\n## ")[0]
    gaps = re.findall(r"^\d+\. (.+)$", sec, re.M)
    notq = [g for g in gaps if not g.rstrip().endswith("?")]
    tables = "\n".join(open(p, encoding="utf-8").read() for p in T.values())
    # An answer would show in a table as: a calendar date, a seed, an order of the lists,
    # a first number, a count per list or per school, a key form, a learner count after reset.
    probes = [r"\b\d{4}-\d{2}-\d{2}\b", r"\bseed\b", r"census, then|then the", r"\bfirst\b.*\bnumber\b",
              r"\b64\b", r"per list|per school|each list holds", r"key_form|child_key|entry_id", r"\bsource_entr"]
    answered = [p for p in probes if re.search(p, tables, re.I)]
    print("gaps: %d; not a question: %d; probes for an answer in a table: %d, found: %d %s" % (
        len(gaps), len(notq), len(probes), len(answered), answered))
    return 1 if notq or answered or not gaps else 0

sys.exit({"a1": a1, "a2": a2, "a3": a3, "a4": a4, "a5": a5}[sys.argv[1]]())
