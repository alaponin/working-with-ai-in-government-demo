#!/bin/zsh
# The reviewer's route to the number of settings: a list written by hand from reading the brief's table
# (lines 23-27) and the 13 ruled recommendation lines of the paper (73 ... 424), one phrase per value,
# each phrase checked by grep -F at the one line it cites, then the names set beside settings.csv.
W=/Users/arnelaponin/Documents/Dev/wai-demo
E=$W/mini-registry/_working/round-02-groundwork-v2-review/_evidence
L=$E/F1_reviewer_settings.tsv
date -u +%Y-%m-%dT%H:%M:%SZ
notfound=0
while IFS=$'\t' read -r name src phrase; do
  doc=${src%%:*}; n=${src##*:}
  [[ $doc == B ]] && f=$W/brief/MINI-REGISTRY-BRIEF.md || f=$W/mini-registry/docs/GAPS-PAPER.md
  if sed -n "${n}p" $f | grep -qF -- "$phrase"; then echo "found   $src  $name"; else echo "MISSING $src  $name"; notfound=$((notfound+1)); fi
done < $L
echo "## the ruled lines the list was read from (recommendation lines, by grep):"
grep -n '^\*\*Recommendation' $W/mini-registry/docs/GAPS-PAPER.md | cut -d: -f1 | tr '\n' ' '; echo
echo "reviewer's list: $(wc -l < $L | tr -d ' ') settings; phrases not found at their line: $notfound"
echo "settings.csv: $(tail -n +2 $W/mini-registry/docs/groundwork/settings.csv | wc -l | tr -d ' ') rows"
cut -f1 $L | sort > $E/F1_mine.txt
tail -n +2 $W/mini-registry/docs/groundwork/settings.csv | cut -d, -f1 | sort > $E/F1_csv.txt
echo "missing from settings.csv: $(comm -23 $E/F1_mine.txt $E/F1_csv.txt | wc -l | tr -d ' ') $(comm -23 $E/F1_mine.txt $E/F1_csv.txt | tr '\n' ' ')"
echo "extra in settings.csv: $(comm -13 $E/F1_mine.txt $E/F1_csv.txt | wc -l | tr -d ' ') $(comm -13 $E/F1_mine.txt $E/F1_csv.txt | tr '\n' ' ')"
echo "## gap 14 re-traced: each quotation at its source line"
grep -c 'no two different children share all three fields' <(sed -n 196p $W/mini-registry/docs/GAPS-PAPER.md)
grep -c 'the same family name, given names and date of birth (capitals ignored)' <(sed -n 13p $W/brief/MINI-REGISTRY-BRIEF.md)
grep -c "through the brief's own rule" <(sed -n 133p $W/mini-registry/docs/GAPS-PAPER.md)
echo "## gaps in GROUNDWORK.md: numbered, and those not ending in ?"
grep -c '^[0-9][0-9]*\. \*\*' $W/mini-registry/docs/GROUNDWORK.md
grep '^[0-9][0-9]*\. \*\*' $W/mini-registry/docs/GROUNDWORK.md | grep -vc '?$'
echo "## gap 14's words in any of the three CSVs (an answer would show here)"
grep -il 'capitals ignored\|share' $W/mini-registry/docs/groundwork/*.csv; echo "grep EXIT=$?"
