import os
from time import time
import asyncio
import aiohttp


async def get_file(i, url, session):
    print(f"getting file number {i}")
    async with session.get(url, allow_redirects=True) as response:
        await write_file(i, response)


async def write_file(i, response):
    print(f"writing file number {i}")
    filename = response.url.name
    data = await response.read()
    with open(f'./img/{filename}', 'wb') as file:
        file.write(data)


async def main():
    url = 'https://loremflickr.com/640/480'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(30):
            task = asyncio.create_task(get_file(i, url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    print(f'{time() - t0} seconds')
