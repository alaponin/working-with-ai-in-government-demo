#!/usr/bin/env python3
"""A6: the figure in DUPLICATES.md against the program's last line in its log,
and each table row of DUPLICATES.md against duplicates.csv (child, learner
numbers, caught)."""
import csv
import re
import sys

md, log, csv_path = sys.argv[1:4]
md_text = open(md, encoding="utf-8").read()
log_lines = [l.strip() for l in open(log, encoding="utf-8") if l.startswith("the search catches")]
print("log's figure line: %s" % log_lines)
m = re.search(r"\*\*The search catches (\d+) of the (\d+)\.\*\*", md_text)
print("DUPLICATES.md figure: %s of %s" % (m.group(1), m.group(2)))
lm = re.match(r"the search catches (\d+) of the (\d+)", log_lines[-1])
print("figure agrees with log: %s" % ((m.group(1), m.group(2)) == (lm.group(1), lm.group(2))))
print("log line quoted in DUPLICATES.md: %s" % (log_lines[-1] in md_text))
rows = {r["child"]: r for r in csv.DictReader(open(csv_path, encoding="utf-8"))}
bad = 0
seen = 0
for line in md_text.splitlines():
    t = re.match(r"^\| (C\d+) \| [^|]+ \| ([^|]+) \| \**(yes|no)\** \|", line)
    if not t:
        continue
    seen += 1
    c, nums, caught = t.group(1), t.group(2).strip(), t.group(3)
    r = rows[c]
    ok = nums == r["learner_numbers"] and caught == r["caught"]
    bad += not ok
    print("%s table %s %s | csv %s %s | %s" % (c, nums, caught, r["learner_numbers"], r["caught"], "agree" if ok else "DIFFER"))
yes = sum(r["caught"] == "yes" for r in rows.values())
print("table rows: %d; csv rows: %d; caught=yes in csv: %d; disagreements: %d" % (seen, len(rows), yes, bad))
