#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    Args:
        matrix(list): List of integers or floats.
        div(int/float): A number (integer or float)
    Raises:
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    # Check if matrix is a list of lists of integers or floats
    if not all(
        isinstance(row, list) and
        all(isinstance(elem, (int, float)) for elem in row)
        for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists)    of integers/floats")
    # Check if each row has the same size
    if any(len(row) != len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return result_matrix
