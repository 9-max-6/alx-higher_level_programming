#!/usr/bin/python3
"""
module - write_file
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    """
    with open(filename, 'w', encoding="utf-8") as f:
        g = f.write(text)
    return g
