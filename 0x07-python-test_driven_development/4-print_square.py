#!/usr/bin/python3
"""
Prints squares with #'s
Accepts an int size
4-print_square module
"""


def print_square(size):
    """
    Prints square with #'s given int size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
