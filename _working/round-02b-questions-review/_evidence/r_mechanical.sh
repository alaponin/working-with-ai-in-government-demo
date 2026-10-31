#!/bin/zsh
# The four mechanical checks of the review of C-2026-10-31-11, run directly (not through round_record.py run).
O="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
MR=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
CO=/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
E=$MR/_working/round-02b-questions-review/_evidence
REP=$MR/_reports/REPORT_QUESTIONS_2026-10-31.md
INS=$MR/_prompts/PROMPT_QUESTIONS_2026-10-31.md

{ date -u; echo "\$ trace_check.py --constants $MR/CONSTANTS.md --coordination $CO $REP"
  /usr/bin/python3 "$O/trace_check.py" --constants $MR/CONSTANTS.md --coordination $CO $REP; echo "EXIT=$?"; } > $E/R_trace.out 2>&1
{ date -u; echo "\$ placement_check.py --constants $MR/CONSTANTS.md $INS"
  /usr/bin/python3 "$O/placement_check.py" --constants $MR/CONSTANTS.md $INS; echo "EXIT=$?"; } > $E/R_placement.out 2>&1
{ date -u; echo "\$ round_record.py check --record $MR/_working/round-02b-questions/_evidence/record --report $REP --tolerance 2 --out $E/R_record_check.out"
  /usr/bin/python3 -B "$O/round_record.py" check --record $MR/_working/round-02b-questions/_evidence/record --report $REP --tolerance 2 --out $E/R_record_check.out; echo "EXIT=$?"; } > $E/R_record_check.log 2>&1
{ date -u; echo "\$ ledger.py show --constants $CO --code MR --id C-2026-10-31-11"
  /usr/bin/python3 "$O/ledger.py" show --constants $CO --code MR --id C-2026-10-31-11; echo "EXIT=$?"; } > $E/R_ledger_show.out 2>&1
{ date -u; echo "\$ ledger.py check --constants $CO"
  /usr/bin/python3 "$O/ledger.py" check --constants $CO; echo "EXIT=$?"; } > $E/R_ledger_check.out 2>&1
{ date -u; echo "\$ ls -l and shasum of the outputs the report names"
  ls -l $MR/docs/QUESTIONS-PAPER.md $REP; wc -c $MR/docs/QUESTIONS-PAPER.md; shasum -a 256 $MR/docs/QUESTIONS-PAPER.md
  ls -ld $MR/_working/round-02b-questions/_evidence; ls $MR/_working/round-02b-questions/_evidence | wc -l
  echo "--- sources now"; cd /Users/arnelaponin/Documents/Dev/wai-demo
  shasum -a 256 brief/MINI-REGISTRY-BRIEF.md mini-registry/docs/REQUIREMENTS.md mini-registry/docs/GAPS-PAPER.md mini-registry/docs/GROUNDWORK.md mini-registry/docs/groundwork/*.csv; echo "EXIT=$?"; } > $E/R_outputs.out 2>&1
