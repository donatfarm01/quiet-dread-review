"""Two Days of Quiet Dread — make.fun bounty entry.

Writes a single code review comment to /output/entry.txt: one line that
approves a pull request while carrying quiet existential dread.
Deterministic: the same line on every run.
"""

import os

ENTRY = "Approved. Tests are green, the diff is tidy, and this code will still be here when none of us are."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
