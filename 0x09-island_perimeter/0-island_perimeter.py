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
                top = grid[row - 1][col]
                if top == 0:
                    length += 1
                left = grid[row][col - 1]
                if left == 0:
                    length += 1
                right = grid[row][col + 1]
                if right == 0:
                    length += 1
                bottom = grid[row + 1][col]
                if bottom == 0:
                    length += 1
    return length
