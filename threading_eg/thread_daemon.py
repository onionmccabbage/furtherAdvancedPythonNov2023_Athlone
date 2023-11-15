# a daemon thread runs endlessly
from threading import Thread
import time
import timeit

def standardThread():
    '''we will run this as a normal thread'''
    print('starting a standard thread')
    time.sleep(4)
    print('ending standard thread')

def daemonThread():
    '''we will run this function as a daemon thread'''
    print('starting a daemon thread')
    while True: # this loop will never end
        print('heartbeat')
        time.sleep(0.5)

def main():
    '''invoke our functions on threads'''
    s = Thread(target=standardThread)
    d = Thread(target=daemonThread, daemon=True) # this is how we make thread run as a daemon thread
    s.start()
    d.start() # this daemon thread will end when all the other threads are complete
    s.join() # as usual, it is good practice to let standard threads join the main thread
    # d.join() # Noooooooo!!!!!!!
    # we let all standard threads end, then our main thread ends, and the daemon thread must also end


if __name__ == '__main__':
    main()
