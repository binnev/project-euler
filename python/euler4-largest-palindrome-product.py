"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from python.tools.utils import profile


def is_palindrome(number):
    p = str(number)  # convert to string so we can reverse digits easily
    return p == p[::-1]  # if the number is equal to its reverse


@profile
def euler4():
    start, end = 100, 999  # bounds for all possible 3-digit numbers
    candidates = list(range(start, end + 1))  # create list of all 3-digit numbers
    candidates.reverse()  # reverse so that we can start from the largest
    palindromes = list()  # empty list to store palindromes
    jj_crit = len(candidates)  # limits the search area

    """ Visualise a grid of the candidate numbers multiplied together to create all
    possible products, with the largest number (999*999) in the top left.
    
    We will go through each row until we find a palindrome product. Then we will limit the
    search area to avoid needlessly finding smaller palindromes. """

    # for each candidate number
    for ii, c in enumerate(candidates):
        # generate a row of products
        row = candidates[ii:jj_crit]
        products = [c * r for r in row]
        # for each product
        for jj, p in enumerate(products):
            if is_palindrome(p):  # if it's a palindrome
                palindromes.append(p)  # add it to the list
                # update the max search area; this limits the length of future rows
                jj_crit = jj + ii
                break  # stop searching in this row; subsequent palindromes will be smaller
        # limit the search area in the ii direction too
        if ii >= jj_crit:
            break

    return max(palindromes)


if __name__ == "__main__":
    assert euler4() == 906609
