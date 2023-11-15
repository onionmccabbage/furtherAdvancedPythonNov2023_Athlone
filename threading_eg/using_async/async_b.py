import asyncio
import random

async def makeRandom(idx,thresold):
    print(f'Begin makeRandom({idx})')
    i = random.randint(0,10)
    while i< thresold:
        print(f'makeRandom({i}) is too low. Retrying')
        await asyncio.sleep(idx + 1)
        i = random.randint(0,10)
    print(f'Finished: makeRandom({idx})=={i}')
    return i

async def main():
    results = await asyncio.gather(  *(makeRandom(i, 10-i-1) for i in range(3)))
    return results

if __name__ == '__main__':
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print(f'r1:{r1} r2:{r2} r3:{r3}')


