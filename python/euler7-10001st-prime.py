# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""
from python.tools.utils import profile
from tools.primes import eratosthenes_sieve


@profile
def euler7():
    N = 10000

    primes = sorted(eratosthenes_sieve(150000))
    return primes[N]


if __name__ == "__main__":
    assert euler7() == 104743
