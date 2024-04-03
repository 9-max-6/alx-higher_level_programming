#!/usr/bin/python3
"""
module - class student
"""


class Student:
    """
    Public instance attributes:
    first_name
    last_name
    age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a
    dictionary representation of a Student instance
    (same as 8-class_to_json.py)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs and type(attrs) is list:
            new_dict = {}
            for item in attrs:
                try:
                    new_dict[item] = self.__dict__[item]
                except KeyError:
                    pass
            return new_dict
        else:
            return self.__dict__
