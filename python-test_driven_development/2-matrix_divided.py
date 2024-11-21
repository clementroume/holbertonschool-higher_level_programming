#!/usr/bin/python3
"""1. Divide a matrix"""


def matrix_divided(matrix, div):
    "matrix divided function"
    errormsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errormsg)
    if not isinstance(matrix, list):
        raise TypeError(errormsg)
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(errormsg)
        for values in rows:
            if not isinstance(values, (int, float)):
                raise TypeError(errormsg)
        if len(rows) == 0:
            raise TypeError(errormsg)
    if len({len(rows) for rows in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(value / div, 2) for value in lists] for lists in matrix]
