// The reviewer's own reading of the list of windows (not the round's code).
// CGWindowListCopyWindowInfo, every window (on screen or not), one line each:
// number, owner pid, owner name, layer, on screen (1/0).
ObjC.import('CoreGraphics');
function run() {
  var a = ObjC.castRefToObject($.CGWindowListCopyWindowInfo($.kCGWindowListOptionAll, $.kCGNullWindowID));
  var out = [];
  for (var i = 0; i < a.count; i++) {
    var d = a.objectAtIndex(i);
    var on = d.objectForKey('kCGWindowIsOnscreen');
    out.push([
      ObjC.unwrap(d.objectForKey('kCGWindowNumber')),
      ObjC.unwrap(d.objectForKey('kCGWindowOwnerPID')),
      ObjC.unwrap(d.objectForKey('kCGWindowOwnerName')),
      ObjC.unwrap(d.objectForKey('kCGWindowLayer')),
      on ? (ObjC.unwrap(on) ? 1 : 0) : 0
    ].join('\t'));
  }
  return out.join('\n');
}
