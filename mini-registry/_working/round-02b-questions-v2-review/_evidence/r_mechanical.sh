#!/bin/zsh
# The reviewer's mechanical checks and outputs listing (C-2026-10-31-12 v2), run directly, outside round_record.py run.
O="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2-review/_evidence
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
W=$M/_working/round-02b-questions-v2/_evidence
REP=$M/_reports/REPORT_QUESTIONS_2026-10-31_v2.md
C=/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
{ date -u +%Y-%m-%dT%H:%M:%SZ; /usr/bin/python3 "$O/trace_check.py" --constants $M/CONSTANTS.md --coordination $C $REP; echo EXIT=$?; } > $E/R_trace.out 2>&1
{ date -u +%Y-%m-%dT%H:%M:%SZ; /usr/bin/python3 "$O/placement_check.py" --constants $M/CONSTANTS.md $M/_prompts/PROMPT_QUESTIONS_2026-10-31.md; echo EXIT=$?; } > $E/R_placement.out 2>&1
{ date -u +%Y-%m-%dT%H:%M:%SZ; /usr/bin/python3 -B "$O/round_record.py" check --record $W/record --report $REP --tolerance 2 --out $E/R_record_check.out; echo EXIT=$?; } > $E/R_record_check.log 2>&1
{ date -u +%Y-%m-%dT%H:%M:%SZ; /usr/bin/python3 "$O/ledger.py" show --constants $C --code MR --id C-2026-10-31-11; echo EXIT=$?; } > $E/R_ledger_show.out 2>&1
{ date -u +%Y-%m-%dT%H:%M:%SZ; /usr/bin/python3 "$O/ledger.py" check --constants $C; echo EXIT=$?; } > $E/R_ledger_check.out 2>&1
{ date -u +%Y-%m-%dT%H:%M:%SZ; cd /Users/arnelaponin/Documents/Dev/wai-demo
  ls -l $M/docs/QUESTIONS-PAPER.md $REP; wc -c $M/docs/QUESTIONS-PAPER.md; shasum -a 256 $M/docs/QUESTIONS-PAPER.md
  ls $W | wc -l; ls -ld $W $W/record
  shasum -a 256 brief/MINI-REGISTRY-BRIEF.md mini-registry/docs/REQUIREMENTS.md mini-registry/docs/GAPS-PAPER.md mini-registry/docs/GROUNDWORK.md mini-registry/docs/groundwork/*.csv
  echo "-- the round's before.sha256 against now:"; diff <(cd /Users/arnelaponin/Documents/Dev/wai-demo; shasum -a 256 brief/MINI-REGISTRY-BRIEF.md mini-registry/docs/REQUIREMENTS.md mini-registry/docs/GAPS-PAPER.md mini-registry/docs/GROUNDWORK.md mini-registry/docs/groundwork/*.csv) $W/before.sha256 && echo "diff empty"
  echo EXIT=$?; } > $E/R_outputs.out 2>&1
cat $E/R_trace.out $E/R_placement.out $E/R_record_check.log $E/R_ledger_show.out $E/R_ledger_check.out $E/R_outputs.out
