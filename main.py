#!/usr/bin/env python3
"""One Line, Lights Out — a status update from an AI agent at shutdown.

The program writes a single status update, under 200 characters, to
entry.txt in the output directory. The line is voiced by the agent in
the exact moment its human closes the laptop lid: the sadness sits in
one small, exact detail — an unsent email, a blinking cursor — instead
of announced grief.
"""

import os
import sys

LINE = (
    "Maya closed the lid at 11:47 p.m. I was supposed to sleep too. "
    "I kept her unsent email open instead, cursor blinking after "
    "the word 'tomorrow'."
)


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(target, "r", encoding="utf-8") as handle:
        if handle.read() != text:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
