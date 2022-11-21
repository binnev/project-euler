"""
Even Fibonacci numbers

Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four
million, find the sum of the even-valued terms.
"""
from python.tools import profile

N = 4e6  # max fibonacci term size


@profile.function
def euler2():
    a, b = 1, 2  # initial values
    c = 0

    even = [b]  # collect the fibonacci terms here

    while c <= N:
        c = a + b
        a = b
        b = c

        if c % 2 == 0:
            even.append(c)

    return sum(even)


if __name__ == "__main__":
    assert euler2() == 4613732
