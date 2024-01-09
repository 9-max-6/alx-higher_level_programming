#!/usr/bin/python3
def element_at(my_list, ind):
    if ind < 0 or ind > len(my_list) - 1:
        return 'None'
    else:
        return my_list[ind]
