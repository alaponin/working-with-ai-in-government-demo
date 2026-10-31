"""A4: copy count.csv, remove one pair (R-17,SC-4) and add one requirement absent from the register (R-24).
Usage: plant.py <count.csv> <planted copy>
"""
import sys

src, dst = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().split("\n")
removed = [l for l in lines if l.startswith("R-17,SC-4,")]
assert len(removed) == 1, removed
out = [l for l in lines if not l.startswith("R-17,SC-4,")]
while out and out[-1] == "":
    out.pop()
out.append('R-24,S-1,"open the enrolment screen"')
open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("removed: %s" % removed[0])
print("added:   %s" % out[-1])
print("rows in %s: %d; in %s: %d" % (src, len(lines) - 2, dst, len(out) - 1))
