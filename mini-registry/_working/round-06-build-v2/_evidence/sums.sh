#!/bin/zsh
# sums.sh <start|end> — the sha256 of every source and of every file under src/ (data/ apart),
# into sources.<when>.sha256 and src.<when>.sha256 beside this script; data/ into data.<when>.sha256.
W=$1
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
cd $M
{ date -u +%Y-%m-%dT%H:%M:%SZ
  shasum -a 256 ../brief/MINI-REGISTRY-BRIEF.md docs/REQUIREMENTS.md docs/groundwork/* docs/GAPS-PAPER.md \
    docs/QUESTIONS-PAPER.md docs/GOAL.md docs/GOAL-QUESTIONS-PAPER.md docs/COUNT.md docs/count/count.csv \
    _kinds/building.md CONSTANTS.md _prompts/PROMPT_BUILD_2026-10-31.md _reviews/REVIEW_BUILD_2026-10-31.md
} > $E/sources.$W.sha256
cd $M/src
{ date -u +%Y-%m-%dT%H:%M:%SZ
  find . -type f -not -path './data/*' -not -name .DS_Store | LC_ALL=C sort | xargs shasum -a 256
} > $E/src.$W.sha256
{ date -u +%Y-%m-%dT%H:%M:%SZ
  find ./data -type f | LC_ALL=C sort | xargs shasum -a 256
} > $E/data.$W.sha256
wc -l $E/sources.$W.sha256 $E/src.$W.sha256 $E/data.$W.sha256
