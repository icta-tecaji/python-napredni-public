import multiprocessing
import time
import numpy as np


def cpu_bound(number):
    numbers2 = numbers * numbers
    return np.sum(numbers2)


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = np.array([5_000_000 + x for x in range(10)])

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
