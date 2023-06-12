#!/usr/bin/python3
# printMatrixInteger

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        print(" ".join("{:d}".format(col) for col in row))
