#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    A function to safe print a list
    """


    for i in range(0, x):
        try:
            print("{my_list[i]}", end="")
        except Exception as e:
            print("Error occured: ", e.args[0])
