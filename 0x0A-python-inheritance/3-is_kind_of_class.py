#!/usr/bin/python3
"""
Module 3-is_kind_of_class:

This module includes the `is_kind_of_class` method.
It checks if an object is an instance of a class or a class that it
inherited from and returns `True` if it is.
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
- To determine the specific class of an object, use `type()`.
- To check if an object is an instance of a class or any of its
parent classes, use `isinstance()`.
- To check if one class is a subclass of another, use `issubclass()`.

Return:
- The method returns `True` if the object is an instance of
a class that it inherited from.
    """
    return isinstance(obj, a_class)
