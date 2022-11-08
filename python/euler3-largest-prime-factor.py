"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# I've written a function to find prime factors. I'll want to reuse this so I've
# put it in a library
from python.tools.primes import prime_factors
from python.tools.utils import profile

number = 600851475143


@profile
def euler3():
    return max(prime_factors(number))


if __name__ == "__main__":
    assert euler3() == 6857
