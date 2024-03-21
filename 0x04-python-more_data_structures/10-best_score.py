#!/usr/bin/python3


def best_score(a_dictionary):
    sorted_list = []
    keys = list(a_dictionary.keys())
    for key in keys:
        sorted_list.append(a_dictionary[key])
    sorted_list = sorted(sorted_list)
    if sorted_list.count(sorted_list[-1]) == 1:
        return(sorted_list[-1])
    else:
        return None
