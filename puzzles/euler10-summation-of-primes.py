# Summation of primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from euler_functions import sieve_primes, primes_by_trial_division, profile

with profile():
    print(sum(sieve_primes(2000000)))

with profile():
    print(sum(primes_by_trial_division(limit=2000000)))
