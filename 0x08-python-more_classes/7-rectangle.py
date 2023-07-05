#!/usr/bin/python3
"""
Module 7-rectangle
Contains the Rectangle class with private attributes width and height,
public methods for area and perimeter, a method to print using a given symbol,
a deletion method, public attribute to keep track of the number of instances.
"""


class Rectangle():
    """
    Class that represents a rectangle.

    Attributes:
        number_of_instances (int): Number of instances created and not deleted.
        print_symbol (any): Symbol used to print string representation.

    Methods:
        __init__(self, width, height)
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
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with the given width and height."""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Delete an instance of the rectangle."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str.strip()

    def __repr__(self):
        """Return a string representation to recreate the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
