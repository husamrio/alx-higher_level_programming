#!/usr/bin/python3
"""
Module 2-is_same_class:

This module includes the `is_same_class` method.
It checks if an object is an exact instance of a specified class and returns
`True` if it is.
"""


def is_same_class(obj, a_class):
    """
   Notes:
- To determine the specific class of an object, use `type()`.
- To check if an object is an instance of a class or any of its parent
classes, use `isinstance()`.
- To check if one class is a subclass of another, use `issubclass()`.

Return:
- The method returns `True` if the object is exactly an
instance of the specified class.
    """
    return type(obj) == a_class