# -*- coding: utf-8 -*-
"""
Double-base palindromes

Problem 36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

"""

# %% first solution -- brute force

from time import clock
import numpy as np

limit = 1000000

def baseTenTo(n10, base=10):
    """function to convert base-10 numbers to other bases """
    new = []
    while n10 > 0:
        n10, b = divmod(n10, base)
        new.append(str(b))
    return int("".join(reversed(new)))

def toBinary(n10):
    return "{:b}".format(n10)

winners = []
t1 = clock()
for i in range(limit):
    n = str(i)  # string of the base 10 number
    if n[::-1] != n:  # if not a palindrome in base 10
        continue  # skip, because it has to be a palindrome in both
    n2 = toBinary(i)#str(baseTenTo(i, 2))  # string of the base-2 number
    if n2[::-1] == n2:
        # skip numbers with leading zeros in either base
        if (n[0] == "0") or (n2[0] == "0"):
            continue
        winners.append(i)

print("found",len(winners),"DB palindromes:", winners)
print("sum =",sum(winners))
print("time elapsed=",clock()-t1)
