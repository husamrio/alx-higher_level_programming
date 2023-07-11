#!/usr/bin/python3
"""

Writes data to a text file and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes data to a text file and returns the number of
    characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
