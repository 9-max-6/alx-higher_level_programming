#!/usr/bin/python3
def new_in_list(the_list, ind, element):
    copy = the_list.copy()
    if ind < 0 or ind > len(the_list) - 1:
        return the_list.copy()
    else:
        copy[ind] = element
        return copy