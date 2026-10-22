"""Starts a local OpenCode server, runs one prompt, and prints the conversation.

Usage: uv run python examples/quickstart.py /path/to/repo "What does this project do?"
"""

from __future__ import annotations

import sys

from opencode import OpencodeServer
from opencode.types import SessionMessageAssistant, SessionMessageUser


def main(directory: str, prompt: str) -> None:
    with OpencodeServer(cwd=directory) as server, server.client() as client:
        session = client.session.create(title="Quickstart")
        client.session.prompt(session.id, text=prompt)
        client.with_options(timeout=None).session.wait(session.id)

        for message in client.message.list(session.id):
            if isinstance(message, SessionMessageUser):
                print(f"> {message.text}")
            elif isinstance(message, SessionMessageAssistant):
                print(message.to_json(indent=2))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".", sys.argv[2] if len(sys.argv) > 2 else "Summarize this repository.")
