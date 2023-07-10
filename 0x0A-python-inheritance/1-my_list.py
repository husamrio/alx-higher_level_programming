#!/usr/bin/python3
"""
Module 1-my_list:

This module contains the `MyList` class, which inherits from the `list` class.
It has a public instance method for printing a sorted version of the list.

"""


class MyList(list):
    """Inherits from the `list` class.

Methods:
- `print_sorted(self)`: Prints a sorted version of the list.
    """
    def print_sorted(self):
        """prints list of ints all sorted in ascending order"""
        print(sorted(self))
