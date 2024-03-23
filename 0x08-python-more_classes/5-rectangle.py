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

    def area(self):
        """ method to return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """method to return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """method to print rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
        return ("".join(rect))
    
    def __repr__(self):
        """canononical rep of the rectangle object"""
        
        return (f'Rectangle({self.__dict__["_Rectangle__height"]}, {self.__dict__["_Rectangle__width"]})')
    
    def __del__(self):
        """A destructor the python way"""
        print("Bye rectangle...")
