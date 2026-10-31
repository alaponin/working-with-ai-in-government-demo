#!/bin/zsh
# The four mechanical checks, run directly by the reviewer.
S="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
W=/Users/arnelaponin/Documents/Dev/wai-demo
M=$W/mini-registry
E=$M/_working/round-08-note-v2-review/_evidence
C=$W/_coordination/CONSTANTS.md
REP=$M/_reports/REPORT_NOTE_2026-10-31_v2.md
date -u +%Y-%m-%dT%H:%M:%SZ
echo "# trace over the report"
/usr/bin/python3 -B "$S/trace_check.py" --constants $M/CONSTANTS.md --coordination $C $REP; echo "trace exit $?"
echo "# placement over the instruction under review"
/usr/bin/python3 -B "$S/placement_check.py" --constants $M/CONSTANTS.md $M/_prompts/PROMPT_NOTE_2026-10-31.md; echo "placement exit $?"
echo "# round_record check, with the options check.out prints on # run with:, --out of the reviewer's own"
/usr/bin/python3 -B "$S/round_record.py" check --record $M/_working/round-08-note-v2/_evidence/record --report $REP --tolerance 2 --out $E/record_check.out > $E/record_check.stdout 2>&1; echo "record check exit $?"
grep -E '^## Findings|^## ' $E/record_check.out
sed -n '/^## Findings/,/^## Read/p' $E/record_check.out
echo "# ledger show C-2026-10-31-31"
/usr/bin/python3 -B "$S/ledger.py" show --constants $C --code MR --id C-2026-10-31-31 > $E/ledger_show.out 2>&1; echo "show exit $?"
echo "# ledger check"
/usr/bin/python3 -B "$S/ledger.py" check --constants $C > $E/ledger_check.out 2>&1; echo "check exit $?"
echo "lines naming MR:"; grep -n 'MR' $E/ledger_check.out || echo "(none)"
tail -3 $E/ledger_check.out
date -u +%Y-%m-%dT%H:%M:%SZ
