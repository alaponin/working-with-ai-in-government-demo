#!/bin/zsh
# The four mechanical checks, run directly by the reviewer (not through round_record.py run).
O="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
C=/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
E=$M/_working/round-06-build-review/_evidence
R=$M/_reports/REPORT_BUILD_2026-10-31.md
echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) trace check over the report"
/usr/bin/python3 "$O/trace_check.py" --constants $M/CONSTANTS.md --coordination $C $R; echo "trace exit $?"
echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) placement check over the instruction under review"
/usr/bin/python3 "$O/placement_check.py" --constants $M/CONSTANTS.md $M/_prompts/PROMPT_BUILD_2026-10-31.md; echo "placement exit $?"
echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) record check, the options check.out prints on '# run with:', the reviewer's own --out"
/usr/bin/python3 -B "$O/round_record.py" check --record $M/_working/round-06-build/_evidence/record --report $R --tolerance 2 --out $E/record_check.out; echo "record check exit $?"
echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) ledger show C-2026-10-31-25"
/usr/bin/python3 "$O/ledger.py" show --constants $C --code MR --id C-2026-10-31-25 > $E/ledger_show.out 2>&1; echo "show exit $?"
grep -E '^[0-9]{8}T|^  (kind|account|written|computer|started_by|verdict|outcome):' $E/ledger_show.out
echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) ledger check"
/usr/bin/python3 "$O/ledger.py" check --constants $C > $E/ledger_check.out 2>&1; echo "check exit $?"
wc -l < $E/ledger_check.out
echo '--- lines naming MR'
grep -n 'MR' $E/ledger_check.out
