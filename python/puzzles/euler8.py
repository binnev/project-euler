# Largest product in a series
"""
The four adjacent digits in the 1000-digit number that have the greatest
product are 9 x 9 x 8 x 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?

"""
from python.tools import utils, profile
from python.tools.primes import product



@profile.function
def euler8():
    number = utils.load_puzzle_input("euler8")
    number = [int(n) for n in number.strip().replace("\n", "")]
    length = 13
    products = []
    for ii in range(len(number) - 1 - length):
        digits = number[ii : ii + length]
        products.append(product(digits))
    return max(products)


if __name__ == "__main__":
    assert euler8() == 23514624000
