#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    a functon to delete a key
    """

    if a_dictionary.get(key) is None:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
