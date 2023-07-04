#!/usr/bin/python3
"""
Module 2-rectangle
Contains class Rectangle with private attribute width and height,
and public area and perimeter methods
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self._width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ Getter returns height """
        return self._height

    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """ Return width * height """
        return self._width * self._height

    def perimeter(self):
        """ Return 2*width + 2*height (or return 0 if width or height is 0)"""
        if self._width == 0 or self._height == 0:
            return 0
        return (2 * self._width) + (2 * self._height)
