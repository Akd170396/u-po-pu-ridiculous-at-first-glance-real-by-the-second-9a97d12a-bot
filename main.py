"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
sounds absurd until the business logic lands: emotional-support chickens
rented to burned-out offices, paid for by HR.
"""

import os
import sys

ENTRY = (
    "We rent emotional-support chickens to burned-out offices by the hour "
    "\u2014 HR pays $40 a cuddle, because one calm hen costs less than a "
    "single burnout claim."
)


def validate(text: str) -> None:
    """Gate mirror: 1-200 chars, one sentence, not only whitespace."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: fail loudly if what landed differs.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise RuntimeError("entry.txt read-back mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
