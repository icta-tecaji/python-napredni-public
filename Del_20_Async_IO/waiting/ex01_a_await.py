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
    result_f = await f(2, "prva")
    result_g = await g(2, "druga")
    print(f"finished at {time.strftime('%X')}")
    print(result_f, result_g)


if __name__ == "__main__":
    asyncio.run(main())
