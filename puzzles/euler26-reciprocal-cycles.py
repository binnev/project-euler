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


def repeats(a, d, z=5, limit=1000, confidence=10):
    A = a  # dividend
    digits = ""
    ii = 0
    stop = False
    while stop is False:
        digits += str(a // d)  # append the quotient
        a = (10 * a) % d  # find the next decimal by remainder * 10

        #        print("\n")
        #        print("ii = ",ii)
        #        print("digits found so far:",digits)
        # make a mask and compare it to the digits found so far#
        for m in range(1, ceil(len(digits) / 2) + 1):
            mask = digits[-m:]
            #            print("m =",m)
            # if the mask contains only zeroes
            if set(mask) == {"0"}:
                continue  # ignore it
            #            print("considering mask:",mask)

            # if the mask occurs more than once in the digits then it is repeating
            reps = digits.count(mask)
            if reps > 1:
                #                print("found repeating mask",mask)

                # the mask length * number of repeats must be > confidence lim.
                # this is to punish short masks
                if reps * len(mask) < confidence:
                    continue

                # if the repeated occurrences are *contiguous* then we have a
                # repeating sequence
                check = mask * reps  # make a contiguous sequence of mask
                if check == digits[-len(check) :]:  # check it matches last digits
                    #                    print("it's a repeating sequence")
                    stop = True
                    break
            else:
                #                print("no repeats of mask")
                pass

        # stop the loop if z zeroes have been found in a row
        if digits[-z:].count("0") == z:
            #            print("reached the zero limit ({})".format(z))
            break

        ii += 1
        if ii > limit:
            #            print("found the max number of digits ({})".format(limit))
            break

    if stop is True:
        #        print("fraction",A,"/",d,"=",digits,"contains repeating pattern",mask,
        #              "(len={})".format(len(mask)))
        pass

    return mask if stop is True else None


top_d, top_mask = None, ""
N = 1000
for d in range(1, N):
    if d % 10 == 0:
        print(d)
    mask = repeats(1, d, limit=2000, confidence=5)
    if mask is None:
        continue
    if len(mask) > len(top_mask):
        top_mask = mask
        top_d = d
        print("new top d =", d, "with mask length", len(mask))


print("top mask =", top_mask, "(len = {})".format(len(top_mask)))

"""
this algorithm is REALLY inefficient at the moment. It takes a minute to run.
It also seems to get slower as d gets larger. Why is this?
Investigate the relationship between d and len(mask). It is always:
    d = len(mask) + 1
"""
#%%
