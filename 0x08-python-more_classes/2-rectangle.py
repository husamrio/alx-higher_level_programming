#!/usr/bin/python3
"""
Module 3-rectangle
Contains class Rectangle with private attributes width and height,
and public area and perimeter methods
"""


class Rectangle:
    """
    Defines class rectangle with private attributes width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        get_width(self)
        set_width(self, value)
        get_height(self)
        set_height(self, value)
        area(self)
        perimeter(self)
    """

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        """ Getter returns width """
        return self.__width

    def set_width(self, value):
        """ Setter sets width if int >= 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        """ Getter returns height """
        return self.__height

    def set_height(self, value):
        """ Setter sets height if int >= 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Return 2*width + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

# Test the Rectangle class


my_rectangle = Rectangle(5, 6)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                        my_rectangle.perimeter()))
