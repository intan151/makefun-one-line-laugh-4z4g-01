#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry.

Writes exactly one funny line of text to /output/entry.txt.
Standard library only, no network, deterministic.
"""
import os

JOKE = (
    "I bought a standing desk to sit less \u2014 now I just stand still "
    "and scroll, like a very upright potato."
)

MAX_CHARS = 140


def main() -> None:
    text = JOKE
    # Gate checks from RULES.txt: 1-140 chars, UTF-8, not only whitespace,
    # a single self-contained line.
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    # Extra validation: no stray leading/trailing whitespace (it would count
    # toward the 140-char gate and add nothing to the joke), and the text
    # must survive a UTF-8 round-trip unchanged.
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert text.encode("utf-8").decode("utf-8") == text, "entry must be UTF-8"
    out_path = os.path.join("/output", "entry.txt")
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
