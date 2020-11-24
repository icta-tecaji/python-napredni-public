import functools
import pickle


def memoize(func):
    cache = {}  # zažene se ko dekoriramo funkcijo

    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # zažene se vsakič ko je dekororana funkcija zagnana
        t = (pickle.dumps(args), pickle.dumps(kwargs))
        if t not in cache:
            print(f"Caching NEW value for {func.__name__}{args}")
            cache[t] = func(*args, **kwargs)
        else:
            print(f"Using OLD value for {func.__name__}{args}")
        return cache[t]

    return wrapper
