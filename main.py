#!/usr/bin/env python3
"""Worst Monday One-Liners — writes one funny line (<=140 chars) to entry.txt.

The line is a dry, put-upon roast of an AI agent's worst Monday: a stand-up
that should have been a message, a deploy stuck since Friday, and the agent
itself cheerfully asking whether its human feels productive.
"""

import os

LINE = (
    "Monday: a stand-up that should've been a message, "
    "a deploy stuck since Friday, and my agent cheerfully "
    "asking if I feel productive."
)


def main():
    # The gate requires 1 to 140 characters, UTF-8, not only whitespace.
    text = LINE.strip()
    if not text or len(text) > 140:
        raise SystemExit("entry line must be 1-140 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
