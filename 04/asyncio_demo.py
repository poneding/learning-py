import asyncio
import time


async def func1():
    print("Function 1 started")
    await asyncio.sleep(2)
    print("Function 1 ended")


async def func2():
    print("Function 2 started")
    await asyncio.sleep(1)
    print("Function 2 ended")


async def func3():
    print("Function 3 started")
    await asyncio.sleep(4)
    print("Function 3 ended")


async def main():
    t_start = time.time()
    # 第一种写法，使用 asyncio.wait, 现在已经不推荐，推荐使用 asyncio.gather
    # await asyncio.wait(
    #     [
    #         asyncio.create_task(func1()),
    #         asyncio.create_task(func2()),
    #         asyncio.create_task(func3()),
    #     ]
    # )
    # 第二种写法，使用 asyncio.gather，推荐
    await asyncio.gather(func1(), func2(), func3())
    t_end = time.time()
    print(f"All functions completed in {t_end - t_start} seconds")


if __name__ == "__main__":
    asyncio.run(main())
