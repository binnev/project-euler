# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""
# modify my find_primes function to go to number, not value
def sieve_primes(N):
    # function to generate the list of primes below N, using the sieve of
    # Eratosthenes

    N = round(N)
    ints = list(range(2,N))
    composites = set([])

    # start sieving from the smallest prime -- 2
    for i in ints:

        if i not in composites:  # if this number is not a known composite
            # generate the multiples of p up to N
            mult = set(range(i, N, i)[1:])  # exclude the first one -- it's a prime
            # add these to the set of composites
            composites.update(mult)

    ints = set(ints).difference(composites)
    return ints

primes = sorted(find_primes(1000000))
