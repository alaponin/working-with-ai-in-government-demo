#!/usr/bin/env python3
"""A4: for each child of the set, every compared field's value on each of its
list entries, read straight from the list files, with whether the values are
equal exactly, equal with capitals ignored only, or different. Independent of
count.py: it reads the set from A2_set.txt and the list files by name."""
import json
import os
import re
import sys

set_txt, data_dir = sys.argv[1], sys.argv[2]
FIELDS = ("family_name", "given_names", "date_of_birth")
pat = re.compile(r"^\s+(C\d+)\s+\d+ entries\s+(.*)$")
lists = {}
n = 0
for line in open(set_txt, encoding="utf-8"):
    m = pat.match(line)
    if not m:
        continue
    n += 1
    child, entries = m.group(1), [e.strip() for e in m.group(2).split("·")]
    print("%s  %s" % (child, " · ".join(entries)))
    recs = []
    for e in entries:
        lst, k = e.rsplit(":", 1)
        if lst not in lists:
            with open(os.path.join(data_dir, lst + ".json"), encoding="utf-8") as f:
                lists[lst] = {r["entry"]: r for r in json.load(f)}
        recs.append(lists[lst][int(k)])
    for fld in FIELDS:
        vals = [r[fld] for r in recs]
        if len(set(vals)) == 1:
            verdict = "equal, letter for letter"
        elif len({v.lower() for v in vals}) == 1:
            verdict = "equal with capitals ignored only"
        else:
            verdict = "DIFFERENT"
        print("    %-13s %s  -> %s" % (fld, " | ".join('"%s"' % v for v in vals), verdict))
print("children read: %d" % n)
