#!/usr/bin/python3
"""
Module 6-rectangle
Contains Rectangle class with width and height attributes,
methods for area and perimeter calculation, printing, and instance count
"""


class Rectangle:
    """
    Represents a rectangle with width and height

    Attributes:
        number_of_instances (int): Number of instances created

    Methods:
        __init__(self, width=0, height=0)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with specified width and height"""
        self._width = width
        self._height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Delete Rectangle and decrease instance count"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Get the width"""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get the height"""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self._height = value

    def area(self):
        """Calculate the area"""
        return self._width * self._height

    def perimeter(self):
        """Calculate the perimeter"""
        return 2 * (self._width + self._height)

    def __str__(self):
        """Return a string representation"""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width for _ in range(self._height)])

    def __repr__(self):
        """Return a string representation for object recreation"""
        return f"Rectangle({self._width}, {self._height})"
