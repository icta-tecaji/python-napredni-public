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
    try:
        result = await asyncio.wait_for(
            asyncio.gather(f(2, "prva"), g(2, "druga")), timeout=1.5
        )
    except asyncio.TimeoutError:
        print("oops took longer than 1.5s!")
    else:
        print(result)

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())
