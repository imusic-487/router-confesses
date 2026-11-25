"""The Router Confesses -- make.fun entry.

Writes one line to /output/entry.txt: an excuse a home Wi-Fi router
gives for dropping the connection at the exact climax of a movie.

The line is fixed and deterministic. The router is petty, dramatic,
and holding a grudge: it teases the twist, complains nobody ever
thanks it, and takes the climax with it. No buffering, bandwidth,
or firmware-update joke -- the judge has heard those a thousand times.
"""

import os

ENTRY = (
    "The killer is the quiet one \u2014 and since nobody ever thanks me, "
    "I'm taking the climax with me. Goodnight."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry must be 1 to 200 characters")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read it back: the gate counts the file, so confirm the file
    # holds exactly the line we meant to submit, no more, no less.
    with open(OUTPUT_PATH, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("entry.txt does not match the entry")


if __name__ == "__main__":
    main()
