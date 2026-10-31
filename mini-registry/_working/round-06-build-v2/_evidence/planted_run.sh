#!/bin/zsh
# Runs the checks in each planted copy and prints what failed, by name; the diff of each plant
# against the real src/ first. Full TAP output in planted_<name>.tap.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence
R=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
date -u +%Y-%m-%dT%H:%M:%SZ
for n in search-forgives-spaces sc3-without-line window-added; do
  echo "=== $n: \$ diff -r src planted/$n/src (data/ left out)"
  diff -r -x data $R $E/planted/$n/src
  echo "=== $n: \$ cd planted/$n/src && node reset.js && node --test test/"
  (cd $E/planted/$n/src && node reset.js > /dev/null && node --test test/ > $E/planted_$n.tap 2>&1); echo "EXIT=$?"
  grep -E '^not ok' $E/planted_$n.tap
  grep -E '^ *# (R-20|R-21):' $E/planted_$n.tap
  grep -E "^ *error: '.*planted window" $E/planted_$n.tap | cut -c1-220
  grep -E '^# (pass|fail)' $E/planted_$n.tap
done
date -u +%Y-%m-%dT%H:%M:%SZ
