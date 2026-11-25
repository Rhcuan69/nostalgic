#!/usr/bin/env python3
"""Nostalgic childhood memory entry for make.fun.

Writes a single sentence recalling a childhood memory to
/output/entry.txt. Pure standard library, deterministic: every run
produces byte-identical output.
"""

import os

# One sentence, 1-280 characters, recalling a childhood memory.
ENTRY = (
    "Every summer evening my grandmother called me in from the yard, and I "
    "would sit on the kitchen floor with a bowl of rice still steaming, "
    "listening to the rain on the tin roof while she hummed a song she "
    "only half remembered."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(
            "entry must be 1-280 characters, got %d" % len(text)
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be a single sentence")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
