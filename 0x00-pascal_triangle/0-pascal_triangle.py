#!/usr/bin/python3
"""Pascal Triangle Interview """


def pascal_triangle(n):
    """returns a list of numbers which
    represents the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # define a row and fill first and last idx with 1
        current_row = [0] * (i+1)
        current_row[0] = 1
        current_row[len(current_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(current_row):
                y = pascal_triangle[i - 1][j]
                z = pascal_triangle[i - 1][j - 1]
                current_row[j] = y + z

        pascal_triangle[i] = current_row

    return pascal_triangle
