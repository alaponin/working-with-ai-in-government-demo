"""The reviewer's own toy (C-2026-10-31-12 v2), written from QUESTIONS-PAPER.md's recommendations as
stated, not from the round's toy.py. No random draw: names, dates and schools are laid by arithmetic.
It also reads the ruled settings rows 10 to 13 of settings.csv literally, on the lists as made,
and Q-8 A's own words, which the round's program does not.
usage: r_toy.py      prints the recommendations together, each rival with every other
                     recommendation, and the further combinations the paper names.
"""
import datetime, itertools

L = ["census", "candidate", "grant"]
S = ["S1", "S2", "S3"]
# Q-5 A, paper line 104: census+candidate 3 (2 match, 1 spelt), census+grant 3 (1, 2), candidate+grant 2 (1, 1)
Q5A = [((0, 1), 0), ((0, 1), 0), ((0, 1), 1), ((0, 2), 0), ((0, 2), 1), ((0, 2), 1), ((1, 2), 0), ((1, 2), 1)]
# Q-5 B, paper line 106: all 8 on the census and one other, 4 and 4, 2 spelt differently in each
Q5B = [((0, 1), 0), ((0, 1), 0), ((0, 1), 1), ((0, 1), 1), ((0, 2), 0), ((0, 2), 0), ((0, 2), 1), ((0, 2), 1)]
REC = {"q1": datetime.date(2026, 10, 31), "q2": ([0, 1, 2], +1), "q4": 1, "q5": Q5A,
       "q6": [24, 22, 22], "q7": [20, 20, 20], "q8": "A", "q9": "A", "q10": "A", "q11": "A",
       "q12": "A", "q13": 64, "q14": "A", "q14_pair": False, "q9_draw": "turn"}
FAM = ["Oruvo", "Taleni", "Mekari", "Sopuna", "Dravic", "Ulmeri", "Kesoni", "Varuta", "Pilona", "Nedari"]
GIV = ["Ami", "Bero", "Cela", "Dovi", "Esa", "Fen"]

def fmt(d, li, q10):
    if q10 == "A":
        return d.strftime("%Y-%m-%d")
    return [d.strftime("%Y-%m-%d"), d.strftime("%d.%m.%Y"), d.strftime("%m/%d/%Y")][li]

def iso(s):
    if "." in s:
        dd, mm, yy = s.split("."); return "%s-%s-%s" % (yy, mm, dd)
    if "/" in s:
        mm, dd, yy = s.split("/"); return "%s-%s-%s" % (yy, mm, dd)
    return s

def build(**over):
    c = dict(REC); c.update(over)
    ref = c["q1"]
    lo = datetime.date(ref.year - 13, ref.month, ref.day) + datetime.timedelta(days=1)
    hi = datetime.date(ref.year - 6, ref.month, ref.day)
    carried = [0, 0, 0]
    for (a, b), _ in c["q5"]:
        carried[a] += 1; carried[b] += 1
    single = [c["q6"][i] - carried[i] for i in range(3)]
    if min(single) < 0 or sum(single) + 8 != 60:
        return None, "cannot be laid: single-list children per list %s (lists hold %s, the 8 take %s)" % (single, c["q6"], carried)
    # 60 children by arithmetic: child i, family FAM[i%10]+letter, given GIV[i%6], date spread lo..hi
    span = (hi - lo).days
    kids = []
    school_of = [S[k] for k in range(3) for _ in range(c["q7"][k])]
    for i in range(60):
        kids.append({"id": "C%02d" % (i + 1), "f": FAM[i % 10] + "abcdef"[i // 10],
                     "g": GIV[i % 6], "d": lo + datetime.timedelta(days=(span * i) // 59),
                     "s": school_of[i]})
    if c["q14_pair"]:  # Q-14 B laying one pair: C60 differs from C59 in capitals only
        kids[59].update(f=kids[58]["f"].upper(), g=kids[58]["g"], d=kids[58]["d"])
    order, step = c["q2"]
    rank = {l: n for n, l in enumerate(order)}
    lists = [[], [], []]
    def put(li, k, f, d):
        sch = k["s"] if (c["q9"] == "A" or li == 0) else ""
        lists[li].append({"f": f, "g": k["g"], "d": fmt(d, li, c["q10"]), "s": sch, "child": k["id"]})
    # the 8 are children 0..7 (Q-7's schools: the 8 spread over S1..S3 by school_of), singles follow
    for n, ((a, b), spelt) in enumerate(c["q5"]):
        k = kids[n * 7]  # every 7th child, so the 8 fall in all three schools
        first, later = sorted((a, b), key=lambda x: rank[x])
        put(first, k, k["f"], k["d"])
        f2, d2 = k["f"], k["d"]
        if spelt:
            f2 = k["f"][0] + ("y" if k["f"][1] != "y" else "z") + k["f"][2:]  # one letter, not capitals
            if c["q8"] == "B" and n % 2 == 0:
                d2 = d2 + datetime.timedelta(days=1)
        put(later, k, f2, d2)
    eight = {kids[n * 7]["id"] for n in range(8)}
    rest = [k for k in kids if k["id"] not in eight]
    p = 0
    for li in range(3):
        for k in rest[p:p + single[li]]:
            put(li, k, k["f"], k["d"])
        p += single[li]
    # entry numbers (Q-11 A): a fixed permutation, i -> (7*i) mod n, numbered 1 upwards
    for li in range(3):
        n = len(lists[li])
        perm = sorted(range(n), key=lambda i: (7 * i + 3) % n if n > 1 else 0)
        lists[li] = [lists[li][i] for i in perm]
        for j, e in enumerate(lists[li], 1):
            e["key"] = "%s:%d" % (L[li], j)
    allent = {e["key"]: e for li in range(3) for e in lists[li]}
    key = [(e["key"], e["child"]) for e in allent.values() if c["q11"] == "A" or e["child"] in eight]
    truth = {e["key"]: e["child"] for e in allent.values()}  # the toy's own, for counting only
    # the reset: every entry through line 13's rule, Q-2's order, capitals ignored, nothing else forgiven
    learners, rec, mto, turn = [], {}, 0, 0
    for li in order:
        seq = lists[li] if step > 0 else list(reversed(lists[li]))
        for e in seq:
            d = iso(e["d"]) if c["q10"] == "B" else e["d"]
            hit = [x for x in learners if x["f"].casefold() == e["f"].casefold()
                   and x["g"].casefold() == e["g"].casefold() and x["d"] == d]
            if len(hit) == 1:
                rec[e["key"]] = hit[0]["n"]
            elif not hit:
                n = (max(x["n"] for x in learners) + 1) if learners else c["q4"]
                s = e["s"]
                if not s:  # Q-9 B: the reset supplies a school, in turn S1, S2, S3
                    s = S[turn % 3]; turn += 1
                learners.append({"n": n, "f": e["f"], "g": e["g"], "d": d, "s": s, "from": e["key"]})
                rec[e["key"]] = n
            else:
                mto += 1
    if c["q12"] == "B":  # round 7 compares again
        rec = {}
        for k2, e in allent.items():
            d = iso(e["d"]) if c["q10"] == "B" else e["d"]
            m = [x["n"] for x in learners if x["f"].casefold() == e["f"].casefold() and x["g"].casefold() == e["g"].casefold() and x["d"] == d]
            rec[k2] = m[0] if len(m) == 1 else None
    by = {}
    for k2, ch in truth.items():
        by.setdefault(ch, []).append(k2)
    multi = [ch for ch, es in by.items() if len({x.split(":")[0] for x in es}) > 1]
    on_two = all(len(by[ch]) == 2 for ch in multi)
    spelt = [ch for ch in multi if len({allent[x]["f"] for x in by[ch]}) > 1]
    caps_only = [ch for ch in spelt if len({allent[x]["f"].casefold() for x in by[ch]}) == 1]
    other4 = [ch for ch in multi if ch not in spelt]
    # ruled row 12 as Q-8 reads it (all three fields), literally on the lists: letter for letter, same capitals
    row12 = [ch for ch in other4 if len({(allent[x]["f"], allent[x]["g"], allent[x]["d"]) for x in by[ch]}) == 1]
    # Q-8 A's own words, paper line 159: the 4's given names and date match on both lists, letter for letter
    q8a = [ch for ch in spelt if len({(allent[x]["g"], allent[x]["d"]) for x in by[ch]}) == 1]
    ages = []
    for e in allent.values():
        b = datetime.date.fromisoformat(iso(e["d"]))
        ages.append(ref.year - b.year - ((ref.month, ref.day) < (b.month, b.day)))
    # ruled row 13 under Q-14's answer: different children sharing all three fields
    trip = {}
    for k in kids:
        t = (k["f"].casefold(), k["g"].casefold(), k["d"]) if c["q14"] == "A" else (k["f"], k["g"], k["d"])
        trip.setdefault(t, []).append(k["id"])
    sharing = sum(1 for v in trip.values() if len(v) > 1)
    caught = [ch for ch in multi if len({rec[x] for x in by[ch]}) == 1 and None not in {rec[x] for x in by[ch]}]
    # children per school: read from the lists (Q-7 A's own words), and from the learners' records
    per_lists = {s: 0 for s in S}; none_on_lists = 0
    per_learn = {s: 0 for s in S}; two_schools = 0
    lby = {x["n"]: x for x in learners}
    for ch, es in by.items():
        ss = {allent[x]["s"] for x in es if allent[x]["s"]}
        if len(ss) == 1: per_lists[ss.pop()] += 1
        else: none_on_lists += 1
        ls = {lby[rec[x]]["s"] for x in es if rec.get(x) in lby}
        if len(ls) == 1: per_learn[ls.pop()] += 1
        else: two_schools += 1
    r = {"children": len(by), "schools": len({x["s"] for x in learners}), "entries": len(allent),
         "per_list": [len(x) for x in lists], "on_more_than_one": len(multi), "each_on_exactly_2": on_two,
         "spelt": len(spelt), "capitals_only": len(caps_only), "ages": (min(ages), max(ages)),
         "learners": len(learners), "highest": max(x["n"] for x in learners), "more_than_one": mto,
         "caught": len(caught), "key_rows": len(key), "row12_other4_letter_for_letter": "%d of %d" % (len(row12), len(other4)),
         "q8A_4_given_and_date_letter_for_letter": "%d of %d" % (len(q8a), len(spelt)), "row13_sharing": sharing,
         "per_school_from_lists": [per_lists[s] for s in S], "children_no_school_on_lists": none_on_lists,
         "per_school_from_learners": [per_learn[s] for s in S], "children_at_two_schools": two_schools,
         "schools_supplied_by_reset": turn}
    fails = []
    for k2, want in [("children", 60), ("schools", 3), ("entries", 68), ("on_more_than_one", 8),
                     ("each_on_exactly_2", True), ("spelt", 4), ("capitals_only", 0), ("caught", 4),
                     ("more_than_one", 0), ("row13_sharing", 0)]:
        if r[k2] != want: fails.append("%s=%s (want %s)" % (k2, r[k2], want))
    if not (r["ages"][0] >= 6 and r["ages"][1] <= 12): fails.append("ages %s" % (r["ages"],))
    if c["q13"] is not None and r["learners"] != c["q13"]: fails.append("learners %d against Q-13's %d" % (r["learners"], c["q13"]))
    if r["highest"] != c["q4"] + r["learners"] - 1: fails.append("highest %d" % r["highest"])
    if r["row12_other4_letter_for_letter"] != "4 of 4": fails.append("ruled row 12: other 4 letter for letter %s" % r["row12_other4_letter_for_letter"])
    if c["q8"] == "A" and r["q8A_4_given_and_date_letter_for_letter"] != "4 of 4":
        fails.append("Q-8 A as worded: the 4's given names and date letter for letter %s" % r["q8A_4_given_and_date_letter_for_letter"])
    if c["q9"] == "A" and r["per_school_from_lists"] != c["q7"]: fails.append("Q-7 read from the lists %s" % r["per_school_from_lists"])
    if c["q9"] == "B" and r["per_school_from_learners"] != c["q7"]: fails.append("Q-7 read from the learners %s" % r["per_school_from_learners"])
    return r, "; ".join(fails)

def show(name, r, why):
    print(name)
    if r is None:
        print("   can be met: no -", why); return
    print("   can be met: %s%s" % ("yes" if not why else "no", "" if not why else " - " + why))
    print("   " + " ".join("%s=%s" % kv for kv in r.items()))

if __name__ == "__main__":
    show("TOGETHER: the 14 recommendations", *build())
    RIV = [("Q-1 B 2027-03-01", dict(q1=datetime.date(2027, 3, 1))),
           ("Q-2 B lists reversed, entries from the last", dict(q2=([2, 1, 0], -1))),
           ("Q-3 B another seed (no draw here: nothing changes)", dict()),
           ("Q-4 B first number 1001", dict(q4=1001)),
           ("Q-5 B all 8 on the census and one other", dict(q5=Q5B)),
           ("Q-6 B 60, 4, 4", dict(q6=[60, 4, 4])),
           ("Q-7 B 25, 20, 15", dict(q7=[25, 20, 15])),
           ("Q-8 B the 4's given names and date left free (2 of the 4 dates differ)", dict(q8="B")),
           ("Q-9 B the census alone carries a school; the reset supplies one in turn", dict(q9="B")),
           ("Q-10 B each list its own form of date, turned by the reset", dict(q10="B")),
           ("Q-11 B key table of the 16 entries of the 8", dict(q11="B")),
           ("Q-12 B no record; round 7 compares again", dict(q12="B")),
           ("Q-13 B no setting", dict(q13=None)),
           ("Q-14 B capitals heeded, no pair laid", dict(q14="B"))]
    print("\nEACH RIVAL WITH EVERY OTHER RECOMMENDATION")
    for name, ov in RIV:
        show(name, *build(**ov))
    print("\nFURTHER")
    show("Q-6 B with Q-5 B", *build(q6=[60, 4, 4], q5=Q5B))
    show("Q-6 'any other spread holding the 8 as Q-5 A lays them': 28, 20, 20", *build(q6=[28, 20, 20]))
    show("Q-6 the least each list can hold under Q-5 A: 6+46, 5, 5 -> 58, 5, 5", *build(q6=[58, 5, 5]))
    show("Q-14 B with one pair laid", *build(q14="B", q14_pair=True))
    show("Q-10 B with Q-8 B", *build(q10="B", q8="B"))
    show("Q-9 B with Q-7 B 25, 20, 15", *build(q9="B", q7=[25, 20, 15]))
    for o in itertools.permutations([0, 1, 2]):
        for st in (+1, -1):
            r, why = build(q2=(list(o), st))
            print("Q-2 order %s step %+d: learners %d caught %d %s" % (list(o), st, r["learners"], r["caught"], "met" if not why else why))
