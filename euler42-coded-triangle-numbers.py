# -*- coding: utf-8 -*-
"""
Coded triangle numbers
Problem 42
The nth term of the sequence of triangle numbers is given by, t_n = 0.5*n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?

"""
import string

# extract words from txt file
words = open("p042_words.txt").read().replace('"',"").split(",")
# find the length of the longest word
letters = string.ascii_uppercase
# define function to score words
def score(word):
    return sum(letters.index(l)+1 for l in word)
# define function for triangle numbers
def triangle(n):
    return int(0.5*n*(n+1))
# now compute the triangle numbers
triangles = [triangle(ii) for ii in range(1,50)]

triangle_words = 0
for word in words:
    if score(word) in triangles:
        triangle_words += 1

print("found",triangle_words,"triangle words")
