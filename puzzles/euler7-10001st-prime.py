# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""

from euler_functions import sieve_primes, primes_by_trial_division, profile
N = 10000

with profile():
    primes = sorted(sieve_primes(104744))
    print(primes[N])

with profile():
    for ii, prime in enumerate(primes_by_trial_division()):
        if ii == N:
            print(prime)
            break