#!/usr/bin/env python3
"""Round 7, the duplicates count.

Stage 2  --stage set    : from the key table, every child (same_child) named on
                          two or more list entries (list_entry), with its entries,
                          and their count. Written before anything else is counted.
Stage 3  --stage count  : for each child of the set, the learner number each of
                          its entries made or found, read from the reset's record
                          (enrolments.json, ruling Q-12). Caught: every entry of
                          the child points to one learner. Missed: two or more.
                          Then, read from the list files themselves, which of the
                          three compared fields (capitals ignored) differ between
                          its entries, both values quoted.

Reads only the files named on its command line; writes only --out / --csv.
"""
import argparse
import csv
import json
import os
import sys
from collections import OrderedDict

COMPARED = ("family_name", "given_names", "date_of_birth")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def the_set(key_table_path):
    rows = load(key_table_path)
    by_child = OrderedDict()
    for r in rows:
        by_child.setdefault(r["same_child"], []).append(r["list_entry"])
    chosen = OrderedDict(
        (c, e) for c, e in sorted(by_child.items()) if len(e) >= 2
    )
    return len(rows), len(by_child), chosen


def entry_record(data_dir, list_entry, cache):
    lst, n = list_entry.rsplit(":", 1)
    if lst not in cache:
        cache[lst] = {r["entry"]: r for r in load(os.path.join(data_dir, lst + ".json"))}
    return cache[lst][int(n)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=("set", "count"), required=True)
    ap.add_argument("--key-table", required=True)
    ap.add_argument("--enrolments")
    ap.add_argument("--data-dir", help="folder of the three list files")
    ap.add_argument("--out", help="the set's list (stage set)")
    ap.add_argument("--csv", help="duplicates.csv (stage count)")
    a = ap.parse_args()

    n_rows, n_children, chosen = the_set(a.key_table)

    if a.stage == "set":
        lines = [
            "key_table: %s" % a.key_table,
            "key table rows: %d; children named: %d" % (n_rows, n_children),
            "children named on two or more entries:",
        ]
        for c, es in chosen.items():
            lines.append("  %s  %d entries  %s" % (c, len(es), " · ".join(es)))
        lines.append("count of the set: %d" % len(chosen))
        text = "\n".join(lines) + "\n"
        sys.stdout.write(text)
        if a.out:
            with open(a.out, "w", encoding="utf-8") as f:
                f.write(text)
        return 0

    enrol = load(a.enrolments)
    by_entry = {}
    for r in enrol:
        by_entry.setdefault(r["list_entry"], []).append(r["learner_number"])
    cache = {}
    out_rows = []
    caught = 0
    print("enrolments: %s (%d rows)" % (a.enrolments, len(enrol)))
    for c, es in chosen.items():
        nums = []
        for e in es:
            got = by_entry.get(e, [])
            if len(got) != 1:
                print("ANOMALY: %s has %d enrolment rows: %r" % (e, len(got), got))
            nums.append(got[0] if got else None)
        is_caught = len(set(nums)) == 1 and nums[0] is not None
        caught += is_caught
        recs = [entry_record(a.data_dir, e, cache) for e in es]
        diffs = []
        for fld in COMPARED:
            vals = [r[fld] for r in recs]
            if len({str(v).lower() for v in vals}) > 1:
                diffs.append(
                    "%s: %s" % (fld, " vs ".join('"%s" (%s)' % (v, e) for v, e in zip(vals, es)))
                )
        row = OrderedDict(
            child=c,
            entries=" · ".join(es),
            learner_numbers=" · ".join(str(n) for n in nums),
            caught="yes" if is_caught else "no",
            fields_differing="; ".join(diffs) if diffs else "none",
        )
        out_rows.append(row)
        print("%s | %s | %s | caught=%s | %s" % tuple(row.values()))
    print("the search catches %d of the %d" % (caught, len(chosen)))
    if a.csv:
        with open(a.csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()), lineterminator="\n")
            w.writeheader()
            w.writerows(out_rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
