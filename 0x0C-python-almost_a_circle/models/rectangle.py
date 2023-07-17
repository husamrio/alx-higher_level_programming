#!/usr/bin/python3
"""
# This module contains the Rectangle class
# The class inherits from the Base class and initializes the superclass' id
# It has private attributes: width, height, x, and y
# It has a public method to calculate the area of the rectangle
# It can display the rectangle using "#" characters
# It can print a string representation in the format:
[Rectangle] (<id>) <x>/<y> - <width>/<height>
# It can update its attributes in the order: arg1=id,
arg2=width, arg3=height, arg4=x, arg5=y
# It can return a dictionary representation of its attributes
"""


from models.base import Base


class Rectangle(Base):
    """
    defines class Rectangle; inherits from class Base
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
        __str__          to_dictionary(self)
    Class Attributes:
        __width          __height
        __x              __y
    Inherited Attributes:
        id
    """

    def to_dictionary(self):
        """Return dictionary representation"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d

    @property
    def x(self):
        """getter x"""
        return self.__x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @property
    def height(self):
        """getter height"""
        return self.__height

    @property
    def width(self):
        """getter width"""
        return self.__width

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def __str__(self):
        """Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def display(self):
        """Print to stdout a rectangle using #'s"""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.width = v
                elif k == 2:
                    self.height = v
                elif k == 3:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
