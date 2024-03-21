#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    a = 0
    c = 0

    for b in my_list:
        a += b[0] * b[1]
        c += b[1]

    return (a / c)