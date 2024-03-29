#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    A function to safe print a list
    """

    num_print = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            num_print += 1
        except IndexError:
            break
    print("")
    return num_print
