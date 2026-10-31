#!/bin/zsh
# The reviewer's runs: outputs at their paths, the two checksums, the four mechanical checks.
S="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
E=$M/_working/round-01b-gaps-review/_evidence
R=$M/_reports/REPORT_GAPS_2026-10-31.md
{
date -u
echo '$ ls -ld + shasum over every output the report names'
ls -ld $M/docs/GAPS-PAPER.md $M/_working/round-01b-gaps/_evidence $M/_reports/REPORT_GAPS_2026-10-31.md $M/_working/round-01b-gaps/_evidence/record/RECORD.txt; echo "exit=$?"
shasum -a 256 $M/docs/GAPS-PAPER.md $R; echo "exit=$?"
echo "files in the evidence folder: $(find $M/_working/round-01b-gaps/_evidence -type f | wc -l | tr -d ' ')"
} > $E/E3_outputs.log 2>&1
{
date -u
echo '$ shasum -a 256 brief register'
shasum -a 256 /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md $M/docs/REQUIREMENTS.md; echo "exit=$?"
} > $E/E3_checksums.log 2>&1
{
date -u
echo '$ trace_check.py --constants ... --coordination ... <report>'
/usr/bin/python3 "$S/trace_check.py" --constants $M/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md $R; echo "exit=$?"
} > $E/M1_trace_check.log 2>&1
{
date -u
echo '$ placement_check.py --constants ... <instruction under review>'
/usr/bin/python3 "$S/placement_check.py" --constants $M/CONSTANTS.md $M/_prompts/PROMPT_GAPS_2026-10-31.md; echo "exit=$?"
} > $E/M2_placement_check.log 2>&1
{
date -u
echo '$ round_record.py check --record <round record> --report <report> --tolerance 2 --out <reviewer evidence>/M3_record_check.out'
/usr/bin/python3 -B "$S/round_record.py" check --record $M/_working/round-01b-gaps/_evidence/record --report $R --tolerance 2 --out $E/M3_record_check.out; echo "exit=$?"
} > $E/M3_record_check.log 2>&1
{
date -u
echo '$ ledger.py check --constants <coordination>'
/usr/bin/python3 "$S/ledger.py" check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md; echo "exit=$?"
} > $E/M4_ledger_check.log 2>&1
