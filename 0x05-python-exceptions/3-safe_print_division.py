#!/usr/bin/python3
def safe_print_division(a, b):
    """
    a function that divides 2 integers and prints the result.
    """

    try:
        c = a / b
    except (ValueError, TypeError):
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
