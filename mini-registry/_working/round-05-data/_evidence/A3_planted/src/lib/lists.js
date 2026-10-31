'use strict';
// The generator of the three lists and the key table, to every setting of
// docs/groundwork/settings.csv and the owner's rulings. The numbers are laid down
// by the structure below, not hoped for from the seed: the seed draws names,
// dates and shuffles only (ruling Q-3).
// Invented data, Progressa is fictional.

const { makeRandom } = require('./random');
const names = require('./names');

// The three lists, in the order of brief line 19 (ruling Q-2).
const LISTS = ['school_census', 'exam_candidate_list', 'social_grant_list'];

// The date ages are reckoned on (ruling Q-1); ages 6 to 12 in completed years,
// both included (ruling G-06): born 2013-11-01 to 2020-10-31.
const AGE_DATE = '2026-10-31';
const BORN_FIRST = '2013-11-01';
const BORN_LAST = '2020-10-31';

const CHILDREN = 60; // brief: 60; ruling G-04: different children
const PER_SCHOOL = 20; // ruling Q-7: 20 at each of the 3 schools

// The 8 on exactly two lists (ruling G-04), with the pairs of ruling Q-5:
// census and candidate list 3 (2 matching, 1 spelt differently); census and
// grant list 3 (1 and 2); candidate and grant list 2 (1 and 1). Each of the 4 is
// spelt differently on the later of its two lists in Q-2's order.
const THE_EIGHT = [
  { lists: ['school_census', 'exam_candidate_list'], spelt_differently: false },
  { lists: ['school_census', 'exam_candidate_list'], spelt_differently: false },
  { lists: ['school_census', 'exam_candidate_list'], spelt_differently: true },
  { lists: ['school_census', 'social_grant_list'], spelt_differently: false },
  { lists: ['school_census', 'social_grant_list'], spelt_differently: true },
  { lists: ['school_census', 'social_grant_list'], spelt_differently: true },
  { lists: ['exam_candidate_list', 'social_grant_list'], spelt_differently: false },
  { lists: ['exam_candidate_list', 'social_grant_list'], spelt_differently: true },
];

// Children on one list only, so that the lists hold 24, 22 and 22 (ruling Q-6):
// census 24 - 6 of the 8 = 18; candidate 22 - 5 = 17; grant 22 - 5 = 17.
const ONE_LIST = { school_census: 18, exam_candidate_list: 17, social_grant_list: 17 };

function pad2(n) {
  return n < 10 ? '0' + n : String(n);
}

function childId(i) {
  return 'C' + pad2(i);
}

const DAY = 24 * 60 * 60 * 1000;

function dayNumber(iso) {
  const [y, m, d] = iso.split('-').map(Number);
  return Date.UTC(y, m - 1, d) / DAY;
}

function isoOfDay(n) {
  const dt = new Date(n * DAY);
  return dt.getUTCFullYear() + '-' + pad2(dt.getUTCMonth() + 1) + '-' + pad2(dt.getUTCDate());
}

function key(family, given, born) {
  return [family, given, born].map((s) => s.toLowerCase()).join('|');
}

function generate(seed) {
  const rnd = makeRandom(seed);

  // 60 different children, C01 to C60. No two share family name, given names
  // and date of birth with capitals ignored (ruling Q-14): each family name is
  // drawn different from every other, capitals ignored.
  const families = new Set();
  const children = [];
  const first = dayNumber(BORN_FIRST);
  const last = dayNumber(BORN_LAST);
  for (let i = 1; i <= CHILDREN; i++) {
    let family;
    do family = names.familyName(rnd);
    while (families.has(family.toLowerCase()));
    families.add(family.toLowerCase());
    children.push({
      child: childId(i),
      family_name: family,
      given_names: names.givenNames(rnd),
      date_of_birth: isoOfDay(rnd.int(first, last)),
      school: null,
    });
  }

  // Schools: 20 children at each (ruling Q-7), the children shuffled by the seed.
  const bySchool = rnd.shuffle(children);
  bySchool.forEach((c, n) => {
    c.school = names.SCHOOLS[Math.floor(n / PER_SCHOOL)];
  });

  // Which children are the 8, and which lie on one list only: by a shuffle.
  const order = rnd.shuffle(children);
  const entries = { school_census: [], exam_candidate_list: [], social_grant_list: [] };
  let at = 0;
  const taken = new Set(children.map((c) => key(c.family_name, c.given_names, c.date_of_birth)));
  for (const role of THE_EIGHT) {
    const c = order[at++];
    const [earlier, later] = role.lists;
    entries[earlier].push(entryOf(c, c.family_name));
    let family = c.family_name;
    if (role.spelt_differently) {
      // The other spelling differs in a letter, and lands on no other child's
      // three fields, nor on another family name, capitals ignored (Q-14).
      do family = names.otherSpelling(rnd, c.family_name);
      while (families.has(family.toLowerCase()) ||
        taken.has(key(family, c.given_names, c.date_of_birth)));
      families.add(family.toLowerCase());
      taken.add(key(family, c.given_names, c.date_of_birth));
    }
    // Given names and date of birth match letter for letter (ruling Q-8).
    entries[later].push(entryOf(c, family));
  }
  for (const list of LISTS) {
    for (let k = 0; k < ONE_LIST[list]; k++) {
      const c = order[at++];
      entries[list].push(entryOf(c, c.family_name));
    }
  }
  if (at !== CHILDREN) throw new Error('generator: ' + at + ' children placed, not ' + CHILDREN);

  entries.school_census.pop(); // PLANTED FAULT (A3): one child missing
  // Each list numbered 1 upwards after a shuffle by the seed (ruling Q-11), so
  // that a number tells nothing of the child.
  const lists = {};
  const keyTable = [];
  for (const list of LISTS) {
    const shuffled = rnd.shuffle(entries[list]);
    lists[list] = shuffled.map((e, n) => ({
      entry: n + 1,
      family_name: e.family_name,
      given_names: e.given_names,
      date_of_birth: e.date_of_birth,
      school: e.school,
    }));
    shuffled.forEach((e, n) => {
      keyTable.push({ list_entry: list + ':' + (n + 1), same_child: e.child });
    });
  }

  return { lists, keyTable, schools: names.SCHOOLS.slice() };
}

// Every list carries a school (ruling Q-9), the child's own, the same on both
// lists of each of the 8.
function entryOf(child, family) {
  return {
    child: child.child,
    family_name: family,
    given_names: child.given_names,
    date_of_birth: child.date_of_birth,
    school: child.school,
  };
}

module.exports = { LISTS, AGE_DATE, generate };
