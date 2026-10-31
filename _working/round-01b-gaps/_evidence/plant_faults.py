"""Make a copy of the paper with five planted faults, to show check_paper.py catches each.

usage: plant_faults.py <GAPS-PAPER.md> <planted copy>
1. G-13's section renamed G-15 (one unanswered, one extra)
2. a quote of the brief's line 14 altered by one word (not found)
3. a quote of the brief's line 27 cited at line 26 (wrong line)
4. G-09's Position B removed (one position)
5. G-14's closing line removed
"""
import sys

s = open(sys.argv[1], encoding="utf-8").read()
plants = [
    ("## G-13 — the note's one page", "## G-15 — the note's one page"),
    ("«if it finds none, it gives the child a new learner number and saves the record;»",
     "«if it finds none, it gives the pupil a new learner number and saves the record;»"),
    ("`../brief/MINI-REGISTRY-BRIEF.md:27` «| Ages | 6 to 12 |»",
     "`../brief/MINI-REGISTRY-BRIEF.md:26` «| Ages | 6 to 12 |»"),
    ("**Position B — the pages only.**", "Position B, the pages only."),
    ("**G-14 — closed, not reopened.**", "G-14 closed."),
]
for old, new in plants:
    assert s.count(old) >= 1, old
    s = s.replace(old, new, 1)
open(sys.argv[2], "w", encoding="utf-8").write(s)
print("planted: %d" % len(plants))
