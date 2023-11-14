from threading import Thread
import random
import time

class MyClass: # implicitly inherit from object
    '''override __call__ to make this class callable (e.g. from a Thread)'''
    def __call__(self, n):
        for _ in range(10):
            print(f'{n} is sleeping')
            time.sleep(random.random()*0.1)

def main():
    ''' invoke the class method'''
    c1 = MyClass()
    thread_l = []
    for _ in range(8):
        thread_l.append( Thread(target=c1, args=(_,)) )
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
