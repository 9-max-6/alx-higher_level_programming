#!/usr/bin/python3
"""Defines a function that checks if an object is exactly an instance of a class."""

def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        If obj is exactly an instance of a_class ? True : False
     """
    if type(obj) == a_class:
        return True
    return False
