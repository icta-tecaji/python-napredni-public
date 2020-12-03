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


async def main():
    print(f"started at {time.strftime('%X')}")
    coro_f = f(2, "prva")
    coro_g = g(2, "druga")
    result_f = await coro_f
    result_g = await coro_g
    print(f"finished at {time.strftime('%X')}")
    print(result_f, result_g)


if __name__ == "__main__":
    asyncio.run(main())
