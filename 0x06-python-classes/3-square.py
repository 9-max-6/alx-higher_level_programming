#!/usr/bin/python3
"""
Module defining a class square
"""


class Square:
    """
    A class Square with one private variable __size and  a function
    to determine its area
    """
    __size = None

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        A method to determie the area of the instance of the Square class
        """
        return self.__size ** 2
