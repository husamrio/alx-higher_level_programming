#!/usr/bin/python3
"""

This function returns a dictionary representation of an object,
using simple data structures such as lists, dictionaries, and
strings, for the purpose of JSON serialization.
"""


def class_to_json(obj):
    """This function takes a Python object as an argument and
    returns a dictionary representation of it, using simple data
    structures such as lists, dictionaries, and strings, for the
    purpose of JSON serialization
    """
    return obj.__dict__
