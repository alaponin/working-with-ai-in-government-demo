"""Review plants (C-2026-10-31-30). Copies with shutil.copyfile (no file times kept); changes copies only.

Q1, for the round's count.py: in a copy of enrolments.json, caught child C53's second entry
    exam_candidate_list:8 is moved apart, to learner number 9999, which no entry holds.
    Must: C53 caught=no; figure 3 of 8.
Q2, for this review's route2.py: in a copy of the list folder, caught child C26's
    social_grant_list:17 family name "Velnokgal" -> "Velnokgel" (one letter).
    Must: C26 joined=no; figure 3 of 8. And a capitals-only change on C31 (must stay joined).
"""
import json, os, shutil, sys

data, out = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(out, "lists"), exist_ok=True)

dst = os.path.join(out, "enrolments.Q1.json")
shutil.copyfile(os.path.join(data, "enrolments.json"), dst)
rows = json.load(open(dst, encoding="utf-8"))
hit = [r for r in rows if r["list_entry"] == "exam_candidate_list:8"]
assert len(hit) == 1, hit
used = {r["learner_number"] for r in rows}
assert 9999 not in used
print("Q1: exam_candidate_list:8 learner_number %s -> 9999 (9999 held by no entry)" % hit[0]["learner_number"])
hit[0]["learner_number"] = 9999
json.dump(rows, open(dst, "w", encoding="utf-8"), indent=2)

for f in ("school_census", "exam_candidate_list", "social_grant_list", "key_table"):
    shutil.copyfile(os.path.join(data, f + ".json"), os.path.join(out, "lists", f + ".json"))
p = os.path.join(out, "lists", "social_grant_list.json")
rows = json.load(open(p, encoding="utf-8"))
r = [x for x in rows if x["entry"] == 17][0]
print("Q2: social_grant_list:17 family_name %r -> %r" % (r["family_name"], "Velnokgel"))
r["family_name"] = "Velnokgel"
json.dump(rows, open(p, "w", encoding="utf-8"), indent=2)
p = os.path.join(out, "lists", "exam_candidate_list.json")
rows = json.load(open(p, encoding="utf-8"))
r = [x for x in rows if x["entry"] == 13][0]
print("Q2: exam_candidate_list:13 family_name %r -> %r (capitals only)" % (r["family_name"], r["family_name"].upper()))
r["family_name"] = r["family_name"].upper()
json.dump(rows, open(p, "w", encoding="utf-8"), indent=2)
