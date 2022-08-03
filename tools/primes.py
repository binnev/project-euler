import math
from pathlib import Path

from euler_functions import is_even


class Primes:
    """Sort of singleton class to handle caching known primes in a file"""

    _primes: tuple[int] = None
    filename = Path(__file__).parent / "primes.txt"

    @classmethod
    def all(cls) -> tuple:
        if not cls._primes:
            cls.read()
        return cls._primes

    @classmethod
    def read(cls):
        with open(cls.filename.as_posix(), "r") as file:
            raw = file.read()
            cls._primes = tuple(map(int, raw.split(",")))

    @classmethod
    def add(cls, *primes: int):
        if not primes:
            return
        with open(cls.filename.as_posix(), "a") as file:
            new = ",".join(map(str, primes))
            file.write(f",{new}")
        cls.read()

    @classmethod
    def up_to(cls, N):
        if N < cls.all()[-1]:
            return tuple(filter(lambda x: x < N, cls.all()))
        else:
            return sieve_primes(N)

    @classmethod
    def first(cls, N):
        if N < len(cls.all()):
            return cls.all()[:N]
        else:
            difference = N - len(cls.all())
            for _ in range(difference):
                cls.next()
            return cls.all()

    @classmethod
    def next_by_trial(cls):
        biggest_prime = cls.all()[-1]
        n = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2
        while True:
            if is_prime(n):
                cls.add(n)
                return n
            n += 2

    @classmethod
    def next_by_sieve(cls, distance=100):
        biggest_prime = max(Primes.all())
        end = biggest_prime + distance
        new_primes = []
        composites = set()
        for p in Primes.all():
            composites.update(range(2 * p, end, p))
        start = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2
        for n in range(start, end, 2):  # consider only odd numbers
            if n not in composites:
                composites.update(range(2 * n, end, n))
                Primes.add(n)
                return n
        # return Primes.all()[:end]


def is_prime(n):
    square_root = math.sqrt(n)
    for p in Primes.all():
        if p > square_root:
            return True
        if n % p == 0:
            return False
    return True


def next_prime_by_trial_division(N=math.inf) -> list[int]:
    biggest_prime = max(Primes.all())
    start = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2
    for n in range(start, N, 2):
        if is_prime(n):
            Primes.add(n)
            yield n


def sieve_primes(limit) -> list[int]:
    if limit < 2:
        return []
    primes = [2]
    composites = set()
    for n in range(3, limit, 2):  # consider only odd numbers
        if n not in composites:
            composites.update(range(2 * n, limit, n))
            primes.append(n)
    return primes


def partial_sieve(limit, primes: list[int] = None):
    """Sieve a search space above a known list of primes"""
    if limit < 2:
        return []
    primes = primes or [2]
    biggest_prime = primes[-1]
    composites = set()
    if biggest_prime >= limit:
        return [p for p in primes if p <= limit]

    start = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2
    print(f"Sieving for primes between {start} and {limit}")

    # populate composites from upper edge of known space onwards
    for p in primes:
        remainder = biggest_prime % p
        biggest_multiple = biggest_prime - remainder
        composites.update(range(biggest_multiple + p, limit + 1, p))

    # search space from upper edge of known space onwards
    for n in range(start, limit + 1, 2):
        if n not in composites:
            composites.update(range(n + n, limit + 1, n))
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
