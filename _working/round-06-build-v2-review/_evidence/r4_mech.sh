#!/bin/zsh
# The four mechanical checks, run directly by the reviewer (not through round_record.py run).
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence
S="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
MR=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
CO=/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
REP=$MR/_reports/REPORT_BUILD_2026-10-31_v2.md
INS=$MR/_prompts/PROMPT_BUILD_2026-10-31.md
REC=$MR/_working/round-06-build-v2/_evidence/record
echo "# r4_mech.sh started $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "=== trace"
/usr/bin/python3 "$S/trace_check.py" --constants $MR/CONSTANTS.md --coordination $CO $REP; echo "trace exit $?"
echo "=== placement"
/usr/bin/python3 "$S/placement_check.py" --constants $MR/CONSTANTS.md $INS; echo "placement exit $?"
echo "=== record check (options of check.out's '# run with:', own --out)"
grep '^# run with:' $REC/check.out
/usr/bin/python3 -B "$S/round_record.py" check --record $REC --report $REP --tolerance 2 --out $E/record_check.out; echo "record check exit $?"
echo "=== ledger show"
/usr/bin/python3 "$S/ledger.py" show --constants $CO --code MR --id C-2026-10-31-25 > $E/ledger_show.out 2>&1; echo "show exit $?"
echo "=== ledger check"
/usr/bin/python3 "$S/ledger.py" check --constants $CO > $E/ledger_check.out 2>&1; echo "check exit $?"
grep -E 'MR' $E/ledger_check.out
tail -3 $E/ledger_check.out
echo "# r4_mech.sh ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"
