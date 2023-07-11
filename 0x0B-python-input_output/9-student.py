#!/usr/bin/python3
"""

This class, named Student, has public instance attributes for
first_name, last_name, and age. It also includes a public method
called to_json, which returns the dictionary representation of
the Student object
"""


class Student():
    """
    This class has public attributes for first_name, last_name, and age.
    It also includes a public method called to_json, which returns the
    dictionary representation of the object
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This function generates a dictionary representation of an object,
        utilizing basic data structures like lists, dictionaries, and
        strings, to enable JSON serialization
        """
        return self.__dict__
