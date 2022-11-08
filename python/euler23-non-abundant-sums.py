# -*- coding: utf-8 -*-
"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""
from itertools import combinations_with_replacement
from math import sqrt

from python.tools.utils import profile


def d(N, debug=False):
    n = 1  # initialise n
    divisors = []
    limit = sqrt(N)  # ceil(sqrt(N))
    while n <= limit:  # search up to the square root
        if N % n == 0:  # if it divides evenly
            divisors.append(n)  # store the divisor
            dividend = N // n
            divisors.append(dividend)  # and the dividend
        n += 1  # increment n

    if N in divisors:  # this mainly covers the case when N == 2
        divisors.remove(N)

    if debug is True:
        return set(divisors)
    else:
        return sum(set(divisors))


@profile
def euler23():
    limit = 28123

    # calculate all the abundant numbers below limit
    Na = [N for N in range(2, limit + 1) if d(N) > N]  # unexpectedly quick

    # find all the permutations of sums of 2 abundant numbers.
    # this gives us the set of numbers < limit which CAN be expressed as such
    can = [i + j for i, j in combinations_with_replacement(Na, 2)]  # ~2.5 sec

    # find the set of numbers from 1..limit
    N = set(range(1, limit + 1))

    # find the members of N that are not in "can"
    # these are the numbers that CAN'T be constructed from the sum of 2 abundants
    cant = N.difference(can)

    return sum(cant)


if __name__ == "__main__":
    assert euler23() == 4179871
