"""Re-establish the paper's 64, 68 and '4 of the 8' by simulating its recommendations G-03 B, G-04 A, G-05 A
on a toy data set built to the brief's numbers, and enrolling every entry through the brief's line-13 rule.
The figures are worked out by running, not by the paper's arithmetic."""
children = []
for i in range(60):
    children.append({"key": i, "fam": "Fam%02d" % i, "giv": "Giv%02d" % i, "dob": "2015-01-%02d" % (i % 28 + 1)})
# 8 on two lists; of those 4 with the family name spelt differently (one letter) on the second list;
# 2 of the other 4 differ in capitals only (G-05: 'some ... differing in capitals only')
entries = []
for c in children:
    entries.append(("census", c["key"], c["fam"], c["giv"], c["dob"]))
for k in range(8):
    c = children[k]
    if k < 4:
        fam = c["fam"] + "x"           # spelt differently
    elif k < 6:
        fam = c["fam"].upper()          # capitals only
    else:
        fam = c["fam"]
    entries.append(("grant", c["key"], fam, c["giv"], c["dob"]))
learners = []          # (fam, giv, dob) lower-cased
joined = {}            # child key -> set of learner indexes it ended up in
for lst, key, fam, giv, dob in entries:
    probe = (fam.lower(), giv.lower(), dob)
    hits = [i for i, l in enumerate(learners) if l == probe]
    if len(hits) == 1:
        idx = hits[0]
    elif not hits:
        learners.append(probe); idx = len(learners) - 1
    else:
        raise SystemExit("more than one found")
    joined.setdefault(key, set()).add(idx)
print("entries: %d" % len(entries))
print("children (distinct keys): %d" % len(joined))
print("learners after reset: %d" % len(learners))
print("of the 8 on two lists, held as one learner (caught): %d" % sum(1 for k in range(8) if len(joined[k]) == 1))
