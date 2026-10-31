#!/bin/zsh
# Stage 1, before anything under src/ is written: node answers, the checks run on src/ as it stands.
cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
date -u +%Y-%m-%dT%H:%M:%SZ
echo '$ node --version'; node --version
echo '$ node reset.js && node --test test/'
node reset.js && node --test test/ > /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A1_stage1.tap 2>&1; X=$?
grep -E '^(not ok|# (tests|pass|fail))' /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A1_stage1.tap
echo "EXIT=$X"
echo '$ ls -R src'; ls -R . | grep -v '^$'
date -u +%Y-%m-%dT%H:%M:%SZ
