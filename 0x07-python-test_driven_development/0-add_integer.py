#!/usr/bin/python3

def add_integer(a, b=98):
    types = [float, int]
    if type(a) not in types:
         raise TypeError("a must be an integer")
    if type(b) not in types:
        raise TypeError("b must be an integer")
    if type(a) is types[1]:
        a = int(a)
    if type(b) is types[1]:
        b = int(b)
    return (a + b)
