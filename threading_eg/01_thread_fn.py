# normal Python will always run on a single thread known as the main thread
from threading import Thread
import random
import time

def myFn(n):
    '''this is a normal function. Like all functions it can be invoked as a new thread'''
    for _ in range(0, 10): # on average this loop will take about 0.5 sec
        print(f'{n} is sleeping')
        # emulate a long-running series of code steps
        time.sleep(random.random()*0.1) # sleep for up to 1/10 sec

def main():
    '''invoke our function on a thread'''
    # NB Thread is a thread-access object (not a thread itself)
    t1 = Thread(target=myFn, args=(1,)) # careful - a one-member tuple needs a comma
    t2 = Thread(target=myFn, args=(2,)) # careful - a one-member tuple needs a comma
    t3 = Thread(target=myFn, args=(3,)) # careful - a one-member tuple needs a comma
    # we need to start the new threads
    t1.start()
    t2.start()
    t3.start()
    # remember - the main thread is also running
    # we are not obliged to use 'join' but we usually do
    # The main thread becomes trivial - all the important stuff happens on other threads
    t1.join() # the main thread will pause until the other thread (re)joins
    t2.join() # remember the main thread is now blocked until the other thread (re)joins
    t3.join()

if __name__ == '__main__':
    start = time.time()
    main()
    # myFn(1) # on the main thread
    # myFn(2)
    # myFn(3)
    end = time.time()
    print(f'Total time {end-start}') # about 0.5 sec