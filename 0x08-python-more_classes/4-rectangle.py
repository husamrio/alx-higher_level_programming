#!/usr/bin/python3
"""
Module 4-refactored-rectangle
Contains the Rectangle class with width and height attributes,
as well as methods for area, perimeter, and displaying the rectangle.
"""


class Rectangle:
    """
    Class that represents a rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height)
        get_width(self)
        set_width(self, value)
        get_height(self)
        set_height(self, value)
        calculate_area(self)
        calculate_perimeter(self)
        display(self)
        __str__(self)
        __repr__(self)
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
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    def get_height(self):
        """Get the height of the rectangle."""
        return self.__height

    def set_height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def calculate_area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def calculate_perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def display(self):
        """Display the rectangle as a string of '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __str__(self):
        """Return a string representation of the rectangle."""
        return self.display()

    def __repr__(self):
        """Return a string representation of the rectangle
        that can be used to recreate it."""
        return f"Rectangle({self.get_width()}, {self.get_height()})"
