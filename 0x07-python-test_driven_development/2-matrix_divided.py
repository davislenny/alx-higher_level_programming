#!/usr/bin/python3
"""
The matrix_divided module
Contains the 'matrix_divided' function that 
divides all elements of matrix 'matrix' by 'div'
"""


def matrix_divided(matrix, div):
    """
    The function returns a new matrix with results 
    rounded to 2 decimal places
    Raise:
        TypeError if elements are not integers or float
        or if the rows differ in size
        ZeroDivisionError when div == 0
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(err_msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(err_msg)

    return [[round(x / div, 2) for x in row] for row in matrix]
