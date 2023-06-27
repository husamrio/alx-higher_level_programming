#!/usr/bin/python3
"""
This module contains a Square class.

The Square class represents a square shape and provides methods to manipulate
"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square. Defaults to 0 if not provided.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be greater than or equal to 0.")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        for i in range(self.__size):
            print("#" * self.__size)

        if not self.__size:
            print()
