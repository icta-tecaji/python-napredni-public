import functools
import time


def logtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time

        with open("timelog.txt", "a") as outfile:
            outfile.write(f"[{time.time()}]\t{func.__name__}\t{total_time}\n")

        return result

    return wrapper
