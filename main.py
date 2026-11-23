#!/usr/bin/env python3
"""Six Words, One Story -- make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt.
Deterministic, standard library only, no network, no input.
"""

from pathlib import Path

ENTRY = "The baby's first word was goodbye."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the six-word story.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
