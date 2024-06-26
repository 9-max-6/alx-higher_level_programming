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

    def update(self, *args, **kwargs):
        """method to update attributes"""
        if not args:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        attributes = ['id', 'size', 'x', 'y']
        for index, value in enumerate(args):
            if index < len(args):
                setattr(self, attributes[index], value)

    def to_dictionary(self):
        """returns the dict rep of a rectangle"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key.startswith("_Rectangle__"):
                new_k = key.replace("_Rectangle__", "")
                if new_k == "height":
                    new_k = "size"
                new_dict[new_k] = value
            else:
                new_dict[key] = value
        del new_dict["width"]
        return new_dict
