"""Work out the paper's figures (64 learners, 68 entries, 4 of the 8 caught, R-12's 4) from a toy
data set built to the brief's numbers and the settings 1 to 4 of G-05 as version 2 states them,
with every entry enrolled at reset through the brief's line 13 rule (G-03, Position B).
Invented names only. usage: figures.py
"""
lists = ["census", "candidates", "grants"]
children = []  # (key, family, given, dob)
for i in range(60):
    children.append(("C%02d" % i, "Fam%02d" % i, "Given%02d" % i, "2016-%02d-%02d" % (i % 12 + 1, i % 28 + 1)))
entries = []  # (list, key, family, given, dob)
for n, (k, f, g, d) in enumerate(children):
    entries.append((lists[n % 3], k, f, g, d))
for n, (k, f, g, d) in enumerate(children[:8]):           # the 8, each on exactly two lists (setting 4)
    other = lists[(n + 1) % 3]
    fam = f[:-1] + "x" if n < 4 else f                     # 4 spelt differently in one letter (1); the rest identical, same capitals (2)
    entries.append((other, k, fam, g, d))
learners = []  # (family, given, dob, keys)
def search(f, g, d):
    return [L for L in learners if (L[0].lower(), L[1].lower(), L[2]) == (f.lower(), g.lower(), d)]
for lst in lists:                                          # fixed order: census, candidates, grants
    for (l, k, f, g, d) in entries:
        if l != lst:
            continue
        found = search(f, g, d)
        if len(found) == 1:
            found[0][3].append(k)
        elif not found:
            learners.append((f, g, d, [k]))
        else:
            raise SystemExit("more than one found")
keys3 = [(c[1].lower(), c[2].lower(), c[3]) for c in children]
print("entries: %d" % len(entries))
print("children: %d; sharing all three, capitals ignored: %d" % (len(children), len(keys3) - len(set(keys3))))
print("learners after reset: %d" % len(learners))
eight = [c[0] for c in children[:8]]
caught = sum(1 for k in eight if any(L[3].count(k) == 2 for L in learners))
print("of the 8 on two lists, held as one learner (caught): %d" % caught)
fams = {}
for (l, k, f, g, d) in entries:
    fams.setdefault(k, []).append(f)
heed = sum(1 for k in eight if len(set(fams[k])) > 1)
ignore = sum(1 for k in eight if len(set(x.lower() for x in fams[k])) > 1)
print("R-12, letter for letter heeding capitals: %d; ignoring capitals: %d" % (heed, ignore))
