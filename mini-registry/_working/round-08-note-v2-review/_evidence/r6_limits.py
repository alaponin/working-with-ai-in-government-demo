#!/usr/bin/python3
"""Reviewer's own comparison: the limits listed again (R6_limits_relisted.md) against the record,
the note, the round's LIMITS.md and the report's list of what was left out."""
import re, datetime
R = "/Users/arnelaponin/Documents/Dev/wai-demo"
M = R + "/mini-registry"
E = M + "/_working/round-08-note-v2-review/_evidence"
short = {"brief": "brief/MINI-REGISTRY-BRIEF.md", "req": "mini-registry/docs/REQUIREMENTS.md",
         "gaps": "mini-registry/docs/GAPS-PAPER.md", "qp": "mini-registry/docs/QUESTIONS-PAPER.md",
         "gqp": "mini-registry/docs/GOAL-QUESTIONS-PAPER.md", "goal": "mini-registry/docs/GOAL.md",
         "count": "mini-registry/docs/COUNT.md", "dup": "mini-registry/docs/DUPLICATES.md",
         "build": "mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md",
         "D11": "_coordination/_ledger/20261031T195657Z_MR_ruled_D-2026-10-31-11.yaml"}
print("run at", datetime.datetime.utcnow().isoformat() + "Z")
note = open(M + "/docs/NOTE.md", encoding="utf-8").read().replace("**", "")
note1 = " ".join(note.split())
report = open(M + "/_reports/REPORT_NOTE_2026-10-31_v2.md", encoding="utf-8").read()
# the report's left-out table: the rows between its heading "Left out, with the reason" and the next blank paragraph
lo = report.split("**Left out, with the reason**", 1)[1]
lo_rows = re.findall(r"^\| ([A-Z]\d\d[a-z]?) \|", lo.split("\n\n", 2)[1], re.M)
print("report's left-out table rows:", len(lo_rows), lo_rows)
lim = open(M + "/_working/round-08-note-v2/_evidence/LIMITS.md", encoding="utf-8").read()
round_rows = {}
for ln in lim.split("\n"):
    m = re.match(r"\| ([A-Z]\d\d[a-z]?) \| (.*)", ln)
    if m:
        cells = [c.strip() for c in ln.strip().strip("|").split(" | ")]
        round_rows[cells[0]] = cells
round_limits = [k for k, c in round_rows.items() if len(c) > 4 and c[4] == "yes"]
print("round's LIMITS.md rows: %d; marked a limit: %d" % (len(round_rows), len(round_limits)))
mine = []
for ln in open(E + "/R6_limits_relisted.md", encoding="utf-8"):
    if ln.startswith("| M"):
        mine.append([c.strip() for c in ln.strip().strip("|").split(" | ")])
bad = unacc = innote = leftout = 0
mapped = set()
for row in mine:
    rid, what, src, words, rr, where, target = row
    s, n = src.split(":")
    text = open(R + "/" + short[s], encoding="utf-8").read().split("\n")[int(n) - 1]
    at = words in text
    if not at:
        bad += 1
    for k in re.findall(r"[A-Z]\d\d[a-z]?", rr):
        mapped.add(k)
    if where == "note":
        ok = target in note1
        innote += ok
    else:
        ok = target in lo_rows
        leftout += ok
    if not ok:
        unacc += 1
    print("%s  source %s  %-9s %s  [%s]" % (rid, "found" if at else "NOT FOUND", where, "accounted" if ok else "UNACCOUNTED", rr))
print("== my rows: %d; words not found at source: %d; in the note: %d; left out with the round's reason: %d; unaccounted: %d"
      % (len(mine), bad, innote, leftout, unacc))
print("== round's limits not mapped to a row of mine:", sorted(set(round_limits) - mapped))
print("== my rows with no round row:", [r[0] for r in mine if not re.findall(r"[A-Z]\d\d[a-z]?", r[4].split("(")[0])])
print("== round's left-out limits each with a reason in LIMITS.md:",
      all(round_rows[k][6] == "left out" and len(round_rows[k][7]) > 20 for k in lo_rows if k in round_rows))
