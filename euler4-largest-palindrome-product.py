"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

start, end = 1,9999
candidates = list(range(start, end+1))
candidates.reverse()
palindromes = list()
jj_crit=None

# generate all the products and put them in a set (avoiding duplicates)
for ii, c in enumerate(candidates):
    if jj_crit is not None:
        if ii >= jj_crit:
            break
    row = candidates[ii:jj_crit]
#    print("this row: from {} to {}".format(ii,jj_crit))
    products = [c*r for r in row]
#    print("c={} products={}".format(c,products).rjust(70))
    for jj, r in enumerate(row):
        p = str(c*r)  # find the products in descending order
        mid = round(len(p)/2)
        if p[:mid] == p[:mid-1:-1]:  # palindrome test
#            print("found a palindrome ({}) at ii = {}, jj = {}, c = {}, r = {}".format(p,ii,jj,c,r))
            palindromes.append(int(p))
            jj_crit=jj+ii
            break  # stop searching in this row

#palindromes = sorted(palindromes, reverse=True)
print(max(palindromes))
#%%