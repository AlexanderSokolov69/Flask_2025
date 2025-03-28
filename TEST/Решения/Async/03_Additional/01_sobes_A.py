import time
import asyncio


async def do_task(name, *args):
    COEFF = .01
    times = [(args[0], args[1]), (args[2], args[3])]
    for n, (t1, t2) in enumerate(times, 1):
        print(f"{name} started the {n} task.")
        await asyncio.sleep(COEFF * t1)
        print(f"{name} moved on to the defense of the {n} task.")
        await asyncio.sleep(COEFF * t2)
        print(f"{name} completed the {n} task.")
        if n < len(times):
            print(f"{name} is resting.")
            await asyncio.sleep(COEFF * 5)


async def interviews(*data):
    tasks = []
    for participant in data:
        tasks.append(
            do_task(*participant)
        )
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews(*data))
    print(time.time() - t0)
    data = [('Harry', 7, 6, 1, 9), ('Mike', 8, 5, 5, 9), ('George', 9, 2, 1, 5), ('Antony', 9, 2, 8, 6)]
    t0 = time.time()
    asyncio.run(interviews(*data))
    print(time.time() - t0)
