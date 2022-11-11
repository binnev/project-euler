# Summation of primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from python.tools.primes import eratosthenes_sieve
from python.tools import profile
from python.tools import primes

N = 2000000


@profile.function
def by_sieve():
    return sum(eratosthenes_sieve(N))


@profile.function
def by_trial():
    return sum(primes.primes_by_trial_division(limit=N))


def euler10():
    return by_sieve()


if __name__ == "__main__":
    assert euler10() == 142913828922
