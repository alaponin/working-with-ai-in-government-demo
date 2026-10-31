#!/bin/zsh
# The reviewer's mechanical checks for REVIEW_GROUNDWORK_2026-10-31_v2.md. Each writes one log beside this file.
O="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
R=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
E=$R/_working/round-02-groundwork-v2-review/_evidence
C=/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
REP=$R/_reports/REPORT_GROUNDWORK_2026-10-31_v2.md
run() { local name=$1; shift; { date -u +%Y-%m-%dT%H:%M:%SZ; echo "\$ $*"; "$@"; echo "EXIT=$?"; } > $E/$name.out 2>&1; }

run M1_trace /usr/bin/python3 "$O/trace_check.py" --constants $R/CONSTANTS.md --coordination $C $REP
run M2_placement /usr/bin/python3 "$O/placement_check.py" --constants $R/CONSTANTS.md $R/_prompts/PROMPT_GROUNDWORK_2026-10-31.md
run M3_record_check /usr/bin/python3 -B "$O/round_record.py" check --record $R/_working/round-02-groundwork-v2/_evidence/record --report $REP --tolerance 2 --out $E/M3_record_check.check.out
run M4_ledger_show /usr/bin/python3 "$O/ledger.py" show --constants $C --code MR --id C-2026-10-31-07
run M5_ledger_check /usr/bin/python3 "$O/ledger.py" check --constants $C

# B6 and the outputs: sources, the four groundwork files, the report
{ date -u +%Y-%m-%dT%H:%M:%SZ
  echo "## sources (B6)"; ( cd /Users/arnelaponin/Documents/Dev/wai-demo && shasum -a 256 brief/MINI-REGISTRY-BRIEF.md mini-registry/docs/REQUIREMENTS.md mini-registry/docs/GAPS-PAPER.md )
  echo "## outputs: size sha256 path"
  for f in $R/docs/GROUNDWORK.md $R/docs/groundwork/settings.csv $R/docs/groundwork/lists.csv $R/docs/groundwork/search_rule.csv $REP $R/_working/round-02-groundwork-v2/_evidence/GROUNDWORK_v1.md; do
    echo "$(stat -f %z $f) $(shasum -a 256 $f | cut -d' ' -f1) $f"; done
  ls -ld $R/_working/round-02-groundwork-v2/_evidence; echo "evidence entries: $(ls $R/_working/round-02-groundwork-v2/_evidence | wc -l | tr -d ' ')"
  echo "## B1: the first review's recorded checksums (R2_outputs.out of round-02-groundwork-review) against now"
  for f in docs/GROUNDWORK.md docs/groundwork/settings.csv docs/groundwork/lists.csv docs/groundwork/search_rule.csv; do
    old=$(grep " $R/$f\$" $R/_working/round-02-groundwork-review/_evidence/R2_outputs.out | head -1 | cut -d" " -f2)
    new=$(shasum -a 256 $R/$f | cut -d' ' -f1)
    [[ "$old" == "$new" ]] && echo "same     $f ${new:0:8} (full 64 characters equal)" || echo "CHANGED  $f  ${old:0:8} -> ${new:0:8}"; done
  echo "## B1: diff of GROUNDWORK_v1.md (the round's copy; its checksum above) against docs/GROUNDWORK.md now"
  diff $R/_working/round-02-groundwork-v2/_evidence/GROUNDWORK_v1.md $R/docs/GROUNDWORK.md; echo "diff EXIT=$?"
  echo "## times UTC birth / modified"
  for f in $REP $R/docs/GROUNDWORK.md $R/_working/round-02-groundwork-v2/_evidence/record/check.out; do
    echo "$(TZ=UTC stat -f '%SB / %Sm' -t %H:%M:%S $f) $f"; done
} > $E/R2_outputs.out 2>&1

# B3: the round's checks of A2, A3, A4 re-run by the reviewer (outside any record), compared with version 1's logs
{ date -u +%Y-%m-%dT%H:%M:%SZ
  cd $R/_working/round-02-groundwork/_evidence
  for a in a2 a3 a4; do
    /usr/bin/python3 check_groundwork.py $a > $E/B3_$a.out 2>&1; echo "check_groundwork.py $a EXIT=$?"
    A=${a:u}; diff <(tail -n +3 $R/_working/round-02-groundwork/_evidence/${A}_check.out | grep -v '^EXIT=') $E/B3_$a.out; echo "diff against v1 ${A}_check.out EXIT=$?"
  done
} > $E/B3_rerun.out 2>&1
