#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text to /output/entry.txt: a quiet, earned
moment of pride for someone in a scene. The line is a fixed constant;
the program's only job is to check it against the competition gate
and write it out, untouched.
"""

import os

ENTRY = (
    "She sounded out the last word of her grandson's letter, "
    "folded it into her apron pocket, and walked on to the market "
    "like nothing at all had happened."
)

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 240


def gate_check(text):
    """Enforce the competition gate exactly as published.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 240
    characters, not only white space. Returns True when the text
    passes, False otherwise.
    """
    if not isinstance(text, str):
        return False
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    # The entry is one line: no newline or carriage return anywhere.
    if "\n" in text or "\r" in text:
        return False
    # It must survive a UTF-8 round trip byte for byte, since the
    # sealed scorer reads the file as UTF-8 text.
    try:
        if text.encode("utf-8").decode("utf-8") != text:
            return False
    except UnicodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("entry fails the gate check")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
