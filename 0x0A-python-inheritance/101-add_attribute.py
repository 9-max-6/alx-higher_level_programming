#!/usr/bin/python3
"""A function to add attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute couldn't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
