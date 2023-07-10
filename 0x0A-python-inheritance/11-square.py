#!/usr/bin/python3
"""
Module 10-square contains several classes.
The parent class is called BaseGeometry. It has a public instance
method for calculating the area and validating integers.
There is a subclass called Rectangle. It has private attributes
for width and height that are validated by the parent class.
The Rectangle class extends the parent’s area method and can be
printed using the str method.
There is also a subclass called Square. It has a private attribute
for size that is validated by the superclass. The Square class can
also be printed using the str method.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class inherits from the Rectangle class, which in
    turn inherits from the BaseGeometry class. The Square class has
    an init method that takes a size parameter and a str method for
    printing.
    methods:
        __init__(self, size)
        __str__(self)
    """
    def __init__(self, size):
        """initializes size
        Args:
            size (int): private
            The Square class initializes a private size attribute as an integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
