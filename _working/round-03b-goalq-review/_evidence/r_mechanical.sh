#!/bin/zsh
# The four mechanical checks of the review form, part one, section 6, run directly (not through round_record.py run).
S="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq-review/_evidence
MR=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
CO=/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
REP=$MR/_reports/REPORT_GOALQ_2026-10-31.md
INS=$MR/_prompts/PROMPT_GOALQ_2026-10-31.md
W=$MR/_working/round-03b-goalq/_evidence

{ echo "# trace $(date -u +%FT%TZ)"; /usr/bin/python3 "$S/trace_check.py" --constants $MR/CONSTANTS.md --coordination $CO $REP; echo "EXIT=$?"; } > $E/R_trace.out 2>&1
{ echo "# placement $(date -u +%FT%TZ)"; /usr/bin/python3 "$S/placement_check.py" --constants $MR/CONSTANTS.md $INS; echo "EXIT=$?"; } > $E/R_placement.out 2>&1
{ echo "# record check $(date -u +%FT%TZ)"; /usr/bin/python3 -B "$S/round_record.py" check --record $W/record --report $REP --tolerance 2 --out $E/R_record_check.out; echo "EXIT=$?"; } > $E/R_record_check.log 2>&1
{ echo "# ledger show $(date -u +%FT%TZ)"; /usr/bin/python3 "$S/ledger.py" show --constants $CO --code MR --id C-2026-10-31-17; echo "EXIT=$?"; } > $E/R_ledger_show.out 2>&1
{ echo "# ledger check $(date -u +%FT%TZ)"; /usr/bin/python3 "$S/ledger.py" check --constants $CO; echo "EXIT=$?"; } > $E/R_ledger_check.out 2>&1
{ echo "# outputs $(date -u +%FT%TZ)"; ls -ld $MR/docs/GOAL-QUESTIONS-PAPER.md $W $REP; echo "EXIT=$?"; wc -c $MR/docs/GOAL-QUESTIONS-PAPER.md $REP; shasum -a 256 $MR/docs/GOAL-QUESTIONS-PAPER.md; ls $W | wc -l; stat -f '%Sm %N' -t '%FT%T%z' $REP $MR/docs/GOAL-QUESTIONS-PAPER.md; } > $E/R_outputs.out 2>&1
