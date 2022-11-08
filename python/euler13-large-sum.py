# Large sum
"""
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.

"""
from python.tools import utils


@utils.profile
def euler13():
    numbers = utils.load_puzzle_input("euler13")

    numbers = numbers.split("\n")
    while "" in numbers:
        numbers.remove("")
    numbers = [int(n) for n in numbers]
    return int(str(sum(numbers))[:10])


if __name__ == "__main__":
    assert euler13() == 5537376230
