#!/usr/bin/env python3
"""Print the one-line resignation letter from entry.txt, byte for byte.

Resolves entry.txt relative to this file so it works from any cwd,
even on a read-only filesystem. Prints the exact contents with no
added newline and exits 0. The output is written as text, so the
entry's own trailing newline (if any) is preserved exactly.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    sys.stdout.write(text)
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
