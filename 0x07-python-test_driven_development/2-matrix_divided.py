#!/usr/bin/python3
"""
This module contains a function that divides all
elements of a matrix by a given number and returns a new matrix.
The input matrix must be a list of lists of
integers or floats with the same size.
The result is rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given
    number and returns a new matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(error_msg)

    result_matrix = []
    row_length = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
            new_row.append(round(element / div, 2))
        result_matrix.append(new_row)
    return result_matrix
