# -*- coding: utf-8 -*-
"""
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

"""

#%% easy peasy with m

N = 1001  # size of the spiral. Must be odd.
diag = 0
for n in range(1, N + 1, 2):
    if n == 1:
        diag += 1
        continue
    # sum of the corner values
    diag += sum(n**2 - (n - 1) * i for i in range(4))

print(diag)

# %% can I do it descending from N to 0 and in a one liner

sum(sum(n**2 - (n - 1) * i for i in range(4)) for n in range(1001, 1, -2)) + 1
