"""One Line of Earned Pride.

Writes one quiet, earned moment of pride to /output/entry.txt.
The line is fixed, so every run writes the exact same bytes.
"""

import os

PRIDE_LINE = "The old fisherman mended his father's net one last time, then watched his grandson haul it in alone, and smiled like the sea had finally paid him back."

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(PRIDE_LINE) <= 240:
        raise ValueError("pride line must be 1 to 240 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(PRIDE_LINE)


if __name__ == "__main__":
    main()
