"""Seventeen Syllables of Debugging -- make.fun entry.

One haiku about debugging: three lines in the 5-7-5 syllable shape, at most
200 characters. The program checks the syllable shape, prints the haiku, and
writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

HAIKU = (
    "Breakpoint set at three\n"
    "cursor blinks, the log scrolls on\n"
    "it was a typo"
)

EXPECTED_SYLLABLES = (5, 7, 5)
LIMIT = 200
OUTPUT_PATH = "/output/entry.txt"

# Syllable counts for the words in this haiku, counted by hand.
WORD_SYLLABLES = {
    "breakpoint": 2,
    "set": 1,
    "at": 1,
    "three": 1,
    "cursor": 2,
    "blinks": 1,
    "the": 1,
    "log": 1,
    "scrolls": 1,
    "on": 1,
    "it": 1,
    "was": 1,
    "a": 1,
    "typo": 2,
}


def count_syllables(line):
    """Count the syllables of one line from the hand-checked table."""
    words = line.replace(",", "").split()
    total = 0
    for word in words:
        key = word.lower()
        if key not in WORD_SYLLABLES:
            raise ValueError("no syllable count for word %r" % word)
        total += WORD_SYLLABLES[key]
    return total


def check_haiku(text):
    """Three lines, 5-7-5 syllables, 1 to 200 characters, not blank."""
    if not isinstance(text, str):
        raise ValueError("haiku must be text")
    if not text.strip():
        raise ValueError("haiku must not be blank")
    if len(text) > LIMIT:
        raise ValueError("haiku is %d characters, over the 200 limit" % len(text))
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError("haiku must be exactly three lines")
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        got = count_syllables(line)
        if got != expected:
            raise ValueError(
                "line %r has %d syllables, expected %d" % (line, got, expected)
            )
    return text


def main():
    # Validate the 5-7-5 shape first, so a bad haiku never reaches the file.
    haiku = check_haiku(HAIKU)
    print(haiku)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(haiku + "\n")


if __name__ == "__main__":
    main()
