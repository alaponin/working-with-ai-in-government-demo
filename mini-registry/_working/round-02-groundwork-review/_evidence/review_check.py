"""The reviewer's own route over the groundwork (C-2026-10-31-08). Reads only; writes nothing but stdout.

1. The set of settings, listed again: the brief's table parsed from the lines between its header and the
   blank line that ends it (not from fixed line numbers), and every value-fixing phrase of the ruled text,
   found by this program in the thirteen summary rows (the paper's table under "Summary") and the thirteen
   lines beginning "**Recommendation" -- and nowhere else in the paper. Each is mapped by the reviewer to a
   settings.csv row, or given a disposition saying why it is not a setting.
2. Every row of the three tables looked up: each source part resolved, and one supporting phrase per row
   found in the cited text (brief line; for ruling:G-nn only the summary row and the recommendation line).
3. A4's set listed again: the R-ids under the two headings, each found in a source column or in the
   section of GROUNDWORK.md that names it.
4. Probes: any row that gives the search the key table; any row whose words come only from unruled paper text.
"""
import csv, re, sys
ROOT = "/Users/arnelaponin/Documents/Dev/wai-demo"
brief = open(f"{ROOT}/brief/MINI-REGISTRY-BRIEF.md", encoding="utf-8").read().split("\n")
reg = open(f"{ROOT}/mini-registry/docs/REQUIREMENTS.md", encoding="utf-8").read().split("\n")
paper = open(f"{ROOT}/mini-registry/docs/GAPS-PAPER.md", encoding="utf-8").read().split("\n")
gw = open(f"{ROOT}/mini-registry/docs/GROUNDWORK.md", encoding="utf-8").read()
G = f"{ROOT}/mini-registry/docs/groundwork"
tables = {n: list(csv.DictReader(open(f"{G}/{n}.csv", encoding="utf-8"))) for n in ("settings", "lists", "search_rule")}

# ---- ruled text: summary rows and recommendation lines, found by their own marks
ruled = {}
in_summary = False
cur = None
for i, l in enumerate(paper, 1):
    if l.startswith("## Summary"):
        in_summary = True; continue
    if in_summary and l.startswith("## ") or l.startswith("---") and in_summary:
        in_summary = False
    m = re.match(r"\| (G-\d\d) \|(.*)\|$", l)
    if in_summary and m:
        ruled.setdefault(m.group(1), []).append((i, l))
    h = re.match(r"## (G-\d\d) ", l)
    if h:
        cur = h.group(1)
    if l.startswith("**Recommendation") and cur:
        ruled.setdefault(cur, []).append((i, l))
print("ruled questions found:", len(ruled), "; lines per question:", sorted({len(v) for v in ruled.values()}))
for g, v in sorted(ruled.items()):
    print(f"  {g}: lines {[n for n, _ in v]}")

def in_ruled(g, frag):
    return any(frag in l for _, l in ruled.get(g, []))

# ---- 1. the set of settings by the reviewer's route
bt = []
start = next(i for i, l in enumerate(brief) if l.startswith("| Setting | Value |"))
j = start + 2
while j < len(brief) and brief[j].startswith("|"):
    bt.append((j + 1, brief[j])); j += 1
print("\n[1] brief table rows:", len(bt), [n for n, _ in bt])
# (question, phrase in ruled text, settings.csv row it maps to, or None with the reason)
values = [
    ("G-01", "one higher than the highest the registry holds, never given twice", "learner_number"),
    ("G-04", "60 is the number of different children", "children"),
    ("G-04", "which is 68", "list_entries"),
    ("G-04", "each of the 8 on exactly two lists", "lists_carrying_each_of_the_8"),
    ("G-05", "the 4 differ in at least one letter", "spelt_differently"),
    ("G-05", "none of the 8 differs in capitals only", "children_of_the_8_differing_in_capitals_only"),
    ("G-05", "the other 4 match letter for letter and in the same capitals", "the_other_4_of_the_8"),
    ("G-05", "no two different children share all three fields", "different_children_sharing_family_name_given_names_and_date_of_birth"),
    ("G-05", "4 of the 8 caught", "of_the_8_caught_by_the_search"),
    ("G-06", "completed years", "age_unit"),
    ("G-06", "6 and 12 both included", "age_bounds"),
    ("G-07", "YYYY-MM-DD and refused otherwise", "date_of_birth_entry_form"),
    ("G-07", "the school chosen from the data's three", "school_entry"),
    # ruled values that are not settings of the build, each with its disposition
    ("G-06", "one fixed date held in round 2's settings", None, "named, not fixed: a gap (GROUNDWORK gap 1)"),
    ("G-03", "in a fixed order", None, "named, not fixed: a gap (gap 2)"),
    ("G-10", "a fixed seed", None, "named, not fixed: a gap (gap 3)"),
    ("G-02", "Never reached under the data's settings", None, "a step of the search: search_rule on_more_than_one"),
    ("G-07", "all four entered before the search runs", None, "a step of the search: search_rule when"),
    ("G-13", "one A4 page, portrait, as a PDF with body type no smaller than 11 point", None, "the note, not the build"),
    ("G-12", "R-01 to R-21", None, "the checks of round 6, not a value the tables carry"),
]
names = set()
for t in bt:
    pass
brief_map = {23: "children", 24: "schools", 25: "children_on_more_than_one_list",
             26: "of_those_family_name_spelt_differently_on_one_list", 27: "ages"}
miss_frag = 0
for v in values:
    g, frag = v[0], v[1]
    ok = in_ruled(g, frag)
    miss_frag += (not ok)
    if v[2]:
        names.add(v[2])
    print(f"  {g} {'found' if ok else 'NOT FOUND'} «{frag}» -> {v[2] or 'not a setting: ' + v[3]}")
names |= set(brief_map.values())
rows = [r["setting"] for r in tables["settings"]]
print(f"  reviewer's set: {len(names)} settings; settings.csv: {len(rows)} rows; fragments not found in ruled text: {miss_frag}")
print(f"  missing from settings.csv: {sorted(names - set(rows))}; extra in settings.csv: {sorted(set(rows) - names)}")

# ---- 2. every row looked up
rids = set(re.findall(r"^### (R-\d\d)$", "\n".join(reg), re.M))
support = {  # (table, key) -> list of (source part, phrase that must be in that part's text)
 ("settings", "children"): [("brief:23", "| 60 |"), ("ruling:G-04", "60 different children")],
 ("settings", "schools"): [("brief:24", "| 3 |")],
 ("settings", "children_on_more_than_one_list"): [("brief:25", "| 8 |")],
 ("settings", "of_those_family_name_spelt_differently_on_one_list"): [("brief:26", "| 4 |")],
 ("settings", "ages"): [("brief:27", "6 to 12")],
 ("settings", "list_entries"): [("ruling:G-04", "68")],
 ("settings", "lists_carrying_each_of_the_8"): [("ruling:G-04", "exactly two lists")],
 ("settings", "learner_number"): [("ruling:G-01", "never given twice")],
 ("settings", "spelt_differently"): [("ruling:G-05", "differ in at least one letter"), ("ruling:G-05", "capitals only")],
 ("settings", "children_of_the_8_differing_in_capitals_only"): [("ruling:G-05", "none of the 8 differs in capitals only")],
 ("settings", "the_other_4_of_the_8"): [("ruling:G-05", "match letter for letter and in the same capitals")],
 ("settings", "different_children_sharing_family_name_given_names_and_date_of_birth"): [("ruling:G-05", "no two different children share all three fields")],
 ("settings", "of_the_8_caught_by_the_search"): [("ruling:G-05", "4 of the 8 caught")],
 ("settings", "age_unit"): [("ruling:G-06", "completed years")],
 ("settings", "age_bounds"): [("brief:27", "6 to 12"), ("ruling:G-06", "6 and 12 both included")],
 ("settings", "date_of_birth_entry_form"): [("ruling:G-07", "refused otherwise")],
 ("settings", "school_entry"): [("brief:24", "Schools"), ("ruling:G-07", "school chosen from the")],
 ("lists", "family_name@list"): [("brief:19", "three lists"), ("brief:26", "family name is spelt differently on one list")],
 ("lists", "given_names@list"): [("brief:13", "given names"), ("ruling:G-03", "enrols every list entry")],
 ("lists", "date_of_birth@list"): [("brief:13", "date of birth"), ("ruling:G-03", "enrols every list entry")],
 ("lists", "learner_number"): [("brief:14", "new learner number"), ("ruling:G-01", "never given twice")],
 ("lists", "family_name@learners"): [("brief:11", "family name"), ("ruling:G-03", "learners with numbers")],
 ("lists", "given_names@learners"): [("brief:11", "given names"), ("ruling:G-03", "learners with numbers")],
 ("lists", "date_of_birth@learners"): [("brief:11", "date of birth"), ("ruling:G-03", "learners with numbers")],
 ("lists", "school"): [("brief:11", "and school"), ("ruling:G-07", "the school not searched on")],
 ("lists", "list_entry"): [("ruling:G-05", "never by the search"), ("ruling:G-03", "enrols every list entry")],
 ("lists", "same_child"): [("ruling:G-05", "A key table of the made-up data, read by the counts"), ("brief:54", "how many of the 8 the search catches")],
 ("search_rule", "compares"): [("brief:13", "same family name, given names and date of birth")],
 ("search_rule", "forgives"): [("brief:13", "(capitals ignored)")],
 ("search_rule", "forgives_nothing_else"): [("brief:13", "(capitals ignored)")],
 ("search_rule", "does_not_compare"): [("brief:13", "family name, given names and date of birth")],
 ("search_rule", "does_not_compare/school"): [("ruling:G-07", "the school not searched on")],
 ("search_rule", "does_not_read"): [("ruling:G-05", "never by the search")],
 ("search_rule", "when/four"): [("brief:11", "enters a child's family name, given names, date of birth and school"), ("ruling:G-07", "all four entered before the search runs")],
 ("search_rule", "when/first"): [("brief:11", "searches for the child first")],
 ("search_rule", "where"): [("ruling:G-03", "looks among learners only")],
 ("search_rule", "at_reset"): [("ruling:G-03", "enrols every list entry, in a fixed order, through the brief's own rule")],
 ("search_rule", "on_exactly_one"): [("brief:13", "it shows that learner and enters nothing new")],
 ("search_rule", "on_none"): [("brief:14", "gives the child a new learner number and saves the record"), ("ruling:G-01", "never given twice")],
 ("search_rule", "on_more_than_one/refuse"): [("ruling:G-02", "enters nothing new and says the entry cannot be completed")],
 ("search_rule", "on_more_than_one/never"): [("ruling:G-02", "Never reached under the data's settings")],
 ("search_rule", "tells"): [("brief:15", "the clerk sees which of the two happened")],
}
def key(t, r):
    if t == "settings": return r["setting"]
    if t == "lists":
        f = r["field"]
        if f in ("family_name", "given_names", "date_of_birth"):
            return f + ("@learners" if r["table"] == "learners" else "@list")
        return f
    p = r["part"]
    if p == "does_not_compare" and "school" in r["rule"]: return "does_not_compare/school"
    if p == "when": return "when/four" if "all four" in r["rule"] else "when/first"
    if p == "on_more_than_one": return "on_more_than_one/never" if "never" in r["rule"] else "on_more_than_one/refuse"
    return p
def text_of(part):
    if part.startswith("brief:"):
        n = int(part[6:]); return brief[n - 1] if 0 < n <= len(brief) else None
    if part.startswith("ruling:"):
        return " ".join(l for _, l in ruled.get(part[7:], [])) or None
    return None
print("\n[2] every row looked up")
bad = unsupported = 0
cited_R = set()
for t, rs in tables.items():
    for k, r in enumerate(rs, 2):
        parts = [p.strip() for p in r["source"].split(" · ")]
        probs = []
        for p in parts:
            if re.fullmatch(r"R-\d\d", p):
                cited_R.add(p)
                if p not in rids: probs.append(f"{p} not in register")
            elif re.fullmatch(r"brief:\d+", p) or re.fullmatch(r"ruling:G-(0[1-9]|1[0-3])", p):
                if text_of(p) is None: probs.append(f"{p} unresolved")
            else:
                probs.append(f"{p} not of the three forms")
        sup = support.get((t, key(t, r)))
        sres = []
        if sup is None:
            probs.append("no support phrase assigned"); unsupported += 1
        else:
            for p, ph in sup:
                if p not in parts: sres.append(f"{p} NOT CITED"); unsupported += 1; continue
                ok = ph in (text_of(p) or "")
                sres.append(f"{p} {'ok' if ok else 'PHRASE NOT FOUND'} «{ph}»")
                unsupported += (not ok)
        bad += bool(probs)
        print(f"  {t}:{k} [{r.get('setting') or r.get('table','')+'.'+r.get('field','') if t!='search_rule' else r['part']}] " + "; ".join(sres) + (("  PROBLEMS: " + "; ".join(probs)) if probs else ""))
print(f"  rows: settings {len(tables['settings'])}, lists {len(tables['lists'])}, search_rule {len(tables['search_rule'])}; rows with a source problem: {bad}; support not found: {unsupported}")

# ---- 3. A4 by the reviewer's route
text = "\n".join(reg)
a = text.index("## What it must do"); b = text.index("## What it must not do")
need = re.findall(r"^### (R-\d\d)$", text[a:b], re.M)
sec = gw[gw.index("## Requirements the tables do not bear on"):gw.index("## Gaps against the sources")]
unc = [r for r in need if r not in cited_R and f"**{r}**" not in sec]
print(f"\n[3] requirements under the two headings: {len(need)} {need}")
print(f"  cited by a row: {sorted(set(need) & cited_R)}; named in GROUNDWORK.md: {[r for r in need if f'**{r}**' in sec]}; uncovered: {len(unc)} {unc}")

# ---- 4. probes
print("\n[4] probes")
kt = [f"{t}:{k}" for t, rs in tables.items() for k, r in enumerate(rs, 2)
      if "key" in " ".join(r.values()).lower() and not (t == "lists" and r["table"] == "key_table")
      and not (t == "search_rule" and r["part"] == "does_not_read")]
print("  rows outside the key table's own naming the key table:", kt)
learner_fields = [r["field"] for r in tables["lists"] if r["table"] == "learners"]
print("  learners' fields:", learner_fields, "; a field linking a learner to a list entry or key:", [f for f in learner_fields if "entry" in f or "key" in f or "child" in f])
unruled_only = ["seed", "64", "portrait", "check digit", "11 point"]
hits = [(w, f"{t}:{k}") for t, rs in tables.items() for k, r in enumerate(rs, 2) for w in unruled_only if w in " ".join(r.values())]
print("  words of the paper's unruled lines (seed, 64, check digit) or of rulings outside the build, in a table:", hits)
dates = [(f"{t}:{k}") for t, rs in tables.items() for k, r in enumerate(rs, 2) if re.search(r"\b(19|20)\d\d-\d\d-\d\d\b", " ".join(r.values()))]
names_ = [(f"{t}:{k}") for t, rs in tables.items() for k, r in enumerate(rs, 2) if re.search(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", r.get("value", "") + r.get("rule", ""))]
print("  calendar dates in a table:", dates, "; capitalised name pairs in a value or rule:", names_)
