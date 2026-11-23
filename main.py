#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. No network, no dependencies, no input: the joke is
fixed in this file, so the program is deterministic.
"""

import os

# The em dash is a single Unicode code point, so the joke stays well
# under the 280-code-point limit at 78 characters.
JOKE = "The demo crashed, so my agent debugged it live \u2014 and filed the bug against me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    if not text or not (1 <= len(text) <= 280):
        raise SystemExit("joke must be 1-280 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
