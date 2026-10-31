#!/bin/zsh
# Outputs at their paths and sizes; sources unchanged; the times the report gives in words.
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
V=$M/_working/round-08-note-v2/_evidence
date -u +%Y-%m-%dT%H:%M:%SZ
echo "# outputs: size and sha256 against the report's outputs line"
for f in $M/docs/NOTE.md $M/docs/note/build.py $M/docs/note/NOTE.pdf $M/docs/note/NOTE.html $M/docs/note/register_exceptions.txt $M/_reports/REPORT_NOTE_2026-10-31_v2.md; do
  if [ -f "$f" ]; then echo "found $(stat -f '%z' "$f") $(shasum -a 256 "$f" | cut -c1-16) $(TZ=UTC stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%SZ' "$f") $f"; else echo "MISSING $f"; fi
done
echo "evidence folder: $(ls -1 $V | wc -l | tr -d ' ') entries; record folder: $(ls -1 $V/record | wc -l | tr -d ' ') entries"
echo "# A7: the round's start checksums of the sources, checked now (first line a stamp)"
tail -n +2 $V/sources.start.sha256 | grep -v '^#' > /tmp/rv_sources.sha256 2>/dev/null || true
head -2 $V/sources.start.sha256
grep -E '^[0-9a-f]{64}  ' $V/sources.start.sha256 | shasum -a 256 -c - 2>&1 | tail -25; echo "SOURCES SHASUM -c EXIT=${pipestatus[2]}"
echo "sources listed: $(grep -cE '^[0-9a-f]{64}  ' $V/sources.start.sha256)"
echo "# src/ against the round's start list"
grep -E '^[0-9a-f]{64}  ' $V/src.start.sha256 | shasum -a 256 -c - 2>&1 | grep -v ': OK$'; echo "src files: $(grep -cE '^[0-9a-f]{64}  ' $V/src.start.sha256), not OK lines above (none = all OK)"
echo "# A6: the two builds' texts, and the windows"
cmp $V/text.build1.txt $V/text.build2.txt && echo "text.build1 = text.build2 (cmp exit 0)"
shasum -a 256 $V/text.build1.txt $V/text.build2.txt $V/html.build1.html $V/html.build2.html $M/docs/note/NOTE.html | cut -c1-16,65-
cmp $V/win.before.tsv $V/win.after.tsv && echo "win.before = win.after (cmp exit 0)"; echo "windows listed before: $(grep -c . $V/win.before.tsv) after: $(grep -c . $V/win.after.tsv)"
grep -E 'EXIT|windows|smallest|largest|used' $V/A6_build_twice.log
echo "# the report's window line against the report's mtime and window.out"
TZ=UTC stat -f 'report mtime %Sm' -t '%Y-%m-%dT%H:%M:%S' $M/_reports/REPORT_NOTE_2026-10-31_v2.md
grep -n -E 'closes|last written|files the round names' $V/record/window.out | head -5
echo "# A8, A9 logs: their results"
grep -E 'exit|clean' $V/A8_checks.log
grep -E '^[0-9]{8}T.*C-2026-10-31-31' $V/A9_ledger_show.log
