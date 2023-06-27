#!/usr/bin/python3
"""Print square"""


class Square:
    """This is a class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """This method initializes an instance of the Square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This method returns the size of the square"""
        return self.__size

    @property
    def position(self):
        """This method returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This method sets the position of the square"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """This method sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints out a square using # taking into account posit"""
        if not self.size:
            print()
            return

        print("\n" * self.position[1], end="")
        print("\n".join([" " * self.position[0] +
                        "#" * self.size
                         for i in range(self.size)]))

    def __str__(self):
        """This method returns a string representation of the square"""
        return f"" if not self.size else (
                f"\n" * self.position[1] +
                f"\n".join([" " * self.position[0] +
                            "#" * self.size
                            for i in range(self.size)]))
