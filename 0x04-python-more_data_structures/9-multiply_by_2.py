#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary with all values doubled.
    """
    keys = list(a_dictionary.keys())
    new_dict = {}
    for key in keys:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
