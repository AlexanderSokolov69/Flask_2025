import asyncio
import os
from math import sqrt
from time import time


async def is_prime(x):
    print('Processing %i...' % x)
    if x < 2:
        print('%i is not a prime number.' % x)
    elif x == 2:
        print('%i is a prime number.' % x)
    elif x % 2 == 0:
        print('%i is not a prime number.' % x)
    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print('%i is not a prime number.' % x)
                return
            elif i % 100000 == 1:
                await asyncio.sleep(0)
        print('%i is a prime number.' % x)


async def main():
    tasks = []
    tasks.append(asyncio.create_task(is_prime(9637529763296797)))
    tasks.append(asyncio.create_task(is_prime(427920331)))
    tasks.append(asyncio.create_task(is_prime(157)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    print(f'{time() - t0} seconds')
