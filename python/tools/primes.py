import math
from pathlib import Path

from euler_functions import is_even
from tools.exceptions import TrialDivisionError


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
            return eratosthenes_sieve(N)

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


def is_prime(n: int, primes: list[int]) -> bool:
    """Trial division"""
    square_root = math.sqrt(n)
    if primes[-1] < square_root:
        raise TrialDivisionError(f"Not enough known primes to check if {n} is prime")
    for p in primes:
        if p > square_root:
            return True
        if n % p == 0:
            return False
    return True


def next_prime_by_trial_division(primes: list[int]) -> int:
    biggest_prime = max(primes)
    start = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2
    n = start
    while True:
        if is_prime(n, primes):
            return n
        n += 2


def next_prime_by_sieve(primes: list[int]) -> int:
    biggest_prime = max(primes)
    limit = biggest_prime + 100
    while True:
        new_primes = partial_sieve(limit, primes)
        if new_primes:
            return new_primes[0]
        else:
            limit += 100


def eratosthenes_sieve(limit: int) -> list[int]:
    if limit < 2:
        return []
    primes = [2]
    composites = set()
    for n in range(3, limit + 1, 2):  # consider only odd numbers
        if n not in composites:
            composites.update(range(n**2, limit, n))
            primes.append(n)
    return primes


def eratosthenes_sieve2(limit: int) -> list[int]:
    if limit < 2:
        return []
    #          0      1
    numbers = [False, False] + [True] * (limit - 1)
    for n in range(2, limit + 1):  # consider only odd numbers
        if numbers[n]:
            for composite in range(n**2, limit + 1, n):
                numbers[composite] = False
    primes = [index for index, value in enumerate(numbers) if value is True]
    return primes


def sundaram_sieve(limit: int) -> list[int]:
    k = (limit - 1) // 2
    square_root = math.sqrt(k)
    A = [True] * (k + 1)
    i = 1
    while i < square_root:
        j = i
        while (composite := i + j + 2 * i * j) <= k:
            A[composite] = False
            j += 1
        i += 1
    T = [index for index, value in enumerate(A) if value is True]
    T = [2 * t + 1 for t in T]
    return [2] + T[1:]


def atkin_sieve(limit: int) -> list[int]:
    results = [2, 3, 5]
    sieve_list = [False] * (limit + 1)
    sq = math.ceil(math.sqrt(limit))
    for n, _ in enumerate(sieve_list):
        r = n % 60  # modulo remainder
        if r in [1, 13, 17, 29, 37, 41, 49, 53]:
            solutions = [
                m for x in range(1, sq) for y in range(1, sq) if (m := 4 * x**2 + y**2) <= limit
            ]
            for m in solutions:
                sieve_list[m] = not sieve_list[m]

        if r in [7, 19, 31, 43]:
            solutions = [
                m for x in range(1, sq) for y in range(1, sq) if (m := 3 * x**2 + y**2) <= limit
            ]
            for m in solutions:
                sieve_list[m] = not sieve_list[m]

        if r in [11, 23, 47, 59]:
            solutions = [
                m
                for x in range(1, sq)
                for y in range(1, sq)
                if x > y and (m := 3 * x**2 - y**2) <= limit
            ]
            for m in solutions:
                sieve_list[m] = not sieve_list[m]

    for n, n_is_prime in enumerate(sieve_list):
        if n == 1:
            continue
        if n_is_prime:
            results.append(n)
            n_sq = n**2
            for mult in range(n_sq, limit, n_sq):
                # Note that the multiples that can be factored by 2, 3, or 5 need not be marked,
                # as these will be ignored in the final enumeration of primes.
                sieve_list[mult] = False
    return results


def partial_sieve(limit, primes: list[int]) -> list[int]:
    """Sieve a search space above a known list of primes"""
    biggest_prime = primes[-1]
    if limit < biggest_prime:
        return []
    composites = set()
    new_primes = []
    start = biggest_prime + 1 if biggest_prime == 2 else biggest_prime + 2

    # populate composites from upper edge of known space onwards
    for p in primes:
        remainder = biggest_prime % p
        biggest_multiple = biggest_prime - remainder
        composites.update(range(biggest_multiple + p, limit + 1, p))

    # search space from upper edge of known space onwards
    for n in range(start, limit + 1, 2):
        if n not in composites:
            composites.update(range(n + n, limit + 1, n))
            new_primes.append(n)
    return new_primes


def generate_primes_by_trial_division(limit=math.inf) -> list[int]:
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


def primes_by_trial_division(limit: int) -> list[int]:
    return list(generate_primes_by_trial_division(limit))
