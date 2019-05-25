def prime_factors(number):
    from math import sqrt
    N = number
    factors = []
    product = 1
    p = 2

    while product != number:  # done
        if p <= sqrt(number):  # done
            while N % p == 0:
                factors.append(p)
                N = int(N/p)
                product *= p
            p += 1 if p % 2 == 0 else 2

        else:  # if p > sqrt(number) -- done
            if N != 1:  # done
                factors.append(N)
                product *= N  # done

    # organise into a dict
    factors = {key: factors.count(key) for key in set(factors)}

    return factors


def prod(vector):
    product = 1
    for v in vector:
        product *= v
    return product


start, end = 2, 20

factors = {}
for n in range(start, end+1):

    factors_n = prime_factors(n)

    for f, p in factors_n.items():

        if f in factors:
            if factors[f] < p:
                factors[f] = p
        else:
            factors[f] = p

product = prod([key**value for key, value in factors.items()])

print("product = ", product)
print("check:")
for n in range(start, end+1):
    print("{} / {} gives {} remainder".format(product, n, product%n))