#!/usr/bin/python3
"""
Module - class rectangle
"""
from models import base


class Rectangle(base.Base):
    """
    Class rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(width) is int and width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(height) is int and height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(x) is int and x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if type(y) is int and y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__height * self.width

    def display(self):
        """
        prints out the rectange using #
        """
        for i in range(self.y):
            print("")
        for i in range(self.__height):
            for i in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """print rectangle"""
        args = [self.id, self.x, self.y, self.width, self.height]
        return "[Rectangle] ({}) {}/{} - {}/{}".format(*args)

    def update(self, *args):
        """ function to update arguments"""
        for i in range(len(args)):
            if (i == 0):
                self.id = args[0]
            if (i == 1):
                self.width = args[1]
            if (i == 2):
                self.height = args[2]
            if (i == 3):
                self.x = args[3]
            if (i == 4):
                self.y = args[4]
