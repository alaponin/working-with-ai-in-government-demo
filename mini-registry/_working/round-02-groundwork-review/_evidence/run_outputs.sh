#!/bin/zsh
# Outputs at their paths and sizes; sources' checksums; times of the key writes (birth and modification, UTC); the gaps section.
MR=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
cd /Users/arnelaponin/Documents/Dev/wai-demo
echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "## outputs: size sha256 path"
for f in $MR/docs/GROUNDWORK.md $MR/docs/groundwork/settings.csv $MR/docs/groundwork/lists.csv $MR/docs/groundwork/search_rule.csv $MR/_reports/REPORT_GROUNDWORK_2026-10-31.md; do
  print -r -- "$(stat -f %z $f) $(shasum -a 256 $f | cut -c1-64) $f"; done
ls -ld $MR/_working/round-02-groundwork/_evidence; echo "evidence files: $(ls $MR/_working/round-02-groundwork/_evidence | wc -l | tr -d ' ')"
echo "## sources (A6)"
shasum -a 256 brief/MINI-REGISTRY-BRIEF.md mini-registry/docs/REQUIREMENTS.md mini-registry/docs/GAPS-PAPER.md
echo "## times, UTC: birth / last modified"
for f in $MR/_working/round-02-groundwork/_evidence/SETTINGS_SET.md $MR/docs/groundwork/settings.csv $MR/docs/groundwork/lists.csv $MR/docs/groundwork/search_rule.csv $MR/docs/GROUNDWORK.md $MR/_reports/REPORT_GROUNDWORK_2026-10-31.md $MR/_working/round-02-groundwork/_evidence/record/check.out; do
  print -r -- "$(TZ=UTC stat -f '%SB / %Sm' -t '%H:%M:%S' $f) $f"; done
echo "## the gaps section (A5): numbered lines, and those not ending in a question mark"
sed -n '/^## Gaps against the sources/,$p' $MR/docs/GROUNDWORK.md | grep -c -E '^[0-9]+\. '
sed -n '/^## Gaps against the sources/,$p' $MR/docs/GROUNDWORK.md | grep -E '^[0-9]+\. ' | grep -v -E '\?$' | wc -l | tr -d ' '
echo "## the search rule's parts (A3)"
cut -d, -f1 $MR/docs/groundwork/search_rule.csv | sort | uniq -c
grep -n -E '^compares|^forgives|^does_not' $MR/docs/groundwork/search_rule.csv
