# -*- coding: utf-8 -*-
"""
Integer right triangles
Problem 39 
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
if __name__ == '__main__':

    # grind out the pythagorean triples with circumference <= 1000
    triples = {}

    for circumference in range(1, 1000 + 1):

        a = 1
        while a < circumference - 1:
            b = ((circumference - a) ** 2 - a**2) / (2 * (circumference - a))
            c = ((circumference - a) ** 2 + a**2) / (2 * (circumference - a))

            if (b % 1 == 0 and c % 1 == 0) and (b > 0 and c > 0):
                triple = tuple(sorted((int(ii) for ii in (a, b, c))))  # unordered
                if circumference in triples:
                    triples[circumference].add(triple)
                else:
                    triples[circumference] = {triple}

            a += 1

    circ_max = 0
    combos_max = 0
    for circ, combos in triples.items():
        if len(combos) > combos_max:
            circ_max = circ
            combos_max = len(combos)

    print("circumfernce", circ_max, "gives max combos", combos_max)
