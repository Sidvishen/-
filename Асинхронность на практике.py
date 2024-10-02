import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(2 /power)
        print(f'Силач {name} поднял {i} шара')
    print(f'Силач {name} закончил соревнования')
async def start_tournament():
    tasks = []
    tasks.append(start_strongman('Pasha', 3))
    tasks.append(start_strongman('Denis', 2))
    tasks.append(start_strongman('Apalon', 4))
    await asyncio.gather(*tasks)

asyncio.run(start_tournament())