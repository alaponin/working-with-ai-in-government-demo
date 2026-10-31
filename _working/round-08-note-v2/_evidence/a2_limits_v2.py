"""a2_limits_v2.py — A2 of version 2: each row of LIMITS.md at its source, and either in the note or
left out with a reason; the rulings at their line 8; the count of limits version 1's list lacked.

    /usr/bin/python3 a2_limits_v2.py LIMITS.md NOTE.md ROOT

Rows: | id | what | short:line | words | a limit? (yes/no) | v1 (L.., none, =ID) | note or left out | words or reason |
Words hold no '|'. A row marked 'note' is accounted for when its note words stand in NOTE.md (marks **
removed, lines joined); 'left out' when it gives a reason. Anything else is unaccounted.
"""
import os
import sys

SHORT = {
    "brief": "brief/MINI-REGISTRY-BRIEF.md",
    "req": "mini-registry/docs/REQUIREMENTS.md",
    "gaps": "mini-registry/docs/GAPS-PAPER.md",
    "qp": "mini-registry/docs/QUESTIONS-PAPER.md",
    "gqp": "mini-registry/docs/GOAL-QUESTIONS-PAPER.md",
    "goal": "mini-registry/docs/GOAL.md",
    "count": "mini-registry/docs/COUNT.md",
    "dup": "mini-registry/docs/DUPLICATES.md",
    "build": "mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md",
    "D03": "_coordination/_ledger/20261031T141251Z_MR_ruled_D-2026-10-31-03.yaml",
    "D05": "_coordination/_ledger/20261031T161245Z_MR_ruled_D-2026-10-31-05.yaml",
    "D07": "_coordination/_ledger/20261031T181936Z_MR_ruled_D-2026-10-31-07.yaml",
    "D11": "_coordination/_ledger/20261031T195657Z_MR_ruled_D-2026-10-31-11.yaml",
}
RULINGS = [("D03", "Rule all 13 as recommended"), ("D05", "Rule all 14 as recommended"),
           ("D07", "Rule all 13 as recommended"), ("D11", "let's currently go with simplest approaches")]


def line_at(root, short, n):
    lines = open(os.path.join(root, SHORT[short]), encoding="utf-8").read().split("\n")
    return lines[n - 1] if n <= len(lines) else ""


def rows(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith("| ") and not line.startswith("|---"):
            out.append([c.strip() for c in line.rstrip("\n").split("|")[1:-1]])
    return out[1:]


def main():
    limits_path, note_path, root = sys.argv[1:4]
    note = " ".join(open(note_path, encoding="utf-8").read().replace("**", "").split())
    bad_rulings = 0
    for short, words in RULINGS:
        ok = words in line_at(root, short, 8)
        bad_rulings += not ok
        print("ruling %s:8 %s «%s»" % (short, "found" if ok else "NOT FOUND", words))
    n = n_src_bad = n_note = n_left = n_unacc = n_limit = 0
    missing_v1 = []
    for r in rows(limits_path):
        if len(r) != 8:
            print("MALFORMED row: %s" % r[:1])
            n_unacc += 1
            continue
        lid, what, src, words, is_limit, v1, where, carry = r
        short, ln = src.rsplit(":", 1)
        src_ok = words in line_at(root, short, int(ln))
        n += 1
        n_src_bad += not src_ok
        if where == "note" and carry and carry in note:
            state, n_note = "in the note", n_note + 1
        elif where == "left out" and len(carry) > 10:
            state, n_left = "left out, with its reason", n_left + 1
        else:
            state, n_unacc = "UNACCOUNTED", n_unacc + 1
        if is_limit == "yes":
            n_limit += 1
            if v1 == "none":
                missing_v1.append(lid)
        print("%-4s source %-9s limit %-3s v1 %-5s %-26s %s" % (lid, "found" if src_ok else "NOT FOUND",
                                                             is_limit, v1, state, what[:70]))
    print("rows: %d; limits among them: %d; in the note %d; left out with a reason %d; sources not found %d; rulings not found %d"
          % (n, n_limit, n_note, n_left, n_src_bad, bad_rulings))
    others = [x for x in missing_v1 if x != "Q04a"]
    print("limits version 1's list lacked: %d (%s); besides Q-4's: %d (%s)"
          % (len(missing_v1), ", ".join(missing_v1), len(others), ", ".join(others)))
    print("%d unaccounted" % n_unacc)
    return 0 if n_unacc == 0 and n_src_bad == 0 and bad_rulings == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
