#!/usr/bin/python3
"""
Module 0-add_integer
Calculates the sum of two numbers and returns it as an integer
"""


def add_integer(a, b=98):
    """
    Calculates the sum of a and b and returns it as an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
