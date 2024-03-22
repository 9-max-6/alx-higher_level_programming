#!/usr/bin/python3
"""
Module defining a class square
"""


class Square:
    __size = 3

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return self.__size ** 2
    def size(self):
        return self.__size
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value