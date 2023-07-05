#!/usr/bin/python3
"""Module containing the Rectangle class."""


class Rectangle:
    """Class representing a rectangle.

    Class Attributes:
        number_of_instances (int): The total number of Rectangle instances.
        print_symbol (any): The symbol used when printing the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__class__.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the larger of two Rectangle instances based on their area.

        Args:
            rect_1 (Rectangle): The first rectangle instance.
            rect_2 (Rectangle): The second rectangle instance.

        Returns:
            Rectangle: The larger of the two rectangles.

        Raises:
            TypeError: If either rect_1 or rect_2 is not Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol.

        Returns:
            str: A string representation of the rectangle. If either width or
            height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""

        row = str(self.print_symbol) * self.width
        rows = [row for _ in range(self.height)]

        return "\n".join(rows)

    def __repr__(self):
        """Return a string rep of the rectangle in the format
        'Rectangle(width, height)'.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Handle deletion of a Rectangle instance."""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
