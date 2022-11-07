# Summation of primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
from python.tools.primes import eratosthenes_sieve
from python.tools.utils import profile
from python.tools import primes

N = 2000000


@profile
def by_sieve():
    return sum(eratosthenes_sieve(N))


@profile
def by_trial():
    return sum(primes.primes_by_trial_division(limit=N))


if __name__ == "__main__":
    assert by_sieve() == 142913828922
    assert by_trial() == 142913828922
