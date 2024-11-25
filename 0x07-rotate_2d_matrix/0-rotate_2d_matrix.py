#!/usr/bin/python3
"""0-rotate_2d_matrix
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """Rotates 2d matrix 90 degrees clockwise"""
    n =  len(matrix)

    matrix.reverse()

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]