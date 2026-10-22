# Async

`AsyncOpencode` has the same resources and methods as `Opencode`. Methods return awaitables, list methods return an
`AsyncPaginator`, and streams return an `AsyncStream`. It runs on [AnyIO](https://anyio.readthedocs.io), so it works
under both asyncio and trio.

=== "asyncio"

    ```python
    import asyncio
    from opencode import AsyncOpencode


    async def main() -> None:
        async with AsyncOpencode("http://127.0.0.1:4096") as client:
            session = await client.session.create(title="Async")
            await client.session.prompt(session.id, text="Hello")
            async for message in client.message.list(session.id):
                print(message.type)


    asyncio.run(main())
    ```

=== "trio"

    ```python
    import trio
    from opencode import AsyncOpencode


    async def main() -> None:
        async with AsyncOpencode("http://127.0.0.1:4096") as client:
            info = await client.server.info()
            print(info.version)


    trio.run(main)
    ```

## Concurrency

One client can serve many concurrent tasks; it shares one connection pool.

```python
import asyncio


async def titles(client: AsyncOpencode, ids: list[str]) -> list[str]:
    sessions = await asyncio.gather(*(client.session.get(i) for i in ids))
    return [s.title for s in sessions]
```

## Pages and streams

```python
page = await client.session.list(limit=20)  # (1)!
async for session in client.session.list():  # (2)!
    ...

async with await client.event.subscribe() as events:  # (3)!
    async for event in events:
        print(event.type)
```

1. `await` the paginator for the first page.
2. `async for` over it for every item across pages.
3. `subscribe()` returns an `AsyncStream` once awaited.
