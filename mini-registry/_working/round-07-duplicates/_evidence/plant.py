#!/usr/bin/env python3
"""A5: plant faults in scratch copies of enrolments.json (copied with
shutil.copyfile, which keeps no file times) and write them under planted/.

  P1 (the instruction's plant): caught child C19's second entry
     social_grant_list:7 pointed to another learner (11, C31's);
     missed child C24's second entry exam_candidate_list:20 pointed to its
     first entry's learner (20).
     Must: C19 -> caught=no, C24 -> caught=yes; figure 4 - 1 + 1 = 4.
  P2: P1's first edit alone. Must: C19 -> no; figure 3.
  P3: P1's second edit alone. Must: C24 -> yes; figure 5.

The real enrolments.json is only read."""
import json
import os
import shutil
import sys

src, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)

EDIT_CAUGHT = ("social_grant_list:7", 11)
EDIT_MISSED = ("exam_candidate_list:20", 20)
PLANTS = {
    "P1": [EDIT_CAUGHT, EDIT_MISSED],
    "P2": [EDIT_CAUGHT],
    "P3": [EDIT_MISSED],
}
for name, edits in PLANTS.items():
    dst = os.path.join(outdir, "enrolments.%s.json" % name)
    shutil.copyfile(src, dst)
    with open(dst, encoding="utf-8") as f:
        rows = json.load(f)
    for entry, new in edits:
        hit = [r for r in rows if r["list_entry"] == entry]
        assert len(hit) == 1, (entry, hit)
        print("%s: %s learner_number %s -> %s" % (name, entry, hit[0]["learner_number"], new))
        hit[0]["learner_number"] = new
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)
        f.write("\n")
    print("%s written: %s" % (name, dst))
