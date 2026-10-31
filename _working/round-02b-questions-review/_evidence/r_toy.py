"""Review of C-2026-10-31-11: the "Taken together" numbers re-established by the reviewer's own toy run.

usage: r_toy.py
Written from the paper's 14 recommendations as docs/QUESTIONS-PAPER.md states them, not from the
round's taken_together.py. Route: no random draw at all; every name and date is laid down by
arithmetic, the lists are composed table-first from Q-5 and Q-6, and the reset is a separate
function that sees only what a list entry carries. It then varies what the paper says does not
matter (Q-2: the order; Q-3: the seed, here the laying of names) and probes three cells of the
rivals (Q-6 B with Q-5 A; Q-9 B; Q-14 B). It reads no file and writes none.
"""
import datetime
import itertools

AGE_DATE = datetime.date(2026, 10, 31)                         # Q-1
FIRST = 1                                                      # Q-4
LISTS = ["school_census", "exam_candidate_list", "social_grant_list"]  # Q-2 A: the brief's line 19
SCHOOLS = ["S1", "S2", "S3"]                                   # Q-7: 20 each
# Q-5 A: census+candidate 3 (2 match, 1 differ); census+grant 3 (1, 2); candidate+grant 2 (1, 1)
PAIRS = {(0, 1): (2, 1), (0, 2): (1, 2), (1, 2): (1, 1)}
SINGLE = None                                                  # Q-6 A: 24, 22, 22 entries -> derived


def age(dob):
    return AGE_DATE.year - dob.year - ((AGE_DATE.month, AGE_DATE.day) < (dob.month, dob.day))


def build(pairs, totals, shift=0, school_lists=(0, 1, 2), capital_twins=0):
    """Return lists (entries without the child) and the key table, by construction."""
    lo, hi = datetime.date(2013, 11, 1), datetime.date(2020, 10, 31)   # Q-1 A: ages 6..12
    span = (hi - lo).days
    kids = []
    for i in range(60):
        fam = "Fam" + "abcdefghij"[(i + shift) % 10] + "klmnopqrst"[((i + shift) // 10) % 10] + "son"
        kids.append({"key": "C%02d" % (i + 1), "family": fam, "given": "Giv%02d" % i,
                     "dob": lo + datetime.timedelta(days=(i * 37 + shift) % (span + 1)),
                     "school": SCHOOLS[i // 20]})                      # Q-7 A
    kids[-1]["dob"], kids[-2]["dob"] = lo, hi                          # both bounds of Q-1 A laid
    # Q-14 B probe: make child 59 differ from child 58 in capitals only (all three fields)
    for t in range(capital_twins):
        a, b = kids[58 - 2 * t], kids[59 - 2 * t]
        b["family"], b["given"], b["dob"] = a["family"].upper(), a["given"], a["dob"]
    lists = [[], [], []]
    k = 0
    for (a, b), (m, d) in pairs.items():
        for kind in ["M"] * m + ["D"] * d:
            c = kids[k]; k += 1
            lists[a].append((c, c["family"]))
            # Q-8 A: only the family name differs, in one letter (not capitals), on the later list (Q-5 A)
            fam = c["family"] if kind == "M" else c["family"][:-1] + "x"
            lists[b].append((c, fam))
    need = [t - len(l) for t, l in zip(totals, lists)]
    assert sum(need) == 60 - k and min(need) >= 0, (need, k)
    for li, n in enumerate(need):
        for _ in range(n):
            c = kids[k]; k += 1
            lists[li].append((c, c["family"]))
    out, key = [], []
    for li, l in enumerate(lists):
        ents = []
        for n, (c, fam) in enumerate(l, 1):                         # Q-11 A: list:number
            ent = {"entry": "%s:%d" % (LISTS[li], n), "family": fam, "given": c["given"],
                   "dob": c["dob"].isoformat(),                      # Q-10 A: YYYY-MM-DD
                   "school": c["school"] if li in school_lists else None}   # Q-9 A: every list
            ents.append(ent)
            key.append((ent["entry"], c["key"]))                     # Q-11 A: all entries
        out.append(ents)
    return out, key


def reset(lists, order):
    """Every entry enrolled through the brief's rule (line 13), capitals ignored, in `order` (Q-2)."""
    learners, made_from, multi = [], [], 0                          # Q-12 A: list_entry, learner_number
    for li in order:
        for e in lists[li]:
            same = [l for l in learners if (l["family"].casefold(), l["given"].casefold(), l["dob"]) ==
                    (e["family"].casefold(), e["given"].casefold(), e["dob"])]
            if len(same) == 1:
                made_from.append((e["entry"], same[0]["no"]))
            elif not same:
                no = (max(l["no"] for l in learners) if learners else FIRST - 1) + 1   # Q-4 A
                learners.append({"no": no, "family": e["family"], "given": e["given"],
                                 "dob": e["dob"], "school": e["school"]})
                made_from.append((e["entry"], no))
            else:
                multi += 1
    return learners, made_from, multi


def counts(lists, key, order):
    learners, made_from, multi = reset(lists, order)
    ents = {e["entry"]: e for l in lists for e in l}
    child = {}
    for ent, c in key:
        child.setdefault(c, []).append(ent)
    on_two = [c for c, es in child.items() if len({x.split(":")[0] for x in es}) > 1]
    differ = [c for c in on_two if len({ents[x]["family"] for x in child[c]}) > 1]
    differ_ci = [c for c in on_two if len({ents[x]["family"].casefold() for x in child[c]}) > 1]
    lno = dict(made_from)
    caught = [c for c in on_two if len({lno[x] for x in child[c]}) == 1]
    ages = [age(datetime.date.fromisoformat(e["dob"])) for e in ents.values()]
    return {"children": len(child), "schools": len({e["school"] for e in ents.values() if e["school"]}),
            "entries": len(ents), "per_list": [len(l) for l in lists], "on_two": len(on_two),
            "spelt_differently": len(differ), "spelt_differently_capitals_ignored": len(differ_ci),
            "ages": (min(ages), max(ages)), "learners": len(learners),
            "highest": max(l["no"] for l in learners),
            "without_school": sum(1 for l in learners if not l["school"]),
            "more_than_one": multi, "caught": len(caught)}


lists, key = build(PAIRS, (24, 22, 22))
base = counts(lists, key, (0, 1, 2))
print("THE RECOMMENDATIONS TOGETHER (Q-2 order census, candidate, grant):")
for k, v in base.items():
    print("  %s: %s" % (k, v))

print("\nQ-1 A bounds: age on 2026-10-31 of 2013-10-31 %d, 2013-11-01 %d, 2020-10-31 %d, 2020-11-01 %d" % (
    age(datetime.date(2013, 10, 31)), age(datetime.date(2013, 11, 1)), age(datetime.date(2020, 10, 31)),
    age(datetime.date(2020, 11, 1))))

print("\nQ-2 B: every other order of the three lists, and each list's entries reversed:")
for o in itertools.permutations(range(3)):
    c = counts(lists, key, o)
    rev = [list(reversed(l)) for l in lists]
    r = counts(rev, key, o)
    print("  order %s: learners %d caught %d · entries reversed: learners %d caught %d" % (
        o, c["learners"], c["caught"], r["learners"], r["caught"]))

print("\nQ-3 B (names and dates laid another way, as another seed would):")
for s in (1, 7, 123):
    l2, k2 = build(PAIRS, (24, 22, 22), shift=s)
    c = counts(l2, k2, (0, 1, 2))
    print("  shift %d: children %d entries %d on_two %d differ %d learners %d caught %d" % (
        s, c["children"], c["entries"], c["on_two"], c["spelt_differently"], c["learners"], c["caught"]))

print("\nQ-6 A with Q-5 A, children on one list only per list:", [24 - 6, 22 - 5, 22 - 5])
print("Q-6 B (60, 4, 4) with Q-5 A as recommended:")
try:
    build(PAIRS, (60, 4, 4))
    print("  built")
except AssertionError as e:
    print("  cannot be built: entries still needed per list after the 8 are laid", e.args[0][0],
          "- the candidate and grant lists already hold 5 each from Q-5 A")
print("Q-6 A with Q-5 B (all 8 on the census, 4 with each other list, 2 differing in each):")
c = counts(*build({(0, 1): (2, 2), (0, 2): (2, 2)}, (24, 22, 22)), (0, 1, 2))
print("  children %d entries %d per_list %s on_two %d learners %d caught %d" % (
    c["children"], c["entries"], c["per_list"], c["on_two"], c["learners"], c["caught"]))

print("\nQ-9 B (the census alone carries a school), all else as recommended:")
c = counts(*build(PAIRS, (24, 22, 22), school_lists=(0,)), (0, 1, 2))
print("  learners %d without a school %d" % (c["learners"], c["without_school"]))
for o in itertools.permutations(range(3)):
    c = counts(*build(PAIRS, (24, 22, 22), school_lists=(0,)), o)
    print("  Q-9 B under order %s: without a school %d" % (o, c["without_school"]))

print("\nQ-14 B (one pair of different children differing in capitals only), all else as recommended:")
c = counts(*build(PAIRS, (24, 22, 22), capital_twins=1), (0, 1, 2))
print("  children %d learners %d caught %d" % (c["children"], c["learners"], c["caught"]))
