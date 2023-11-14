from collections.abc import Callable, Iterable, Mapping
from threading import Thread
import random
import time
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
    start = time.time()
    main()
    end = time.time()
    print(f'Total time {end-start}')