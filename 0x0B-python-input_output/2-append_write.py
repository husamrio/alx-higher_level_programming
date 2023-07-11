#!/usr/bin/python3
"""Module 2-read_lines contains a function that reads a specified
number of lines from a file and outputs them to the screen.."""


def append_write(filename="", text=""):
    """Reads a specified number of lines from a file and
    outputs them to the screen. If the specified number is
    less than 1 or greater than the total number of lines in the
    file, the entire file is printed.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
