#!/usr/bin/python3
"""
This is a custom code variation that defines a Square class.
It includes detailed comments explaining the purpose of
each method and attribute
"""


class Square:
    """
    Represents a square shape.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square object.

        Args:
            size (int): The size of the square's sides.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute."""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' character, considering the position."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        print("\n".join([" " * self.__position[0] +
                         "#" * self.__size
                         for i in range(self.__size)]))
