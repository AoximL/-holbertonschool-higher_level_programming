#!/usr/bin/python3
"""
12-pascal_triangle.py
Create Pascal's Triangle
"""


def pascal_triangle(n):
    """Return Pascal's Triangle as a list of lists of integers"""
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # First element of each row is always 1

        # Build the middle elements by adding
        # adjacent elements from previous row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
