import os
import aiohttp
import asyncio

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org', 'http://vk.com']


async def get_url(url, session):
    print(f'GETTING URL: {url}')
    async with session.get(url) as resp:
        print(f'URL {url} RECEIVED STATUS: {resp.status}')
        text = await resp.text()
        print(f'URL {url} LEN TEXT: {len(text)}')
        return url, text


async def main():
    counter = 0
    async with aiohttp.ClientSession() as session:
        tasks = [get_url(url, session) for url in urls]
        for future in asyncio.as_completed(tasks):
            counter += 1
            res_url, res_text = await future
            print(f"the {counter} len result for url {res_url} was: {len(res_text)}")


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
