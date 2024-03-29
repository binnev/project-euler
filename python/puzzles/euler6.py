"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
"""
from python.tools import profile


@profile.function
def euler6():
    N = 100
    natural = range(1, N + 1)
    sum_of_squares = sum(n**2 for n in natural)
    square_of_sums = sum(natural) ** 2

    return square_of_sums - sum_of_squares


if __name__ == "__main__":
    assert euler6() == 25164150
