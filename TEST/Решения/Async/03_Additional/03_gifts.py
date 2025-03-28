import asyncio
import time

COEFF = 100


async def buy_gift(item, time_to_choose, time_to_buy):
    print(f'Buy {item}')
    time.sleep(time_to_choose / COEFF)
    await asyncio.sleep(time_to_buy / COEFF)
    print(f'Got {item}')


async def stops(i, stop, arrive):
    print(f'Buying gifts at {i} stop')
    temp = sorted([x for x in gifts if x[1] + x[2] <= stop], key=lambda y: -(y[1] + y[2]))
    tasks = []
    res = stop
    for gift in temp:
        if res - gift[1] - gift[2] >= 0:
            tasks.append(asyncio.create_task(buy_gift(*gift)))
            res -= gift[1] + gift[2]
            gifts.remove(gift)
    await asyncio.gather(*tasks)
    print(f'Arrive from {i} stop')
    time.sleep(arrive / COEFF)


async def arrival():
    tasks = []
    for item in gifts:
        tasks.append(asyncio.create_task(buy_gift(*item)))
    await asyncio.gather(*tasks)


def main():
    for i, trip in enumerate(trips, 1):
        asyncio.run(stops(i, *trip))
    if gifts:
        print("Buying gifts after arrival")
        asyncio.run(arrival())


if __name__ == '__main__':
    line = input()
    trips = []
    while line:
        trips.append(tuple(map(int, line.split())))
        line = input()

    line = input()
    gifts = []
    while line:
        gift, t_c, t_b = line.split()
        gifts.append((gift, int(t_c), int(t_b)))
        line = input()
    main()
