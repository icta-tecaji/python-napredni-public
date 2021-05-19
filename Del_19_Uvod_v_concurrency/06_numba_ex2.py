import math
import time
import numpy as np
from numba import njit


@njit
def std(xs):
    # compute the mean
    mean = 0
    for x in xs:
        mean += x
    mean /= len(xs)
    # compute the variance
    ms = 0
    for x in xs:
        ms += (x - mean) ** 2
    variance = ms / len(xs)
    std = math.sqrt(variance)
    return std


a = np.random.normal(0, 1, 10000000)

start = time.time()
std(a)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))
