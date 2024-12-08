#!/usr/bin/python3
"""Method for calculating island perimeter"""

def island_perimeter(grid):
    """Returns the perimeter of an island represented by a matrix `grid`

    Args:
        grid - list of list of ints
    """
    perimeter = 0
    m = len(grid)  # number of rows in the grid
    n = len(grid[0])  # number of columns in the grid
    for row_idx, row in enumerate(grid):
        for col_idx, elem in enumerate(row):
            if elem:  # if the current cell is land
                perimeter += 4  # add 4 for each land cell

                # Check for shared borders with the cell below
                if row_idx < m - 1 and grid[row_idx + 1][col_idx]:
                    perimeter -= 2  # subtract 2 for the shared border

                # Check for shared borders with the cell to the right
                if col_idx < n - 1 and grid[row_idx][col_idx + 1]:
                    perimeter -= 2  # subtract 2 for the shared border

    return perimeter
