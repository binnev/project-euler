# -*- coding: utf-8 -*-
"""
Maximum path sum I
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method! ;o)

"""
# %%
import time
tStart = time.time()

raw = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

raw = [r.split(" ") for r in raw.split("\n")]  # separate into rows and numbers
tri = [[int(p) for p in r] for r in raw]  # convert to integers from strings

def highest_value_child(tri):
    col = 0  # initialise column location. Set to zero so it chooses the only element in row 0
    values = []
    indices = []
    for ii, row in enumerate(tri):

        if ii == 0:  # if it's the first row
            values.append(row[col])  # just grab the only element

        else:
            # get the cells that are adjacent to the previous column
            adj = row[col], row[col+1]
            # find out whether the max adjacent is left or right
            col += adj.index(max(adj))  # take one step into the max cell
            values.append(max(adj))  # store the max cell

        indices.append((ii, col))

    return indices, values

indices, values = highest_value_child(tri)
print("using the highest value child method, we go through values:\n",
      values,
      "which gives a total of:", sum(values))

# generate the rank triangle
rank = []
for ii, row in enumerate(tri):
    rank.append([])  # add another row

    for jj, value in enumerate(row):

        # identify "parents" and "children"
        lParent = tri[ii-1][jj-1] if jj-1 >=0 else 0
        rParent = tri[ii-1][jj] if jj < len(tri[ii-1]) else 0
        parents = lParent, rParent

        lChild = tri[ii+1][jj] if ii+1 < len(tri) else 0
        rChild = tri[ii+1][jj+1] if ii+1 < len(tri) else 0
        children = lChild, rChild

#        print("value is:", value,
#              "\nparents are:", parents,
#              "\nchildren are:", children)

        # calculate rank by summing value and the max parents and children
        r = value + max(parents) + max(children)
        rank[ii].append(r)

# use hvc on rank triangle
indices, _ = highest_value_child(rank)
# retrieve the values from tri using indices
values = [tri[i][j] for i, j in indices]

print("using the highest value child method on the rank triangle, "
      "we go through values:\n",
      values,
      "which gives a total of:", sum(values))

print ("Run Time = " + str(time.time() - tStart))

""" for the follow-up problem, use the opposite approach -- start from the
BOTTOM of the pyramid! """
