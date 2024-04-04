#!/usr/bin/python3
"""
Module - the square class
"""
from models import rectangle


class Square(rectangle.Rectangle):
    """
    Class square extends rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print rectangle"""
        args = [self.id, self.x, self.y, self.height]
        return "[Square] ({}) {}/{} - {}".format(*args)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
