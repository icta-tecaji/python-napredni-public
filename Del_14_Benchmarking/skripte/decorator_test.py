from timethis import timethis, timethis_process_time


@timethis
def countdown(n):
    while n > 0:
        n -= 1


@timethis_process_time
def countdown2(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    countdown(10000000)
    countdown2(10000000)
