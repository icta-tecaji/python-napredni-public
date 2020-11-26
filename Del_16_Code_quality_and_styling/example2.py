#example2.py -> PyFlakes
import sys


def print_is_divisible(dividend, divisor):
    is_divisible = ((dividend % divisor) == 0)
    if is_divisble:
        print(f'{dividend} is divisible by {divisor}')
    else:
        print(f'{dividend} is not divisible by {divisor}')