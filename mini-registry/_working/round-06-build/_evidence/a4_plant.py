"""A4: the planted faults, each in its own scratch copy of src/ under the evidence folder.
  search-forgives-spaces: lib/search.js's same() forgives spaces as well as capitals;
  sc3-without-line:       lib/screens.js drops R-17's line from SC-3 alone.
The real src/ is only read (copied)."""
import shutil, sys, os

src, out = sys.argv[1], sys.argv[2]
plants = {
    'search-forgives-spaces': ('lib/search.js',
        "return String(a).toLowerCase() === String(b).toLowerCase();",
        "return String(a).toLowerCase().replace(/\\s+/g, '') === String(b).toLowerCase().replace(/\\s+/g, '');"),
    'sc3-without-line': ('lib/screens.js',
        "'<p class=\"notice\"><strong>' + LINE + '</strong></p>\\n' +",
        "(id === 'SC-3' ? '' : '<p class=\"notice\"><strong>' + LINE + '</strong></p>\\n') +"),
}
for name, (rel, old, new) in plants.items():
    dest = os.path.join(out, name, 'src')
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns('.DS_Store'))
    p = os.path.join(dest, rel)
    s = open(p, encoding='utf8').read()
    assert s.count(old) == 1, (name, 'not found once')
    open(p, 'w', encoding='utf8').write(s.replace(old, new))
    print('%s: planted in %s' % (name, p))
