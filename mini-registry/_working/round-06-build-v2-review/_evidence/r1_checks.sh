#!/bin/zsh
# The reviewer's own run: list of windows before, the project's checks, list of windows after.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence
SRC=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
read_windows() {  # $1 = out file
  local t0=$(perl -MTime::HiRes=time -e 'printf "%.3f", time')
  /usr/bin/osascript -l JavaScript "$E/windows.js" > "$1" 2> "$1.err"
  local rc=$?
  local t1=$(perl -MTime::HiRes=time -e 'printf "%.3f", time')
  echo "reading $(basename $1): exit $rc, $(grep -c . "$1") windows listed, $(wc -c < "$1.err" | tr -d ' ') bytes on the error stream, $(perl -e "printf '%.0f', ($t1-$t0)*1000") ms"
}
echo "# r1_checks.sh started $(date -u +%Y-%m-%dT%H:%M:%SZ) on $(hostname)"
echo "frontmost before: $(lsappinfo info -only name $(lsappinfo front))"
read_windows $E/win.before.tsv
echo "# $(date -u +%H:%M:%SZ) cd src && node reset.js && node --test test/"
cd $SRC && node --version && node reset.js && node --test test/ > $E/R1_checks.tap 2>&1
echo "EXIT=$?"
echo "# $(date -u +%H:%M:%SZ) checks ended"
read_windows $E/win.after.tsv
echo "frontmost after: $(lsappinfo info -only name $(lsappinfo front))"
cut -f1 $E/win.before.tsv | sort > $E/win.before.nums
cut -f1 $E/win.after.tsv | sort > $E/win.after.nums
echo "windows in the after list, not in the before list (by number): $(comm -13 $E/win.before.nums $E/win.after.nums | grep -c .)"
comm -13 $E/win.before.nums $E/win.after.nums | while read n; do grep "^$n	" $E/win.after.tsv; done
echo "windows in the before list, gone from the after list: $(comm -23 $E/win.before.nums $E/win.after.nums | grep -c .)"
echo "windows owned by osascript or node in either list: $(cat $E/win.before.tsv $E/win.after.tsv | awk -F'\t' '$3 ~ /osascript|node/' | grep -c .)"
echo "--- TAP summary and window diagnostics"
grep -E '^# (tests|pass|fail|R-20|R-21)|^(not )?ok .*(R-20|R-21)|^not ok' $E/R1_checks.tap
echo "ok lines: $(grep -c '^ok' $E/R1_checks.tap)"
echo "# r1_checks.sh ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"
