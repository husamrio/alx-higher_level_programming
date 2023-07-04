#!/usr/bin/python3
"""Defines a Rectangle class with private attribute width and height."""


class Rectangle:
    def __init__(self, width=0, height=0):
        # Initialize width and height attributes
        self.__width = 0
        self.__height = 0
        # Set the width and height using the property setters
        self.width = width
        self.height = height

    @property
    def width(self):
        # Getter for width
        return self.__width

    @width.setter
    def width(self, value):
        # Setter for width
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        # Getter for height
        return self.__height

    @height.setter
    def height(self, value):
        # Setter for height
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        # Calculate and return the area of the rectangle
        return self.__width * self.__height

    def perimeter(self):
        # Calculate and return the perimeter of the rectangle
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        # Return a string representation of the rectangle using '#' characters
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        # Return a string representation that can be used to recreate
        # the rectangle object
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        # Destructor method that prints a message when the
        # rectangle object is deleted
        print("Bye, rectangle...")
