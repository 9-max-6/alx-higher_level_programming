#!/usr/bin/python3
"""
Module defining a class square
"""


class Square:
    """
    A class Square with one private variable __size and  a method
    to determine its area, a setter for the size and a getter
    """

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """
        Determines the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        A getter for the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A setter for the size value of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        """
        Rich comparison method: less than
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Rich comparison method: less than or equal to
        """
        return self.size <= other.size

    def __eq__(self, other):
        """
        Rich comparison method: equal to
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Rich comparison: not equal to
        """
        return self.size != other.size

    def __gt__(self, other):
        """
        Rich comparison method: greater than
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Rich comparison method: greater than or equal to
        """
        return self.size >= other.size
