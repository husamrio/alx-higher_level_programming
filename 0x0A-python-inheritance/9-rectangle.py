#!/usr/bin/python3
"""
Module 9-rectangle

This module contains the parent class BaseGeometry, which includes
the public instance methods area and integer_validation.
It also contains the subclass Rectangle, which instantiates the
private attributes
width and height, validated by the parent class.
The Rectangle class extends the area method from its parent
and overrides the __str__ method to provide a custom string representation.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry and includes the
    following methods:
- __init__(self, width, height): Initializes the instance
with the given width and height.
- area(self): Calculates and returns the area of the rectangle.
- __str__: Provides a custom string representation of the rectangle.

    """
    def __init__(self, width, height):
        """This method validates and initializes the private attributes
        width and height.
Arguments:
- width (int): The width of the rectangle.
- height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This method overrides the parent's empty area method
        and returns the calculated area of the rectangle.
"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
