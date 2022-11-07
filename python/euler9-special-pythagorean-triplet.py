# special pythagorean triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.  # NOT a**2 + b**2 + c**2 = 1000!
Find the product abc.
"""
import matplotlib.pyplot as plt

from python.tools.utils import profile


@profile
def euler9():
    triples = {}

    for circumference in range(1, 2000):

        a = 1
        while a < circumference:
            b = ((circumference - a) ** 2 - a**2) / (2 * (circumference - a))
            c = ((circumference - a) ** 2 + a**2) / (2 * (circumference - a))

            if (b % 1 == 0 and c % 1 == 0) and (b > 0 and c > 0):
                triple = tuple(sorted((int(ii) for ii in (a, b, c))))  # unordered
                if circumference in triples:
                    triples[circumference].add(triple)
                else:
                    triples[circumference] = {triple}

            a += 1

    fig, ax = plt.subplots(figsize=(10, 10))
    cm = plt.cm.viridis

    for circumference, abcs in triples.items():

        aa, bb = [a for (a, b, c) in sorted(abcs)], [b for (a, b, c) in sorted(abcs)]
        plt.plot(aa, bb, "-o", c=cm(circumference / max(triples)), mew=0)

    plt.show()


if __name__ == "__main__":
    assert euler9() == 31875000
