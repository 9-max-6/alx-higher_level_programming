#!/usr/bin/python3
"""
module - read_file
"""


def read_file(filename=""):
    """
    a function that reads a
    text file (UTF8) and prints it to stdout:
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
