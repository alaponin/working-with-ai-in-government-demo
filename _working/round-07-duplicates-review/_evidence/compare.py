"""Set the second route's eight rows beside the round's duplicates.csv, field by field."""
import csv, sys, re
log, csvp = sys.argv[1], sys.argv[2]
mine = {}
for line in open(log, encoding="utf-8"):
    m = re.match(r"^(C\d+) \| (.+?) \| (yes|no) \| (.*)$", line.rstrip("\n"))
    if m:
        mine[m.group(1)] = (m.group(2), m.group(3), m.group(4))
theirs = {r["child"]: (r["entries"], r["caught"], r["fields_differing"]) for r in csv.DictReader(open(csvp, encoding="utf-8"))}
print("route2 rows: %d; csv rows: %d" % (len(mine), len(theirs)))
print("only in route2:", sorted(set(mine) - set(theirs)) or "-")
print("only in csv:", sorted(set(theirs) - set(mine)) or "-")
dis = 0
for c in sorted(set(mine) & set(theirs)):
    a, b = mine[c], theirs[c]
    same = [a[0] == b[0], a[1] == b[1], a[2] == b[2]]
    if not all(same):
        dis += 1
    print("%s entries:%s caught/joined:%s(%s|%s) fields:%s" % (c, "=" if same[0] else "DIFF", "=" if same[1] else "DIFF", a[1], b[1], "=" if same[2] else "DIFF"))
print("route2 joined: %d; csv caught=yes: %d" % (sum(v[1] == "yes" for v in mine.values()), sum(v[1] == "yes" for v in theirs.values())))
print("disagreeing rows:", dis)
