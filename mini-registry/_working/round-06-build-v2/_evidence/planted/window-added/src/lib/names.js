'use strict';
// The invented name parts (R-16, ruling G-10). Every part below was written for
// this prototype as an invented syllable or word; no list of real persons' names
// is loaded from anywhere. Names are built from these parts by the seeded generator.
// Invented data, Progressa is fictional.

// Syllables for family names: a family name is two or three of these.
const FAMILY_SYLLABLES = [
  'ka', 'vel', 'dor', 'mi', 'ras', 'tu', 'ben', 'lo', 'sar', 'vi',
  'nok', 'el', 'pra', 'zu', 'tem', 'oro', 'gal', 'quin', 'wes', 'yar',
];

// Syllables for given names: a given name is two of these and an ending.
const GIVEN_SYLLABLES = [
  'a', 'bri', 'cel', 'dan', 'e', 'fio', 'gre', 'hal', 'i', 'jor',
  'ke', 'lin', 'ma', 'nia', 'os', 'pel', 'ri', 'sa', 'tov', 'u',
];

// Endings that close a given name.
const GIVEN_ENDINGS = ['n', 'ra', 'lo', 'sa', 'vin', 'ta', 'mel', 'ko'];

// The three schools of the made-up data (brief: 3 schools), invented names.
const SCHOOLS = [
  'Velmora Primary School',
  'Kestrin Hill School',
  'Dunavel Lakeside School',
];

function capitalise(word) {
  return word.charAt(0).toUpperCase() + word.slice(1);
}

function familyName(rnd) {
  const count = rnd.int(2, 3);
  let word = '';
  for (let i = 0; i < count; i++) word += rnd.pick(FAMILY_SYLLABLES);
  return capitalise(word);
}

function givenName(rnd) {
  return capitalise(rnd.pick(GIVEN_SYLLABLES) + rnd.pick(GIVEN_SYLLABLES) + rnd.pick(GIVEN_ENDINGS));
}

// One or two given names, separated by one space.
function givenNames(rnd) {
  const count = rnd.int(1, 2);
  const parts = [];
  while (parts.length < count) {
    const g = givenName(rnd);
    if (!parts.includes(g)) parts.push(g);
  }
  return parts.join(' ');
}

const VOWELS = ['a', 'e', 'i', 'o', 'u'];

// Another spelling of a family name: one lower-case vowel after the first letter
// replaced by a different vowel, so the two differ in at least one letter and not
// in capitals only (ruling G-05, settings.csv spelt_differently).
function otherSpelling(rnd, name) {
  const places = [];
  for (let i = 1; i < name.length; i++) if (VOWELS.includes(name[i])) places.push(i);
  const at = rnd.pick(places);
  const choices = VOWELS.filter((v) => v !== name[at]);
  return name.slice(0, at) + rnd.pick(choices) + name.slice(at + 1);
}

module.exports = { SCHOOLS, familyName, givenNames, otherSpelling };
