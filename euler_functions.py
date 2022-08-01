import cProfile
import math
import pstats
from pathlib import Path


def read_primes_file() -> list[int]:
    filename = Path(__file__).parent / "primes.txt"
    with open(filename.as_posix(), "r") as file:
        raw = file.read()
        return list(map(int, raw.split(",")))


PRIMES = read_primes_file()


def is_even(n: int) -> bool:
    return n % 2 == 0


def sieve_primes(N, known_primes: list = None) -> list[int]:
    primes = known_primes or [2]
    composites = set()
    biggest_prime = max(primes)
    start = biggest_prime + 1 if is_even(biggest_prime) else biggest_prime + 2
    for n in range(start, N, 2):  # consider only odd numbers
        if n not in composites:
            composites.update(range(2 * n, N, n))
            primes.append(n)
    return primes


def primes_by_trial_division(limit=math.inf) -> list[int]:
    known_primes = []

    def is_prime(n):
        square_root = math.sqrt(n)
        for p in known_primes:
            if p > square_root:
                return True
            if n % p == 0:
                return False
        return True

    candidate = 1
    while candidate < limit:
        candidate += 1
        if is_prime(candidate):
            known_primes.append(candidate)
            yield candidate


def prime_factors(number, output="dict"):
    """function to find the prime factors of a number by (modified) trial division.

    By default, the factors will be returned in dict format: {factor: exponent}:
    In [1]: prime_factors(24)
    Out[1]: {2: 3, 3: 1}
    Representing 24 = 2^3 * 3^1 = 2*2*2*3

    If optional argument output='list' is passed, the factors will be returned in list
    form:
    In [1]: prime_factors(24, output="list")
    Out[1]: [2, 2, 2, 3]
    """

    from math import sqrt

    N = number  # remainder of number to be factorised
    factors = []  # list of factors found so far
    product = 1  # product of the factors
    p = 2  # trial number. Skip 1.

    # when the product of the factors equals the number itself, we know we've found
    # all the factors. Until then, keep looping
    while product != number:
        if p <= sqrt(number):  # search up to the square root of the number
            while N % p == 0:  # while trial number p divides remainder N evenly
                factors.append(p)  # add p to list of known factors
                N = int(N / p)  # divide remainder N by factor p
                product *= p  # multiply product by factor p
            p += 1 if p % 2 == 0 else 2  # increment p so as to skip even numbers
        else:  # if p > sqrt(number)...
            if N != 1:  # and remainder N is not 1
                factors.append(N)  # N must be the last prime factor; add to factors
                product *= N  # update product

    # output factors
    if output == "list":
        return factors
    else:
        # organise into a dict
        factors = {key: factors.count(key) for key in set(factors)}
        return factors


def nonprime_factors(number):
    """function to return the non-prime factors of a number"""
    factors = set()
    naturals = range(1, number + 1)  # natural numbers from 1 to the number
    for n in naturals:  # for each natural number
        if number % n == 0:  # if n is a divisor of the number
            # if the divisor and the reciprocal are both already in factors
            if (n in factors) and (int(number / n) in factors):
                # stop searching; we've found all the factors
                break
            # add the factor and the reciprocal to the list of factors
            factors.add(n)
            factors.add(int(number / n))
        if n > number:
            break
    return factors


def product(iterable):
    from functools import reduce

    return reduce(lambda a, b: a * b, iterable)


def profile(string: str):
    print(("> " + string + " <").center(100, "="))
    cProfile.run(string, sort="tottime", filename="foo")
    p = pstats.Stats("foo")
    print
