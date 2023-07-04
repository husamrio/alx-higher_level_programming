#!/usr/bin/python3
"""
Rectangle Module
Contains Rectangle class with private attributes width and height,
and public methods for area and perimeter.
"""


class Rectangle:
    """
    Rectangle class with private attributes width and height.

    Args:
        width (int): Width of the rectangle
        height (int): Height of the rectangle

    Methods:
        __init__(self, width, height)
        get_width(self)
        set_width(self, value)
        get_height(self)
        set_height(self, value)
        area(self)
        perimeter(self)
    """

    def __init__(self, width=0, height=0):
        """Initialize a rectangle."""
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        """Get the width of the rectangle."""
        return self.__width

    def set_width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0.")
        self.__width = value

    def get_height(self):
        """Get the height of the rectangle."""
        return self.__height

    def set_height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0.")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
