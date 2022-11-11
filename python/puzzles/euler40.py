# -*- coding: utf-8 -*-
"""
Champernowne's constant
Problem 40 
An irrational decimal fraction is created by concatenating the positive 
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the 
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""
if __name__ == '__main__':

    limit = 1000000
    decimal = ""
    i = 0
    while len(decimal) <= limit:
        decimal += str(i)
        i += 1

    product = 1
    for p in range(7):
        i = 10**p
        product *= int(decimal[i])

    print(product)
