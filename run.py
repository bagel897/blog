from multiprocessing import Event, Process
from pathlib import Path
from shutil import which
from subprocess import run
from time import sleep


def synchronize(path: Path, stopped: Event):
    while not stopped.is_set():
        sleep(10)
        run(["git", "pull"], cwd=path)


if which("deno") is None:
    run(executable="paru", args=[" -s", "deno", " --sudoloop" " --noconfirm"])
path = Path.home() / ".deno/bin/pagic"
if not path.exists():
    run(
        [
            "deno",
            "install",
            "--unstable",
            "--allow-read",
            "--allow-write",
            "--allow-net",
            "--allow-run",
            "--name=pagic",
            "https://deno.land/x/pagic/mod.ts",
        ],
    )
event = Event()
watcher = Process(target=synchronize, args=(Path("./blag"), event))
watcher.start()
try:
    run([path.as_posix(), "build", "--watch", "--serve"])
except KeyboardInterrupt:
    event.set()
    watcher.join()
