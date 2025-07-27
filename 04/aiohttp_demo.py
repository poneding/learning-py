import asyncio
import time

# uv add aiohttp
import aiohttp


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.content.read()
            print("Read {} bytes from {}".format(len(content), url))
            print("Read {} from {}".format(resp.content_length, url))


async def main():
    t_start = time.time()
    urls = [
        "https://www.baidu.com",
        "https://www.python.org",
        "https://www.github.com",
    ]

    tasks = [download_one(url) for url in urls]
    await asyncio.gather(*tasks)

    t_end = time.time()
    print(f"All downloads completed in {t_end - t_start} seconds")


if __name__ == "__main__":
    asyncio.run(main())
