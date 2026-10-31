#!/usr/bin/env python3
"""A3: the children of the set (A2_set.txt) against the rows of duplicates.csv,
both ways: missing = in the set, no row; extra = a row, not in the set;
duplicate rows counted too."""
import csv
import re
import sys

set_txt, csv_path = sys.argv[1], sys.argv[2]
pat = re.compile(r"^\s+(C\d+)\s+\d+ entries")
the_set = [m.group(1) for m in (pat.match(l) for l in open(set_txt, encoding="utf-8")) if m]
rows = [r["child"] for r in csv.DictReader(open(csv_path, encoding="utf-8"))]
missing = sorted(set(the_set) - set(rows))
extra = sorted(set(rows) - set(the_set))
dups = sorted({c for c in rows if rows.count(c) > 1})
print("set: %d children; csv: %d rows" % (len(the_set), len(rows)))
print("missing: %s" % (missing or "-"))
print("extra: %s" % (extra or "-"))
print("duplicate rows: %s" % (dups or "-"))
print("%d missing, %d extra" % (len(missing), len(extra)))
