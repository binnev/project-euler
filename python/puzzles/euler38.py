# -*- coding: utf-8 -*-
"""
Pandigital multiples
Problem 38 
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 
5, giving the pandigital, 918273645, which is the concatenated product of 9 
and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?

"""


def is_pandigital(i):
    i = str(i)
    return True if sorted(i) == constant else False


if __name__ == "__main__":

    constant = [str(i) for i in range(1, 10)]
    pans = []

    for i in range(9999):
        #    print("considering",i)
        product = ""
        ms = []
        m = 1

        while len(product) < 9:
            product += str(i * m)
            ms.append(m)
            m += 1

        if is_pandigital(product):
            print(i, "multiplied by", ms, "gives pandigital", product)
            pans.append(product)

    print(max(pans))
