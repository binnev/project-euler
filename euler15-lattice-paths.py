""" Euler 15 - lattice paths """
import sys, numpy as np, matplotlib.pyplot as plt, time, itertools as it
from copy import deepcopy

codePath = "C:/gdrive/code/python"
if codePath not in sys.path:
    sys.path.insert(0, codePath)
from myfunctions import visualise_dict

# %% using Pascal's Triangle to calculate how many paths go through each node on the diagonal

t1 = time.clock()

def pascal_row(N):
    """Function to generate row N of Pascal's Triangle.
    Start with 1, and multiply this by (Nrow-s)/(1+s), where s is horizontal
    steps. For row N, the width of the triangle is N+1, and the number of steps
    S is N-1.
    """
    N=20
    row = [1]
    for s in range(N):
        row.append(int(row[-1] * (N-s)/(1+s)))
    return row

P = pascal_row(20)
sum(p**2 for p in P)
t2 = time.clock()
print("elapsed time =",t2-t1)
# %% trying to generate all permutations myself
"""
N = 10  # grid edge size
Nsteps = 2*N  # number of steps required in any path

def generate_binary_permutations(N):
    # N = number of elements in the set to rearrange
    import numpy as np

    # generate each column of the array
    columns = []
    for ii in range(N):
        columns.append(([0]*2**ii + [1]*2**ii) * 2**(N-ii-1))

    return [list(row) for row in np.array(columns)[::-1].T]

# generate Nsteps permutations -- i.e the full "tree" for 2N steps
permutations = generate_binary_permutations(Nsteps)

# now remove the impossible ones -- with more than 2 R or D steps
paths = [p for p in permutations if p.count(0) <=N and p.count(1) <=N]

print(N, len(permutations), len(paths), len(paths)/len(permutations))

# %% trying to step through each path step by step (really slow)
N=2
Nsteps = 2*N

oldpaths = [[]]

t1 = time.clock()
for step in range(Nsteps):
    print("step",step,"number of active paths =",len(oldpaths))
#    print("\tso far, the old paths are:")
#    print("\t",oldpaths)

    # duplicate each existing path without making a link to the same object
    paths = []
    for p in oldpaths:
        paths.append(deepcopy(p))
        paths.append(deepcopy(p))

#    print("\tafter duplicating each path, paths looks like:")
#    print("\t",paths)
    # append a 0 to one of the dupes, and a 1 to the other.
    for ii, p in enumerate(paths):
#        print("\tlooking at path number",ii)
        if ii % 2 == 0:
#            print("\tappending a zero to",p)
            p.append(0)
#            print("\tnow it looks like",p)
        elif ii % 2 != 0:
#            print("\tappending a one to",p)
            p.append(1)
#            print("\tnow it looks like",p)

    oldpaths = [p for p in paths if (p.count(0)<=N and p.count(1)<=N)]
#    oldpaths = paths

#    print("\tafter this iteration's operations, paths looks like:")
#    print("\t",oldpaths)
print("for N =",N,"the number of paths is",len(oldpaths))
t2= time.clock()
print("time elapsed =",t2-t1)
#"""