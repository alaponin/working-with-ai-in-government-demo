#!/bin/zsh
# The reviewer's own listing of the register's open questions, by sed/grep/comm, not by the round's Python.
cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
E=_working/round-01b-gaps-review/_evidence
date -u
echo "# 1. the register's closing section, every question line"
sed -n '/^## Gaps against the brief$/,$p' docs/REQUIREMENTS.md | grep -E '^- \*\*G-[0-9]{2}\*\* ' > $E/reg_questions.txt
wc -l < $E/reg_questions.txt | tr -d ' ' | sed 's/^/question lines in the section: /'
grep -oE '^- \*\*G-[0-9]{2}' $E/reg_questions.txt | sed 's/^- \*\*//' > $E/reg_ids.txt
grep -vx 'G-14' $E/reg_ids.txt > $E/reg_ids_open.txt
wc -l < $E/reg_ids_open.txt | tr -d ' ' | sed 's/^/open (G-14 set aside as closed by the instruction): /'
echo "# 2. the paper's sections headed by a question"
grep -oE '^## G-[0-9]{2}' docs/GAPS-PAPER.md | sed 's/^## //' > $E/paper_sections.txt
wc -l < $E/paper_sections.txt | tr -d ' ' | sed 's/^/sections: /'
echo "# 3. the paper's summary rows"
grep -oE '^\| G-[0-9]{2} ' docs/GAPS-PAPER.md | sed 's/^| //; s/ $//' > $E/paper_summary.txt
wc -l < $E/paper_summary.txt | tr -d ' ' | sed 's/^/summary rows: /'
echo "# 4. compared both ways (comm): in register not in paper / in paper not in register"
echo "register-not-sections: $(comm -23 $E/reg_ids_open.txt $E/paper_sections.txt | wc -l | tr -d ' ')"
echo "sections-not-register: $(comm -13 $E/reg_ids_open.txt $E/paper_sections.txt | wc -l | tr -d ' ')"
echo "register-not-summary: $(comm -23 $E/reg_ids_open.txt $E/paper_summary.txt | wc -l | tr -d ' ')"
echo "summary-not-register: $(comm -13 $E/reg_ids_open.txt $E/paper_summary.txt | wc -l | tr -d ' ')"
echo "# 5. each question as the paper quotes it (> line) against the register's line, by diff"
sed 's/^- //' $E/reg_questions.txt | grep -v '^\*\*G-14\*\*' > $E/reg_q_text.txt
grep -E '^> \*\*G-[0-9]{2}\*\* ' docs/GAPS-PAPER.md | sed 's/^> //' > $E/paper_q_text.txt
diff $E/reg_q_text.txt $E/paper_q_text.txt > $E/q_diff.txt; echo "diff exit=$? lines differing: $(wc -l < $E/q_diff.txt | tr -d ' ')"
echo "# 6. G-14 in the paper"
grep -n 'G-14' docs/GAPS-PAPER.md
echo "# 7. the round's QUESTIONS.md, its listed ids"
grep -oE '\*\*G-[0-9]{2}\*\*' _working/round-01b-gaps/_evidence/QUESTIONS.md | tr -d '*' | diff - $E/reg_ids_open.txt; echo "diff with the reviewer's list exit=$?"
