#!/bin/zsh
# A3, A5, A6, A7, A13 of version 2, after the last write under src/.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence
V1=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
date -u +%Y-%m-%dT%H:%M:%SZ
zsh $E/sums.sh end > /dev/null

echo '=== A3: $ /usr/bin/python3 a3_checks.py docs/count/count.csv A2_tests.tap (the program of version 1, unchanged, copied here)'
/usr/bin/python3 $E/a3_checks.py $M/docs/count/count.csv $E/A2_tests.tap; echo "EXIT=$?"

echo '=== A5: round 5 files and version 1 files, start of this round against its end: $ diff src.start.sha256 src.end.sha256'
diff <(tail -n +2 $E/src.start.sha256) <(tail -n +2 $E/src.end.sha256) | sed -E 's/^([<>]) ([0-9a-f]{12})[0-9a-f]+/\1 \2…/'
echo "files under src/ (data/ apart): $(tail -n +2 $E/src.end.sha256 | wc -l | tr -d ' '); changed in this round: $(diff <(tail -n +2 $E/src.start.sha256) <(tail -n +2 $E/src.end.sha256) | grep -c '^>')"
echo '$ diff data.start.sha256 data.end.sha256'; diff <(tail -n +2 $E/data.start.sha256) <(tail -n +2 $E/data.end.sha256) && echo "data/: $(tail -n +2 $E/data.end.sha256 | wc -l | tr -d ' ') files, unchanged"

echo '=== A13: src/ against version 1: round 5 files of version 1 (src.end.sha256 of version 1) and the six files of version 1 report outputs line'
{ tail -n +2 $V1/src.end.sha256 | grep -v ' ./data/' | grep -v -E ' \./(server\.js|lib/enrol\.js|lib/screens\.js|test/goal\.test\.js|test/requirements\.test\.js|package\.json)$'
  sed -n 's/^outputs: //p' $M/_reports/REPORT_BUILD_2026-10-31.md | tr '·' '\n' | sed -nE 's#^ */Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/([^ ]+) [0-9]+ bytes sha256 ([0-9a-f]{64}).*#\2  ./\1#p'
} | LC_ALL=C sort -k2 > $E/src.v1.sha256
echo "version 1 files listed: $(wc -l < $E/src.v1.sha256 | tr -d ' ')"
diff <(LC_ALL=C sort -k2 $E/src.v1.sha256) <(tail -n +2 $E/src.end.sha256 | LC_ALL=C sort -k2) | sed -E 's/^([<>]) ([0-9a-f]{12})[0-9a-f]+/\1 \2…/'
echo "changed against version 1: $(diff <(LC_ALL=C sort -k2 $E/src.v1.sha256) <(tail -n +2 $E/src.end.sha256 | LC_ALL=C sort -k2) | grep '^>' | awk '{print $3}' | tr '\n' ' ')"

echo '=== A6: $ grep -rnE "listen|fetch|http\.request|https|[^a-z_]net[^a-z_]|dgram|child_process|execFile|osascript|open\(" over src/ (data/ left out)'
cd $M/src
grep -rnE 'listen|fetch|http\.request|https|[^a-z_]net[^a-z_]|dgram|child_process|execFile|osascript|open\(' '--include=*.js' '--include=*.json' --exclude-dir=data . | cut -c1-200
echo '$ grep -c dependencies package.json'; grep -c dependencies package.json

echo '=== A7: $ diff sources.start.sha256 sources.end.sha256'
diff <(tail -n +2 $E/sources.start.sha256) <(tail -n +2 $E/sources.end.sha256) && echo "sources: $(tail -n +2 $E/sources.end.sha256 | wc -l | tr -d ' ') of $(tail -n +2 $E/sources.start.sha256 | wc -l | tr -d ' ') unchanged"
date -u +%Y-%m-%dT%H:%M:%SZ
