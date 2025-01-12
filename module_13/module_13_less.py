import time, asyncio

async def get_temp():
    print('first')
    await asyncio.sleep(2)
    print('25 sec')

async def get_press():
    print('second')
    await asyncio.sleep(4)
    print('101 kPa')

async def main():
    print('start')
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_press())
    await task1
    await task2
    print('finish')

start = time.time()
asyncio.run(main())
finish = time.time()

print(finish - start)

"""async def notification():
    time.sleep(10)
    print('До доставки осталось 10 минут')

async def main():
    task = asyncio.create_task(notification())
    print('Собирается в поездку')
    print('Едем')

asyncio.run(main())"""