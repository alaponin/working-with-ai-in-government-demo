#!/bin/zsh
# The reviewer's planted faults, each in its own scratch copy of src/ (cp -R, file times not kept).
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence
SRC=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
P=$E/planted
mkdir -p $P
echo "# r3_planted.sh started $(date -u +%Y-%m-%dT%H:%M:%SZ)"
plant() {  # $1 name, $2 file, $3 perl substitution
  local d=$P/$1
  rm -rf $d; mkdir -p $d; cp -R $SRC $d/src
  perl -0pi -e "$3" $d/src/$2
  echo; echo "=== plant $1: $2"
  echo "copied with times not kept: src/server.js mtime $(stat -f %Sm -t %Y-%m-%dT%H:%M:%S $d/src/server.js) (real $(stat -f %Sm -t %Y-%m-%dT%H:%M:%S $SRC/server.js))"
  diff $SRC/$2 $d/src/$2
  (cd $d/src && node reset.js > /dev/null && node --test test/ > $E/planted_$1.tap 2>&1; echo "EXIT=$?")
  grep -E '^not ok|^# (pass|fail)|^# R-2[01]' $E/planted_$1.tap
  grep -E -A3 '^not ok' $E/planted_$1.tap | grep -E "error: |windows? (added|[0-9]+ of)|could not be read" | head -6
}
# (a) R-20's "after" list gets one window more.
plant r20-after-window test/requirements.test.js 's/(  const after = await readWindows\(\);\n)/$1  after.set("999999", { pid: 1, owner: "planted window" });\n/'
# (b) R-21's "when they ended" list, in goal.test.js, gets one window more.
plant r21-end-window test/goal.test.js 's/(  const end = await readWindows\(\);\n)/$1  end.set("999998", { pid: 1, owner: "planted window" });\n/'
# (c) the list cannot be read: the program is not there. The check must fail, not pass.
plant list-unreadable test/requirements.test.js "s{'/usr/bin/osascript', \[}{'/usr/bin/osascript-absent', [}"
# (d) the base instruction's plant: F-4 (more than one learner found) saves a record.
echo; echo "=== F-4 in enrol.js, as it stands:"; grep -n -i -E 'F-4|more than one|length > 1|matches.length' $SRC/lib/enrol.js | head -10
echo "# r3_planted.sh ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"
