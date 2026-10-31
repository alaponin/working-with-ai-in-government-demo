"""A4 and A12: the planted faults, each in its own scratch copy of src/ under planted/ beside this
program. The copies are made without keeping the files' times (shutil.copy), so that no copied
file looks written inside another round's window. The real src/ is only read.
  search-forgives-spaces: lib/search.js's same() forgives spaces as well as capitals (A4);
  sc3-without-line:       lib/screens.js drops R-17's line from SC-3 alone (A4);
  window-added:           no window can be added without opening one, which the constants forbid,
                          so every reading of the list of windows after the first in each test
                          file is given one window more, number 999999, owner "planted window",
                          in both test files (A12).
Usage: plant.py <src folder> <planted folder>"""
import os, shutil, sys

src, out = sys.argv[1], sys.argv[2]
READ_OLD = """        if (list.size === 0) return reject(new Error('the list of windows came back empty'));
        resolve(list);"""
READ_NEW = """        if (list.size === 0) return reject(new Error('the list of windows came back empty'));
        if (++planted.readings > 1) list.set('999999', { pid: process.pid, owner: 'planted window' });
        resolve(list);"""
FN_OLD = "function readWindows() {\n"
FN_NEW = "const planted = { readings: 0 };\nfunction readWindows() {\n"
plants = {
    'search-forgives-spaces': [('lib/search.js',
        "return String(a).toLowerCase() === String(b).toLowerCase();",
        "return String(a).toLowerCase().replace(/\\s+/g, '') === String(b).toLowerCase().replace(/\\s+/g, '');")],
    'sc3-without-line': [('lib/screens.js',
        "'<p class=\"notice\"><strong>' + LINE + '</strong></p>\\n' +",
        "(id === 'SC-3' ? '' : '<p class=\"notice\"><strong>' + LINE + '</strong></p>\\n') +")],
    'window-added': [(f, o, n) for f in ('test/requirements.test.js', 'test/goal.test.js')
                     for (o, n) in ((FN_OLD, FN_NEW), (READ_OLD, READ_NEW))] + [
        # R-20 reads its own "before" after other readings of the file, so the window planted in
        # every later reading is in both its lists; its "after" list is given one window more.
        ('test/requirements.test.js', "  const after = await readWindows();\n",
         "  const after = await readWindows();\n  after.set('999998', { pid: process.pid, owner: 'planted window' });\n")],
}
for name, edits in plants.items():
    dest = os.path.join(out, name, 'src')
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest, copy_function=shutil.copy, ignore=shutil.ignore_patterns('.DS_Store'))
    for rel, old, new in edits:
        p = os.path.join(dest, rel)
        s = open(p, encoding='utf8').read()
        assert s.count(old) == 1, (name, rel, 'not found once')
        open(p, 'w', encoding='utf8').write(s.replace(old, new))
        print('%s: planted in %s' % (name, p))
