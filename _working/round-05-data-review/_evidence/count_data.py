#!/usr/bin/python3
"""The reviewer's own count of the made-up data of round 5.

Reads src/data/*.json and docs/groundwork/search_rule.csv and nothing of the
round's code; shares no code with it (Python, written by the review). Applies the
search rule itself, from search_rule.csv, in the order of ruling Q-2.
Usage: /usr/bin/python3 -I count_data.py <mini-registry root>
"""
import csv, datetime, hashlib, json, os, re, sys
from collections import Counter, defaultdict

ROOT = sys.argv[1]
DATA = os.path.join(ROOT, "src", "data")
LISTS = ["school_census", "exam_candidate_list", "social_grant_list"]  # brief line 19, ruling Q-2
ON = datetime.date(2026, 10, 31)  # ruling Q-1


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def out(label, value, fixed_by):
    print("%-58s %-28s %s" % (label, value, fixed_by))


lists = {l: load(l + ".json") for l in LISTS}
key = load("key_table.json")
learners = load("learners.json")
enrol = load("enrolments.json")
schools = load("schools.json")
reads = load("reads.json")

child_of = {r["list_entry"]: r["same_child"] for r in key}
entries = []
for l in LISTS:
    for e in lists[l]:
        name = "%s:%d" % (l, e["entry"])
        entries.append(dict(e, list=l, name=name, child=child_of.get(name)))

print("files read:", ", ".join(sorted(os.listdir(DATA))))
print("%-58s %-28s %s" % ("figure", "counted here", "fixed by"))
children = sorted(set(child_of.values()))
out("children (distinct same_child in key_table)", len(children), "settings.csv:2 children 60 · G-04")
out("entries without a child in key_table", sum(1 for e in entries if e["child"] is None), "Q-11 (all 68 keyed)")
out("schools in schools.json", len(schools), "settings.csv:3 schools 3")
by_child = defaultdict(list)
for e in entries:
    by_child[e["child"]].append(e)
school_of = {}
mixed = 0
for c, es in by_child.items():
    s = set(e["school"] for e in es)
    if len(s) != 1:
        mixed += 1
    school_of[c] = es[0]["school"]
out("children whose entries name two schools", mixed, "Q-9 (same on both lists)")
per_school = Counter(school_of.values())
out("children per school", [per_school[s] for s in schools], "Q-7 20 each")
out("entries without a school", sum(1 for e in entries if not e.get("school")), "Q-9 every list carries one")
out("entries per list (census, candidate, grant)", [len(lists[l]) for l in LISTS], "Q-6 24, 22, 22")
out("entries in all", len(entries), "settings.csv:7 list_entries 68 · G-04")
out("key_table rows", len(key), "Q-11 all 68")
numbering_ok = all([e["entry"] for e in lists[l]] == list(range(1, len(lists[l]) + 1)) for l in LISTS)
out("each list numbered 1 upwards", numbering_ok, "Q-11")

multi = {c: es for c, es in by_child.items() if len(es) > 1}
out("children on more than one list", len(multi), "settings.csv:4 · 8")
out("of those, on exactly two different lists", sum(1 for es in multi.values() if len(es) == 2 and len(set(e["list"] for e in es)) == 2), "settings.csv:8 exactly 2 · G-04")
pairs = Counter()
spelt = []
for c, es in sorted(multi.items()):
    es = sorted(es, key=lambda e: LISTS.index(e["list"]))
    pairs[es[0]["list"] + "+" + es[1]["list"]] += 1
    a, b = es
    if a["family_name"] != b["family_name"]:
        spelt.append((c, a, b))
for p in ["school_census+exam_candidate_list", "school_census+social_grant_list", "exam_candidate_list+social_grant_list"]:
    out("  the 8 on " + p, pairs[p], "Q-5 A: 3, 3, 2")
out("of the 8, family name spelt differently", len(spelt), "settings.csv:5 · 4")
out("  of those, differing in capitals only", sum(1 for _, a, b in spelt if a["family_name"].lower() == b["family_name"].lower()), "settings.csv:11 · 0 (G-05)")
out("  of those, given names or date also differing", sum(1 for _, a, b in spelt if a["given_names"] != b["given_names"] or a["date_of_birth"] != b["date_of_birth"]), "Q-8 A · 0")
sp_pairs = Counter(a["list"] + "+" + b["list"] for _, a, b in spelt)
for p in ["school_census+exam_candidate_list", "school_census+social_grant_list", "exam_candidate_list+social_grant_list"]:
    out("  the 4 on " + p, sp_pairs[p], "Q-5 A: 1, 2, 1")
for c, a, b in spelt:
    print("    %s  %s=%s  ->  %s=%s   (given %r, born %s)" % (c, a["name"], a["family_name"], b["name"], b["family_name"], a["given_names"], a["date_of_birth"]))
same4 = [(c, es) for c, es in multi.items() if es[0]["family_name"] == es[1]["family_name"]]
out("of the 8, all three fields letter for letter", sum(1 for c, es in same4 if all(es[0][f] == es[1][f] for f in ("family_name", "given_names", "date_of_birth"))), "settings.csv:12 · the other 4")

iso = re.compile(r"^\d{4}-\d{2}-\d{2}$")
bad = [e["name"] for e in entries if not iso.match(e["date_of_birth"])]
out("dates not YYYY-MM-DD (entries)", len(bad), "Q-10 · 0")
ages = []
for e in entries:
    y, m, d = map(int, e["date_of_birth"].split("-"))
    born = datetime.date(y, m, d)
    ages.append(ON.year - born.year - ((ON.month, ON.day) < (born.month, born.day)))
out("ages on 2026-10-31, lowest and highest", (min(ages), max(ages)), "settings.csv:6,16 · 6 to 12 (Q-1, G-06)")
out("ages counted", sorted(Counter(ages).items()), "")

triples = defaultdict(set)
for e in entries:
    triples[(e["family_name"].lower(), e["given_names"].lower(), e["date_of_birth"].lower())].add(e["child"])
out("three-field keys shared by two different children", sum(1 for v in triples.values() if len(v) > 1), "settings.csv:13 · 0 (Q-14)")

# The search rule, applied here from search_rule.csv.
with open(os.path.join(ROOT, "docs", "groundwork", "search_rule.csv"), encoding="utf-8") as f:
    rule = list(csv.DictReader(f))
field = {"family name": "family_name", "given names": "given_names", "date of birth": "date_of_birth"}
compared = [field[r["rule"]] for r in rule if r["part"] == "compares"]
print("rule compares, from search_rule.csv:", compared, "; forgives:", [r["rule"] for r in rule if r["part"] == "forgives"])
mine = []
my_enrol = []
for e in entries:  # in Q-2's order: lists by line 19, each by entry number
    found = [l for l in mine if all(l[k].lower() == e[k].lower() for k in compared)]
    if len(found) == 1:
        my_enrol.append((e["name"], found[0]["n"]))
    elif len(found) == 0:
        n = max([l["n"] for l in mine] or [0]) + 1
        mine.append(dict(n=n, family_name=e["family_name"], given_names=e["given_names"], date_of_birth=e["date_of_birth"], school=e["school"]))
        my_enrol.append((e["name"], n))
    else:
        my_enrol.append((e["name"], None))
out("learners by this rule, applied here", len(mine), "Q-13 · 64")
out("searches finding more than one", sum(1 for _, n in my_enrol if n is None), "search_rule.csv:17 · never reached")
learner_of = dict(my_enrol)
joined = sum(1 for c, es in multi.items() if learner_of[es[0]["name"]] == learner_of[es[1]["name"]])
out("of the 8, joined by the rule (both entries one learner)", joined, "settings.csv:14 · 4 (G-05)")
joined_spelt = sum(1 for c, a, b in spelt if learner_of[a["name"]] == learner_of[b["name"]])
out("  of the 4 spelt differently, joined", joined_spelt, "0: the rule misses them")

out("learners.json, rows", len(learners), "Q-13 · 64")
out("learners.json numbers are 1..64 in order", [l["learner_number"] for l in learners] == list(range(1, 65)), "Q-4 · G-01")
mine_rows = [dict(learner_number=l["n"], family_name=l["family_name"], given_names=l["given_names"], date_of_birth=l["date_of_birth"], school=l["school"]) for l in mine]
out("learners.json equals the learners made here", learners == mine_rows, "G-03")
out("enrolments.json, rows", len(enrol), "Q-12 · 68")
out("enrolments.json equals the record made here", [(r["list_entry"], r["learner_number"]) for r in enrol] == my_enrol, "Q-12 · Q-2")
out("reads.json files", [r["file"] for r in reads], "G-10")

print("sha256 of data/:")
for n in sorted(os.listdir(DATA)):
    with open(os.path.join(DATA, n), "rb") as f:
        b = f.read()
    print("  %s %6d %s" % (hashlib.sha256(b).hexdigest(), len(b), n))
