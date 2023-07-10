#!/usr/bin/python3
"""
Module 4-inherits_from.py:

This module includes the `inherits_from` method. It checks
if an object is an instance
of a class that it inherits from or is a subclass of and
returns `True` if it is.
"""


def inherits_from(obj, a_class):
    """
    Notes:
- To determine the specific class of an object, use `type()`.
- To check if an object is an instance of a class or any of its
parent classes, use `isinstance()`.
- To check if one class is a subclass of another, use `issubclass()`.

Return:
- The method returns `True` if the object is an instance of a class
that it inherits from or is a subclass of.
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
