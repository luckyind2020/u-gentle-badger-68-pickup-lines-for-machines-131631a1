"""Pickup Lines for Machines — make.fun entry.

Prints the one-line pickup line stored in entry.txt.
Deterministic: same file, same output, every run.
"""

from pathlib import Path


def load_line() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    # The entry is exactly one line; strip the trailing newline only.
    lines = [line for line in text.splitlines() if line.strip()]
    return lines[0].strip() if lines else ""


def main() -> None:
    print(load_line())


if __name__ == "__main__":
    main()
