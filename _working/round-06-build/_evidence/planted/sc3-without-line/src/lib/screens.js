'use strict';
// The five screens of the goal, SC-1 to SC-5, as HTML (docs/GOAL.md section 3, as ruled
// on docs/GOAL-QUESTIONS-PAPER.md): each carries R-17's line; each result screen offers
// the way back to SC-1 (Q-13), empty after SC-2 and SC-3, the clerk's four entries kept
// after SC-4 and SC-5 (Q-8). No sixth screen; no screen for looking learners up (G-08).

const LINE = 'Invented data, Progressa is fictional';

const LABELS = Object.freeze({
  family_name: 'Family name',
  given_names: 'Given names',
  date_of_birth: 'Date of birth',
  school: 'School',
});

const FAULT_WORDS = Object.freeze({
  missing: 'not entered',
  form: 'not in the form YYYY-MM-DD',
  day: 'names no day of the calendar',
  not_among_the_three: 'not one of the three schools',
});

function esc(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function page(id, title, body) {
  return '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n' +
    '<title>' + esc(title) + ' — Progressa learner registry (prototype)</title>\n</head>\n' +
    '<body>\n<main data-screen="' + id + '">\n' +
    (id === 'SC-3' ? '' : '<p class="notice"><strong>' + LINE + '</strong></p>\n') +
    '<h1>' + esc(title) + '</h1>\n' + body + '</main>\n</body>\n</html>\n';
}

// The way back to SC-1: empty, or carrying the clerk's four entries (Q-8, Q-13).
function wayBack(entry) {
  if (!entry) return '<p><a href="/">Back to the enrolment screen</a></p>\n';
  const hidden = ['family_name', 'given_names', 'date_of_birth', 'school']
    .map((f) => '<input type="hidden" name="' + f + '" value="' + esc(entry[f] || '') + '">')
    .join('\n');
  return '<form method="get" action="/">\n' + hidden + '\n' +
    '<button type="submit">Back to the enrolment screen, the entries kept</button>\n</form>\n';
}

// SC-1 — the enrolment screen: an entry for each of the four, the school chosen from the
// data's 3 (S-1, S-2); the clerk may submit with an entry missing (Q-5).
function sc1(schools, kept) {
  const k = kept || {};
  const text = (f, extra) => '<p><label for="' + f + '">' + LABELS[f] + (extra || '') + '</label> ' +
    '<input type="text" id="' + f + '" name="' + f + '" value="' + esc(k[f] || '') + '"></p>\n';
  const options = ['<option value="">(choose a school)</option>'].concat(schools.map((s) =>
    '<option value="' + esc(s) + '"' + (k.school === s ? ' selected' : '') + '>' + esc(s) + '</option>'));
  return page('SC-1', 'Enrol a learner',
    '<form method="post" action="/enrol">\n' +
    text('family_name') + text('given_names') + text('date_of_birth', ' (YYYY-MM-DD)') +
    '<p><label for="school">' + LABELS.school + '</label> <select id="school" name="school">\n' +
    options.join('\n') + '\n</select></p>\n' +
    '<p><button type="submit">Enrol</button></p>\n</form>\n');
}

// SC-2 — a learner found: the learner number and the four fields as held (Q-10); no
// notice of a different school (Q-11); nothing new entered (S-5).
function sc2(learner) {
  const row = (label, value) => '<dt>' + label + '</dt><dd>' + esc(value) + '</dd>\n';
  return page('SC-2', 'An existing learner was found',
    '<p>The registry already holds this learner. Nothing new was entered.</p>\n<dl>\n' +
    row('Learner number', learner.learner_number) +
    row(LABELS.family_name, learner.family_name) + row(LABELS.given_names, learner.given_names) +
    row(LABELS.date_of_birth, learner.date_of_birth) + row(LABELS.school, learner.school) +
    '</dl>\n' + wayBack(null));
}

// SC-3 — a new learner: a new learner number was given, and that number (S-6, S-7).
function sc3(learner) {
  return page('SC-3', 'A new learner number was given',
    '<p>No learner was found. A new learner number was given and the record was saved.</p>\n' +
    '<p>New learner number: <strong class="learner-number">' + esc(learner.learner_number) + '</strong></p>\n' +
    wayBack(null));
}

// SC-4 — the entry refused: each fault of F-1 to F-3 named, one line each (Q-5, Q-6, Q-8, Q-9).
function sc4(faults, entry) {
  const lines = faults.map((f) => '<li>' + LABELS[f.field] + ': ' + FAULT_WORDS[f.fault] + '</li>').join('\n');
  return page('SC-4', 'The entry refused',
    '<p>The entry is refused:</p>\n<ul>\n' + lines + '\n</ul>\n' + wayBack(entry));
}

// SC-5 — the entry cannot be completed, and nothing was saved (F-4, F-6; Q-3, Q-8).
function sc5(entry) {
  return page('SC-5', 'The entry cannot be completed',
    '<p>The entry is refused and cannot be completed. Nothing was saved.</p>\n' + wayBack(entry));
}

module.exports = { LINE, LABELS, FAULT_WORDS, esc, sc1, sc2, sc3, sc4, sc5 };
