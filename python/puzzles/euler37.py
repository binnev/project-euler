# -*- coding: utf-8 -*-
"""
Truncatable primes
Problem 37 
The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, and remain prime at each 
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

import sys
if __name__ == '__main__':

    codePath = "C:/gdrive/code/python"
    if codePath not in sys.path:
        sys.path.insert(0, codePath)
    from myfunctions import sieve_primes

    """ strategy #1: brute force. Just find loads of primes and check them all for 
    truncatability
    """

    primes = {str(p) for p in sieve_primes(1000000)}  # generate primes; store as str
    #%
    def is_truncatable(n):

        n = str(n)

        if n not in primes:
            raise Exception(n, " ain't prime, yo")

        for ii in range(1, len(n)):

            # remove digits from the right
            if n[:-ii] not in primes:
                #            print(n[:-ii],"ain't prime, yo")
                return False
            # remove digits from the left
            if n[ii:] not in primes:
                return False
        #            print(n[ii:],"ain't prime, yo")

        return True


    truncatable = []
    bad = "2", "3", "5", "7"
    for p in primes:
        if p in bad:
            continue
        if is_truncatable(p):
            truncatable.append(p)

    print(sum(int(t) for t in truncatable))
    # %%
    """
    strategy #2: 
    
    We can build a truncatable prime from a list of digits. Because the number has
    to be truncatable from the right, all of the digits in the number will at some
    point be "exposed" on the right edge of the number. Therefore all digits must 
    be one of the numbers which a prime number can end in: 1, 3, 7, 9
    
    However, the first digit can be any of the primes from 1-10: 2, 3, 5, 7. 
    
    But, if I'm not going to generate the list of primes beforehand, then I need to 
    have some way of checking if the expanded numbers are prime... I think I'll 
    need the prime list anyway. But maybe I can still save computational time. 
    """

    limit = 6  # number of digits to search
    primes = {str(p) for p in sieve_primes(1 * 10**limit)}  # generate primes; store as str

    start = "2", "3", "5", "7"  # digits I can start the number with
    add = "1", "3", "7", "9"  # numbers I can add to the right


    def expand_number(n, level=0, storage=None):  # get the recursion working on this.

        if level == 0:
            #        print("level = 0 so we're initialising storage = []")
            storage = []  # initialise storage

        if len(n) >= limit:
            #        print(n,"has len =",len(n),">= limit",limit)
            storage.append(n)
            #        print("storage =",storage)
            return None

        for a in add:
            #        print("adding",a,"to",n)
            expand_number(n + a, level + 1, storage)

        if level == 0:
            return storage  # return the list


    truncatable = []
    for n in start:
        for m in expand_number(n):
            if is_truncatable(p):
                truncatable.append(p)

                """no, this doesn't work because we only consider number of length
                = limit. I need to find the truncatable numbers, then expand THOSE"""

    truncatable = []
