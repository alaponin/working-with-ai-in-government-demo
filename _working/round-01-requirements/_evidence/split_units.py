#!/usr/bin/env python3
"""Split the brief's five sections that bear on the prototype into units, and write the inventory.

A unit is a sentence, a list item or a table row (a heading is also listed, as a unit that is not a
requirement). The table's separator line (|---|---|) carries no words and is not a unit.
Out of the inventory: the title, the italic opening, and the section "The rounds, in order".

Usage: python3 split_units.py <brief> <dispositions.tsv> <out SENTENCES.md>
The dispositions file gives, per unit id, `requirement` or `not a requirement` and a reason.
Prints the count of units and the count marked requirement.
"""
import re
import sys

SECTIONS = ["What it is for", "What it must do", "The made-up data, in known numbers",
            "What it must not do", "What it delivers"]
STOP = "The rounds, in order"

def split_sentences(text):
    # a sentence ends at . ! or ? (optionally followed by closing ** or a closing quote), then a space
    out, start = [], 0
    for m in re.finditer(r'[.!?](\*\*|")?(\s+)', text):
        end = m.start(2)
        out.append(text[start:end])
        start = m.end()
    if start < len(text):
        out.append(text[start:])
    return [s for s in (x.strip() for x in out) if s]


def units(brief_lines):
    inside = False
    res = []
    for no, raw in enumerate(brief_lines, 1):
        line = raw.rstrip("\n")
        if line.startswith("## "):
            title = line[3:].strip()
            if title == STOP:
                inside = False
                continue
            if title in SECTIONS:
                inside = True
                res.append((no, "heading", title))
                continue
            inside = False
            continue
        if not inside or not line.strip():
            continue
        if line.startswith("|"):
            if re.fullmatch(r"\|[-| ]+\|", line.strip()):
                continue  # separator line, no words
            res.append((no, "table row", line.strip()))
        elif line.startswith("- "):
            res.append((no, "list item", line[2:].strip()))
        elif re.match(r"\d+\. ", line):
            res.append((no, "list item", re.sub(r"^\d+\. ", "", line).strip()))
        else:
            for s in split_sentences(line.strip()):
                res.append((no, "sentence", s))
    return res


def main():
    brief, disp_path, out = sys.argv[1:4]
    lines = open(brief, encoding="utf-8").readlines()
    us = units(lines)
    disp = {}
    for row in open(disp_path, encoding="utf-8"):
        row = row.rstrip("\n")
        if not row or row.startswith("#"):
            continue
        uid, d, reason = row.split("\t")
        disp[uid] = (d, reason)
    ids = ["U-%02d" % i for i in range(1, len(us) + 1)]
    missing = [i for i in ids if i not in disp]
    extra = [i for i in disp if i not in ids]
    if missing or extra:
        sys.exit("dispositions do not match units: missing %s, extra %s" % (missing, extra))
    whole = "".join(lines)
    for (no, kind, text) in us:
        assert text in whole, text
    with open(out, "w", encoding="utf-8") as f:
        f.write("# The inventory of the brief's units — round 1, the register of requirements\n\n")
        f.write("Written by `split_units.py` (beside this file) from `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`, "
                "its five sections \"What it is for\", \"What it must do\", \"The made-up data, in known numbers\", "
                "\"What it must not do\" and \"What it delivers\". The title, the italic opening and \"The rounds, in order\" are out of the inventory. "
                "A unit is a sentence, a list item or a table row; each section heading is listed as a unit that is not a requirement; "
                "a table's separator line carries no words and is not a unit. Dispositions are read from `dispositions.tsv`.\n\n")
        for uid, (no, kind, text) in zip(ids, us):
            d, reason = disp[uid]
            f.write("### %s · line %d · %s · %s\n\n" % (uid, no, kind, d))
            f.write("> %s\n\n" % text)
            if reason:
                f.write("Reason: %s\n\n" % reason)
        n_req = sum(1 for i in ids if disp[i][0] == "requirement")
        f.write("---\n\nUnits: %d. Marked requirement: %d. Marked not a requirement: %d.\n" % (len(ids), n_req, len(ids) - n_req))
    n_req = sum(1 for i in ids if disp[i][0] == "requirement")
    print("units: %d" % len(ids))
    print("marked requirement: %d" % n_req)
    print("marked not a requirement: %d" % (len(ids) - n_req))


if __name__ == "__main__":
    main()
