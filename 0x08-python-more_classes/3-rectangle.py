#!/usr/bin/python3
"""
Module: 3-rectangle
Contains Rectangle class with private attributes width and height,
public methods for area and perimeter calculations, and printing rectangles.
"""


class Rectangle:
    """
    Represents a rectangle with private attributes width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height)
        get_width(self)
        set_width(self, value)
        get_height(self)
        set_height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
    """

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be >= 0.")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        picture = "\n".join(["#" * self.__width for _ in range(self.__height)])
        return picture
        + "\n<3-rectangle.Rectangle object at {}>".format(hex(id(self)))


if __name__ == "__main__":
    # Test the Rectangle class
    my_rectangle = Rectangle(4, 2)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                            my_rectangle.perimeter()))
    print(my_rectangle)
    print("--")
    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                            my_rectangle.perimeter()))
    print(my_rectangle)
