#!/usr/bin/python3
def replace_in_list(the_list, ind, element):
    if ind < 0 or ind > len(the_list) - 1:
        return the_list
    else:
        the_list[ind] = element
        return the_list