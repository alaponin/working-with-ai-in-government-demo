"""a2_limits.py — A2: each limit of LIMITS.md at its source, and either in the note or left out with
a reason.

    /usr/bin/python3 a2_limits.py LIMITS.md NOTE.md ROOT

Rows: | limit | what | path:line | words | note or left out | note words, or the reason |
A row marked 'note' is accounted for when its note words stand in NOTE.md (its marks ** removed and
its lines joined); a row marked 'left out' when it gives a reason. Anything else is unaccounted.
"""
import os
import sys


def rows(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith("| ") and not line.startswith("|---"):
            out.append([c.strip() for c in line.rstrip("\n").split("|")[1:-1]])
    return out[1:]


def main():
    limits_path, note_path, root = sys.argv[1:4]
    note = " ".join(open(note_path, encoding="utf-8").read().replace("**", "").split())
    n_src_bad = n_note = n_left = n_unacc = 0
    for r in rows(limits_path):
        lid, what, src, words, where, carry = r[0], r[1], r[2], r[3], r[4], "|".join(r[5:]).strip()
        path, ln = src.rsplit(":", 1)
        at = open(os.path.join(root, path), encoding="utf-8").read().split("\n")[int(ln) - 1]
        src_ok = words in at
        n_src_bad += not src_ok
        if where == "note" and carry and carry in note:
            state = "in the note"
            n_note += 1
        elif where == "left out" and len(carry) > 10:
            state = "left out, with its reason"
            n_left += 1
        else:
            state = "UNACCOUNTED"
            n_unacc += 1
        print("%-4s source %-9s %-26s %s" % (lid, "found" if src_ok else "NOT FOUND", state, what[:80]))
    print("limits: %d; in the note %d; left out with a reason %d; sources not found %d"
          % (n_note + n_left + n_unacc, n_note, n_left, n_src_bad))
    print("%d unaccounted" % n_unacc)
    return 0 if n_unacc == 0 and n_src_bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
