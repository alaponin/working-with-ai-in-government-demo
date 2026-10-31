#!/bin/zsh
# r4_mech.sh — the four mechanical checks, run directly by the reviewer (not through round_record.py run).
O="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator"
R=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
C=/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
E=$R/_working/round-08-note-review/_evidence
REPORT=$R/_reports/REPORT_NOTE_2026-10-31.md
INSTR=$R/_prompts/PROMPT_NOTE_2026-10-31.md
REC=$R/_working/round-08-note/_evidence/record
date -u +%FT%TZ
echo '$ trace_check.py'
/usr/bin/python3 "$O/scripts/trace_check.py" --constants $R/CONSTANTS.md --coordination $C $REPORT; echo "trace exit $?"
date -u +%FT%TZ
echo '$ placement_check.py'
/usr/bin/python3 "$O/scripts/placement_check.py" --constants $R/CONSTANTS.md $INSTR; echo "placement exit $?"
date -u +%FT%TZ
echo '$ round_record.py check (the options check.out prints on # run with:, --out the reviewer own)'
/usr/bin/python3 -B "$O/scripts/round_record.py" check --record $REC --report $REPORT --tolerance 2 --out $E/record_check.out; echo "record check exit $?"
date -u +%FT%TZ
echo '$ ledger.py show C-2026-10-31-31'
/usr/bin/python3 "$O/scripts/ledger.py" show --constants $C --code MR --id C-2026-10-31-31 > $E/ledger_show.out 2>&1; echo "show exit $?"
grep -nE '^2026|kind:|account:|started_by:|effort:|written:' $E/ledger_show.out
date -u +%FT%TZ
echo '$ ledger.py check'
/usr/bin/python3 "$O/scripts/ledger.py" check --constants $C > $E/ledger_check.out 2>&1; echo "check exit $?"
echo "-- lines of ledger check naming MR:"
grep -n 'MR' $E/ledger_check.out || echo "(none)"
echo "-- last lines of ledger check:"
tail -5 $E/ledger_check.out
