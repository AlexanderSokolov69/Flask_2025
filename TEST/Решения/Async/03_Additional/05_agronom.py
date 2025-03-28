import asyncio

COEFF = .001


async def soak(name, t):
    print(f"1 Soaking of the {name} started")
    await asyncio.sleep(t * COEFF)
    print(f"2 Soaking of the {name} is finished")


async def shelter(name, t):
    print(f"3 Shelter of the {name} is supplied")
    await asyncio.sleep(t * COEFF)
    print(f"4 Shelter of the {name} is removed")


async def transplant(name, t):
    print(f"5 The {name} has been transplanted")
    await asyncio.sleep(t * COEFF)
    print(f"6 The {name} has taken root")


async def fertilize(name):
    print(f"7 Application of fertilizers for {name}")
    await asyncio.sleep(3 * COEFF)
    print(f"7 Fertilizers for the {name} have been introduced)")


async def treat(name):
    print(f"8 Treatment of {name} from pests")
    await asyncio.sleep(5 * COEFF)
    print(f"8 The {name} is treated from pests")


async def process_plant(name, sk, sh, tr):
    print(f"0 Beginning of sowing the {name} plant")
    await soak(name, sk)
    await shelter(name, sh)
    await transplant(name, tr)
    print(f"9 The seedlings of the {name} are ready")


async def sowing(*data):
    tasks = []
    for d in data:
        tasks.append(process_plant(*d))
        tasks.append(fertilize(d[0]))
        tasks.append(treat(d[0]))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
    asyncio.run(sowing(*data))
