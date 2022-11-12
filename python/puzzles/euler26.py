# -*- coding: utf-8 -*-
"""
Reciprocal cycles

Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

"""
from math import ceil

from python.tools import profile


def gen_decimals(d: int, limit=100) -> (list[int], list[int]):
    """
    Keep yielding decimal digits until we hit the limit
    """
    remainder = 1
    ii = 0
    while True:
        div, remainder = divmod(remainder * 10, d)
        yield div
        if not remainder or ii == limit:
            return
        ii += 1


def find_longest_substring(input: list[int]) -> list[int]:
    """
    Now we just need to make it dynamic; have a for loop iterating over the digit generator,
    and every iteration, do a form of this mask check.
    something like:
    input = []
    for digit in generate():
        if digit == 0 and not input:
            continue
        input.append(digit)
        if find_longest(input):
            return it

    :param input:
    :return:
    """
    input = "".join(map(str, input))
    input = input.lstrip("0")  # ignore leading zeros
    input = list(map(int, input))

    match_length = 5
    for mask_length in range(1, 20):
        mask = input[:mask_length]
        repeated_mask = mask[::]
        while len(repeated_mask) < match_length:
            repeated_mask += mask

        if repeated_mask == input[: len(repeated_mask)]:
            return mask
    return []


def get_decimals(d: int) -> (list[int], list[int]):
    """
    Generate the fixed and repeating parts of the decimal
    """
    digits = []
    remainders = []
    rem = 1
    ii = 0
    while True:
        dig, rem = divmod(rem * 10, d)
        digits.append(dig)
        if not rem:
            fixed = digits
            repeating = []
            break
        if rem in remainders:
            ind = remainders.index(rem)
            fixed = digits[:ind]
            repeating = digits[ind:]
            break
        if dig:
            remainders.append(rem)

        ii += 1

    return fixed, repeating


@profile.function
def euler26():
    N = 1000
    max_d = 0
    max_repeats = 0
    for d in range(2, N):
        fixed, repeating = get_decimals(d)
        repeats = len(repeating)
        if repeats > max_repeats:
            max_repeats = repeats
            max_d = d
    return max_d


if __name__ == "__main__":
    assert euler26() == 983
