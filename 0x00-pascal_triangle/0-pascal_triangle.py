#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n

    Args:
        n (int): number of rows in Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]
        # Start the new row with 1
        new_row = [1]

        # Fill in the middle values of the row
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        # End the row with 1
        new_row.append(1)

        # Add the new row to the triangle
        triangle.append(new_row)

    return triangle

