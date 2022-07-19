# -*- coding: utf-8 -*-
"""
Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

number = str(2**1000)
number = [int(n) for n in number]
sum(number)


# easy money