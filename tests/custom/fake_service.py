"""A stand-in for `opencode serve --service`, used by test_service.py.

Usage: python fake_service.py REGISTRATION_FILE VERSION [MODE]

MODE is ``serve`` (default), ``fail`` (exit 1 with an error on stderr) or ``lose`` (exit 0 without registering, like
a contender that lost the startup race). A serving instance writes the registration file, answers ``GET /api/info``
and the persistent-terminal endpoints, and exits on SIGTERM. It runs without a password: auth is covered by the
mocked probes in test_service.py and by the live test.
"""

from __future__ import annotations

import os
import sys
import json
import uuid
import socketserver
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from typing_extensions import override


def main() -> None:
    file, version = Path(sys.argv[1]), sys.argv[2]
    mode = sys.argv[3] if len(sys.argv) > 3 else "serve"
    if mode == "fail":
        sys.stderr.write("fake service: boom\n")
        sys.exit(1)
    if mode == "lose":
        sys.exit(0)
    handoff_env = os.environ.get("OPENCODE_PTY_HANDOFF")

    class Handler(BaseHTTPRequestHandler):
        def _send(self, status: int, body: object) -> None:
            data = json.dumps(body).encode()
            self.send_response(status)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self) -> None:
            if self.path == "/api/info":
                self._send(200, {"version": version, "pid": os.getpid(), "handoff": handoff_env})
            else:
                self._send(404, {})

        def do_POST(self) -> None:
            if self.path == "/api/experimental/persistent-pty/handoff":
                self._send(200, {"handoff": None})
            else:
                self._send(204 if self.path.endswith("/shutdown") else 404, {})

        @override
        def log_message(self, format: str, *args: object) -> None:
            pass

    class Server(ThreadingHTTPServer):
        @override
        def server_bind(self) -> None:
            # HTTPServer.server_bind resolves the host name with getfqdn, which can stall for many seconds on CI.
            socketserver.TCPServer.server_bind(self)
            self.server_name, self.server_port = "127.0.0.1", self.server_address[1]

    server = Server(("127.0.0.1", 0), Handler)
    url = f"http://127.0.0.1:{server.server_address[1]}"
    file.parent.mkdir(parents=True, exist_ok=True)
    record = {"id": str(uuid.uuid4()), "version": version, "url": url, "pid": os.getpid()}
    temporary = file.with_name(file.name + f".{os.getpid()}.tmp")
    temporary.write_text(json.dumps(record))
    os.replace(temporary, file)
    server.serve_forever()


if __name__ == "__main__":
    main()
