#!/usr/bin/python3
"""
Module containing the function add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Function to safely add two integers
    """
    types = [float, int]
    if type(a) not in types:
        raise TypeError("a must be an integer")
    if type(b) not in types:
        raise TypeError("b must be an integer")
    if a is float('inf') or b is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(a) is types[0]:
        a = int(a)
    if type(b) is types[0]:
        b = int(b)
    return (a + b)
