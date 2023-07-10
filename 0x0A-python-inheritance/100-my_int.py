#!/usr/bin/python3
"""
Module 100-my_int contains a class called MyInt that inherits
from the int class. The MyInt class is sneaky because it has
inverted the == and != operators.
"""


class MyInt(int):
    """
    The MyInt class has several methods, including an init method
    that takes a num parameter, an eq method for checking equality,
    and a ne method for checking inequality.
    """
    def __init__(self, num):
        """initialize number"""
        self.num = num

    def __eq__(self, other):
        """
        The ne method returns
        True if the two values being compared are not equal.
        """
        return self.num != other

    def __ne__(self, other):
        """
        The eq method returns True if the
        two values being compared are equal
        """
        return self.num == other
