# Pagination

List endpoints with cursors return a page. Iterating a page fetches the following pages as needed.

```python
for session in client.session.list(limit=50):  # (1)!
    print(session.title)
```

1. `limit` is the page size, not a cap on the total.

To work page by page:

```python
page = client.session.list(limit=50)
page.data  # this page only
page.has_next_page()
next_page = page.next_page()

for page in client.session.list(limit=50).iter_pages():
    print(len(page.data))
```

## Async

Async list methods return an `AsyncPaginator`. `await` it for the first page, or `async for` over it for every item:

```python
first = await client.session.list(limit=50)
async for session in client.session.list(limit=50):
    print(session.title)
```

Endpoints without cursors return a plain list or a response model. The [resources reference](../reference/resources.md)
shows each method's return type.
