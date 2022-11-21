# -*- coding: utf-8 -*-
"""
Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import combinations, permutations
import sys

if __name__ == "__main__":

    codePath = r"C:\gdrive\code\python"
    if codePath not in sys.path:
        sys.path.insert(0, codePath)
    from myfunctions import sieve_primes, prime_factors

    from math import sqrt

    for dd in reversed(range(1, 10)):
        digits = "".join(str(i) for i in reversed(range(1, dd + 1)))
        # need primes up to the square root of the largest pandigital
        limit = round(sqrt(int(digits)))
        prime_endings = "1379"  # use this to filter out definite non-primes easily
        pans = ["".join(p) for p in permutations(digits) if p[-1] in prime_endings]
        # compute list of primes to use as potential factors for trial divisions
        primes = sorted(sieve_primes(limit))

        for ii, N in enumerate(pans):

            N = int(N)
            isPrime = True  # assume N is prime to start with

            # try trial division with list of primes first
            limit = sqrt(N)

            for p in primes:
                if p > limit:  # if we get above sqrt(N),
                    break  # stop trial dividing
                if N % p == 0:  # if p is a prime factor of N
                    isPrime = False  # set prime flag to false
                    break  # stop dividing; we only need to prove it isn't prime

            if isPrime:
                raise Exception("solution = {}".format(N))
