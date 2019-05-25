from math import sqrt
from numpy import product as prod

#%%
"""
primes = set()
factors = []
product = 1
x = 2
number = 14431758493#1803 < -- this number causes a mistake

y = number

# while the product of the factors is not the whole number (i.e. we haven't
# found all the factors yet)
while product != number:

    # while x evenly divides y - i.e. divide y by x as many times as possible
    while (y % x == 0):
        factors.append(x)  # add x to the factors list
        y /= x  # divide y by x
        product *= factors[-1]  # update the product with the latest root
#    primes.add(x)
    x += 1 if x%2==0 else 2

#    # after x no longer evenly divides y, get the next prime
#    isPrime = True  # assume x is prime
#    for p in primes:
#        if x % p == 0:  # if a known prime divides x
#            isPrime = False  # x is not prime
#            if x % 2 == 0:
#                x += 1
#            else:
#                x += 2

    print("x, y, product, number = {}, {}, {}, {}".format(x, y, product,number))

print("factors = {}".format(factors))
print("product of factors = {}".format(prod(factors)))
#"""
# %% find the first N primes
"""
N = 9999999

def find_primes(N):
    # function to generate the list of primes below N, using the sieve of
    # Eratosthenes

    N = round(N)
    ints = list(range(2,N))
    comp = set([])

#    print("\n the starting integers = {}".format(ints))

    # start sieving from the smallest prime -- 2
    for i in ints:
    #    print("\n considering i={}".format(i))

        if i not in comp:  # if this number is not a known composite
#            print("{} is not a composite".format(i))
            # generate the multiples of p up to N
            mult = set(range(i, N, i)[1:])
#            print("multiples = {}".format(mult))
            # add these to the set of composites
            comp.update(mult)

    ints = set(ints).difference(comp)
    return ints

primes = sorted(find_primes(N))
print(primes[-20:])
#"""
# %% trial division with precalculated list of primes

"""
N = number = 14431758
factors = []
product=1

if primes[-1] >= sqrt(number):  # if we have enough primes

    for p in primes:
#        print("considering prime ", p)
        if p <= sqrt(number):
#            print("\t{} <= sqrt {} ({:.1f})".format(p, number, sqrt(number)))
            while N % p == 0:
                print("\t\t{} is a factor of {}".format(p, number))
                factors.append(p)
                N = int(N/p)
                product *= factors[-1]

        else:
            print("\t{} > sqrt{} ({:.1f})".format(p, number, sqrt(number)))
            if N != 1:
                factors.append(N)
                product *= N
            break

else:
    raise Exception("not enough primes! Need more primes man!")

print("\nfactors = {}".format(factors))
print("product of factors = {}".format(product))
print("number = {}".format(number))
#"""

# %% trial division, finding the primes as we go along

N = number = 10
factors = []
product=1
p = 2

while product != number:
    if p <= sqrt(number):
        while N % p == 0:
            print("\t\t{} is a factor of {}".format(p, number))
            factors.append(p)
            N = int(N/p)
            product *= factors[-1]
        p += 1 if p % 2 == 0 else 2

    else:
        print("\t{} > sqrt{} ({:.1f})".format(p, number, sqrt(number)))
        if N != 1:
            factors.append(N)
            product *= N
        break

print("\nfactors = {}".format(factors))
print("product of factors = {}".format(product))
print("number = {}".format(number))








