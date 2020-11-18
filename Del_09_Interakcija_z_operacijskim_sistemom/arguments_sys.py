import sys

if __name__ == "__main__":
    TEST = "dsdsdsd"
    try:
        first_argument = sys.argv[1]
        if first_argument == "-u":
            print(TEST.upper())
        else:
            print(TEST)
    except IndexError:
        print(TEST)
