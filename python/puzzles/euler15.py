""" Euler 15 - lattice paths """
import sys, numpy as np, matplotlib.pyplot as plt, time, itertools as it
from copy import deepcopy

from python.tools import profile


def pascal_row(N):
    """Function to generate row N of Pascal's Triangle.
    Start with 1, and multiply this by (Nrow-s)/(1+s), where s is horizontal
    steps. For row N, the width of the triangle is N+1, and the number of steps
    S is N-1.
    """
    N = 20
    row = [1]
    for s in range(N):
        row.append(int(row[-1] * (N - s) / (1 + s)))
    return row


@profile.function
def euler15():
    P = pascal_row(20)
    return sum(p**2 for p in P)


if __name__ == "__main__":
    assert euler15() == 137846528820
