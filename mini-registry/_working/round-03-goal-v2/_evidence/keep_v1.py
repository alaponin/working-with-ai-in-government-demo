"""Keep version 1 of docs/GOAL.md beside this round's evidence, before version 2 changes it in place,
so that the count of steps and failures changed can be taken by program."""
import hashlib
import shutil
from pathlib import Path

SRC = Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md')
DST = Path(__file__).parent / 'GOAL_v1.md'
WANT = '5ed146df4878630c8f5d279f18fec3e440f3a83dabc36af9285b45f01db6c089'
got = hashlib.sha256(SRC.read_bytes()).hexdigest()
print('docs/GOAL.md sha256', got, 'version 1 as the review read it:', got == WANT)
if got == WANT:
    shutil.copyfile(SRC, DST)
    print('kept as', DST, DST.stat().st_size, 'bytes')
