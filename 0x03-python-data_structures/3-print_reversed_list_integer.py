#!/usr/bin/python3
def print_reversed_list_integer(the_list=[]):
    if the_list:
        the_list.reverse()
        for i in range(len(the_list)):
            print("{:d}".format(the_list[i]))