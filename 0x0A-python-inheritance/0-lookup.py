#!/usr/bin/python3
"""
Module 0-lookup:

This module contains the `lookup` method, which returns a
list of an object's attributes and methods.
"""


def lookup(obj):
    """Generates a list of the attributes and methods of an object."""
    return dir(obj)
