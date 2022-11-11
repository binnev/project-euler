# Largest product in a grid
"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

"""

import numpy as np
from python.tools import utils, profile
from python.tools.primes import product


@profile.function
def euler11better():
    grid = utils.load_puzzle_input("euler11")

    grid = [g.split(" ") for g in grid.strip().split("\n")]
    grid = np.array(grid).astype(int)

    span = 4
    max_prod = 0
    for ii in range(grid.shape[0] - span):
        for jj in range(grid.shape[1] - span):
            for vector in [
                grid[ii, jj : jj + span],  # horizontal
                grid[ii : ii + span, jj],  # vertical
                grid[range(ii, ii + span), range(jj, jj + span)],  # diagonal
                grid[range(ii, ii - span, -1), range(jj, jj + span)],  # diagonal up
            ]:

                if (prod := product(vector)) > max_prod:
                    max_prod = prod

    return max_prod


@profile.function
def euler11old():
    grid = utils.load_puzzle_input("euler11")

    grid = [g.split(" ") for g in grid.strip().split("\n")]  # split string into entries
    del grid[0]
    grid = np.array(grid).astype(int)

    span = 4
    products = set()
    # scan horizontal spans
    for ii in range(grid.shape[0]):  # scroll through the rows
        for jj in range(grid.shape[1]):  # scroll through the columns
            if jj + span <= grid.shape[1]:  # horizontal
                vector = grid[ii, jj : jj + span]
                products.add(product(vector))
            if ii + span <= grid.shape[0]:  # vertical
                vector = grid[ii : ii + span, jj]
                products.add(product(vector))
            if (ii + span <= grid.shape[0]) and (jj + span <= grid.shape[1]):  # diag down
                vector = grid[range(ii, ii + span), range(jj, jj + span)]
                products.add(product(vector))
            if (ii - span >= 0) and (jj + span <= grid.shape[1]):  # diag up
                vector = grid[range(ii, ii - span, -1), range(jj, jj + span)]
                products.add(product(vector))

    return max(products)


def euler11():
    return euler11better()


if __name__ == "__main__":
    assert euler11() == 70600674
