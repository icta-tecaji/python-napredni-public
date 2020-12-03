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
    task_f = asyncio.create_task(f(2, "prva"))
    task_g = asyncio.create_task(g(2, "druga"))
    await asyncio.sleep(1)  # <- f() and g() are already running!
    result_f = await task_f
    result_g = await task_g
    print(f"finished at {time.strftime('%X')}")
    print(result_f, result_g)


if __name__ == "__main__":
    asyncio.run(main())
