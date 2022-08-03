import time

from tools.primes import eratosthenes_sieve, primes_by_trial_division

functions = [
    eratosthenes_sieve,
    primes_by_trial_division,
]
limit = 999999


def profile(func):
    t1 = time.perf_counter()
    func(limit)
    t2 = time.perf_counter()
    return t2 - t1


def main():
    results = {func.__name__: profile(func) for func in functions}
    for name, t in sorted(results.items(), key=lambda kv: kv[1]):
        print(f"{name}: {t}")


if __name__ == "__main__":
    main()
