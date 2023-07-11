#!/usr/bin/python3
"""
This function calculates Pascal's Triangle up to a specified number
of rows.
"""


def pascal_triangle(n):
    """
    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.

    Example:
        pascal_triangle(5) returns [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
        [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
