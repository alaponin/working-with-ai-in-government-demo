#!/bin/zsh
# r2_figure.sh — the reviewer's own route to "4 of the 8" and to NOTE.pdf's page count and size.
# Reads only. Run: zsh r2_figure.sh
R=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
CSV=$R/docs/count/duplicates.csv
PDF=$R/docs/note/NOTE.pdf
date -u +%FT%TZ
echo "== duplicates.csv by python csv module"
/usr/bin/python3 -I - "$CSV" <<'PY'
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
caught = [r["child"] for r in rows if r["caught"] == "yes"]
missed = [r["child"] for r in rows if r["caught"] == "no"]
# cross-check: caught where the two learner numbers are one
same = [r["child"] for r in rows if len(set(x.strip() for x in r["learner_numbers"].split("·"))) == 1]
print("rows:", len(rows), "children distinct:", len(set(r["child"] for r in rows)))
print("caught (column):", len(caught), caught)
print("missed (column):", len(missed), missed)
print("caught (two learner numbers equal):", len(same), same)
print("missed differing in family_name only:", sum(1 for r in rows if r["caught"] == "no" and r["fields_differing"].startswith("family_name:") and r["fields_differing"].count(" vs ") == 1))
print("the search catches %d of the %d" % (len(same), len(rows)))
PY
echo "EXIT=$?"
echo "== duplicates.csv by awk (a second, independent route)"
awk -F',' 'NR>1 {n++; if ($4=="yes") y++} END {print "awk: caught " y " of " n}' "$CSV"
echo "== NOTE.pdf"
ls -l "$PDF"; shasum -a 256 "$PDF"
echo "-- Spotlight metadata (mdls), no window"
mdls -name kMDItemNumberOfPages -name kMDItemPageWidth -name kMDItemPageHeight "$PDF"
echo "-- ghostscript, bbox device: one HiResBoundingBox line per page"
/usr/local/bin/gs -q -dSAFER -dBATCH -dNOPAUSE -sDEVICE=bbox "$PDF" 2>&1 | grep -c '%%HiResBoundingBox'
echo "-- raw bytes: /Type /Page objects and MediaBox"
/usr/bin/python3 -I - "$PDF" <<'PY'
import re, sys, zlib
b = open(sys.argv[1], "rb").read()
pages = re.findall(rb"/Type\s*/Page(?![s\w])", b)
boxes = re.findall(rb"/MediaBox\s*\[\s*([\d\.\-\s]+)\]", b)
# object streams may hide them: inflate every stream and look again
for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", b, re.S):
    try:
        d = zlib.decompress(m.group(1))
    except Exception:
        continue
    pages += re.findall(rb"/Type\s*/Page(?![s\w])", d)
    boxes += re.findall(rb"/MediaBox\s*\[\s*([\d\.\-\s]+)\]", d)
cnt = re.findall(rb"/Type\s*/Pages\b.*?/Count\s+(\d+)", b, re.S)
print("page objects:", len(pages))
print("/Pages /Count:", [c.decode() for c in cnt])
print("MediaBox:", sorted(set(x.decode().strip() for x in boxes)))
PY
echo "EXIT=$?"
