#!/usr/bin/python3

"""
Island Perimeter Interview
"""


def island_perimeter(grid):
    """
    Afunction that returns perimeter of an island
    0 rep water
    1 rep land

    Args:
        grid: a list of list of integers

    Returns:
        int: the perimeter of the island described in grid

    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid_cell = grid[i][j]
            if not grid_cell:
                continue

            '#if there is upper cell, same cols previouse row'
            upper_cell = None if not i else grid[i - 1][j]

            '#left cell same row, previous cols'
            left_cell = None if not j else grid[i][j - 1]

            '#begin with a call perimeter of 4'
            cell_perimeter = 4

            '#if there is land cell abovr, subtract 2 from perimeter'
            if upper_cell:
                cell_perimeter -= 2

            '#if there is land cell to the left, substract'
            if left_cell:
                cell_perimeter -= 2

            '#add calculated cell perimeter to the total perimeter'
            perimeter += cell_perimeter

    return perimeter
