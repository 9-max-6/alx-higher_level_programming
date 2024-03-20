#!/usr/bin/python3
"""
A function to compute the square value of all integers of a matrix
"""


def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for row in matrix:
        sq_matrix.append(list(map(lambda x: x**2, row)))

    return sq_matrix
