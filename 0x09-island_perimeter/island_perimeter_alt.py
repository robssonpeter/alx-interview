#!/usr/bin/python3
def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
