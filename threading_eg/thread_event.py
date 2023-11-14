from threading import Thread, Event
import time

event = Event() # we can use events to sommunicate to events

class MyClass:
    def __call__(self,n):
        global event
        print(f'{n} is waiting for event...')
        event.wait() # this thread will pause until the event is received
        print(f'{n} is continuing after the event')

if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    t1 = Thread(target=m1, args=('A',))
    t2 = Thread(target=m2, args=('B',))
    t1.start()
    t2.start()
    # wait on the main thread
    time.sleep(4)
    event.set() # trigger the eent to happen
    t1.join()
    t2.join()