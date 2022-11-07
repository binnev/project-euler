"""
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from python.tools import utils

N = 1000


@utils.profile
def brute():
    # test divisibility of every number
    multiples = []
    for n in range(N):
        if (n % 3 == 0) or (n % 5 == 0):
            multiples.append(n)

    return sum(multiples)


@utils.profile
def oneliner():
    return sum(n for n in range(N) if (n % 3 == 0 or n % 5 == 0))


@utils.profile
def multiply():
    # multiply instead; probably faster than checking
    divisors = 3, 5
    numbers = []
    for d in divisors:
        numbers += list(range(d, N, d))

    return sum(set(numbers))


if __name__ == "__main__":
    assert brute() == 233168
    assert oneliner() == 233168
    assert multiply() == 233168
