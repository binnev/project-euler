# -*- coding: utf-8 -*-
"""
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

"""
import matplotlib.pyplot as plt
import numpy as np

# %% simple solution

power = 5

# work out how many orders of magnitude of N to search
num_digits = 2  # initialise with at least 2 digits i.e. N = 99

# while the max digit power sum is greater than the max N
while 9**power * num_digits > int("9" * num_digits):
    num_digits += 1  # increase the number of digits by 1

N = range(2, int("9" * num_digits))  # range of trial numbers

# sum of numbers for which the digit power sum == the number
sum(n for n in N if sum(d**power for d in (int(i) for i in str(n))) == n)

# %% nice plots
fig, ax = plt.subplots(figsize=(5, 5))
plt.rc("font", size=9)
ax.loglog()
powers = 2, 3, 4, 5
colours = plt.cm.inferno(np.linspace(0.2, 0.9, len(powers)))

for power, colour in zip(powers, colours):
    # work out how many orders of magnitude of N to search
    num_digits = 2
    while 9**power * num_digits > int("9" * num_digits):
        num_digits += 1

    N = range(2, int("9" * num_digits))  # range of trial numbers
    S = []  # digit power sums go here
    yes = []  # numbers that map to themselves go here

    for n in N:

        s = sum(d**power for d in (int(i) for i in str(n)))  # digit power sum
        S.append(s)

        if s == n:
            yes.append(n)

    plt.plot(N, S, c=colour, zorder=-power, label="p={}".format(power))
    plt.plot(yes, yes, "s", ms=10, mfc=colour, mec="k")
    for y in yes:
        plt.text(y * 1.2, y, y, ha="left", va="center")

plt.plot(N, N, "-k", lw=2, label="N")
plt.legend()
plt.setp(ax, xlabel="N", ylabel="digit power sum")

fig.savefig("euler30.png", dpi=150)
# %%
