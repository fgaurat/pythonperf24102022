import asyncio


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')

    c = await add(5,6)
    print(c)

    l = [add(5,6),add(15,26),add(2,4),add(5,26),add(52,4)]
    r = await asyncio.gather(*l)
    print(r)


if __name__=='__main__':
    asyncio.run(main())

