#!/usr/bin/python3
"""Defines a class and a function to check if an object is an instance a class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check the object against.
    Returns:
        If the object is an instance or inherited instance of a_class - True.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
