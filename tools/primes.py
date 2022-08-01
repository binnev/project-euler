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
    def next(cls):
        biggest_prime = cls.all()[-1]
        n = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2
        while True:
            n += 2
            if is_prime(n):
                cls.add(n)
                return n


def sieve_primes(N) -> tuple[int]:
    composites = set()
    biggest_prime = max(Primes.all())
    new_primes = []
    start = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2
    for n in range(start, N, 2):  # consider only odd numbers
        if n not in composites:
            composites.update(range(2 * n, N, n))
            new_primes.append(n)
    Primes.add(*new_primes)
    return Primes.all()[:N]


def is_prime(n):
    square_root = math.sqrt(n)
    for p in Primes.all():
        if p > square_root:
            return True
        if n % p == 0:
            return False
    return True


def primes_by_trial_division(N=math.inf) -> list[int]:
    biggest_prime = max(Primes.all())
    start = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2
    for n in range(start, N, 2):
        if is_prime(n):
            Primes.add(n)
            yield n
