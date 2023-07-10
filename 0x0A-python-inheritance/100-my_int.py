#!/usr/bin/python3
"""The MyInt class is defined as a subclass of the int class.."""


class MyInt(int):
    """The MyInt class inverts the == and != operators of the int class."""

    def __ne__(self, value):
        """The MyInt class overrides the != operator to behave like
        the == operator"""
        return self.real == value

    def __eq__(self, value):
        """The MyInt class overrides the == operator to behave like
        the != operator.."""
        return self.real != value
