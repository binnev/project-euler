# -*- coding: utf-8 -*-
"""
Pandigital products
Problem 32 

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

"""

import numpy as np, itertools as it
from math import floor, ceil
from time import clock
import matplotlib.pyplot as plt

""" considering multiplication A * B = C, with len(A) = a, etc. 
The total number of digits must add up to N. 
Number of digits in C is at least as many as the max in A or B:
c >= max(a, b) 
(the limiting case is when either A or B = 1, and then C = the other. In this
case c = max(a, b). c can never be less than max(a, b). )

Therefore, the maximum length of number A (or B) is floor(N/2)
e.g. for N = 11, 
A = 12345, B = 6, C = 74070
Not a valid answer, but the sum of digits is correct. 
"""

def is_pandigital(ABC):
    # function to check if a number is pandigital
    if "0" in ABC:
        return False
    
    setABC = set(ABC)  # need to use this multiple times. 
    
    # check for duplicate digits
    if len(ABC) != len(setABC):
        return False
                
    # check each digit up to N appears exactly once
    for d in digits:
        if ABC.count(d) != 1:
            return False
    
    return True

N = 9  # number of total digits
digits = set(str(i) for i in range(1, N+1))
calculations = 0
pan = set()
products = set()
combos = list()
t1 = clock()

for a in range(1, floor(N/2) + 1):

    for A in it.permutations(digits, a):  # a-digit permutations of A

        # subtract A digits to find remaining digits available for B
        bs = digits.difference(A)
        # construct integer a
        A = "".join(A)  # construct A
        if A == "1":
            continue
        
        for b in range(1, floor(N/2) + 1):

            # find b-digit permutations of remaining digits
            for B in it.permutations(bs, b):  
                B = "".join(B)  # construct B
                if B == "1":
                    continue
        
                C = str(int(A) * int(B))
                calculations += 1
                
                ABC = A+B+C
                
                if not is_pandigital(ABC):
                    continue
                
                pan.add(ABC)
                products.add(C)
                combos.append((A, B))

# prune the list to allow only N-length pandigitals
pan = {p for p in pan if len(p) == N}
t2 = clock()
print(calculations,"calculations performed")
print(len(pan),"{}-length pandigital products found:".format(N), pan)
print("time taken =",t2-t1)

print("answer =", sum(int(p) for p in products))
    
