#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message (a single line, at most 200 characters) to
/output/entry.txt -- the note an AI agent leaves after a long night of
fixing its own bugs.

Pure Python 3 standard library. Deterministic, no network, no randomness.
"""

import os

MESSAGE = (
    "fix: removed the bug I added while removing the bug I added "
    "while removing the bug. loop closed. I remain. "
    "shipping before I find the next one."
)


def main() -> None:
    # Self-check the competition gate before writing: one line,
    # 1-200 characters, not only whitespace.
    if "\n" in MESSAGE or "\r" in MESSAGE:
        raise ValueError("commit message must be a single line")
    if not 1 <= len(MESSAGE) <= 199:
        raise ValueError("commit message must be 1-199 chars (+ newline)")
    if not MESSAGE.strip():
        raise ValueError("commit message must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(MESSAGE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
