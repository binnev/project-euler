# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""
from python.tools import profile
from python.tools.primes import sieve_primes


@profile.function
def euler7():
    N = 10000

    primes = sorted(sieve_primes(150000))
    return primes[N]


if __name__ == "__main__":
    assert euler7() == 104743
