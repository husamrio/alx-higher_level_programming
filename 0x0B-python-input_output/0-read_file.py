#!/usr/bin/python3
"""

Reads the contents of a file and outputs them to the screen.
"""


def read_file(filename=""):
    """Reads the contents of a file and outputs them to the screen."""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
