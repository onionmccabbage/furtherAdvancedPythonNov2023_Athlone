import threading

# here is a global asset
counter = 0 # this could be a file i/o, a DB, an API ...
lock = threading.Lock() # an instance of a lock factory

def workerA():
    '''This function will increment the counter'''
    global counter
    lock.acquire() # get unique access to the lock
    # when accessing a shared asset it is good practice to handle exceptions
    try:
        while counter <10:
            counter+=1
            print(f'Worker A increments the counter to {counter}')
    except Exception as e:
        print(f'something went wrong {e}')
    finally:
        lock.release()

def workerB():
    '''This function will decrement the counter'''
    global counter
    lock.acquire() # get unique access to the lock
    try:
        while counter >-10:
            counter-=1
            print(f'Worker B decrements the counter to {counter}')
    except Exception as e:
        print(f'something went wrong {e}')
    finally:
        lock.release()

def main():
    '''use our workers'''
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t1.start() # whichever thread starts first gets the lock first
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()