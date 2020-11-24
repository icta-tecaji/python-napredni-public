import functools
import time


class CalledTooOftenError(Exception):
    pass


def once_per_minute(func):
    last_invoked = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal last_invoked
        elapsed_time = time.time() - last_invoked
        if elapsed_time < 60:
            raise CalledTooOftenError(f"Only {elapsed_time} has passed")
        last_invoked = time.time()
        return func(*args, **kwargs)

    return wrapper
