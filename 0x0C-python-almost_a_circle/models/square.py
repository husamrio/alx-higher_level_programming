#!/usr/bin/python3
"""
The module contains a class called Square, which inherits from the
 Rectangle class. The Square class initializes its superclass’ id,
width (as size), height (as size), x, and y attributes. It also has
 a public attribute called size. When printed, it displays in the
 format: [Square] (<id>) <x>/<y> - <size>. The Square class can update
   its attributes in the following order: arg1=id, arg2=size, arg3=x,
   arg4=y. It also has a method that returns a dictionary representation
   of its attributes.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherited Attributes:
    id
    __width
    __height
    __x
    __y

Class Attributes:
    size

Inherited Methods:
    Base.init(self, id=None)
    Rectangle.init(self, width, height, x=0, y=0, id=None)
    update(self, *args, **kwargs)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    x(self)
    x(self, value)
    y(self)
    y(self, value)
    area(self)
    display(self)

Methods:
    __str__
    __init__(self, size, x=0, y=0, id=None)
    update(self, *args, **kwargs)
    size(self)
    size(self, value)
    to_dictionary(self)
    """
    @property
    def size(self):
        """Getter size"""
        return self.width

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Prints [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

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
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d

    @size.setter
    def size(self, value):
        """Setter size - sets width and height as size"""
        self.width = value
        self.height = value
