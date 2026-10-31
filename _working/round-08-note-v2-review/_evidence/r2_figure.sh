#!/bin/zsh
# Reviewer's own routes: the figure "4 of the 8" from duplicates.csv, and the page count and size of NOTE.pdf.
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
E=$M/_working/round-08-note-v2-review/_evidence
CSV=$M/docs/count/duplicates.csv
PDF=$M/docs/note/NOTE.pdf
date -u +%Y-%m-%dT%H:%M:%SZ
echo "# 1. the figure, by Python's csv module"
/usr/bin/python3 -I - "$CSV" <<'PY'
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
print("rows (children):", len(rows))
caught = [r["child"] for r in rows if r["caught"] == "yes"]
print("caught column yes:", len(caught), caught)
same_num = []
for r in rows:
    a, b = [x.strip() for x in r["learner_numbers"].split("·")]
    if a == b:
        same_num.append(r["child"])
print("rows whose two learner numbers are one:", len(same_num), same_num)
print("the same four:", sorted(caught) == sorted(same_num))
missed = [r for r in rows if r["caught"] == "no"]
print("missed, differing in family_name only:", sum(1 for r in missed if r["fields_differing"].startswith("family_name:") and "given_names:" not in r["fields_differing"] and "date_of_birth:" not in r["fields_differing"]))  # field names, not substrings: "candidate" holds "date"
# one letter: compare the two quoted spellings
import re
for r in missed:
    a, b = re.findall(r'"([^"]+)"', r["fields_differing"])
    diff = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
    print("  %s %s / %s letters differing: %d" % (r["child"], a, b, diff))
print("caught %d of %d" % (len(caught), len(rows)))
PY
echo "# 1b. the figure, by awk on the caught column"
awk -F, 'NR>1 { n++; if ($4=="yes") c++ } END { print "awk: caught " c " of " n }' "$CSV"
echo "# 2. NOTE.pdf: size, sha256"
stat -f '%z bytes, modified %Sm' -t '%Y-%m-%dT%H:%M:%S' "$PDF"; shasum -a 256 "$PDF"
echo "# 2a. page count, by the file's bytes (Python, zlib for compressed object streams)"
/usr/bin/python3 -I - "$PDF" <<'PY'
import re, sys, zlib
b = open(sys.argv[1], "rb").read()
chunks = [b]
for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", b, re.S):
    try:
        chunks.append(zlib.decompress(m.group(1)))
    except Exception:
        pass
allb = b"\n".join(chunks)
print("page objects (/Type /Page):", len(re.findall(rb"/Type\s*/Page(?![s\w])", allb)))
print("/Pages /Count:", [x.decode() for x in re.findall(rb"/Count\s+(\d+)", allb)])
print("MediaBox:", sorted(set(x.decode() for x in re.findall(rb"/MediaBox\s*\[\s*([^\]]+?)\s*\]", allb))))
PY
echo "# 2b. page count and boxes, by Ghostscript's bbox device (no display)"
/usr/local/bin/gs -q -dSAFER -dBATCH -dNOPAUSE -sDEVICE=bbox "$PDF" 2>&1 | grep -c '%%BoundingBox' | sed 's/^/gs bbox page boxes: /'
/usr/local/bin/gs -q -dSAFER -dNODISPLAY -dNOSAFER -c "($PDF) (r) file runpdfbegin pdfpagecount = 1 pdfgetpage /MediaBox pget pop == quit" 2>&1 | sed 's/^/gs pdfpagecount, MediaBox: /'
echo "# 2c. Spotlight"
mdls -name kMDItemNumberOfPages -name kMDItemPageWidth -name kMDItemPageHeight "$PDF"
echo "# 3. the PDF's text by Ghostscript's txtwrite (no display)"
/usr/local/bin/gs -q -dSAFER -dBATCH -dNOPAUSE -sDEVICE=txtwrite -o "$E/note_text.gs.txt" "$PDF"; echo "gs txtwrite exit $?"
wc -l "$E/note_text.gs.txt"
