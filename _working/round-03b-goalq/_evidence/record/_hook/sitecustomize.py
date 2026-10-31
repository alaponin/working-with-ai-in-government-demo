# written by round_record.py: traces the files a Python program opens

def _round_record_install():
    import os, sys, json, datetime
    log = os.environ.get("ROUND_RECORD_LOG")
    if not log or getattr(sys, "_round_record_installed", False):
        return
    sys._round_record_installed = True
    run = os.environ.get("ROUND_RECORD_RUN", "?")
    record_dir = os.environ.get("ROUND_RECORD_DIR", "")
    itself = os.environ.get("ROUND_RECORD_SELF", "")
    fd = os.open(log, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
    skip = tuple(sorted({os.path.realpath(p) + os.sep for p in
                         (sys.prefix, sys.base_prefix, sys.exec_prefix, sys.base_exec_prefix)}))
    # the system's own files, which no round reads as evidence: devices, settings, libraries; on
    # Windows, the folder of Windows itself and of the programs installed (compared with forward
    # slashes, as every path is below)
    system = ("/dev/", "/etc/", "/private/etc/", "/System/", "/usr/", "/Library/",
              "/opt/homebrew/", "/proc/", "/sys/")
    if os.name == "nt":
        system += tuple(os.path.realpath(v).replace("\\", "/").rstrip("/") + "/"
                        for v in (os.environ.get(k) for k in ("SystemRoot", "ProgramFiles",
                                                              "ProgramFiles(x86)", "ProgramData"))
                        if v)
        skip = tuple(s.replace("\\", "/") for s in skip)
    wflags = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
    busy = [False]
    utc = datetime.timezone.utc
    def now():
        return datetime.datetime.now(utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    def put(obj):
        obj.update({"t": now(), "run": run, "pid": os.getpid()})
        os.write(fd, (json.dumps(obj) + "\n").encode("utf-8"))
    def emit(event, path, write):
        if isinstance(path, bytes):
            path = os.fsdecode(path)
        if not isinstance(path, str) or not path:
            return
        p = os.path.realpath(os.path.abspath(path))
        if os.name == "nt":
            p = p.replace("\\", "/")
        if p.startswith(skip) or p.startswith(system) or p.endswith(".pyc") or "/__pycache__/" in p:
            return
        if "/site-packages/" in p or "/dist-packages/" in p:
            return
        if record_dir and (p == record_dir or p.startswith(record_dir + ("/" if os.name == "nt" else os.sep))):
            return
        if p == itself:
            return
        put({"event": event, "path": p, "write": write})
    def hook(event, args):
        if busy[0]:
            return
        busy[0] = True
        try:
            if event == "open":
                path, mode, flags = args
                if isinstance(path, int):
                    return
                if os.path.isdir(path):  # a directory opened to list it is not a file read
                    return
                if isinstance(mode, str):
                    write = any(c in mode for c in "wax+")
                else:
                    write = bool(flags & wflags) if isinstance(flags, int) else False
                emit("open", path, write)
            elif event == "os.rename":
                emit("rename-from", args[0], True)
                emit("rename-to", args[1], True)
            elif event == "os.remove":
                emit("remove", args[0], True)
            elif event == "shutil.copyfile":
                emit("copy-from", args[0], False)
                emit("copy-to", args[1], True)
            elif event in ("subprocess.Popen", "os.posix_spawn", "os.exec", "os.system"):
                argv = args[1] if event != "os.system" else args[0]
                if isinstance(argv, (list, tuple)):
                    argv = [os.fsdecode(a) if isinstance(a, bytes) else str(a) for a in argv]
                else:
                    argv = os.fsdecode(argv) if isinstance(argv, bytes) else str(argv)
                put({"event": "spawn", "argv": argv})
        except Exception:
            pass
        finally:
            busy[0] = False
    sys.addaudithook(hook)

_round_record_install()
