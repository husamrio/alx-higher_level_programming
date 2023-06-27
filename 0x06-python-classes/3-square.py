#!/usr/bin/python3
"""
Custom Code Variation 2
This code implements a Square class with a private size attribute
and a public method to calculate the area of the square.
"""


class Square:
    """
    Square class definition.

    Args:
        size (int): The size of the square.

    Functions:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initialize a Square object.

        Attributes:
            __size (int): The size of the square. Defaults to 0 if not provided
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
