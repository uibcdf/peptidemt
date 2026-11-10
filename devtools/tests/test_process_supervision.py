"""Real Linux regression for RSS accounting across thread-created children."""

import importlib.util
import os
import queue
import subprocess
import sys
import threading
from pathlib import Path


def resident_bytes(pid):
    return next(
        int(line.split()[1]) * 1024
        for line in Path(f"/proc/{pid}/status").read_text().splitlines()
        if line.startswith("VmRSS:")
    )


def test_rss_includes_child_created_by_secondary_thread():
    path = Path(__file__).resolve().parents[2] / "src/peptidemt/_hydramp_process.py"
    spec = importlib.util.spec_from_file_location("process_supervision", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    children = queue.Queue()

    def launch_child():
        child = subprocess.Popen(
            [
                sys.executable,
                "-B",
                "-c",
                "import time; payload=bytearray(32*1024**2); print('ready',flush=True); time.sleep(60)",
            ],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        children.put(child)
        child.wait()

    thread = threading.Thread(target=launch_child)
    thread.start()
    child = children.get(timeout=5)
    try:
        assert child.stdout.readline().strip() == "ready"
        expected = resident_bytes(os.getpid()) + resident_bytes(child.pid)
        observed = module.tree_rss(os.getpid())
        # Permit small allocator/sampling fluctuations, not a missing 32 MiB child.
        assert observed >= expected - 1024**2
    finally:
        child.terminate()
        child.wait(timeout=5)
        child.stdout.close()
        thread.join(timeout=5)
        assert not thread.is_alive()
