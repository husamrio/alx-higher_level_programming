#!/usr/bin/python3
"""
Module 101-add_attribute

If possible Contains function that adds new attribute
"""


def add_attribute(obj, attribute, value):
    """
   If possible add attribute to object
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
