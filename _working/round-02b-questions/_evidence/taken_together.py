"""Taken together: a toy data set built to the QUESTIONS-PAPER recommendations, and the known numbers it yields.

usage: taken_together.py
It reads no file and writes none; it prints. It is a toy for checking that the 14 recommendations
hold together, not round 5's generator.
"""
import datetime
import random

# --- the recommendations, one constant each -------------------------------------------------
SEED = 20261031                       # Q-3
AGE_DATE = datetime.date(2026, 10, 31)  # Q-1
FIRST_NUMBER = 1                      # Q-4
LIST_ORDER = ["school_census", "exam_candidate_list", "social_grant_list"]  # Q-2
SCHOOLS = ["School A", "School B", "School C"]  # Q-7: 20 children each
# Q-5: the 8, by pair of lists; "M" = matches on all three fields (Q-8), "D" = family name spelt differently
PAIRS = [((0, 1), "M"), ((0, 1), "M"), ((0, 1), "D"),
         ((0, 2), "M"), ((0, 2), "D"), ((0, 2), "D"),
         ((1, 2), "M"), ((1, 2), "D")]
SINGLES = [18, 17, 17]                # Q-6: children on one list only, per list -> 24, 22, 22 entries

rng = random.Random(SEED)
F1 = ["Kal", "Ter", "Mor", "Vel", "San", "Pir", "Lun", "Dor", "Hav", "Rek", "Til", "Ost"]
F2 = ["berg", "mets", "lane", "vik", "salu", "mae", "oja", "tamm", "kivi", "nurm"]
G = ["Aru", "Belin", "Cato", "Dena", "Elio", "Fira", "Gaspo", "Hela", "Ivon", "Jorek", "Kesa", "Lio",
     "Mira", "Noam", "Oska", "Pella", "Quin", "Rasmo", "Sela", "Tovi"]


def age(d):
    return AGE_DATE.year - d.year - ((AGE_DATE.month, AGE_DATE.day) < (d.month, d.day))


lo, hi = datetime.date(2013, 11, 1), datetime.date(2020, 10, 31)  # ages 6 to 12 on AGE_DATE (Q-1)
taken = set()  # Q-14: (family, given, dob) with capitals ignored, over every entry of every child


def draw():
    while True:
        f = rng.choice(F1) + rng.choice(F2)
        g = rng.choice(G)
        d = lo + datetime.timedelta(days=rng.randrange((hi - lo).days + 1))
        k = (f.lower(), g.lower(), d.isoformat())
        if k not in taken:
            taken.add(k)
            return f, g, d


children = []
for i in range(60):
    f, g, d = draw()
    children.append({"key": "C%02d" % (i + 1), "family": f, "given": g, "dob": d, "school": SCHOOLS[i // 20]})

order = list(range(60))
rng.shuffle(order)
eight, rest = order[:8], order[8:]
entries = [[], [], []]  # per list: dicts with family, given, dob (YYYY-MM-DD, Q-10), school (Q-9), child
for ci, ((a, b), kind) in zip(eight, PAIRS):
    c = children[ci]
    entries[a].append({"family": c["family"], "given": c["given"], "dob": c["dob"].isoformat(), "school": c["school"], "child": c["key"]})
    fam = c["family"]
    if kind == "D":  # spelt differently on the later list of its pair (Q-5): one letter changed
        while True:
            p = rng.randrange(1, len(fam))
            ch = rng.choice("aeiouklmnrst")
            v = fam[:p] + ch + fam[p + 1:]
            k = (v.lower(), c["given"].lower(), c["dob"].isoformat())
            if v.lower() != fam.lower() and k not in taken:
                taken.add(k)
                fam = v
                break
    entries[b].append({"family": fam, "given": c["given"], "dob": c["dob"].isoformat(), "school": c["school"], "child": c["key"]})
pos = 0
for li, n in enumerate(SINGLES):
    for ci in rest[pos:pos + n]:
        c = children[ci]
        entries[li].append({"family": c["family"], "given": c["given"], "dob": c["dob"].isoformat(), "school": c["school"], "child": c["key"]})
    pos += n
# Q-11: each list's entries numbered 1..n after a seeded shuffle; the key table holds all of them
key_table = []
for li in range(3):
    rng.shuffle(entries[li])
    for n, e in enumerate(entries[li], 1):
        e["entry"] = "%s:%d" % (LIST_ORDER[li], n)
        key_table.append((e["entry"], e["child"]))
        del e["child"]  # the list entry carries only what its list carries

# --- the reset: every entry enrolled through the brief's rule, in Q-2's order ---------------------
learners = []        # dicts: number, family, given, dob, school
enrolled_from = []   # Q-12: (list entry, learner number), written after each entry's search
more_than_one = 0
for li in range(3):
    for e in entries[li]:  # in entry-number order
        hits = [l for l in learners if l["family"].lower() == e["family"].lower()
                and l["given"].lower() == e["given"].lower() and l["dob"] == e["dob"]]
        if len(hits) == 1:
            enrolled_from.append((e["entry"], hits[0]["number"]))
        elif not hits:
            num = max([l["number"] for l in learners], default=FIRST_NUMBER - 1) + 1
            learners.append({"number": num, "family": e["family"], "given": e["given"], "dob": e["dob"], "school": e["school"]})
            enrolled_from.append((e["entry"], num))
        else:
            more_than_one += 1

# --- the counts -----------------------------------------------------------------------------
allent = {e["entry"]: e for li in range(3) for e in entries[li]}
by_child = {}
for ent, ch in key_table:
    by_child.setdefault(ch, []).append(ent)
multi = [ch for ch, es in by_child.items() if len({x.split(":")[0] for x in es}) > 1]
spelt = [ch for ch in multi if len({allent[x]["family"] for x in by_child[ch]}) > 1]
spelt_ci = [ch for ch in multi if len({allent[x]["family"].lower() for x in by_child[ch]}) > 1]
ages = [age(datetime.date.fromisoformat(e["dob"])) for e in allent.values()]
lnum = dict(enrolled_from)
caught = [ch for ch in multi if len({lnum[x] for x in by_child[ch]}) == 1]
print("seed %d; ages reckoned on %s; first learner number %d" % (SEED, AGE_DATE, FIRST_NUMBER))
print("children (child keys in the key table): %d" % len(by_child))
print("schools named on the lists: %d" % len({e["school"] for e in allent.values()}))
print("children per school: %s" % [sum(1 for c in children if c["school"] == s) for s in SCHOOLS])
print("entries: %d; per list in order: %s" % (len(allent), [len(x) for x in entries]))
print("key table rows: %d" % len(key_table))
print("children on more than one list: %d" % len(multi))
print("of those spelt differently, letter for letter heeding capitals: %d; capitals ignored: %d" % (len(spelt), len(spelt_ci)))
print("ages: %d to %d" % (min(ages), max(ages)))
print("learners after reset: %d; highest learner number %d; learners without a school %d" % (
    len(learners), max(l["number"] for l in learners), sum(1 for l in learners if not l["school"])))
print("searches finding more than one: %d" % more_than_one)
print("of the 8, caught by the rule (both entries in one learner): %d" % len(caught))
