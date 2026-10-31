#!/bin/zsh
# A2 and A11: every check of src/, the window checks of R-20 and R-21 among them, from a fresh reset.
# The full TAP output is kept in A2_tests.tap; the lines on which A2 and A11 turn are printed here.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence
cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
date -u +%Y-%m-%dT%H:%M:%SZ
echo '$ cd src && node reset.js && node --test test/'
node reset.js > /dev/null && node --test test/ > $E/A2_tests.tap 2>&1; X=$?
grep -E '^(ok|not ok) [0-9]+ - (R-20|R-21)' $E/A2_tests.tap
grep -E '^ *# (R-20|R-21):' $E/A2_tests.tap
grep -E '^not ok' $E/A2_tests.tap
grep -E '^# (tests|pass|fail)' $E/A2_tests.tap
echo "EXIT=$X"
date -u +%Y-%m-%dT%H:%M:%SZ
