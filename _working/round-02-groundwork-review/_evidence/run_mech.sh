#!/bin/zsh
# The four mechanical checks of the review, each command, its exit code and output to its own log.
O="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator"
MR=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
CO=/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
E=$MR/_working/round-02-groundwork-review/_evidence
REP=$MR/_reports/REPORT_GROUNDWORK_2026-10-31.md
run() { local log=$1; shift; { echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "# command: $*"; "$@" 2>&1; echo "EXIT=$?"; } > "$E/$log"; tail -n 3 "$E/$log"; }
run M1_trace.out /usr/bin/python3 "$O/scripts/trace_check.py" --constants $MR/CONSTANTS.md --coordination $CO $REP
run M2_placement.out /usr/bin/python3 "$O/scripts/placement_check.py" --constants $MR/CONSTANTS.md $MR/_prompts/PROMPT_GROUNDWORK_2026-10-31.md
run M3_record_check.out /usr/bin/python3 -B "$O/scripts/round_record.py" check --record $MR/_working/round-02-groundwork/_evidence/record --report $REP --tolerance 2 --out $E/M3_record_check.check.out
run M4_ledger_show.out /usr/bin/python3 "$O/scripts/ledger.py" show --constants $CO --code MR --id C-2026-10-31-07
run M5_ledger_check.out /usr/bin/python3 "$O/scripts/ledger.py" check --constants $CO
