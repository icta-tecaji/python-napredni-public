def my_function():
    try:
        1 / 0
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    import timeit
    setup = "from __main__ import my_function"
    print(timeit.timeit("my_function()", setup=setup, number=10000))

# def f(x):
#     return x**2
# def g(x):
#     return x**4
# def h(x):
#     return x**8

# if __name__ == "__main__":
#     import timeit
#     print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))