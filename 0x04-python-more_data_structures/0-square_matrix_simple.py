#!/usr/bin/python3

# 0. Simple Matrix Squared**
# * [0-square_matrix_simple.py](./0-square_matrix_simple.py):
# This Python function calculates the square value of all integers in a matrix.
# The `matrix` parameter is a two-dimensional array.
# It returns a matrix of the same size as the input `matrix`,
# where each value is the square of the corresponding input value.
# * The original matrix remains unaltered.
# * No external modules are imported for this implementation.

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(pow(elem, 2))
        new_matrix.append(new_row)
    return new_matrix
