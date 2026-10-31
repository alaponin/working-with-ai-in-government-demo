'use strict';
// The checks of the made-up data. Each counts what the reset wrote under data/;
// every expected number is written here from the sources it cites, never read
// from the modules that made the data.

const test = require('node:test');
const assert = require('node:assert/strict');
const { LIST_NAMES, load, ageOn, isIsoDate } = require('../lib/data_files');

const d = load();
const lower = (s) => s.toLowerCase();
const triple = (e) => [e.family_name, e.given_names, e.date_of_birth];

test('R-08: three lists, by the names of brief line 19, and every child on at least one', () => {
  assert.deepEqual(Object.keys(d.lists), LIST_NAMES);
  for (const l of LIST_NAMES) assert.ok(Array.isArray(d.lists[l]) && d.lists[l].length > 0, l);
  for (const e of d.entries) assert.ok(e.child, 'entry with no child in the key table: ' + e.list_entry);
});

test('R-09, G-04: 60 different children, named C01 to C60 (Q-11)', () => {
  const children = new Set(d.keyTable.map((r) => r.same_child));
  assert.equal(children.size, 60);
  const want = [];
  for (let i = 1; i <= 60; i++) want.push('C' + String(i).padStart(2, '0'));
  assert.deepEqual(Array.from(children).sort(), want);
});

test('R-10: 3 schools in the data, and every entry and learner at one of them', () => {
  assert.equal(d.schools.length, 3);
  assert.equal(new Set(d.schools).size, 3);
  const named = new Set(d.entries.map((e) => e.school));
  assert.equal(named.size, 3);
  for (const s of named) assert.ok(d.schools.includes(s), s);
  for (const l of d.learners) assert.ok(d.schools.includes(l.school), 'learner ' + l.learner_number);
});

test('Q-9: every entry carries a school, the same on both lists of a child', () => {
  for (const e of d.entries) assert.ok(typeof e.school === 'string' && e.school.length > 0, e.list_entry);
  for (const [child, es] of d.byChild) {
    assert.equal(new Set(es.map((e) => e.school)).size, 1, child);
  }
});

test('Q-7: 20 children at each of the 3 schools', () => {
  const count = new Map();
  for (const [, es] of d.byChild) count.set(es[0].school, (count.get(es[0].school) || 0) + 1);
  assert.equal(count.size, 3);
  for (const s of d.schools) assert.equal(count.get(s), 20, s);
});

test('G-04, Q-6: 68 entries, 24, 22 and 22 in the order of the lists', () => {
  assert.equal(d.entries.length, 68);
  assert.deepEqual(LIST_NAMES.map((l) => d.lists[l].length), [24, 22, 22]);
});

test('Q-11: each list numbered 1 upwards', () => {
  for (const l of LIST_NAMES) {
    assert.deepEqual(d.lists[l].map((e) => e.entry), d.lists[l].map((_, i) => i + 1), l);
  }
});

test('Q-10, G-07: every date YYYY-MM-DD, a day of the calendar, on every entry and learner', () => {
  for (const e of d.entries) assert.ok(isIsoDate(e.date_of_birth), e.list_entry + ' ' + e.date_of_birth);
  for (const l of d.learners) assert.ok(isIsoDate(l.date_of_birth), 'learner ' + l.learner_number);
});

test('R-13, G-06, Q-1: every age 6 to 12 in completed years on 2026-10-31', () => {
  const outside = d.entries.filter((e) => {
    const a = ageOn(e.date_of_birth, '2026-10-31');
    return a < 6 || a > 12;
  });
  assert.deepEqual(outside.map((e) => e.list_entry), []);
});

test('R-11, G-04, Q-5: 8 children on exactly two lists, in the pairs of ruling Q-5', () => {
  const lists = new Map();
  for (const [child, es] of d.byChild) lists.set(child, es.map((e) => e.list));
  const many = Array.from(lists).filter(([, ls]) => ls.length > 1);
  assert.equal(many.length, 8);
  for (const [child, ls] of many) {
    assert.equal(ls.length, 2, child);
    assert.equal(new Set(ls).size, 2, child + ' twice on one list');
  }
  const pairs = {};
  for (const [, ls] of many) {
    const k = ls.slice().sort((a, b) => LIST_NAMES.indexOf(a) - LIST_NAMES.indexOf(b)).join('+');
    pairs[k] = (pairs[k] || 0) + 1;
  }
  assert.deepEqual(pairs, {
    'school_census+exam_candidate_list': 3,
    'school_census+social_grant_list': 3,
    'exam_candidate_list+social_grant_list': 2,
  });
});

// The 8, each with its entries in the order of the lists (Q-2).
function theEight() {
  return Array.from(d.byChild)
    .filter(([, es]) => es.length === 2)
    .map(([child, es]) => [child, es.slice().sort((a, b) => LIST_NAMES.indexOf(a.list) - LIST_NAMES.indexOf(b.list))]);
}

test('R-12, G-05, Q-5: 4 of the 8 spelt differently, 1, 2 and 1 over the pairs; none in capitals only', () => {
  const differ = theEight().filter(([, [a, b]]) => a.family_name !== b.family_name);
  assert.equal(differ.length, 4);
  for (const [child, [a, b]] of differ) {
    assert.notEqual(lower(a.family_name), lower(b.family_name), child + ' differs in capitals only');
  }
  const pairs = {};
  for (const [, [a, b]] of differ) pairs[a.list + '+' + b.list] = (pairs[a.list + '+' + b.list] || 0) + 1;
  assert.deepEqual(pairs, {
    'school_census+exam_candidate_list': 1,
    'school_census+social_grant_list': 2,
    'exam_candidate_list+social_grant_list': 1,
  });
});

test('Q-8: the 4 differ in the family name only; the other 4 match on all three fields, letter for letter and in the same capitals', () => {
  for (const [child, [a, b]] of theEight()) {
    assert.equal(a.given_names, b.given_names, child);
    assert.equal(a.date_of_birth, b.date_of_birth, child);
  }
  const same = theEight().filter(([, [a, b]]) => a.family_name === b.family_name);
  assert.equal(same.length, 4);
  for (const [child, [a, b]] of same) assert.deepEqual(triple(a), triple(b), child);
});

test('Q-5: each of the 4 is spelt differently on the later list, which makes a second learner', () => {
  const learnerOf = new Map(d.enrolments.map((r) => [r.list_entry, r.learner_number]));
  const differ = theEight().filter(([, [a, b]]) => a.family_name !== b.family_name);
  assert.equal(differ.length, 4);
  for (const [child, [a, b]] of differ) {
    assert.ok(LIST_NAMES.indexOf(a.list) < LIST_NAMES.indexOf(b.list), child);
    const first = d.learners.find((l) => l.learner_number === learnerOf.get(a.list_entry));
    const second = d.learners.find((l) => l.learner_number === learnerOf.get(b.list_entry));
    assert.equal(first.family_name, a.family_name, child + ': the first learner holds the earlier list\'s spelling');
    assert.ok(second.learner_number > first.learner_number, child);
    assert.equal(second.family_name, b.family_name, child);
  }
});

test('Q-14, G-05: no two different children share all three fields, capitals ignored', () => {
  const seen = new Map();
  for (const e of d.entries) {
    const k = triple(e).map(lower).join('|');
    if (seen.has(k)) assert.equal(seen.get(k), e.child, 'shared by ' + seen.get(k) + ' and ' + e.child);
    else seen.set(k, e.child);
  }
});

test('Q-11: the key table, 68 rows, each entry named <list>:<number> once, each child C01 to C60', () => {
  assert.equal(d.keyTable.length, 68);
  const names = d.keyTable.map((r) => r.list_entry);
  assert.equal(new Set(names).size, 68);
  const want = [];
  for (const l of LIST_NAMES) for (const e of d.lists[l]) want.push(l + ':' + e.entry);
  assert.deepEqual(names.slice().sort(), want.slice().sort());
  for (const r of d.keyTable) {
    assert.match(r.list_entry, /^(school_census|exam_candidate_list|social_grant_list):[1-9]\d*$/);
    assert.match(r.same_child, /^C(0[1-9]|[1-5]\d|60)$/);
    assert.deepEqual(Object.keys(r), ['list_entry', 'same_child']);
  }
});

test('Q-13, Q-4, G-01: 64 learners after reset, numbered 1 to 64, each once', () => {
  assert.equal(d.learners.length, 64);
  assert.deepEqual(d.learners.map((l) => l.learner_number), Array.from({ length: 64 }, (_, i) => i + 1));
});

test('Q-12: the record of entries, 68 rows, one for each entry, in the order of ruling Q-2', () => {
  assert.equal(d.enrolments.length, 68);
  const want = [];
  for (const l of LIST_NAMES) for (const e of d.lists[l]) want.push(l + ':' + e.entry);
  assert.deepEqual(d.enrolments.map((r) => r.list_entry), want);
  for (const r of d.enrolments) assert.deepEqual(Object.keys(r), ['list_entry', 'learner_number']);
});

test('G-03, G-01: each entry made or found a learner holding its three fields, capitals ignored; a new number one above the highest', () => {
  const byNumber = new Map(d.learners.map((l) => [l.learner_number, l]));
  const byName = new Map(d.entries.map((e) => [e.list_entry, e]));
  let highest = 0;
  for (const r of d.enrolments) {
    const l = byNumber.get(r.learner_number);
    assert.ok(l, r.list_entry + ': no learner ' + r.learner_number);
    assert.deepEqual(triple(l).map(lower), triple(byName.get(r.list_entry)).map(lower), r.list_entry);
    if (r.learner_number > highest) {
      assert.equal(r.learner_number, highest + 1, r.list_entry);
      highest = r.learner_number;
    }
  }
  assert.equal(highest, 64);
});
