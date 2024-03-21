#!/usr/bin/python3


def best_score(a_dictionary):
    """
    a function that returns a key with the biggest integer value.
    """


    sorted_list = []
    keys = list(a_dictionary.keys())
    for key in keys:
        sorted_list.append(a_dictionary[key])
    sorted_list = sorted(sorted_list)
    for key in keys:
        if a_dictionary[key] == sorted_list[-1]:
            return key