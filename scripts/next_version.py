"""Prints the next release version, or nothing when there is nothing to release.

Every merge to main that changes the package is released (rolling releases). The bump follows
Conventional Commits in the commit subjects since the last ``vX.Y.Z`` tag:

- ``feat!:`` / ``fix!:`` or a ``BREAKING CHANGE:`` footer: major (minor while below 1.0)
- ``feat:``: minor
- anything else: patch

Commits that only touch docs, tests or CI do not trigger a release. With no tag yet, the first
release is 0.1.0.

Usage: python scripts/next_version.py [--force]
"""

from __future__ import annotations

import re
import subprocess
import sys

RELEASE_PATHS = ("src/", "pyproject.toml", "spec/")
BREAKING = re.compile(r"^[a-z]+(\([^)]*\))?!:", re.IGNORECASE)
FEATURE = re.compile(r"^feat(\([^)]*\))?:", re.IGNORECASE)


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout.strip()


def latest_tag() -> str | None:
    tags = git("tag", "--list", "v[0-9]*.[0-9]*.[0-9]*", "--sort=-v:refname").splitlines()
    return tags[0] if tags else None


def main() -> int:
    force = "--force" in sys.argv
    tag = latest_tag()
    if tag is None:
        print("0.1.0")
        return 0

    revision = f"{tag}..HEAD"
    changed = git("diff", "--name-only", revision).splitlines()
    if not force and not any(path.startswith(RELEASE_PATHS) for path in changed):
        return 0  # nothing user-facing changed

    subjects = git("log", "--format=%s", revision).splitlines()
    bodies = git("log", "--format=%b", revision)
    major, minor, patch = (int(part) for part in tag.removeprefix("v").split("."))

    if any(BREAKING.match(subject) for subject in subjects) or "BREAKING CHANGE:" in bodies:
        if major == 0:
            minor, patch = minor + 1, 0
        else:
            major, minor, patch = major + 1, 0, 0
    elif any(FEATURE.match(subject) for subject in subjects):
        minor, patch = minor + 1, 0
    else:
        patch += 1
    print(f"{major}.{minor}.{patch}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
