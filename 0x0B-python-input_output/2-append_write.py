#!/usr/bin/python3
"""
module - append_write()
"""


def append_write(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    """
    with open(filename, 'a', encoding="utf-8") as f:
        g = f.write(text)
    return g
