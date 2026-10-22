"""Opens a shell on an OpenCode server and bridges it to this terminal. Exit the shell to quit.

Usage: OPENCODE_BASE_URL=http://127.0.0.1:4096 OPENCODE_PASSWORD=... uv run python examples/terminal.py

Needs the ``pty`` extra (``pip install "opencode-python-sdk[pty]"``) and a POSIX terminal.
"""

from __future__ import annotations

import os
import shutil
import signal
import sys
import termios
import threading
import tty
from typing import Any

from opencode import Opencode, PtyConnection


def pump_input(term: PtyConnection) -> None:
    """Forwards keystrokes to the remote shell."""
    fd = sys.stdin.fileno()
    while data := os.read(fd, 1024):
        term.send(data)


def main() -> None:
    with Opencode() as client:
        pty = client.pty.create(command=os.environ.get("SHELL", "/bin/sh"), title="examples/terminal.py").data
        try:
            with client.pty.attach(pty.id) as term:
                size = shutil.get_terminal_size()
                term.resize(size.columns, size.lines)

                def on_resize(*_: Any) -> None:
                    size = shutil.get_terminal_size()
                    term.resize(size.columns, size.lines)

                signal.signal(signal.SIGWINCH, on_resize)
                saved = termios.tcgetattr(sys.stdin)
                tty.setraw(sys.stdin)
                try:
                    threading.Thread(target=pump_input, args=(term,), daemon=True).start()
                    for chunk in term:
                        os.write(sys.stdout.fileno(), chunk)
                finally:
                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, saved)
        finally:
            client.pty.remove(pty.id)


if __name__ == "__main__":
    main()
