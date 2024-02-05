#!/usr/bin/python3
"""Checks if an object is an inherited instance of a class."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object.
        a_class (type): The class to check against.
    Returns:
        If obj is an inherited instance of a_class - True.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
