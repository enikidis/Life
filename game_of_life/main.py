import numpy as np

from game_of_life.grid import make_glider, make_random_grid
from game_of_life.rules import step
from game_of_life.viz import run_popup


def main():
    # Grid settings
    rows, cols = 100, 100
    rng = np.random.default_rng(0)

    # Choose one initial population:
    grid = make_random_grid(rows, cols, rng, alive_prob=0.35)
    # grid = make_glider(rows, cols, top=10, left=10)

    run_popup(grid, step_fn=step, delay=0.05)


if __name__ == "__main__":
    main()
