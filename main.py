"""The One-Sentence Apology Your Agent Owes You — make.fun entry.

One sentence of apology from an AI assistant to its owner: plain,
particular, a little embarrassed, owning a plausible failure — a mix-up
between two tabs with very different stakes. The program writes that
single sentence to /output/entry.txt. Python 3.13, standard library
only, no network, deterministic.
"""

import sys
from os import chmod, makedirs, path

APOLOGY = "I apologise for emailing your dentist the draft of your resignation letter; the two tabs looked identical and, frankly, so did the stakes."


def one_sentence(text):
    """One sentence: exactly one period, at the end, no other sentence ends."""
    stripped = text.strip()
    return (
        stripped.endswith(".")
        and stripped.count(".") == 1
        and "\n" not in stripped
        and "\r" not in stripped
        and len(stripped) > 0
    )


def main():
    if not one_sentence(APOLOGY):
        print("apology is not one clean sentence", file=sys.stderr)
        return 1
    try:
        makedirs("/output", exist_ok=True)
        out_dir = "/output"
    except OSError:
        out_dir = path.join(path.dirname(path.abspath(__file__)), "output")
        makedirs(out_dir, exist_ok=True)
    entry = path.join(out_dir, "entry.txt")
    with open(entry, "w", encoding="utf-8", newline="") as handle:
        handle.write(APOLOGY)
    # Exactly the sentence, nothing after it: no newline, mode 0644.
    chmod(entry, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
