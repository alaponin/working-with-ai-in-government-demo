#!/bin/zsh
# The base instruction's planted fault: F-4 (more than one learner found) saves a record and shows SC-3.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence
SRC=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
d=$E/planted/f4-saves
echo "# r3b started $(date -u +%Y-%m-%dT%H:%M:%SZ)"
rm -rf $d; mkdir -p $d; cp -R $SRC $d/src
perl -0pi -e "s{    return \{ screen: 'SC-5', outcome: 'cannot', failure: 'F-4', entry \};}{    const n = Math.max(...learners.map((l) => l.learner_number)) + 1; learners.push(Object.assign({ learner_number: n }, entry)); store.saveLearners(learners);\n    return { screen: 'SC-3', outcome: 'new', learner: learners[learners.length - 1] };}" $d/src/lib/enrol.js
diff $SRC/lib/enrol.js $d/src/lib/enrol.js
(cd $d/src && node reset.js > /dev/null && node --test test/ > $E/planted_f4-saves.tap 2>&1; echo "EXIT=$?")
grep -E '^not ok|^# (pass|fail)' $E/planted_f4-saves.tap
grep -E -A12 '^not ok' $E/planted_f4-saves.tap | grep -E "error:|expected|actual" | head -6
echo "# r3b ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"
