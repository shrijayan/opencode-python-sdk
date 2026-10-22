# Security policy

## Reporting a vulnerability

Please report vulnerabilities privately through
[GitHub security advisories](https://github.com/shrijayan/opencode-python-sdk/security/advisories/new). Do not open
a public issue. You should receive a reply within a few days.

For vulnerabilities in the OpenCode server itself, report to the
[OpenCode project](https://github.com/anomalyco/opencode/security).

## Handling of credentials

- The server password is only sent in the `Authorization` header. It never appears in `repr()`, logs or exception
  messages.
- Response validation errors report field locations and reasons, not values.
- `OpencodeServer` passes the password to the child process through `OPENCODE_PASSWORD`, which the server removes
  from the environment its tools inherit.
