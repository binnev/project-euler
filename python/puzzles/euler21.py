# -*- coding: utf-8 -*-
"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
from math import sqrt

from python.tools import profile


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

    if N in divisors:
        divisors.remove(N)

    if debug is True:
        return set(divisors)
    else:
        return sum(set(divisors))


@profile.function
def euler21():
    amicable = []
    limit = 10000
    N = 1  # initialise
    while N < limit:
        if N not in amicable:  # skip numbers already encountered
            M = d(N)  # find the sum of proper divisors
            if (M < limit) and (M != N):  # if sum is within limit and != N
                if d(M) == N:  # if N and M are amicable
                    amicable.extend([N, M])  # ".extend(list)"== "+= list"
        N += 1

    return sum(amicable)


if __name__ == "__main__":
    assert euler21() == 31626
