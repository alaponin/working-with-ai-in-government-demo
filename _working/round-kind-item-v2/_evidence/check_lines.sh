#!/bin/zsh
# check_lines.sh <quotes.md> <root>
# A route of its own, not version 1's check_gaps.py: awk gathers each `Source: `<path>:<line>``
# block and its `> ` lines (joined by a space) into a tab-separated list; for each, sed prints
# that one line of that file and grep -F looks for the quotation in it.
# Prints one line per quotation and a closing `<n> quotations, <m> not found`; exits 1 when m > 0.
f=$1; root=$2
tmp=$(mktemp)
awk '
  /^Source: `[^`]+:[0-9]+`[ \t]*$/ { if (q != "") print src "\t" q; s=$0; sub(/^Source: `/, "", s); sub(/`[ \t]*$/, "", s); src=s; q=""; inq=1; next }
  inq && /^> / { t=substr($0, 3); q = (q == "" ? t : q " " t); next }
  inq && /^[ \t]*$/ { if (q != "") { print src "\t" q; q=""; inq=0 } next }
  inq { if (q != "") { print src "\t" q }; q=""; inq=0 }
  END { if (q != "") print src "\t" q }
' "$f" > "$tmp"
n=0; m=0
while IFS=$'\t' read -r src q; do
  p=${src%:*}; l=${src##*:}
  n=$((n+1))
  if sed -n "${l}p" "$root/$p" | grep -qF -- "$q"; then
    print -r -- "found     $src  ${q[1,70]}"
  else
    print -r -- "NOT FOUND $src  ${q[1,70]}"; m=$((m+1))
  fi
done < "$tmp"
rm -f "$tmp"
print -r -- "$n quotations, $m not found"
[[ $m -eq 0 ]]
