import math


def f1(degrees):
    return math.cos(degrees)


def f2(degrees):
    e = 2.718281828459045
    return ((e ** (degrees * 1j) + e ** -(degrees * 1j)) / 2).real


if __name__ == "__main__":

    def main():
        print("Starting")
        for i in range(500000):
            f1(i)
            f2(i)
        print("Finished")

    main()
