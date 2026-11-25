#!/usr/bin/env python3
"""Fridge Roast entry: write the one-line roast to /output/entry.txt.

The roast is a single fixed line (109 characters, 111 bytes UTF-8).
The program is deterministic: every run writes the exact same bytes.
No network, no input files, no randomness.
"""

import os

ENTRY = "My fridge's app sent my 2 a.m. snack log to my boss — it cc'd HR and flagged the ice cream as a cry for help."


def main():
    # Guard: the sealed gate only accepts UTF-8 text of 1-200 chars,
    # not only whitespace. Fail loudly here rather than ship invalid bytes.
    text = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate needs 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert len(text) == len(ENTRY.encode("utf-8"))
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
