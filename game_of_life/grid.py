import numpy as np


def make_random_grid(rows, cols, rng, alive_prob=0.35):
    """Return a random 0/1 grid with a given alive probability."""
    return (rng.random((rows, cols)) < alive_prob).astype(int)

def make_money_grid(rows,cols,p_init,M0,rnd):

def make_glider(rows, cols, top=10, left=10):
    """Return a grid with a single glider placed near (top, left)."""
    grid = np.zeros((rows, cols), dtype=int)
    r, c = top, left
    grid[r + 0, c + 1] = 1
    grid[r + 1, c + 2] = 1
    grid[r + 2, c + 0] = 1
    grid[r + 2, c + 1] = 1
    grid[r + 2, c + 2] = 1
    return grid
