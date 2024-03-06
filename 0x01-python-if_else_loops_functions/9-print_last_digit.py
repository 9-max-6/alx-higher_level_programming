#!/usr/bin/python3

def print_last_digit(number):
    m = 10

    while True:
        if (number == 0 or m % number == 0):
            print("{}".format(0), end="")
            return 0
        else:
            if (number < 0):
                number *= -1
            print("{}".format(number % 10), end="")
            return number % 10
    print("")      
