"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers
from 1 to 20?
"""
from python.tools.primes import prime_factors, product
from python.tools import profile


@profile.function
def euler5():
    """Here's the plan: find the prime factors of all the divisors 1 to 20, and use these
    to find the smallest multiple of all divisors."""

    start, end = 2, 20
    factors = dict()  # empty dict to hold all factors
    for n in range(start, end + 1):  # for each divisor
        factors_n = prime_factors(n)  # find its prime factors
        for f, p in factors_n.items():  # for each factor and exponent in the divisor
            # update the global factors dict so that the factor stored has an exponent
            # equal to the one from the divisor
            if f in factors:
                if factors[f] < p:
                    factors[f] = p
            else:
                factors[f] = p

    # assemble the smallest multiple
    return product([factor**exponent for factor, exponent in factors.items()])


if __name__ == "__main__":
    assert euler5() == 232792560
