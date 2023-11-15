# it is called asyncio sincve any i/o operations are s-l-o-w
# but we can use it for ANY long-tail operation (not just i/o)
import asyncio # this is useful since Python 3.8
import timeit # a more accurate tool for timing

# old way (we tend not to use this any more)
# @asyncio.coroutine
# def fn():
#     '''this used to be the way to use asyncio'''
#     print('I am an asynchronous co-routine')

# new way (looks cleaner and runs better)
async def count():
    '''when we make something async we can then use 'await' to call it'''
    print('starting to wait')
    # use await to call something that is asynchronous
    await asyncio.sleep(2.5) # NB using sleep in asyncio is thread safe
    print('finished waiting')

async def countB():
    print('starting to wait longer')
    # use await to call something that is asynchronous
    await asyncio.sleep(3.5) # NB using sleep in asyncio is thread safe
    print('finished waiting longer')

async def main():
    '''call our async function (which is a co-routine)'''
    await asyncio.gather( count(), countB(), count() )

if __name__ == '__main__':
    '''we can call run on an async function'''
    asyncio.run( main() ) # run our asynchrous code
    # the main thread is still available
    print('This is on the main thread')