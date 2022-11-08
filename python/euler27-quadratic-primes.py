# -*- coding: utf-8 -*-
"""
Quadratic primes
Problem 27
Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40, 40**2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n=41, 41**2 + 41 + 41 is clearly
divisible by 41.

The incredible formula n**2−79*n+1601 was discovered, which produces 80 primes
for the consecutive values 0≤n≤79. The product of the coefficients, −79 and
1601, is −126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| ≤ 1000
(i.e. -1000 < a < 1000; -1000 <= b <= 1000)

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.

"""

from python.tools.primes import eratosthenes_sieve

primes = eratosthenes_sieve(100000)  # sieve the primes
max_primes = max(primes)  # evaluate this once instead of on the fly each time
quad = lambda n, a, b: n**2 + a * n + b  # define func for quadratics
a_range = range(-999, 999 + 1)
b_range = range(-1000, 1000 + 1)
n_max = 0
a_crit, b_crit = None, None


def is_prime(n):
    if n < 0:  # mod(n)
        n = -n
    if n > max_primes:
        raise Exception("we've run outta primes")
    return n in primes


# for -1000 < a < 1000
for a in a_range:

    # for -1000 <= b <= 1000
    for b in b_range:

        # the following is applied to each a, b pair

        # 1) if n_max in the quadratic doesn't yield a prime,
        if not is_prime(quad(n_max, a, b)):
            continue  # then skip this a, b pair

        # 2) if n_max DID yield a prime then we'll arrive here.
        # scan downward from n_max to zero (more likely to hit non-primes
        # sooner this way) and if we find a non-prime, discard this a, b pair
        prime = True  # assume result is prime to start with
        n = n_max - 1  # initialise n at n_max-1 (we already tested n_max)
        # decrement n to zero and see if they are all primes
        while n >= 0:
            if not is_prime(quad(n, a, b)):
                prime = False  # set to false so can continue to next a, b pair
                break  # exit the loop when a non-prime result is encountered
            n -= 1  # increment n
        if not prime:  # if a non-prime was found on the way to zero
            continue  # skip to the next a, b pair

        # 3) if 0 <= n <= n_max all yielded primes, then we might be in with a
        # winner. Start scanning upwards from n_max to find a new n_max.
        prime = True  # assume result is prime to start with
        n = n_max + 1  # initialise n at n_max+1 (we already tested n_max)
        # increment n and see if they are all primes
        while True:
            if not is_prime(quad(n, a, b)):
                break  # exit the loop when a non-prime result is encountered
            n += 1  # increment n

        # update value of n_max and the corresponding a, b values
        n_max = n
        a_crit = a
        b_crit = b

print("result = ", a_crit * b_crit)

# # %% brute force to find the beautiful patterns
# from mpl_toolkits.mplot3d import Axes3D
# from scipy.sparse import lil_matrix
#
# t1 = clock()
# R = 1000
#
# a_range = range(-(R - 1), (R - 1) + 1)
# b_range = range(-R, R + 1)
# # b_range = range(-25, 25+1)
# N = np.zeros((len(a_range), len(b_range)))
#
# for i, a in enumerate(a_range):
#     for j, b in enumerate(b_range):
#         prime = True
#         n = 0
#         while prime is True:
#             if not is_prime(quad(n, a, b)):
#                 break  # exit the loop when a non-prime result is encountered
#             n += 1  # increment n
#
#         N[i, j] = n
#
# t2 = clock()
# print("elapsed time:", t2 - t1)
# #%%
# # plot the surface of number of primes found versus coefficients a and b
# aa, bb = np.meshgrid(a_range, b_range)
# aa = aa.T
# bb = bb.T  # not sure why this is required!
# # fig, ax = plt.subplots(figsize=(5,5))
# # plt.setp(ax, xlabel="a", ylabel="b")
# plt.rc("font", size=10)
# # plt.imshow(N.T, cmap=plt.cm.inferno_r, origin="lower")
# # plt.colorbar()
# # fig.savefig("imshow.png", dpi=300)
#
# threshold = 4  # don't plot any values below this
# for threshold in range(10, 71, 2):
#     clip = N >= threshold
#     xx, yy, zz = aa[clip], bb[clip], N[clip]
#
#     #    fig = plt.figure(figsize=(10,10))
#     #    ax = Axes3D(fig)
#     #    plt.setp(ax, xlabel="a", ylabel="b", ylim=[-1100.,  1100.],
#     #             xlim=[-1098.9,  1098.9])
#     #    ax.view_init(elev=80, azim=0)
#     #    aa, bb = np.meshgrid(a_range, b_range)
#     #    #ax.scatter(xx, yy, zz, color=plt.cm.inferno_r(zz/max(zz)))
#     #    ax.plot_surface(aa, bb, N.T, cmap=plt.cm.inferno_r)
#     ##    ax.contour(aa, bb, N.T, cmap=plt.cm.inferno_r, )
#     ##    ax.contour(aa, bb, N.T, zdir='z', offset=+50, cmap=plt.cm.inferno_r, )
#
#     # sort data by z value so that higher ones are always on top
#     zz, yy, xx = (np.array(i) for i in zip(*sorted(zip(zz, yy, xx))))
#
#     fig, ax = plt.subplots(figsize=(6, 5))
#     ax.scatter(
#         xx,
#         yy,
#         np.ones_like(xx) * 5,
#         color=plt.cm.inferno_r(zz / N.max()),
#         marker=".",
#     )
#     plt.setp(
#         ax,
#         xlabel="a",
#         ylabel="b",
#         ylim=[-R, R],
#         xlim=[-R, R],
#         xticks=[-1000, 1000],
#         xticklabels=["-1k", "1k"],
#         yticks=[-1000, 1000],
#         yticklabels=["-1k", "1k"],
#     )
#     #    plt.axis("square")
#
#     plt.title("(a, b) pairs resulting in at least {} primes".format(threshold))
#     fig.savefig("threshold{:03d}.png".format(threshold), dpi=100)
#
# # %% compile the images into a video / gif
#
# import imageio, glob
#
# filenames = glob.glob("threshold*.png")
# images = []
# for f in filenames:
#     images.append(imageio.imread(f))
# imageio.mimsave("threshold.gif", images, duration=0.1)
#
# # %% print out the quadratics for the top results
# from scipy.optimize import curve_fit
#
# for a, b, n in zip(xx, yy, zz):
#     print("n^2 {:+d}n {:+d} yields {}".format(a, b, int(n)))
#
# # plot the actual results
# fig, ax = plt.subplots(figsize=(10, 10))
# plt.scatter(
#     xx,
#     yy,
#     color=plt.cm.inferno_r(zz / N.max()),
#     marker=".",
#     label="data",
# )
#
# # define a function for the curve fit
# def func(a, c, d, e):
#     return c * a**2 + d * a + e
#
#
# popt, pcov = curve_fit(func, xx, yy)
#
# plt.plot(np.sort(xx), func(np.sort(xx), *popt), "r-", label="fit")
