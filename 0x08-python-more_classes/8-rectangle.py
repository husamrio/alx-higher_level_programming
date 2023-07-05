#!/usr/bin/python3
"""
Rectangle Module

Defines the Rectangle class with private attributes for width and height.
Includes methods for calc area and perimeter, custom print using given symbol,
tracking the numb of instances, and a static method to compare two rectangles.
"""


class Rectangle:
    """
    Rectangle class with private attributes width and height.

    Attributes:
        number_of_instances (int): Number of instances created and not deleted.
        print_symbol (any): Symbol used for printing string representation.

    Functions:
        __init__(self, width=0, height=0): Initializes a rectangle instance.
        __del__(self): Deletes an instance of the class.
        width(self): Getter method for width attribute.
        width(self, value): Setter method for width attribute.
        height(self): Getter method for height attribute.
        height(self, value): Setter method for height attribute.
        area(self): Calculates the area of the rectangle.
        perimeter(self): Calculates the perimeter of the rectangle.
        __str__(self): Returns the string representation of the rectangle.
        __repr__(self):Return string representation to recreate a new instance.
        bigger_or_equal(rect_1, rect_2): Method to compare two rectangles.
    """

    number_of_instances = 0
    print_symbol = "*"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Deletes an instance of the class."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation to recreate a new instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare two rectangle and return the bigger one."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
