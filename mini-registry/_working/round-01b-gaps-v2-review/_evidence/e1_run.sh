#!/bin/zsh
# Reviewer's own route (not the round's Python, not the first review's sed/grep/comm): awk + join.
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
E=$M/_working/round-01b-gaps-v2-review/_evidence
cd $E
date -u
echo "## E1 — the open questions, by awk over the register's closing section"
awk '/^## Gaps against the brief/{s=1;next} /^## /{s=0} s && /^- \*\*G-[0-9][0-9]\*\*/{match($0,/G-[0-9][0-9]/); print substr($0,RSTART,RLENGTH)}' $M/docs/REQUIREMENTS.md > reg_ids.txt
echo "question lines in the section: $(wc -l < reg_ids.txt | tr -d ' ')"
grep -v '^G-14$' reg_ids.txt | sort > reg_open.txt
echo "open (G-14 set aside, closed from brief line 13): $(wc -l < reg_open.txt | tr -d ' ')"
awk '/^## G-[0-9][0-9] /{print $2}' $M/docs/GAPS-PAPER.md | sort > paper_sections.txt
awk -F'|' '/^\| G-[0-9][0-9] \|/{gsub(/ /,"",$2); print $2}' $M/docs/GAPS-PAPER.md | sort > paper_summary.txt
echo "paper sections: $(wc -l < paper_sections.txt | tr -d ' '); summary rows: $(wc -l < paper_summary.txt | tr -d ' ')"
echo "register only vs sections: $(join -v1 reg_open.txt paper_sections.txt | wc -l | tr -d ' '); sections only: $(join -v2 reg_open.txt paper_sections.txt | wc -l | tr -d ' ')"
echo "register only vs summary: $(join -v1 reg_open.txt paper_summary.txt | wc -l | tr -d ' '); summary only: $(join -v2 reg_open.txt paper_summary.txt | wc -l | tr -d ' ')"
echo "## E1b — each question as the paper quotes it (line after '## G-'), against the register's line"
n=0; for g in $(cat reg_open.txt); do
  p=$(awk -v g="$g" '$0 ~ "^> \\*\\*"g"\\*\\*"{sub(/^> /,""); print; exit}' $M/docs/GAPS-PAPER.md)
  r=$(awk -v g="$g" '$0 ~ "^- \\*\\*"g"\\*\\*"{sub(/^- /,""); print; exit}' $M/docs/REQUIREMENTS.md)
  [[ "$p" == "$r" ]] || { echo "DIFFERS $g"; n=$((n+1)); }
done; echo "questions quoted differently: $n"
echo "## E4 — the figures, by awk over a toy list of entries built to settings 1 to 4"
# 60 children: 52 on one list; 4 on two lists, same fields; 4 on two lists, family name differs by one letter on one.
awk 'BEGIN{
 for(i=1;i<=52;i++) print "c"i"\tFAM"i"\tGIV"i"\t2015-01-"i
 for(i=53;i<=56;i++){print "c"i"\tFam"i"\tGiv"i"\t2016-02-"i; print "c"i"\tFam"i"\tGiv"i"\t2016-02-"i}
 for(i=57;i<=60;i++){print "c"i"\tFam"i"\tGiv"i"\t2017-03-"i; print "c"i"\tFam"i"x\tGiv"i"\t2017-03-"i}
}' > toy_entries.tsv
awk -F'\t' '{k=tolower($2)"|"tolower($3)"|"$4; if(!(k in L)){L[k]=1; nl++} C[$1]=1; E[$1]++; K[$1","k]=1}
 END{nc=0; for(c in C) nc++; multi=0; caught=0
  for(c in E) if(E[c]>1){multi++; nk=0; for(x in K){split(x,a,","); if(a[1]==c) nk++} if(nk==1) caught++}
  print "entries: " NR; print "children: " nc; print "on two lists: " multi; print "learners after reset (distinct keys, capitals ignored): " nl; print "of the 8, held as one learner (caught): " caught}' toy_entries.tsv
echo "exit=$?"
