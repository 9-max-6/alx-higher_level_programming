#!/usr/bin/python3
"""
The Rectangle module
"""


class Rectangle:
    """
    A class defining the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
