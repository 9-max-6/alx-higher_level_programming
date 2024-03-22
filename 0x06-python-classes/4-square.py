#!/usr/bin/python3
"""
Module defining a class square
"""


class Square:
    """
     A class Square with one private variable __size and  a method 
    to determine its area, a setter for the size and a getter
    """
    __size = None

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        Determines the area of the square
        """
        return self.__size ** 2
    def size(self):
        """
        A getter for the size of the square
        """
        return self.__size
    def size(self, value):
        """
        A setter for the size value of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
