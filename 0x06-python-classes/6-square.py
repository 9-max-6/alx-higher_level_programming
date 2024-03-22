#!/usr/bin/python3

class Square:
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position
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

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in self.__size:
                for i in self.__size:
                    print("#", end="")
                print("")
            print("")