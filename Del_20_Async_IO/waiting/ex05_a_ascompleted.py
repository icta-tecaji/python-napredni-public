import asyncio
import time


async def f(delay, what):
    await asyncio.sleep(delay)
    print("function f", what)
    return what


async def g(delay, what):
    await asyncio.sleep(delay)
    print("function g", what)
    return what


async def h(delay, what):
    await asyncio.sleep(delay)
    raise ValueError
    print("function h", what)
    return what


async def main():
    print(f"started at {time.strftime('%X')}")
    task_f = asyncio.create_task(f(3, "prva"))
    task_g = asyncio.create_task(g(2, "druga"))
    task_h = asyncio.create_task(h(2, "tretja"))

    for fut in asyncio.as_completed([task_f, task_g, task_h], timeout=5.0):
        try:
            res = await fut
            print(f"one task down! -> {res}")
        except Exception:
            print("ouch")

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())
