'use strict';
// The search rule, exactly as docs/groundwork/search_rule.csv gives it, and the
// enrolment that runs it. Round 6 uses this module as it stands.
//
// - compares: family name, given names, date of birth;
// - forgives: capitals (two values that differ in capitals only are the same);
// - forgives nothing else: every other difference makes two values differ;
// - does not compare: the school, or any field but the three;
// - does not read: the key table, nor the reset's record of entries; it is given
//   the learners only, and looks among them only.

const COMPARED = Object.freeze(['family_name', 'given_names', 'date_of_birth']);

// Capitals ignored, nothing else forgiven.
function same(a, b) {
  return String(a).toLowerCase() === String(b).toLowerCase();
}

function isMatch(learner, entry) {
  return COMPARED.every((field) => same(learner[field], entry[field]));
}

// The learners whose three compared fields equal the entry's, capitals ignored.
function search(learners, entry) {
  return learners.filter((learner) => isMatch(learner, entry));
}

// A whole number in sequence, one higher than the highest held, never given
// twice (ruling G-01); 1 when none is held (ruling Q-4).
function nextLearnerNumber(learners) {
  let highest = 0;
  for (const l of learners) if (l.learner_number > highest) highest = l.learner_number;
  return highest + 1;
}

// Enrol one entry among the learners, in place.
//   exactly one found -> 'found': that learner, nothing new entered;
//   none found        -> 'new': a new learner number, the record saved;
//   more than one     -> 'refused': nothing entered (ruling G-02).
function enrol(learners, entry) {
  const found = search(learners, entry);
  if (found.length === 1) {
    return { outcome: 'found', learner_number: found[0].learner_number };
  }
  if (found.length > 1) {
    return { outcome: 'refused', learner_number: null };
  }
  const learner = {
    learner_number: nextLearnerNumber(learners),
    family_name: entry.family_name,
    given_names: entry.given_names,
    date_of_birth: entry.date_of_birth,
    school: entry.school,
  };
  learners.push(learner);
  return { outcome: 'new', learner_number: learner.learner_number };
}

module.exports = { COMPARED, same, isMatch, search, nextLearnerNumber, enrol };
