import numpy as np


def count_neighbors(grid):
    """Count 8-neighbors for each cell using wrap-around edges."""
    return (
        np.roll(grid, 1, 0) + np.roll(grid, -1, 0) +
        np.roll(grid, 1, 1) + np.roll(grid, -1, 1) +
        np.roll(np.roll(grid, 1, 0), 1, 1) +
        np.roll(np.roll(grid, 1, 0), -1, 1) +
        np.roll(np.roll(grid, -1, 0), 1, 1) +
        np.roll(np.roll(grid, -1, 0), -1, 1)
    )


def step(grid):
    """Advance the grid by one Game of Life step."""
    neighbors = count_neighbors(grid)
    return (
        ((grid == 1) & ((neighbors == 2) | (neighbors == 3))) |
        ((grid == 0) & (neighbors == 3))
    ).astype(int)
