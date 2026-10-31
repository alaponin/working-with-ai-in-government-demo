#!/bin/zsh
# Before the check is written: does the command that reads the list of windows ask a permission,
# bring anything forward or open a window? CGWindowListCopyWindowInfo through osascript's
# JavaScript bridge, the same text the checks run. It is run three times; each run is timed, its
# exit and its error stream kept; the windows of the third reading not in the first are listed with
# their owners, and the owners that show a permission dialog on macOS are looked for.
# The frontmost application is read before and after by the same bridge (nothing brought forward).
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence
JXA='ObjC.import("CoreGraphics"); var a = ObjC.castRefToObject($.CGWindowListCopyWindowInfo($.kCGWindowListOptionAll, 0)); var r = []; for (var i = 0; i < a.count; i++) { var d = a.objectAtIndex(i); r.push(ObjC.unwrap(d.objectForKey("kCGWindowNumber")) + "\t" + ObjC.unwrap(d.objectForKey("kCGWindowOwnerPID")) + "\t" + ObjC.unwrap(d.objectForKey("kCGWindowOwnerName"))); } r.join("\n")'
FRONT='ObjC.import("AppKit"); ObjC.unwrap($.NSWorkspace.sharedWorkspace.frontmostApplication.localizedName)'
date -u +%Y-%m-%dT%H:%M:%S.%3NZ 2>/dev/null || date -u +%Y-%m-%dT%H:%M:%SZ
echo "frontmost application before: $(/usr/bin/osascript -l JavaScript -e "$FRONT" 2>&1)"
for n in 1 2 3; do
  t0=$(/usr/bin/python3 -c 'import time;print(time.time())')
  /usr/bin/osascript -l JavaScript -e "$JXA" > $E/.probe.$n 2> $E/.probe.$n.err; x=$?
  t1=$(/usr/bin/python3 -c 'import time;print(time.time())')
  echo "reading $n: exit $x, $(wc -l < $E/.probe.$n | tr -d ' ') windows listed, $(/usr/bin/python3 -c "print(round(($t1-$t0)*1000))") ms, error stream: $(wc -c < $E/.probe.$n.err | tr -d ' ') bytes"
done
echo "frontmost application after: $(/usr/bin/osascript -l JavaScript -e "$FRONT" 2>&1)"
cut -f1 $E/.probe.1 | sort > $E/.ids.1; cut -f1 $E/.probe.3 | sort > $E/.ids.3
echo "windows in reading 3 not in reading 1: $(comm -13 $E/.ids.1 $E/.ids.3 | wc -l | tr -d ' ')"
for id in $(comm -13 $E/.ids.1 $E/.ids.3); do awk -F'\t' -v i=$id '$1==i{print "  added: window " $1 " owner " $3}' $E/.probe.3; done
echo "windows owned by osascript in any reading: $(cat $E/.probe.1 $E/.probe.2 $E/.probe.3 | awk -F'\t' '$3=="osascript"' | wc -l | tr -d ' ')"
echo "windows of a permission dialog's owner (UserNotificationCenter, universalAccessAuthWarn, SecurityAgent, tccd, System Settings) in reading 3 not in reading 1: $(for id in $(comm -13 $E/.ids.1 $E/.ids.3); do awk -F'\t' -v i=$id '$1==i' $E/.probe.3; done | awk -F'\t' '$3~/UserNotificationCenter|universalAccessAuthWarn|SecurityAgent|tccd|System Settings/' | wc -l | tr -d ' ')"
echo "a window number and its owner, the first three lines of reading 1 (number, owner pid, owner):"
head -3 $E/.probe.1
rm -f $E/.probe.* $E/.ids.*
date -u +%Y-%m-%dT%H:%M:%SZ
