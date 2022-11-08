# Longest Collatz sequence
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


"""
import numpy as np

from python.tools import utils


def collatz(n, tree, counter=0, full=False):
    sequence = [n]

    while n not in (tree if full == False else [1]):

        if n % 2 == 0:
            n = int(n / 2)

        else:
            n = n * 3 + 1

        sequence.append(int(n))
        counter += 1

    return sequence, counter


@utils.profile
def euler14():
    tree = {4: 2}  # initialise with the orbit

    N = 1000000
    for n in range(5, N):
        if n not in tree:
            sequence, counter = collatz(n, tree)
            total_length = counter + tree[sequence[-1]]
            for s in sequence[:-1]:
                tree[s] = total_length
                total_length -= 1

    numbers, steps = np.array(list(tree.items())).T
    return numbers[steps == steps.max()][0]


if __name__ == "__main__":
    assert euler14() == 837799
