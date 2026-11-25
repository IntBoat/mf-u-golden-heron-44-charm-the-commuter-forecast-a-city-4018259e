#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Good morning, Zorblax: sunny, with a 90% chance your train actually arrives — and the pigeons have agreed to share the platform."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
