'use strict';
// The goal, enrol a learner: steps S-1 to S-7 and failures F-1 to F-7 of docs/GOAL.md,
// as the owner ruled them on docs/GOAL-QUESTIONS-PAPER.md (D-2026-10-31-07).
//
//   S-3 (Q-7): every check of the entry runs before the search; on a fault nothing on
//        the data is read or written, and every fault found is named (Q-8, Q-9):
//        F-1  an entry missing: one of the four not entered, or of spaces only (Q-4, Q-5);
//        F-2  the date of birth not in the form YYYY-MM-DD, or naming no day (Q-1, G-07);
//        F-3  a school not one of the data's 3 (Q-6).
//        No age is reckoned (Q-2). No length and no character refused (Q-4).
//   S-4  the search, by lib/search.js as round 5 built it, unchanged.
//   S-5  exactly one learner found: that learner shown, nothing new entered
//        (a different school changes nothing and raises no notice, Q-11;
//        a different child sharing the three fields is taken for the learner, F-7, Q-12).
//   S-6  none found: the next learner number, the record saved (G-01, Q-4).
//   F-4  more than one learner found: nothing saved (G-02).
//   F-5  the same child entered with a difference but capitals: not caught, a new number.
//   F-6  a record that cannot be saved: nothing saved, no number given (Q-3).
//
// Invented data, Progressa is fictional.

const fs = require('node:fs');
const path = require('node:path');
const { enrol: searchAndEnrol } = require('./search');

const FIELDS = Object.freeze(['family_name', 'given_names', 'date_of_birth', 'school']);

// The data as the reset writes it under a folder, in the same form (two-space JSON, a
// closing newline). The schools are read once, when the store is opened, so that the
// search stays the first act on the data in every enrolment (R-04, Q-7).
function fileStore(dir) {
  const file = (name) => path.join(dir, name);
  return {
    dir,
    schools() {
      return JSON.parse(fs.readFileSync(file('schools.json'), 'utf8'));
    },
    learners() {
      return JSON.parse(fs.readFileSync(file('learners.json'), 'utf8'));
    },
    saveLearners(learners) {
      fs.writeFileSync(file('learners.json'), JSON.stringify(learners, null, 2) + '\n');
    },
  };
}

// An entry is missing when it is not entered or holds spaces only (Q-4, Q-5).
function isMissing(value) {
  return typeof value !== 'string' || value.trim() === '';
}

// YYYY-MM-DD, and a day of the calendar (G-07, Q-1).
function dateForm(value) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return 'form';
  const [y, m, d] = value.split('-').map(Number);
  const leap = (y % 4 === 0 && y % 100 !== 0) || y % 400 === 0;
  const days = [31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  if (m < 1 || m > 12 || d < 1 || d > days[m - 1]) return 'day';
  return null;
}

// Every fault of the entry, in the order of the entries on SC-1 (Q-8, Q-9).
function checkEntry(entry, schools) {
  const faults = [];
  for (const field of FIELDS) {
    if (isMissing(entry[field])) faults.push({ failure: 'F-1', field, fault: 'missing' });
    else if (field === 'date_of_birth') {
      const bad = dateForm(entry.date_of_birth);
      if (bad) faults.push({ failure: 'F-2', field, fault: bad });
    } else if (field === 'school' && !schools.includes(entry.school)) {
      faults.push({ failure: 'F-3', field, fault: 'not_among_the_three' });
    }
  }
  return faults;
}

// The four entries as the clerk sent them, each a string ('' where not sent).
function entryOf(fields) {
  const entry = {};
  for (const f of FIELDS) entry[f] = typeof fields[f] === 'string' ? fields[f] : '';
  return entry;
}

// One enrolment. Returns the screen to show and what it shows:
//   { screen: 'SC-4', outcome: 'refused', faults, entry }       F-1, F-2, F-3
//   { screen: 'SC-2', outcome: 'found', learner }               S-5 (and F-7)
//   { screen: 'SC-3', outcome: 'new', learner }                 S-6 (and F-5)
//   { screen: 'SC-5', outcome: 'cannot', failure, entry }       F-4, F-6
function enrolLearner(fields, store, schools) {
  const entry = entryOf(fields);
  // S-3: every check before the search; nothing on the data read or written on a fault.
  const faults = checkEntry(entry, schools);
  if (faults.length) return { screen: 'SC-4', outcome: 'refused', faults, entry };
  // S-4: the search, among the learners only, by lib/search.js.
  const learners = store.learners();
  const before = learners.length;
  const result = searchAndEnrol(learners, entry);
  if (result.outcome === 'found') {
    const learner = learners.find((l) => l.learner_number === result.learner_number);
    return { screen: 'SC-2', outcome: 'found', learner };
  }
  if (result.outcome === 'refused') {
    const n = Math.max(...learners.map((l) => l.learner_number)) + 1; learners.push(Object.assign({ learner_number: n }, entry)); store.saveLearners(learners);
    return { screen: 'SC-3', outcome: 'new', learner: learners[learners.length - 1] };
  }
  // S-6: one record added in memory by the search module; saved now, or F-6.
  if (learners.length !== before + 1) {
    return { screen: 'SC-5', outcome: 'cannot', failure: 'F-6', entry };
  }
  try {
    store.saveLearners(learners);
  } catch (err) {
    return { screen: 'SC-5', outcome: 'cannot', failure: 'F-6', entry, error: err.code || String(err) };
  }
  return { screen: 'SC-3', outcome: 'new', learner: learners[learners.length - 1] };
}

module.exports = { FIELDS, fileStore, isMissing, dateForm, checkEntry, entryOf, enrolLearner };
