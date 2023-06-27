#!/usr/bin/python3
"""Implementation of a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be greater than or equal to 0.")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have unequal areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of current square is < area of another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the current square is less than or equal to the
area of another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area current square is > area of another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the current square is greater
than or equal to the area of another square."""
        return self.area() >= other.area()
