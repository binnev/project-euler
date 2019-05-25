# -*- coding: utf-8 -*-
"""
Pentagon numbers
Problem 44 
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first 
ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
difference are pentagonal and D = |Pk − Pj| is minimised; what is the 
value of D?

"""
import matplotlib.pyplot as plt, numpy as np
from functools import reduce
from math import sqrt

def pent(n):
    return int(n*(3*n-1)/2)
pk = 1

def is_pent(P):
    n = (0.5 + sqrt(0.25+6*P))/3
    return True if n % 1 == 0 else False

#Psums, Pdifs, Ds = [], [], []
#pents = [pent(n) for n in range(1, 10)]
#diffs = [pents[i]-pents[i-1] for i in range(1, len(pents))]
#sums =  [pents[i]+pents[i-1] for i in range(1, len(pents))]

#fig, ax = plt.subplots()

pk = 1
ii = 2
while True:
    pj = pk
    pk = pent(ii)
    print("pj and pk are:",pj,pk)
    s = pk+pj
    d = pk-pj
    
    if is_pent(d) and is_pent(s):
        raise Exception("found them:",pj,pk)
    
    ii += 1
#    
#x = np.arange(1, len(pents)+1)
#plt.plot(x, pents, "-k", ms=10, mfc="none")
#plt.plot(x+.5, Psums, "-g")
#plt.plot(x+.5, Pdifs, "-r")


