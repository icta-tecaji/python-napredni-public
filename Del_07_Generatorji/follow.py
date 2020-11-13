import time


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == "__main__":
    with open("./data/access-log") as logfile:
        for line in follow(logfile):
            print(line, end="")
