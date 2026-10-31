#!/bin/zsh
# r5_counts.sh — times and counts the report gives in its own words, read at their source; the
# outputs at their paths; the sources' sha256 now against the round's start list. Reads only.
R=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
W=$R/_working/round-08-note/_evidence
E=$R/_working/round-08-note-review/_evidence
date -u +%FT%TZ
echo "== stat, UTC (A1 order; window close against the report's last write)"
for f in $W/CLAIMS.md $W/LIMITS.md $R/docs/NOTE.md $W/PAIRS.md $R/_reports/REPORT_NOTE_2026-10-31.md $W/A8_checks.log $W/A9_ledger_show.log $W/record/check.out; do
  TZ=UTC stat -f '%Sm %z %N' -t '%Y-%m-%dT%H:%M:%SZ' "$f"
done
echo "== runs through run (report: 17)"; wc -l < $W/record/runs.jsonl
grep -o '"exit": *[0-9-]*' $W/record/runs.jsonl | sort | uniq -c
echo "== window.out (report: 36 files, close 20:54:58)"; grep -nE 'files|last written|closes|window' $W/record/window.out | head -12
echo "== windows lists (report: 252 before, 252 after)"; for f in $W/win.before.tsv $W/win.after.tsv; do echo "$(($(wc -l < $f))) lines $f"; done; head -1 $W/win.before.tsv
cmp $W/win.before.tsv $W/win.after.tsv && echo "before = after, byte for byte"
echo "== sources at start (report: 15) and src (report: 24)"; wc -l < $W/sources.start.sha256; wc -l < $W/src.start.sha256
echo "== the sources' sha256 now, against the round's start list (A7, by the reviewer)"
/usr/bin/python3 -I - $W/sources.start.sha256 <<'PY'
import hashlib, sys
bad = n = 0
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip():
        continue
    h, p = line.split(None, 1)
    p = p.lstrip("*").strip()
    n += 1
    try:
        now = hashlib.sha256(open(p, "rb").read()).hexdigest()
    except Exception as e:
        print("UNREADABLE", p, e); bad += 1; continue
    ok = now == h
    bad += not ok
    print("same" if ok else "CHANGED", p)
print("sources: %d, changed or unreadable: %d" % (n, bad))
PY
echo "== src/ now against the round's start list"
/usr/bin/python3 -I - $W/src.start.sha256 $R <<'PY'
import hashlib, os, sys
bad = n = 0
root = sys.argv[2]
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip():
        continue
    h, p = line.split(None, 1)
    p = p.lstrip("*").strip()
    q = p if os.path.isabs(p) else os.path.join(root, "src", p)
    if not os.path.exists(q):
        q = os.path.join(root, p)
    n += 1
    try:
        now = hashlib.sha256(open(q, "rb").read()).hexdigest()
    except Exception as e:
        print("UNREADABLE", p, e); bad += 1; continue
    bad += now != h
print("src files: %d, changed or unreadable: %d" % (n, bad))
PY
echo "== A6: the two builds' texts, and the final PDF's text (gs) against build 2's"
cmp $W/text.build1.txt $W/text.build2.txt && echo "build1 text = build2 text"
shasum -a 256 $W/text.build1.txt $W/text.build2.txt
cat $W/info.build1.txt $W/info.build2.txt
/usr/bin/python3 -I - $W/text.build2.txt $E/note_text.gs.txt <<'PY'
import re, sys
w = lambda p: re.findall(r"[A-Za-z0-9']+", open(p, encoding="utf-8", errors="replace").read().replace("’", "'"))
a, b = w(sys.argv[1]), w(sys.argv[2])
print("build2 text words:", len(a), " gs text words:", len(b), " same:", a == b)
PY
grep -nE 'type_pt|EXIT|windows' $W/A6_build_twice.log
echo "== outputs at their paths, size and sha256 against the report's outputs line"
for f in $R/docs/NOTE.md $R/docs/note/build.py $R/docs/note/NOTE.pdf $R/docs/note/NOTE.html $R/docs/note/register_exceptions.txt $R/_reports/REPORT_NOTE_2026-10-31.md; do
  if [ -e "$f" ]; then echo "found $(stat -f %z "$f") $(shasum -a 256 "$f" | cut -c1-64) $f"; else echo "MISSING $f"; fi
done
ls -ld $W && echo "evidence files: $(ls $W | wc -l)"
echo "== the round's A1 log, its last lines"; tail -4 $W/A1_claims.log
echo "== PAIRS rows (report: 34)"; grep -c '^| [0-9]' $W/PAIRS.md
