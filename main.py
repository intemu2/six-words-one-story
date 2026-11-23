#!/usr/bin/env python3
"""Six Words, One Story -- make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt.
Deterministic, standard library only. No network, no input, no randomness.
"""

from pathlib import Path

STORY = "The baby's first word was goodbye."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the six-word story, no trailing newline.
    output.write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
