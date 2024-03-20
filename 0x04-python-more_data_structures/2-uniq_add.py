#!/usr/bin/python3

"""
A function that adds all unique integers in a list
"""


def uniq_add(my_list=[]):
    unique_list = []
    su_m = 0
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
            su_m += item
    return su_m
