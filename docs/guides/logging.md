# Logging

The client logs to the `opencode` logger with the standard `logging` module. It is silent unless you configure it.

```python
import logging

logging.basicConfig()
logging.getLogger("opencode").setLevel(logging.DEBUG)
```

| Level | What is logged |
| --- | --- |
| `DEBUG` | Every request and response: method, URL, attempt, status |
| `INFO` | Retries, with the delay and the reason |

Credentials are never logged. The password only travels in the `Authorization` header and never appears in
`repr()`, log lines or exception messages.
