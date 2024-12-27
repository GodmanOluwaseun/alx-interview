#!/usr/bin/python3
"""
0-island_perimeter:
    Returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    Returns perimeter of land part of the grid.
    args:
        grid (list of list) 2d grid containing island and water.
    """
    row = len(grid)
    col = len(grid[0]) if row > 0 else 0
    perimeter = 0

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                perimeter += 4
            if r > 0 and grid[r -1][c] == 1:
                perimeter -= 2
            if c > 0 and grid[r][c -1] == 1:
                perimeter -=2
    return perimeter