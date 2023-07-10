#!/usr/bin/python3
"""
Module 7-base_geometry:

This module contains the `BaseGeometry` class, which has
public instance methods called `area` and `integer_validation`.
"""


class BaseGeometry:
    """
    Methods:
- `area(self)`: Calculates the area of the shape.
- `integer_validator(self, name, value)`: Validates that `value`
is an integer and raises an exception if it is not.
    """
    def area(self):
        """Not implemented at this time"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input as a parameter integer
        Args:
            name (str): assumed always the parameter string
            value (int): when greater than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
