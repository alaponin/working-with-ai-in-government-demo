"""Second route for the duplicates count (review C-2026-10-31-30).

Reads ONLY the three list files and key_table.json; never enrolments.json, never search.js.
Applies the rule of docs/groundwork/search_rule.csv by itself: family name, given names and date
of birth equal, capitals ignored, nothing else forgiven (no trimming, no accents, no spaces).
"""
import json, sys, os, collections, datetime

D = sys.argv[1]
LISTS = ["school_census", "exam_candidate_list", "social_grant_list"]
FIELDS = ["family_name", "given_names", "date_of_birth"]

print("route2 run", datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))

entries = {}
for name in LISTS:
    rows = json.load(open(os.path.join(D, name + ".json"), encoding="utf-8"))
    for r in rows:
        key = "%s:%s" % (name, r["entry"])
        if key in entries:
            print("ANOMALY duplicate entry id", key)
        entries[key] = r
    print("list %-20s %d entries" % (name, len(rows)))
print("entries in the three lists:", len(entries))

kt = json.load(open(os.path.join(D, "key_table.json"), encoding="utf-8"))
by_child = collections.defaultdict(list)
for row in kt:
    by_child[row["same_child"]].append(row["list_entry"])
missing = [r["list_entry"] for r in kt if r["list_entry"] not in entries]
unkeyed = sorted(set(entries) - set(r["list_entry"] for r in kt))
print("key table rows: %d; children named: %d; entries not in a list: %s; list entries not in key table: %s"
      % (len(kt), len(by_child), missing or "-", unkeyed or "-"))

def k(r):
    # the rule: capitals ignored, nothing else forgiven
    return tuple(r[f].lower() for f in FIELDS)

multi = sorted(c for c, es in by_child.items() if len(es) >= 2)
print("children on two or more entries: %d -> %s" % (len(multi), " ".join(multi)))

# collisions: different children whose entries share the rule's key (would distort a join)
key_children = collections.defaultdict(set)
for row in kt:
    key_children[k(entries[row["list_entry"]])].add(row["same_child"])
coll = {kk: v for kk, v in key_children.items() if len(v) > 1}
print("rule keys shared by two or more different children: %d %s" % (len(coll), sorted(map(sorted, coll.values())) or ""))

joined = 0
print()
print("child | entries | joined by the rule | fields differing (both values)")
for c in multi:
    es = by_child[c]
    rs = [entries[e] for e in es]
    keys = {k(r) for r in rs}
    j = len(keys) == 1
    joined += j
    diffs = []
    for f in FIELDS:
        vals = [r[f] for r in rs]
        if len({v.lower() for v in vals}) > 1:
            diffs.append('%s: %s' % (f, " vs ".join('"%s" (%s)' % (v, e) for v, e in zip(vals, es))))
        elif len(set(vals)) > 1:
            diffs.append('%s equal only with capitals ignored: %s' % (f, " vs ".join('"%s"' % v for v in vals)))
    print("%s | %s | %s | %s" % (c, " · ".join(es), "yes" if j else "no", "; ".join(diffs) or "none"))
print()
print("the rule joins %d of the %d" % (joined, len(multi)))
