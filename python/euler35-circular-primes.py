# -*- coding: utf-8 -*-
"""
Circular primes

Problem 35

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

"""

import sys
from time import clock

codePath = "C:/gdrive/code/python"
if codePath not in sys.path:
    sys.path.insert(0, codePath)
from myfunctions import sieve_primes

t1 = clock()
primes = {str(p) for p in sieve_primes(1e6)}  # generate primes; store as str
winners = []

for n in primes:

    isPrime = True  # assume true

    for ii in range(1, len(n)):
        rotation = n[-ii:] + n[:-ii]
        if rotation not in primes:
            isPrime = False
            break  # stop generating rotations

    if isPrime:
        winners.append(n)

print("found", len(winners), "circular primes")
t2 = clock()
print("time elapsed:", t2 - t1)
