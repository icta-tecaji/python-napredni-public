import functools


def my_decorator(func):
    def wrapper():
        print("to se je zgodilo pred klicem funkcije.")
        func()
        print("to se je zgodilo po klicu funkcije.")

    return wrapper


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


# @my_decorator
@do_twice
def say_hey(to):
    print(f"Heyy! {to}")
    return 10


if __name__ == "__main__":
    a = say_hey("pytohn")
    print(say_hey.__name__)
    print(a)
