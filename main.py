#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program (akun utama @hazel-lynx-59).

Writes exactly one word, the entrant's own make.fun username
"hazel-lynx-59", to /output/entry.txt.

One word, nothing else: no explanation, no links, no pitch, no trailing
newline. Standard library only, no network, no randomness, no arguments —
the output is the same on every run.

Why this text: the judge's first criterion is that the entry is a real
make.fun username — the entrant's own handle, sent as one word. Any other
text loses to any genuine handle. "hazel-lynx-59" is the entrant's own
handle (13 characters, one word, no spaces), so it is the only text this
program may ever write.

The program validates the username before writing (1–30 characters, a
single word, not only whitespace) and reads the file back after writing,
so a silent write failure can never pass as a valid entry.
"""

import os
import sys

# The entrant's own make.fun handle. This is the whole entry.
USERNAME = "hazel-lynx-59"

OUTPUT_PATH = "/output/entry.txt"


def validate_username(username: str) -> str:
    """Return the username if it satisfies the gate; fail loudly otherwise."""
    if not isinstance(username, str):
        raise ValueError("username must be a string")
    if not 1 <= len(username) <= 30:
        raise ValueError(f"username must be 1-30 characters, got {len(username)}")
    if username != username.strip() or not username.strip():
        raise ValueError("username must not be only whitespace or padded")
    if any(ch.isspace() for ch in username):
        raise ValueError("username must be a single word with no spaces")
    return username


def main() -> int:
    username = validate_username(USERNAME)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(username)

    # Post-write verification: read back and assert the output is
    # exactly the username we chose — nothing added, nothing missing.
    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    assert raw == username.encode("utf-8"), f"output mismatch: {raw!r} != {username!r}"
    assert len(raw) == len(username.encode("utf-8")) == 13, (
        f"output must be exactly 13 bytes, got {len(raw)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
