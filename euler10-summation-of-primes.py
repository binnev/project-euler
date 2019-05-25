# Summation of primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def sieve_primes(N):
    # function to generate the list of primes below N, using the sieve of
    # Eratosthenes

    N = round(N)
    ints = list(range(2,N))
    composites = set([])

    # start sieving from the smallest prime -- 2
    for i in ints:

        if i not in composites:  # if this number is not a known composite
            # generate the multiples of p up to N
            mult = set(range(i, N, i)[1:])  # exclude the first one -- it's a prime
            # add these to the set of composites
            composites.update(mult)

    primes = set(ints).difference(composites)
    return primes

primes = sorted(sieve_primes(2000000))
print(sum(primes))

# %%
import matplotlib.pyplot as plt, numpy as np
plt.scatter(range(len(primes)), primes, c = plt.cm.viridis(np.array(primes)/max(primes)), edgecolors="none")
plt.xlabel("prime"); plt.ylabel("value")