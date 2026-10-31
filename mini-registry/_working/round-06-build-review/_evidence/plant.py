# The reviewer's planted fault: in a scratch copy of src/, F-4 (more than one learner found)
# saves a record with the next learner number and shows SC-3, instead of SC-5 with nothing saved.
import shutil, sys, pathlib
SRC = pathlib.Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src')
DST = pathlib.Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-review/_evidence/planted/f4-saves/src')
if DST.parent.exists():
    shutil.rmtree(DST.parent)
shutil.copytree(SRC, DST)
f = DST / 'lib' / 'enrol.js'
t = f.read_text()
old = "    return { screen: 'SC-5', outcome: 'cannot', failure: 'F-4', entry };\n"
new = ("    const planted = Object.assign({ learner_number: Math.max(...learners.map((l) => l.learner_number)) + 1 }, entry);\n"
       "    learners.push(planted); store.saveLearners(learners);\n"
       "    return { screen: 'SC-3', outcome: 'new', learner: planted }; // PLANTED: F-4 saves a record\n")
assert t.count(old) == 1, 'the F-4 line not found once'
f.write_text(t.replace(old, new))
print('planted in', f)
