#!/usr/bin/python3
"""
This code defines a Square class and performs necessary validations.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the Square object.

        Args:
            size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
