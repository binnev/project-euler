# Highly divisible triangular number

"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""


def prime_factors(number, output="dict"):
    from math import sqrt

    N = number
    factors = []
    product = 1
    p = 2

    while product != number:  # done
        if p <= sqrt(number):  # done
            while N % p == 0:
                factors.append(p)
                N = int(N / p)
                product *= p
            p += 1 if p % 2 == 0 else 2

        else:  # if p > sqrt(number) -- done
            if N != 1:  # done
                factors.append(N)
                product *= N  # done

    if output == "list":
        return factors
    else:
        # organise into a dict
        factors = {key: factors.count(key) for key in set(factors)}
        return factors


# %% brute force -- trial division


def nonprime_factors(number):
    factors = set()
    naturals = range(1, number + 1)
    for n in naturals:
        if number % n == 0:
            if (n in factors) and (int(number / n) in factors):
                break
            factors.add(n)
            factors.add(int(number / n))
        if n > number:
            break
    return factors


nonprime_factors(550)

# %%
start = time.time()
triangle = 1
ii = 2
factors = []

while len(factors) < 500:
    factors = nonprime_factors(triangle)
    #    print("for number ",triangle," there are ",len(factors)," factors")
    triangle += ii
    ii += 1

end = time.time()
print("elapsed time = ", end - start)
# 76576500 is the number with >500 factors. It is the 12376th triangle number
# %%

triangle = 1

start = time.time()

for ii in range(12376):

    factors = prime_factors(triangle)
    #    print("triangle number ",triangle," has ",len(factors)," prime factors")
    triangle += ii

end = time.time()
print("elapsed time = ", end - start)