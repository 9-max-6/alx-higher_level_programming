#!/usr/bin/python3
"""
The Rectangle module
"""


class Rectangle:
    """
    A class defining the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                [rect.append(f'{self.print_symbol}')
                 for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """canononical rep of the rectangle object"""
        g = self.__dict__["_Rectangle__height"]
        h = self.__dict__["_Rectangle__width"]
        return (f'Rectangle({h}, {g})')

    def __del__(self):
        """A destructor the python way"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method def bigger_or_equal(rect_1, rect_2):
            that returns the biggest rectangle based on the area
        rect_1 must be an instance of Rectangle,
            otherwise raise a TypeError exception with the message
            rect_1 must be an instance of Rectangle
        rect_2 must be an instance of Rectangle,
            otherwise raise a TypeError exception with the message
            rect_2 must be an instance of Rectangle
        Returns rect_1 if both have the same area value
        """
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            h = getattr(rect_1, 'rect_1.height', 0)
            g = getattr(rect_1, 'rect_1.width', 0)
            area_1 = h * g
            a = getattr(rect_2, 'rect_2.height', 0)
            b = getattr(rect_2, 'rect_2.width', 0)
            area_2 = a * b
            if (area_1 == area_2 or area_1 > area_2):
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method def square(cls, size=0):
        that returns a new Rectangle instance with
        width == height == size
        """
        height = width = size
        return cls(width, height)
