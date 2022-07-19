# Summation of primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from euler_functions import sieve_primes

primes = sorted(sieve_primes(2000000))
print(sum(primes))