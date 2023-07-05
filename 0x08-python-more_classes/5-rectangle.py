#!/usr/bin/python3
"""
Module rectangle
Contains the Rectangle class with private attributes width and height,
public methods for calculating area and perimeter, and printing the rectangle.
Also includes a destructor method.
"""


class Rectangle:
    """
    Defines the Rectangle class with private attributes width and height.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Functions:
        __init__(self, width, height)
        get_width(self)
        set_width(self, value)
        get_height(self)
        set_height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """

    def __init__(self, width=0, height=0):
        """ Initializes a rectangle object with given width and height. """
        self.__width = width
        self.__height = height

    def get_width(self):
        """ Returns the width of the rectangle. """
        return self.__width

    def set_width(self, value):
        """ Sets the width of the rectangle if value > 0. """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    def get_height(self):
        """ Returns the height of the rectangle. """
        return self.__height

    def set_height(self, value):
        """ Sets the height of the rectangle if value > 0. """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates and returns the area of the rectangle. """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates and returns the perimeter of the rectangle. """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns a string representation rectangle using '#' symbols. """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join(["#" * self.__width for _ in range(self.__height)])
        return pic

    def __repr__(self):
        """ Returns a string representation to recreate the object. """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Deletes an instance of the Rectangle class. """
        print("Bye rectangle...")


# Create a Rectangle object
if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)

    # Test the area and perimeter methods
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                            my_rectangle.perimeter()))

    # Delete the rectangle object
    del my_rectangle
