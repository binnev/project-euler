# -*- coding: utf-8 -*-
"""
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
from python.tools import utils


@utils.profile
def euler22():
    raw = utils.load_puzzle_input("euler22")
    f = sorted(raw.replace('"', "").split(","))
    scores = [sum(ord(c) - 64 for c in s) for s in f]
    return sum([w * p for w, p in zip(scores, range(1, len(f) + 1))])


if __name__ == "__main__":
    assert euler22() == 871198282
