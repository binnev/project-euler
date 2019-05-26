"""
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

N = 10000000

# brute force method: test divisibility of every number
multiples = []
for n in range(N):
	if (n % 3 == 0) or (n % 5 == 0):
		multiples.append(n)

print(sum(multiples))
# [Finished in 8.5s] for N = 10000000

# one liner
print(sum(n for n in range(N) if (n % 3 == 0 or n % 5 == 0)))
# [Finished in 3.9s] for N = 10000000

# multiply instead; probably faster than checking
divisors = 3, 5
numbers = []
for d in divisors:
    numbers += list(range(d, N, d))

print(sum(set(numbers)))
# [Finished in 2.5s] for N = 10000000