# -*- coding: utf-8 -*-
"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""
from math import sqrt, ceil
from time import clock
import numpy as np
from itertools import product, permutations, combinations, combinations_with_replacement

t0 = clock()

def d(N, debug=False):
    n = 1  # initialise n
    divisors = []
    limit = sqrt(N)#ceil(sqrt(N))
    while n <= limit:  # search up to the square root
        if N % n == 0:  # if it divides evenly
            divisors.append(n)  # store the divisor
            dividend = N // n
            divisors.append(dividend)  # and the dividend
        n += 1  # increment n

    if N in divisors:  # this mainly covers the case when N == 2
        divisors.remove(N)

    if debug is True:
        return set(divisors)
    else:
        return sum(set(divisors))

limit = 28123

t1 = clock()

# calculate all the perfect numbers under 28123
Np = [N for N in range(2, limit+1) if d(N) == N]  # unexpectedly quick

t2 = clock()
print(t2-t1,"seconds to compute perfect numbers")

# calculate all the abundant numbers below limit
Na = [N for N in range(2, limit+1) if d(N) > N]  # unexpectedly quick

t3 = clock()
print(t3-t2,"seconds to compute abundant numbers")

# find all the permutations of sums of 2 abundant numbers.
# this gives us the set of numbers < limit which CAN be expressed as such
can = [i+j for i,j in combinations_with_replacement(Na, 2)]  # ~2.5 sec
#can = {i + j for i in Na for j in Na}  # ~3.5 sec
#can = set(np.matmul(np.array([Na]).T, np.array([Na])).flatten())  # ~11.5 sec

"""
permutations :: all pairings of elements. Even reversed ones. E.g. "AB" and
"BA" will both be included.

combinations :: all pairings of elements, ignoring reversed duplicate ones.
only "AB" will be included.

combinations_with_replacement :: same as combinations, but repeat values are
allowed. "AA" and "AB" will be included, but not "BA"

product ::
"""


t4 = clock()
print(t4-t3,"seconds to compute 'can' sum numbers")

# find the set of numbers from 1..limit
N = set(range(1,limit+1))
t5 = clock()
print(t5-t4,"seconds to compute range from 1..limit")

# find the members of N that are not in "can"
# these are the numbers that CAN'T be constructed from the sum of 2 abundants
cant = N.difference(can)
t6 = clock()
print(t6-t5,"seconds to compute 'cant' non-summable numbers")


print("number of numbers that can't be expressed as sum of two abundants:\n",
      len(cant),
      "\nsum of numbers that can't be expressed as sum of two abundants:\n",
      sum(cant)
      )
