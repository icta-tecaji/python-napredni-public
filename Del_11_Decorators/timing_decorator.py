import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        print(f"Total run time: {total_time}")
        return result

    return wrapper


if __name__ == "__main__":

    # @timer
    # from skripte.timing import logtime
    # from skripte.once_per_minute import once_per_minute
    from skripte.memoization import memoize

    @timer
    @memoize
    def waste_time(num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(10000)])

    waste_time(500)
    print("done")
    waste_time(500)
    print("done")
