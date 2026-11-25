#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single dad joke (at most 200 characters) to /output/entry.txt.
Standard library only.
"""

import os
import sys

ENTRY = "I told the fork it was stirring up trouble. It said, 'Wrong utensil — that's the spoon's job.'"

OUTPUT_FILENAME = "entry.txt"


def main():
    # Gate: text must be 1-200 characters, not only whitespace,
    # and must not end with a trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert not ENTRY.endswith("\n"), "entry must not end with a newline"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)

    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and verify byte-identical output.
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch: output is not byte-identical"
    text = back.decode("utf-8")
    assert 1 <= len(text) <= 200, "written entry must be 1-200 characters"
    assert text.strip(), "written entry must not be only whitespace"
    assert not text.endswith("\n"), "written entry must not end with a newline"

    print("Verified byte-identical read-back ({} bytes).".format(len(back)))
    print("Wrote {} bytes ({} characters) to {}".format(
        len(data), len(ENTRY), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
