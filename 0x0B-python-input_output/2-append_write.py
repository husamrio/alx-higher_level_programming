#!/usr/bin/python3
"""
Module 2-read_lines contains a function that reads a specified
number of lines from a file and outputs them to the screen.
"""


def read_lines(filename="", nb_lines=0):
    """Reads a specified number of lines from a file and
    outputs them to the screen. If the specified number is
    less than 1 or greater than the total number of lines in the
    file, the entire file is printed
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            while nb_lines:
                print(f.readline(), end="")
                nb_lines -= 1
