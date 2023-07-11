#!/usr/bin/python3
"""
This class, named Student, has public instance attributes for
first_name, last_name, and age.
It also includes a public method called to_json, which returns
the dictionary representation of the Student object.
If specific attributes are requested, only those will be included
in the dictionary. Otherwise, all attributes will be included.
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Creates a student object with a full name and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Generates a dictionary representation of the object using simple
        data structures such as lists, dictionaries, and strings for JSON
        serialization.

        Return:
            If specific attributes are requested, only those will be
            included in the dictionary. Otherwise, all attributes will
            be included.
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
