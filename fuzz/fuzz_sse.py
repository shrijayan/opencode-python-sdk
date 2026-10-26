"""Atheris fuzz target for the server-sent-events decoder.

Run with: uv run --with atheris python fuzz/fuzz_sse.py
"""

import sys

import atheris

with atheris.instrument_imports():
    from opencode._streaming import SSEDecoder


def test_one_input(data: bytes) -> None:
    """Feed arbitrary bytes through the SSE decoder, as the response stream would."""
    chunks = [data[i : i + 7] for i in range(0, len(data), 7)]
    for _ in SSEDecoder().iter_bytes(iter(chunks)):
        pass


if __name__ == "__main__":
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()
