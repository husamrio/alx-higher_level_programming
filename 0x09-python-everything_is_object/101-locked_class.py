#!/usr/bin/python3
"""
Defines locked class or object attribute
https://www.python-course.eu/python3_slots.php
"""


class LockedClass():
    """
    prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"

    >>> a = LockedClass()
    >>> a.first_name = 'Hussein'
    'Hussein'

    >>> a.last_name = 'Wario'
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
