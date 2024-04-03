#!/usr/bin/python3
"""
Module - class Base
"""


class Base:
    """
    base class of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
