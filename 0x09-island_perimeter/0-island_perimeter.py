#!/usr/bin/python3
""" The module for finding the island perimeter """


def island_perimeter(grid):
    """ The island perimeter function """
    rows = len(grid)
    columns = len(grid[0])
    length = 0
    for row in range(rows):
        for col in range(columns):
            if grid[row][col]:
                """ Check the top"""
                if row > 0:
                    top = grid[row - 1][col]
                else:
                    top = 0
                if top == 0:
                    length += 1
                if col > 0:
                    left = grid[row][col - 1]
                else:
                    left = 0
                if left == 0:
                    length += 1
                if col < len(range(columns)) - 1:
                    right = grid[row][col + 1]
                else:
                    right = 0
                if right == 0:
                    length += 1
                if row < len(range(rows)) - 1:
                    bottom = grid[row + 1][col]
                else:
                    bottom = 0
                if bottom == 0:
                    length += 1
    return length
