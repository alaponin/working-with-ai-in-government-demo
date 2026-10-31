"""A toy data set built to the QUESTIONS-PAPER answers, and the known numbers it yields.

usage: toy.py together   -- the 14 recommendations together (A5)
       toy.py rivals     -- each question's rival with every other recommendation (A13)
It reads no file and writes none; it prints. A toy for checking that answers hold together,
not round 5's generator. The 8 and the singles are laid by construction; the seed draws names,
dates, schools' order and shuffles.
"""
import datetime
import random
import sys

LISTS = ["school_census", "exam_candidate_list", "social_grant_list"]
SCHOOLS = ["School A", "School B", "School C"]
# Q-5 A: (pair of lists, kind); M = matches on all three fields, D = family name spelt differently
PAIRS_A = [((0, 1), "M"), ((0, 1), "M"), ((0, 1), "D"),
           ((0, 2), "M"), ((0, 2), "D"), ((0, 2), "D"),
           ((1, 2), "M"), ((1, 2), "D")]
# Q-5 B: every one of the 8 on the census and one other list, 4 and 4, 2 spelt differently in each
PAIRS_B = [((0, 1), "M"), ((0, 1), "M"), ((0, 1), "D"), ((0, 1), "D"),
           ((0, 2), "M"), ((0, 2), "M"), ((0, 2), "D"), ((0, 2), "D")]
REC = dict(date=(2026, 10, 31), order=[0, 1, 2], within="up", seed=20261031, first=1,
           pairs=PAIRS_A, totals=[24, 22, 22], spread=[20, 20, 20], q8="family_only",
           q9="every_list", q10="iso", q11="all", q12="record", q13=64, q14="ignored", q14_pairs=0)
F1 = ["Kal", "Ter", "Mor", "Vel", "San", "Pir", "Lun", "Dor", "Hav", "Rek", "Til", "Ost"]
F2 = ["berg", "mets", "lane", "vik", "salu", "mae", "oja", "tamm", "kivi", "nurm"]
G = ["Aru", "Belin", "Cato", "Dena", "Elio", "Fira", "Gaspo", "Hela", "Ivon", "Jorek", "Kesa", "Lio",
     "Mira", "Noam", "Oska", "Pella", "Quin", "Rasmo", "Sela", "Tovi"]


def fmt(d, li, q10):
    if q10 == "iso" or li == 0:
        return d.isoformat()
    return d.strftime("%d.%m.%Y") if li == 1 else d.strftime("%d/%m/%Y")


def to_iso(s):
    if "-" in s:
        return s
    sep = "." if "." in s else "/"
    dd, mm, yy = s.split(sep)
    return "%s-%s-%s" % (yy, mm, dd)


def build(cfg):
    c = dict(REC)
    c.update(cfg)
    rng = random.Random(c["seed"])
    on = [0, 0, 0]
    for (a, b), _ in c["pairs"]:
        on[a] += 1
        on[b] += 1
    singles = [c["totals"][i] - on[i] for i in range(3)]
    if min(singles) < 0 or sum(singles) + len(c["pairs"]) != 60:
        return {"ok": False, "why": "entries still needed per list after the 8 are laid %s" % singles}
    if sum(c["spread"]) != 60 or min(c["spread"]) < 1:
        return {"ok": False, "why": "spread over schools %s" % c["spread"]}
    ad = datetime.date(*c["date"])
    lo = datetime.date(ad.year - 13, ad.month, ad.day) + datetime.timedelta(days=1)
    hi = datetime.date(ad.year - 6, ad.month, ad.day)

    def age(d):
        return ad.year - d.year - ((ad.month, ad.day) < (d.month, d.day))

    def k(f, g, d):
        return (f.lower(), g.lower(), d) if c["q14"] == "ignored" else (f, g, d)
    taken = set()

    def draw():
        while True:
            f, g = rng.choice(F1) + rng.choice(F2), rng.choice(G)
            d = lo + datetime.timedelta(days=rng.randrange((hi - lo).days + 1))
            if k(f, g, d) not in taken and (f.lower(), g.lower(), d) not in {(x[0].lower(), x[1].lower(), x[2]) for x in taken}:
                taken.add(k(f, g, d))
                return f, g, d
    school_of = [s for s, n in zip(SCHOOLS, c["spread"]) for _ in range(n)]
    rng.shuffle(school_of)
    kids = []
    for i in range(60):
        f, g, d = draw()
        kids.append({"key": "C%02d" % (i + 1), "f": f, "g": g, "d": d, "s": school_of[i]})
    idx = list(range(60))
    rng.shuffle(idx)
    eight, rest = idx[:8], idx[8:]
    if c["q14_pairs"]:  # Q-14 B: two different children, singles on the census, differing in capitals only
        a, b = kids[rest[0]], kids[rest[1]]
        b["f"], b["g"], b["d"] = a["f"].upper(), a["g"], a["d"]
    entries = [[], [], []]

    def put(li, ch, f, d):
        s = ch["s"] if (c["q9"] == "every_list" or li == 0) else ""
        entries[li].append({"f": f, "g": ch["g"], "d": fmt(d, li, c["q10"]), "s": s, "child": ch["key"]})
    pos = {l: i for i, l in enumerate(c["order"])}
    for n, (ci, ((a, b), kind)) in enumerate(zip(eight, c["pairs"])):
        ch = kids[ci]
        first, later = (a, b) if pos[a] < pos[b] else (b, a)
        put(first, ch, ch["f"], ch["d"])
        f, d = ch["f"], ch["d"]
        if kind == "D":
            while True:
                p = rng.randrange(1, len(f))
                v = f[:p] + rng.choice("aeiouklmnrst") + f[p + 1:]
                if v.lower() != f.lower():
                    break
            f = v
            if c["q8"] == "free" and n % 2 == 0:  # Q-8 B: some of the 4 differ in the date too
                d = d + datetime.timedelta(days=1) if d < hi else d - datetime.timedelta(days=1)
        put(later, ch, f, d)
    p = 0
    for li, n in enumerate(singles):
        for ci in rest[p:p + n]:
            put(li, kids[ci], kids[ci]["f"], kids[ci]["d"])
        p += n
    key = []
    eight_keys = {kids[ci]["key"] for ci in eight}
    for li in range(3):
        rng.shuffle(entries[li])
        for n, e in enumerate(entries[li], 1):
            e["entry"] = "%s:%d" % (LISTS[li], n)
            if c["q11"] == "all" or e["child"] in eight_keys:
                key.append((e["entry"], e["child"]))
    truth = {e["entry"]: e.pop("child") for li in range(3) for e in entries[li]}  # held by the toy only
    # the reset: every entry through the brief's rule, in the order of Q-2
    learners, rec, mto, supplied = [], {}, 0, 0
    for li in c["order"]:
        seq = entries[li] if c["within"] == "up" else list(reversed(entries[li]))
        for e in seq:
            d = to_iso(e["d"])
            hits = [l for l in learners if l["f"].lower() == e["f"].lower() and l["g"].lower() == e["g"].lower() and l["d"] == d]
            if len(hits) == 1:
                rec[e["entry"]] = hits[0]["n"]
            elif not hits:
                n = max([l["n"] for l in learners], default=c["first"] - 1) + 1
                s = e["s"]
                if not s:
                    s, supplied = rng.choice(SCHOOLS), supplied + 1
                learners.append({"n": n, "f": e["f"], "g": e["g"], "d": d, "s": s})
                rec[e["entry"]] = n
            else:
                mto += 1
    allent = {e["entry"]: e for li in range(3) for e in entries[li]}
    by = {}
    for ent, ch in key:
        by.setdefault(ch, []).append(ent)
    off_key = [x for x in allent if x not in {e for e, _ in key}]
    children = len(by) + len(off_key)
    multi = [ch for ch, es in by.items() if len({x.split(":")[0] for x in es}) > 1]
    spelt = [ch for ch in multi if len({allent[x]["f"] for x in by[ch]}) > 1]
    spelt_ci = [ch for ch in multi if len({allent[x]["f"].lower() for x in by[ch]}) > 1]
    ages = [age(datetime.date.fromisoformat(to_iso(e["d"]))) for e in allent.values()]
    if c["q12"] == "record":
        lnum = rec
    else:  # Q-12 B: round 7 finds each entry's learner by comparing its three fields again
        lnum = {}
        for x, e in allent.items():
            m = [l["n"] for l in learners if l["f"].lower() == e["f"].lower() and l["g"].lower() == e["g"].lower() and l["d"] == to_iso(e["d"])]
            lnum[x] = m[0] if len(m) == 1 else None
    caught = [ch for ch in multi if len({lnum[x] for x in by[ch]}) == 1]
    # children per school, read from the schools the lists carry (a child: a key-table child or an off-key entry)
    groups = list(by.values()) + [[x] for x in off_key]
    per, noschool = {s: 0 for s in SCHOOLS}, 0
    for es in groups:
        ss = {allent[x]["s"] for x in es if allent[x]["s"]}
        if len(ss) == 1:
            per[ss.pop()] += 1
        else:
            noschool += 1
    r = {"children": children, "schools": len({e["s"] for e in allent.values() if e["s"]}),
         "entries": len(allent), "per_list": [len(x) for x in entries], "key_rows": len(key),
         "multi": len(multi), "spelt": len(spelt), "spelt_ci": len(spelt_ci), "ages": (min(ages), max(ages)),
         "learners": len(learners), "highest": max(l["n"] for l in learners), "more_than_one": mto,
         "caught": len(caught), "per_school": [per[s] for s in SCHOOLS], "children_without_school_on_lists": noschool,
         "learners_school_supplied_by_reset": supplied, "learners_without_school": sum(1 for l in learners if not l["s"])}
    fails = []
    for name, want in [("children", 60), ("schools", 3), ("entries", 68), ("multi", 8), ("spelt", 4),
                       ("caught", 4), ("more_than_one", 0)]:
        if r[name] != want:
            fails.append("%s %s, not %s" % (name, r[name], want))
    if not (6 <= r["ages"][0] and r["ages"][1] <= 12):
        fails.append("ages %s" % (r["ages"],))
    if r["per_school"] != c["spread"]:
        fails.append("children per school read from the lists %s, not %s (%d children carry no school on the lists)" % (r["per_school"], c["spread"], noschool))
    if c["q13"] is not None and r["learners"] != c["q13"]:
        fails.append("learners after reset %d, against the setting %d" % (r["learners"], c["q13"]))
    r["ok"], r["why"] = not fails, "; ".join(fails)
    return r


def line(r):
    if "children" not in r:
        return r["why"]
    return ("children %(children)d schools %(schools)d entries %(entries)d per_list %(per_list)s on_two %(multi)d "
            "spelt %(spelt)d (capitals ignored %(spelt_ci)d) ages %(ages)s learners %(learners)d highest %(highest)d "
            "caught %(caught)d more_than_one %(more_than_one)d per_school %(per_school)s key_rows %(key_rows)d "
            "school_supplied_by_reset %(learners_school_supplied_by_reset)d" % r)


RIVALS = [
    (1, "B: another date, 2027-03-01", dict(date=(2027, 3, 1))),
    (2, "B: another fixed order, the lists reversed and each list from its last entry", dict(order=[2, 1, 0], within="down")),
    (3, "B: another seed, 12345", dict(seed=12345)),
    (4, "B: another first number, 1001", dict(first=1001)),
    (5, "B: every one of the 8 on the census and one other list", dict(pairs=PAIRS_B)),
    (6, "B: every child on the census, 60, 4 and 4", dict(totals=[60, 4, 4])),
    (7, "B: another spread, 25, 20 and 15", dict(spread=[25, 20, 15])),
    (8, "B: the 4's given names and date left free", dict(q8="free")),
    (9, "B: a school on the census only; the reset gives every other learner one", dict(q9="census_only")),
    (10, "B: each list its own form of date, turned by the reset", dict(q10="own")),
    (11, "B: the key table holds the 16 entries of the 8 only", dict(q11="eight")),
    (12, "B: no record of entries; round 7 compares again", dict(q12="none")),
    (13, "B: no setting for the learners after reset", dict(q13=None)),
    (14, "B: capitals heeded in share, no such pair laid", dict(q14="heeded")),
]

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "together":
        r = build({})
        print("the 14 recommendations together, seed %d" % REC["seed"])
        print("children: %d" % r["children"])
        print("schools: %d" % r["schools"])
        print("entries: %d; per list in the order of line 19: %s" % (r["entries"], r["per_list"]))
        print("children on more than one list: %d" % r["multi"])
        print("of those spelt differently: %d (capitals ignored: %d)" % (r["spelt"], r["spelt_ci"]))
        print("ages: %d to %d" % r["ages"])
        print("children per school: %s" % r["per_school"])
        print("learners after reset: %d; highest learner number: %d; learners without a school: %d" % (r["learners"], r["highest"], r["learners_without_school"]))
        print("searches finding more than one: %d" % r["more_than_one"])
        print("of the 8, caught by the brief's rule: %d" % r["caught"])
        print("every known number met: %s" % ("yes" if r["ok"] else "no — " + r["why"]))
    else:
        for q, name, cfg in RIVALS:
            r = build(cfg)
            print("Q-%d rival (%s), with every other recommendation: can be met: %s" % (q, name, "yes" if r["ok"] else "no"))
            print("    %s" % (line(r) if r["ok"] else r["why"]))
        print("further runs named in the paper:")
        r = build(dict(totals=[60, 4, 4], pairs=PAIRS_B))
        print("  Q-6 B with Q-5 B: can be met: %s — %s" % ("yes" if r["ok"] else "no", line(r)))
        r = build(dict(q14="heeded", q14_pairs=1))
        print("  Q-14 B with one pair laid: can be met: %s — %s" % ("yes" if r["ok"] else "no", r["why"] or line(r)))
        r = build(dict(q9="census_only", spread=[20, 20, 20]))
        print("  Q-9 B: learners whose school the reset supplies %d; children carrying no school on the lists %d" % (r["learners_school_supplied_by_reset"], r["children_without_school_on_lists"]))
        for o in ([0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1]):
            r = build(dict(order=o))
            print("  Q-2 order %s: learners %d caught %d can be met: %s" % (o, r["learners"], r["caught"], "yes" if r["ok"] else "no"))
