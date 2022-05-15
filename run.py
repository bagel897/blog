from multiprocessing import Event, Process
from pathlib import Path
from subprocess import run
from time import sleep


def synchronize(path: Path, stopped: Event):
    while not stopped.is_set():
        sleep(10)
        run(["git", "pull"], cwd=path)


event = Event()
watcher = Process(target=synchronize, args=(Path("./blag"), event))
watcher.start()
try:
    run(["pagic", "build", "--watch", "--serve"])
except KeyboardInterrupt:
    event.set()
    watcher.join()
