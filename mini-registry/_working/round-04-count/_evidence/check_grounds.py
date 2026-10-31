"""A3: every ground of count.csv is words of that requirement's test in the register.

The test of R-nn is the lines from "**Test.**" under its heading "### R-nn" to the next heading.
For a row with element "none" the ground is "<why>: <the test's words>", the why one of the three
the instruction names; the words after the first ": " are what is looked for.
Usage: check_grounds.py <estate root> <count.csv>
"""
import csv, re, sys

root, csvp = sys.argv[1], sys.argv[2]
req = open(root + "/docs/REQUIREMENTS.md", encoding="utf-8").read().split("\n")
tests = {}
cur = None
for i, l in enumerate(req):
    m = re.match(r"^### (R-\d\d)\s*$", l)
    if m:
        cur, intest = m.group(1), False
        tests[cur] = []
        continue
    if l.startswith("#"):
        cur = None
        continue
    if cur and l.strip() == "**Test.**":
        intest = True
        continue
    if cur and intest:
        tests[cur].append((i + 1, l))

whys = ("the made-up data", "the delivery", "what the prototype must not do outside the goal")
nf = 0
rows = list(csv.DictReader(open(csvp, encoding="utf-8", newline="")))
for r in rows:
    g = r["ground"]
    if r["element"] == "none":
        why, _, g = g.partition(": ")
        if why not in whys:
            nf += 1
            print("NOT FOUND (why not one of the three) %s,%s %r" % (r["requirement"], r["element"], why))
            continue
    hits = [n for n, l in tests.get(r["requirement"], []) if g in l]
    if hits:
        print("found %s,%s at docs/REQUIREMENTS.md:%d  %r" % (r["requirement"], r["element"], hits[0], g))
    else:
        nf += 1
        print("NOT FOUND %s,%s %r" % (r["requirement"], r["element"], g))
print("%d rows, %d tests read, %d not found" % (len(rows), len(tests), nf))
