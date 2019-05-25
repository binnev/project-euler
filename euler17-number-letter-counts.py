# -*- coding: utf-8 -*-
"""
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

"""

strange = ("", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")

tens = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety")

def number_reader(number):

    billions = millions = thousands = hundreds = end = ""

    # deal with the last 2 digits -- this is the most irregular.
    if number <20:
        return strange[number]
    if 20 <= number <100:  # if the number is in the tens
        t, i = [int(n) for n in str(number)][-2:]  # split into tens and ones
        return tens[t]+strange[i]

    if number >= 100:
        end = int(str(number)[-2:])
        h = int(str(number)[-3])  # grab the hundreds
        n = "and" if end != 0 else ""
        hundreds = n if h == 0 else strange[h]+"hundred"+n
        end = number_reader(end)

    if number >= 1000:
        k = int(str(number)[-6:-3])  # grab the thousands
        # here's where we need the recursion. But we don't need to return the thing just yet.
        thousands = "" if k == 0 else number_reader(k)+"thousand"

    if number >= 1000000:
        m = int(str(number)[-9:-6])  # grab the thousands
        # here's where we need the recursion. But we don't need to return the thing just yet.
        millions = "" if m == 0 else number_reader(m)+"million"

    if number >= 1000000000:
        b = int(str(number)[-12:-9])  # grab the thousands
        # here's where we need the recursion. But we don't need to return the thing just yet.
        billions = "" if b == 0 else number_reader(b)+"billion"

    if number >= 1000000000000:
        raise Exception("Number's too big, yo")

    return billions+millions+thousands+hundreds+end

strings = []
for n in range(1001):
    strings.append(number_reader(n))

len("".join(strings))
#%% more elegant version using // and %

def number_reader(number):

    if number >= 1000000000000:
        raise Exception("Number's too big, yo")

    # billions
    b, remainder = divmod(number,1000000000)  # returns quotient and remainder
    billions = number_reader(b)+"billion" if b != 0 else ""

    # millions
    m, remainder = divmod(remainder,1000000)
    millions = number_reader(m)+"million" if m != 0 else ""

    # thousands
    k, remainder = divmod(remainder,1000)
    thousands = number_reader(k)+"thousand" if k != 0 else ""

    # hundreds
    h, remainder = divmod(remainder,100)
    hundreds = number_reader(h)+"hundred" if h != 0 else ""

    # and
    n = "and" if (number > 100 and remainder != 0) else ""

    # sub 100
    if remainder <20:
        end = strange[remainder]
    if 20 <= remainder <100:  # if the number is in the tens
        t, i = [int(n) for n in str(remainder)][-2:]  # split into tens and ones
        end = tens[t]+strange[i]

    return billions+millions+thousands+hundreds+n+end

strings = []
for n in range(1001):
    strings.append(number_reader(n))

len("".join(strings))