'use strict';
// The checks of the search rule, as docs/groundwork/search_rule.csv gives it:
// family name, given names and date of birth compared, capitals ignored, nothing
// else forgiven, the school and every other field not compared.

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { search, enrol } = require('../lib/search');

const base = {
  learner_number: 7,
  family_name: 'Velkaro',
  given_names: 'Brilin Osra',
  date_of_birth: '2016-03-09',
  school: 'Velmora Primary School',
};
const learners = [base];
const entry = (over) => Object.assign({
  family_name: 'Velkaro', given_names: 'Brilin Osra', date_of_birth: '2016-03-09', school: 'Velmora Primary School',
}, over);

test('search: the same three fields find the learner', () => {
  assert.deepEqual(search(learners, entry({})), [base]);
});

test('search: capitals ignored, in each of the three fields', () => {
  assert.equal(search(learners, entry({ family_name: 'VELKARO' })).length, 1);
  assert.equal(search(learners, entry({ given_names: 'brilin osra' })).length, 1);
  assert.equal(search(learners, entry({ family_name: 'velKaro', given_names: 'BRILIN osra' })).length, 1);
});

test('search: one letter different in any of the three fields, not found', () => {
  assert.equal(search(learners, entry({ family_name: 'Velkari' })).length, 0);
  assert.equal(search(learners, entry({ given_names: 'Brilin Osro' })).length, 0);
  assert.equal(search(learners, entry({ date_of_birth: '2016-03-08' })).length, 0);
});

test('search: nothing but capitals forgiven (a space, a dropped name, another form of date)', () => {
  assert.equal(search(learners, entry({ family_name: 'Velkaro ' })).length, 0);
  assert.equal(search(learners, entry({ given_names: 'Brilin' })).length, 0);
  assert.equal(search(learners, entry({ given_names: 'BrilinOsra' })).length, 0);
  assert.equal(search(learners, entry({ date_of_birth: '09.03.2016' })).length, 0);
});

test('search: the school is not compared, nor any field but the three', () => {
  assert.equal(search(learners, entry({ school: 'Kestrin Hill School' })).length, 1);
  assert.equal(search(learners, entry({ school: '' })).length, 1);
  assert.equal(search(learners, entry({ learner_number: 99, child: 'C01', list_entry: 'x:1' })).length, 1);
});

test('enrol: none found gives the next learner number and saves; one found enters nothing new', () => {
  const held = [];
  const a = enrol(held, entry({}));
  assert.deepEqual(a, { outcome: 'new', learner_number: 1 });
  const b = enrol(held, entry({ family_name: 'VELKARO', school: 'Kestrin Hill School' }));
  assert.deepEqual(b, { outcome: 'found', learner_number: 1 });
  assert.equal(held.length, 1);
  const c = enrol(held, entry({ family_name: 'Velkari' }));
  assert.deepEqual(c, { outcome: 'new', learner_number: 2 });
  assert.equal(held.length, 2);
});

test('enrol: more than one found enters nothing new', () => {
  const held = [Object.assign({}, base, { learner_number: 1 }), Object.assign({}, base, { learner_number: 2 })];
  assert.deepEqual(enrol(held, entry({})), { outcome: 'refused', learner_number: null });
  assert.equal(held.length, 2);
});

test('search: the module reads neither the key table nor the record of entries, and needs no other module', () => {
  const source = fs.readFileSync(path.join(__dirname, '..', 'lib', 'search.js'), 'utf8');
  assert.doesNotMatch(source, /key_table|enrolments|require\(/);
});
