#!/usr/bin/python3
"""
A module containing the function matrix_divided(matrix, div)
that safe divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    A function to safe divide a matrix with a number
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(div) is float('inf'):
        raise ValueError("div cannot be infinity")
    new_matrix = []
    len_list = []

    for i in matrix:
        len_list.append(len(i))
    if max(len_list) != min(len_list):
        raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        temp_matrix = []
        for j in i:
            if type(j) is int or type(j) is float:
                j /= div
                temp_matrix.append(round(j, 2))
            else:
                msg = "matrix must be a matrix (list of lists)"
                msg2 = " of integers/floats"
                raise TypeError(msg + msg2)
        new_matrix.append(temp_matrix)
    return new_matrix
