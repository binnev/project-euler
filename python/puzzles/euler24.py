# -*- coding: utf-8 -*-
"""
Lexicographic permutations

Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

import itertools as it

from python.tools import profile


@profile.function
def euler24():
    numbers = list(range(10))
    for ii, perm in enumerate(it.permutations(numbers), start=1):
        if ii == 1_000_000:
            return int("".join(map(str, perm)))


if __name__ == "__main__":
    assert euler24() == 2783915460
