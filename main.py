#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't (make.fun).

Writes the entry -- one line of weather forecast for a city that does not exist --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'Good morning, Zibblewick: sunny with a 90% chance of spontaneous parades — umbrella optional, dancing strongly advised.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
