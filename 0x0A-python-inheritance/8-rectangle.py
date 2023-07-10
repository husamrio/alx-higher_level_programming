#!/usr/bin/python3
"""
Module 8-rectangle:

This module contains two classes: `BaseGeometry` and `Rectangle`.

`BaseGeometry` has public instance methods `area` and `integer_validator`.

`Rectangle` is a subclass of `BaseGeometry` and has private attributes
`width` and `height`, which are validated by the parent class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
This class inherits from the BaseGeometry class and has the
following methods:
    - __init__(self, width, height): Initializes a new instance
    of the class with the given width and height.
"""

    def __init__(self, width, height):
        """
This method validates and initializes the width and height of the object.
Args:
    width (int): The width of the object, which is a private attribute.
    height (int): The height of the object, which is a private attribute.
"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
