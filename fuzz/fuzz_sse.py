"""Atheris fuzz target for the server-sent-events decoder.

Run with: uv run --with atheris python fuzz/fuzz_sse.py
"""

import sys

import atheris

with atheris.instrument_imports():
    from opencode._streaming import _Decoder, _LineSplitter


def test_one_input(data: bytes) -> None:
    """Feed arbitrary text through the line splitter and SSE decoder."""
    text = atheris.FuzzedDataProvider(data).ConsumeUnicodeNoSurrogates(len(data))
    splitter = _LineSplitter()
    decoder = _Decoder()
    for line in splitter.feed(text) + splitter.flush():
        decoder.feed_line(line)


if __name__ == "__main__":
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()
