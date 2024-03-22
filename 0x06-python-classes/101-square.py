#!/usr/bin/python3
"""
Module defining a class square
"""


class Square:
    """
    A class Square with one private variable __size and  a method
    to determine its area, a setter for the size and a getter
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        A getter for the position property
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        A setter for the position property
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """
        Print the square prefixed by #
        """
        if self.size == 0:
            print("")
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")

    def __str__(self):
        """
        The method that will be invoked whenever an object of this
        class is printed.
        """
        if self.size == 0:
            return
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
        return ("")