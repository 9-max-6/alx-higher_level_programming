#!/usr/bin/python3
"""Function to check if an object is an exact instance of a class."""


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
