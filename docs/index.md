---
title: Typed Python client for OpenCode
description: opencode-python-sdk is a typed, sync and async Python client for the OpenCode 2.x server API.
hide:
  - navigation
  - toc
---

<div class="oc-hero" markdown>
<div markdown>

<span class="oc-chip">v{{ version }}</span> <span class="oc-eyebrow">for OpenCode server {{ api_version }}</span>

# Drive OpenCode from Python, <em>fully typed.</em>

<p class="oc-lede">All 142 operations of the OpenCode server API, sync and async, with pydantic models for every
request, response and event. Generated from the same contract as the official TypeScript client.</p>

<div class="oc-install" markdown>

```bash
pip install opencode-python-sdk
```

</div>

<div class="oc-badges" markdown>
[![PyPI](https://img.shields.io/pypi/v/opencode-python-sdk?color=d9730d&label=pypi)](https://pypi.org/project/opencode-python-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/opencode-python-sdk?color=0f6e6a)](https://pypi.org/project/opencode-python-sdk/)
[![CI](https://github.com/shrijayan/opencode-python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/shrijayan/opencode-python-sdk/actions/workflows/ci.yml)
</div>

<div class="oc-actions" markdown>
[Get started](getting-started/index.md){ .md-button .md-button--primary }
[API reference](reference/index.md){ .md-button }
</div>

</div>
<div markdown>

=== "Sync"

    ```python
    from opencode import OpencodeServer

    with OpencodeServer(cwd="/path/to/repo") as server:  # (1)!
        client = server.client()
        session = client.session.create(title="Review")
        client.session.prompt(session.id, text="Summarize the open TODOs")
        client.session.wait(session.id)

        for message in client.message.list(session.id):  # (2)!
            print(message.type)
    ```

    1. Starts `opencode serve` on a free port with a random password, and stops it on exit.
    2. Iterating a page fetches the following pages as needed.

=== "Async"

    ```python
    import asyncio
    from opencode import AsyncOpencode


    async def main() -> None:
        async with AsyncOpencode("http://127.0.0.1:4096") as client:
            session = await client.session.create(title="Review")
            await client.session.prompt(session.id, text="Hello")

            async for message in client.message.list(session.id):
                print(message.type)


    asyncio.run(main())  # (1)!
    ```

    1. Works with asyncio and trio.

</div>
</div>

<div class="oc-grid" markdown>
<div markdown>
<span class="oc-num">01</span>

### Complete

Every operation of the OpenCode 2.1 API, on `Opencode` and `AsyncOpencode`, with 96 typed event classes.
</div>
<div markdown>
<span class="oc-num">02</span>

### Generated from the source

The contract is exported from OpenCode's own Effect `HttpApi`, so names and shapes match the TypeScript client.
</div>
<div markdown>
<span class="oc-num">03</span>

### Safe retries

Only retries when a request cannot have changed server state. A prompt is never sent twice.
</div>
<div markdown>
<span class="oc-num">04</span>

### Forward compatible

New fields, enum values, union variants and events from newer servers are kept, not rejected.
</div>
<div markdown>
<span class="oc-num">05</span>

### Typed errors

Every error the server declares is its own exception class with a typed body.
</div>
<div markdown>
<span class="oc-num">06</span>

### Batteries included

Launch `opencode serve`, paginate lists, and stream server-sent events with one call each.
</div>
</div>

## Where to next { .oc-section-title }

- [Connect to a server](getting-started/connect.md) you already run, or [start one from Python](getting-started/server.md).
- Read the [sessions and prompts guide](guides/sessions.md) for the core workflow.
- Browse the [API reference](reference/index.md), or search it with ++slash++.
- Using an LLM? Point it at [`llms.txt`](https://shrijayan.github.io/opencode-python-sdk/llms.txt) or [`llms-full.txt`](https://shrijayan.github.io/opencode-python-sdk/llms-full.txt).

!!! note "Unofficial"

    This package is community-maintained and not affiliated with or endorsed by the OpenCode team. If the OpenCode
    maintainers want to take it over, the repository and the PyPI name will be transferred.
