# -*- coding: utf-8 -*-
"""
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

import math


def euler34():
    ...


if __name__ == "__main__":

    N = 3000000  # upper limit for N and factorial sum intersecting
    ns = range(3, N)  # skip 1 and 2
    factorials = [math.factorial(i) for i in range(10)]  # precalculate factorials

    def factorial_sum(number):
        return sum(factorials[int(digit)] for digit in str(number))

    fac_sums = []
    solutions = []

    for n in ns:

        f = factorial_sum(n)
        fac_sums.append(f)

        if f == n:
            solutions.append(n)

    print("solution = ", sum(solutions))

    # %% plots

    import matplotlib.pyplot as plt

    plt.rc("font", size=9)
    fig, ax = plt.subplots(figsize=(5, 5))
    plt.setp(
        ax,
        xlabel="N",
    )
    colours = plt.cm.inferno([0.6, 0.8])
    ax.loglog()

    ax.plot(ns, fac_sums, c=colours[1], label="factorial digit sum")
    ax.plot([1, N], [1, N], "-k", label="N")
    plt.legend()
    fig
    for s in solutions:
        ax.plot(s, s, "s", ms=10, mfc=colours[0], mec="k")
        ax.text(s * 1.5, s, s, ha="left", va="center")
    fig.savefig("euler34.png", dpi=150)
