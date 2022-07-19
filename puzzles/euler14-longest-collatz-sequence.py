# Longest Collatz sequence
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


"""
import matplotlib.pyplot as plt, numpy as np, time


def collatz(n, counter=0, full=False):
    sequence = [n]
    #    print("starting Collatz with n = ", n)

    while n not in (tree if full == False else [1]):

        if n % 2 == 0:
            #            print("\t{} is even. Divide by 2".format(n))
            n = int(n / 2)

        else:
            #            print("\t{} is odd. Multiply by 3 and add 1".format(n))
            n = n * 3 + 1

        sequence.append(int(n))
        counter += 1

    #    print("\t{} is in the tree".format(n))
    return sequence, counter


tree = {4: 2}  # initialise with the orbit
# %% Which starting number, under one million, produces the longest chain?
t1 = time.clock()

N = 1000000
for n in range(5, N):
    if n not in tree:
        sequence, counter = collatz(n)
        total_length = counter + tree[sequence[-1]]
        for s in sequence[:-1]:
            tree[s] = total_length
            total_length -= 1

t2 = time.clock()
print("time elapsed: ", t2 - t1)
#%%
numbers, steps = np.array(list(tree.items())).T
s_max = steps.max()
n_max = numbers[steps == steps.max()][0]
print("number with the longest sequence =", n_max, "with", steps.max(), "steps")

fig, ax = plt.subplots(figsize=(10, 10))
ax.semilogy()
# plot the top 10 longest sequences
r = 100
lw = 1
colours = plt.cm.gray(np.linspace(1, 0, r))
for s, c in zip(sorted(steps)[-r:], colours):
    n = numbers[steps == s][0]
    rank = s_max - s
    print(n, s, rank)
    plt.plot(
        np.linspace(s_max - s, s_max - s + r - rank, r + 1 - rank),
        collatz(n, full=True)[0][: r + 1 - rank],
        label=n,
        lw=lw,
        ms=1.5 * lw,
        alpha=1,
        zorder=rank,
        color=c,
        marker="o",
    )
    lw += 0.2


plt.legend()


len(tree)
