#!/usr/bin/python3
"""
Implements island_perimeter function
that solves the island perimeter interview
question
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island
    described in grid
    """
    perimeter = 0
    y_len = len(grid) - 1
    x_len = len(grid[0]) - 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            top = i - 1
            bottom = i + 1
            left = j - 1
            right = j + 1
            if grid[i][j] == 1:
                if ((top >= 0 and grid[top][j] == 0) or
                   top < 0):
                    perimeter += 1
                if ((bottom <= y_len and grid[bottom][j] == 0) or
                   bottom > y_len):
                    perimeter += 1
                if ((left >= 0 and grid[i][left] == 0) or
                   left < 0):
                    perimeter += 1
                if ((right <= x_len and grid[i][right] == 0) or
                   right > x_len):
                    perimeter += 1
    return perimeter
