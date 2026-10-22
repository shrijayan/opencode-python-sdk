# Versioning and releases

| `opencode-python-sdk` | OpenCode server |
| --- | --- |
| 0.1.x | 2.1.x |

`opencode.API_VERSION` is the server version the client was generated from.

The package follows [semantic versioning](https://semver.org). Until 1.0, minor versions may contain breaking changes;
each is noted in the [changelog](changelog.md).

## Compatibility with newer servers

A client keeps working when the server is upgraded within a major version: new fields, enum values, union variants
and event types are kept rather than rejected. See [forward compatibility](../guides/models.md#forward-compatibility).

## Releases

Releases are published to [PyPI](https://pypi.org/project/opencode-python-sdk/) from GitHub Actions with trusted
publishing and build attestations, so no API token is stored in the repository.
