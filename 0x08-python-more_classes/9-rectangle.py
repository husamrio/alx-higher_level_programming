#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0.")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0.")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle.")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle.")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle with equal width and height.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return cls(size, size)

    def __str__(self):
        """
        Returns the string representation of the Rectangle.

        The rectangle is represented by the '#' character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for _ in range(self.__height):
            rect.extend([str(self.print_symbol)] * self.__width)
            if _ != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """
        Returns the string representation of Rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when a Rectangle instance is deleted.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
