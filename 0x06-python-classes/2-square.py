#!/usr/bin/python3
"""
Module defining a class square
"""


class Square:
    """
    A class to define a square with a private variable size
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
