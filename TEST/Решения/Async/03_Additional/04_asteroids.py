import asyncio
from PIL import Image


async def process_file(name):
    print(f"Start {name}")
    average = await calc_average(name)
    result = await calc_percent_amount_quarter(average, name)
    print(f"Ready {name}")
    return result


async def calc_percent_amount_quarter(av, name):
    im = Image.open(name)
    x, y = im.size
    pixels = im.load()
    colours = {}
    different = 0
    q = {"I": 0, "II": 0, "III": 0, "IV": 0}
    for i in range(x):
        for j in range(y):
            if sum(pixels[i, j]) > av:
                colours[pixels[i, j]] = colours.get(pixels[i, j], 0) + 1
                different = different + 1
                if i >= x // 2 and j <= y // 2:
                    q["I"] += 1
                elif i <= x // 2 and j <= y // 2:
                    q["II"] += 1
                elif i <= x // 2 and j >= y // 2:
                    q["III"] += 1
                else:
                    q["IV"] += 1

    mx = max(colours.values())
    percent = int(mx * 100_000 / (x * y))
    amount = int(different * 100 / (x * y))
    quarter = max(q.items(), key=lambda x: x[1])
    print(f"Done {name}, percent {percent}")
    print(f"Done {name}, amount {amount}")
    print(f"Done {name}, quarter {quarter[0]}")
    return percent, amount, quarter[0]


async def calc_average(name):
    await asyncio.sleep(0.1)
    im = Image.open(name)
    x, y = im.size
    pixels = im.load()
    all_pix = 0
    for i in range(x):
        for j in range(y):
            all_pix += sum(pixels[i, j])
    return all_pix / (x * y)


async def asteroids(*names):
    tasks = []
    for name in names:
        tasks.append(
            process_file(name)
        )
    result = await asyncio.gather(*tasks)
    return [(i[0], *i[1]) for i in zip(names, result)]
