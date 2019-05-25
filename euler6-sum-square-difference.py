"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
N = 100
natural = list(range(1,N+1))
sum_of_squares = sum(n**2 for n in natural)
square_of_sums = sum(natural)**2

print(square_of_sums - sum_of_squares)

# %% that was too easy, so let's do it with a for loop for giggles
sum_of_squares = 0
sums = 0
for n in range(1, N+1):
    sum_of_squares += n**2
    sums += n
square_of_sums = sums**2

print(square_of_sums - sum_of_squares)


# trivial
