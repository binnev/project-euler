# -*- coding: utf-8 -*-
"""
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

"""
import itertools as it

# find all the possible 2-digit numbers we can use as numerator/denominator
numbers = [str(i) for i in range(10,100)]

# find all the ways in which we can pair up these numbers.
pairs = list(it.combinations(numbers, 2))

digits = "123456789"
solutions = set()

for a, b in pairs:

    # check for shared digits
    shared_digits = []
    for d in digits:
        if (d in a) and (d in b):
            shared_digits.append(d)

    if not shared_digits:
        continue  # if we can't cancel; skip to next a, b pair

    # cancel out the shared digits
    # only cancel one digit each time. Repeat for multiple digits
    for d in shared_digits:
        a_new, b_new = a, b
        a_new = a_new.replace(d, "", 1)
        b_new = b_new.replace(d, "", 1)

        # catch any zeros
        if "0" in (a_new, b_new):
            continue

        # evaluate the fractions
        frac = int(a)/int(b)
        frac_new = int(a_new)/int(b_new)
        if frac == frac_new:
            solutions.add((int(a), int(b)))

print("found",len(solutions),"solutions:",solutions)

numerator = 1
denominator = 1
for a, b in solutions:
    numerator *= a
    denominator *= b

# %%