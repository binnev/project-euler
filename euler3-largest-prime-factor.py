"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# I've written a function to find prime factors. I'll want to reuse this so I've
# put it in a library
from euler_functions import prime_factors

number = 600851475143
factors = prime_factors(number)
print(max(factors))