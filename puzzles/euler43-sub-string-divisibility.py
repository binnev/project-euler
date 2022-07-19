# -*- coding: utf-8 -*-
"""
Sub-string divisibility
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

"""
from itertools import combinations, permutations
import sys

codePath = r"C:\gdrive\code\python"
if codePath not in sys.path:
    sys.path.insert(0, codePath)
from myfunctions import sieve_primes, prime_factors

digits = "0987654321"
pans = ["".join(p) for p in permutations(digits) if p[0] != "0"]
primes = 2, 3, 5, 7, 11, 13, 17
results = []

for p in pans:

    success = True  # assume number is successful

    for shift, prime in zip(range(1, 8), primes):
        sub = int(p[shift : shift + 3])

        if sub % prime != 0:
            success = False
            break
    if success:
        results.append(p)

print("sum of the results is:", sum(map(int, results)))
