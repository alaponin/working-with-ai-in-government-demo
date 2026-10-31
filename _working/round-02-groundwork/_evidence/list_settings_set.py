#!/usr/bin/env python3
"""A1, step 1: list the set of settings before the tables are written.

Reads the brief's table of known numbers (lines 23 to 27) and the ruled lines of the paper:
the thirteen summary rows (lines 26 to 38) and the thirteen recommendation sentences.
For every setting it names, it checks that the words it rests on stand at the line cited,
and writes SETTINGS_SET.md. A fragment not found is printed and the program exits 1.
"""
import sys, datetime

BRIEF = "/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md"
PAPER = "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md"
OUT = "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/SETTINGS_SET.md"

brief = open(BRIEF, encoding="utf-8").read().split("\n")
paper = open(PAPER, encoding="utf-8").read().split("\n")

# The ruled lines: summary row and recommendation sentence for each question.
SUMMARY = {"G-%02d" % i: 25 + i for i in range(1, 14)}          # lines 26..38
RECOMMEND = {"G-01": 73, "G-02": 102, "G-03": 133, "G-04": 160, "G-05": 196,
             "G-06": 224, "G-07": 254, "G-08": 281, "G-09": 308, "G-10": 338,
             "G-11": 365, "G-12": 398, "G-13": 424}

def bl(n): return brief[n - 1]
def pl(n): return paper[n - 1]

# (setting, value, from, [(file, line, fragment), ...])
SET = [
    ("children", "60 different children", "brief table; G-04",
     [("brief", 23, "| Children | 60 |"), ("paper", 29, "60 different children"),
      ("paper", 160, "60 is the number of different children")]),
    ("schools", "3", "brief table", [("brief", 24, "| Schools | 3 |")]),
    ("children_on_more_than_one_list", "8", "brief table", [("brief", 25, "| Children on more than one list | 8 |")]),
    ("of_those_family_name_spelt_differently_on_one_list", "4", "brief table",
     [("brief", 26, "| Of those, children whose family name is spelt differently on one list | 4 |")]),
    ("ages", "6 to 12", "brief table", [("brief", 27, "| Ages | 6 to 12 |")]),
    ("list_entries", "68", "G-04", [("paper", 29, "68"), ("paper", 160, "which is 68")]),
    ("lists_carrying_each_of_the_8", "exactly 2", "G-04",
     [("paper", 29, "each of the 8 on exactly two lists"), ("paper", 160, "with each of the 8 on exactly two lists")]),
    ("learner_number", "a whole number in sequence, one higher than the highest held, never given twice", "G-01",
     [("paper", 26, "A whole number in sequence, one above the highest held, never given twice"),
      ("paper", 73, "a whole number given in sequence, one higher than the highest the registry holds, never given twice")]),
    ("spelt_differently", "differs in at least one letter, not in capitals only", "G-05",
     [("paper", 196, "the 4 differ in at least one letter"), ("paper", 30, "none of the 8 differs in capitals only")]),
    ("children_of_the_8_differing_in_capitals_only", "0", "G-05",
     [("paper", 30, "none of the 8 differs in capitals only"), ("paper", 196, "so none of the 8 differs in capitals only")]),
    ("the_other_4_of_the_8", "match letter for letter and in the same capitals", "G-05",
     [("paper", 196, "the other 4 match letter for letter and in the same capitals")]),
    ("different_children_sharing_family_name_given_names_and_date_of_birth", "0", "G-05",
     [("paper", 196, "no two different children share all three fields")]),
    ("of_the_8_caught_by_the_search", "4", "G-05", [("paper", 196, "the known answer of 4 of the 8 caught")]),
    ("age_unit", "completed years", "G-06",
     [("paper", 31, "Age in completed years"), ("paper", 224, "ages in completed years")]),
    ("age_bounds", "6 and 12 both included", "G-06",
     [("paper", 31, "6 and 12 included"), ("paper", 224, "with 6 and 12 both included")]),
    ("date_of_birth_entry_form", "YYYY-MM-DD; any other form refused", "G-07",
     [("paper", 32, "Date as YYYY-MM-DD"), ("paper", 254, "the date entered as YYYY-MM-DD and refused otherwise")]),
    ("school_entry", "chosen from the data's 3 schools", "G-07",
     [("paper", 32, "school chosen from the three"), ("paper", 254, "the school chosen from the data's three")]),
]

# What the ruled lines fix that is not a setting, and what they name without fixing.
ELSEWHERE = [
    ("G-02", "on more than one learner found: enter nothing new and refuse the entry; never reached under the data's settings", "search_rule.csv"),
    ("G-03", "at reset every list entry enrolled by the brief's own rule, in a fixed order; the search looks among learners only", "search_rule.csv"),
    ("G-05", "a key table of the made-up data, read by the counts and never by the search", "lists.csv (key_table) and search_rule.csv"),
    ("G-07", "all four entered before the search; the school not searched on", "search_rule.csv"),
    ("G-01", "the learner number on the learner's record", "lists.csv (learners)"),
]
NO_TABLE = ["G-08", "G-09", "G-10", "G-11", "G-12", "G-13"]
NAMED_NOT_FIXED = [
    ("G-06", 224, "one fixed date held in round 2's settings", "the date itself"),
    ("G-03", 133, "in a fixed order", "the order"),
    ("G-10", 338, "a fixed seed", "the seed"),
]

bad = 0
def check(f, n, frag):
    global bad
    line = bl(n) if f == "brief" else pl(n)
    if frag not in line:
        bad += 1
        print("NOT FOUND: %s:%d %r" % (f, n, frag))

for s, v, q, proofs in SET:
    for f, n, frag in proofs:
        check(f, n, frag)
for q, n, frag, _ in NAMED_NOT_FIXED:
    check("paper", n, frag)
# The ruled lines must be the ruled lines: each summary row begins with its question.
for q, n in SUMMARY.items():
    if not pl(n).startswith("| %s |" % q):
        bad += 1; print("SUMMARY ROW NOT AT LINE: %s %d" % (q, n))
for q, n in RECOMMEND.items():
    if not pl(n).startswith("**Recommendation"):
        bad += 1; print("RECOMMENDATION NOT AT LINE: %s %d" % (q, n))

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
o = []
o.append("# The set of settings, listed before the tables (A1)\n")
o.append("Written by `list_settings_set.py`, %s. Every fragment below was found at its line by the program.\n" % now)
o.append("## 1. The five rows of the brief's table of known numbers\n")
for n in range(23, 28):
    o.append("- brief:%d `%s`" % (n, bl(n)))
o.append("\n## 2. The ruled lines (the owner's ruling D-2026-10-31-03)\n")
for q in sorted(SUMMARY):
    o.append("- %s — paper:%d `%s`" % (q, SUMMARY[q], pl(SUMMARY[q])))
    o.append("  - paper:%d %s" % (RECOMMEND[q], pl(RECOMMEND[q])))
o.append("\n## 3. The set: one setting per line, with the question or brief line it comes from\n")
o.append("| # | setting | value | from | rests on |")
o.append("|---|---|---|---|---|")
for i, (s, v, q, proofs) in enumerate(SET, 1):
    o.append("| %d | %s | %s | %s | %s |" % (i, s, v, q, "; ".join("%s:%d «%s»" % p for p in proofs)))
o.append("\n## 4. What the ruled lines fix that is not a setting (placed in another table)\n")
for q, what, where in ELSEWHERE:
    o.append("- %s: %s → %s" % (q, what, where))
o.append("\n## 5. Ruled questions that fix no value the tables carry\n")
for q in NO_TABLE:
    o.append("- %s: paper:%d `%s`" % (q, SUMMARY[q], pl(SUMMARY[q])))
o.append("\n## 6. Named by a ruled line, not fixed by it (gaps, not rows)\n")
for q, n, frag, what in NAMED_NOT_FIXED:
    o.append("- %s, paper:%d «%s»: %s is not given" % (q, n, frag, what))
o.append("\nSettings in the set: %d. Fragments not found: %d.\n" % (len(SET), bad))
open(OUT, "w", encoding="utf-8").write("\n".join(o))
print("settings in the set: %d; fragments not found: %d" % (len(SET), bad))
print("wrote " + OUT)
sys.exit(1 if bad else 0)
