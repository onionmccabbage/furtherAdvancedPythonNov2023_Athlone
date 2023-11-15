from collections.abc import Callable, Iterable, Mapping
from threading import Thread
import random
import time
import timeit
from typing import Any

class MyThread(Thread):
    '''this class inherits from Thread'''
    def __init__(self, n):
        Thread.__init__(self) # we invoke the __init__ of Thread
        self.n = n
    def run(self):
        '''override the run method of Thread'''
        for _ in range(10):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1)


def main():
    ''' invoke the class Threads'''
    thread_l = []
    # how many threads...
    for _ in range(64):
        thread_l.append( MyThread(_) )
    # we can start all the threads
    for t in thread_l:
        t.start()
    # we must start the threads before we use join
    for t in thread_l:
        t.join()

if __name__ == '__main__':
    # start = time.time()
    # timeit is more accurate than time.time
    # timeit makes a good effort to ignore non-python time
    start = timeit.default_timer()
    main()
    # end = time.time()
    end = timeit.default_timer()
    print(f'Total time {end-start}')