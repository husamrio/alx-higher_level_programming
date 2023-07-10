#!/usr/bin/python3
"""
Module 10-square

This module contains the parent class BaseGeometry, which includes
the public instance methods area and integer_validation.

It also contains the subclass Rectangle, which instantiates
private attributes width and height. These attributes are validated
by the parent class.
The Rectangle class extends the parent's area method and uses
the __str__ method for printing.

Finally, the module contains the subclass Square, which instantiates
a private attribute size that is validated by the superclass.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class inherits from the Rectangle class, which in turn
    inherits from the BaseGeometry class. The Square class has a method called
    __init__ that takes one argument, size.

    """
    def __init__(self, size):
        """The __init__ method of the Square class initializes
        the private attribute size, which takes an
        integer as an argument.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
