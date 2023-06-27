#!/usr/bin/python3
"""This script defines the MagicClass & ways of calc area and circum circle."""
import math


class MagicClass:
    """This class rep a circle & provides methods for calc its area """
    def __init__(self, radius=0):
        """Initialize the MagicClass object with a given radius."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
