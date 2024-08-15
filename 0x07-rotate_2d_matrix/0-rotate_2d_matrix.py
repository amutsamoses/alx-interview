#!/usr/bin/python3

"""
Rotate a 2D matrix 90 degrees clockwise using in-place operation
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix by 90 degrees clockwise in-place.
    Args:
        matrix: a ,ist of list representing n x N 2D matrix to be rotated

    Returns:
        None: the matrix is modified in-place
    """

    n = len(matrix)

    '#first we transponse the matrix'
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    '#now we reverse each row'
    for i in range(n):
        matrix[i].reverse()
