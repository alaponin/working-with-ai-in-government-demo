#!/bin/zsh
# Figures re-established by the reviewer's own routes.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence
MR=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
V2=$MR/_working/round-06-build-v2/_evidence
SRC=$MR/src
echo "# r5_figures.sh started $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "=== A13: src/ now (reviewer's sha256, data/ apart) against version 1's checksums (src.v1.sha256)"
grep -v '^20' $E/src.start.sha256 > $E/src.now.nostamp
diff $V2/src.v1.sha256 $E/src.now.nostamp; echo "diff exit $?"
echo "=== A13: version 1's checksums of the six files it wrote, as the first review's R7_outputs.log quoted them"
grep -E 'src/(server|lib/enrol|lib/screens|test/goal|test/requirements|package)' $MR/_working/round-06-build-review/_evidence/R7_outputs.log
echo "=== A13: round 5's files against the first review's src.start.sha256"
diff <(grep -v -E 'goal.test|requirements.test' $MR/_working/round-06-build-review/_evidence/src.start.sha256 | grep -v '^20') <(grep -v -E 'goal.test|requirements.test' $E/src.now.nostamp); echo "diff exit $?"
echo "=== data/ now against the round's data.end.sha256"
diff <(grep -v '^20' $V2/data.end.sha256 | awk '{print $1}') <(grep -v '^20' $E/data.start.sha256 | awk '{print $1}'); echo "diff exit $?"
echo "=== 57 checks: test( calls per file"
for f in $SRC/test/*.test.js; do echo "$(basename $f) $(grep -cE '^test\(' $f)"; done
echo "total $(cat $SRC/test/*.test.js | grep -cE '^test\(')"
echo "=== A3: each of the 13 paired requirements and F-1..F-7 among the names of ok lines in the reviewer's own TAP"
miss=0
for k in R-01 R-02 R-03 R-04 R-05 R-06 R-07 R-14 R-15 R-17 R-18 R-20 R-22 F-1 F-2 F-3 F-4 F-5 F-6 F-7; do
  n=$(grep -cE "^ok [0-9]+ - $k " $E/R1_checks.tap); echo "$k $n"; [ $n -eq 0 ] && miss=$((miss+1))
done
echo "requirements paired with a goal element in count.csv: $(awk -F, 'NR>1 && $2!="none"{print $1}' $MR/docs/count/count.csv | sort -u | tr '\n' ' ')"
echo "without a check: $miss"
echo "=== A6: program launches, connections and osascript under src/ (data/ apart)"
grep -rn -E "listen\(|fetch\(|http\.request|https|require\('node:net'\)|dgram|child_process|open\(|osascript|execFile" $SRC --include=*.js | grep -v '/data/' | sed "s#$SRC/##"
echo "dependencies in package.json: $(grep -c dependencies $SRC/package.json)"
echo "=== times read at their source (UTC)"
for f in $MR/_reports/REPORT_BUILD_2026-10-31_v2.md $SRC/test/goal.test.js $SRC/test/requirements.test.js $V2/A1_stage1.log $V2/A2_tests.log $V2/W0_probe.log $V2/A8_checks.log; do
  echo "$(TZ=UTC stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%SZ' $f) $(stat -f %z $f) $(basename $f)"; done
echo "A1_stage1.log stamps:"; grep -E '^#|20[0-9]{2}-' $V2/A1_stage1.log | head -5
echo "RECORD.txt first write under src/:"; grep -n -E 'src/test/(goal|requirements)' $V2/record/RECORD.txt | head -4
grep -n -E 'closes|last written' $V2/record/window.out | head -4
echo "=== the report's outputs line against the files"
for f in $SRC/test/goal.test.js $SRC/test/requirements.test.js; do echo "$(stat -f %z $f) $(shasum -a 256 $f | cut -d' ' -f1) $(basename $f)"; done
echo "evidence files cited by the report found:"
for f in A1_stage1.log A2_tests.log A2_tests_first.log A3_A5_A6_A7_A13.log A4_A12_planted.log A4_A12_planted_first.log A8_checks.log A10_ledger.log W0_probe.log outputs.log src.v1.sha256 src.start.sha256 src.end.sha256 record/check.out record/window.out record/RECORD.txt record/opened.jsonl; do [ -f $V2/$f ] && echo "found $f $(stat -f %z $V2/$f)" || echo "MISSING $f"; done
echo "=== A8 and A10 logs, exits"
grep -n -E 'exit|clean' $V2/A8_checks.log | head
grep -c -E '_MR_(issued|started|finished)_C-2026-10-31-25' $V2/A10_ledger.log
echo "=== the ledger's report paths: ~/IdeaProjects/mini-registry"
ls -ld ~/IdeaProjects/mini-registry 2>&1
echo "# r5_figures.sh ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"
