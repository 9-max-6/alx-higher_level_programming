#!/usr/bin/python3
"""
Print square module
"""


def print_square(size):
    """
    print_square - a function to print a square of #

    Args:
    size - the size of the square

    Raises:
    TypeError - if the size is not an integer
    ValueError - if the size is < 0
    """
    if type(size) is int:
        if size == 0:
            return
        if size < 0:
            raise ValueError("size must be >= 0")
        for i in range(size):
            for j in range(size):
                print("#", end="")
            if (i < size - 1):
                print("")
    else:
        raise TypeError("size must be an integer")
