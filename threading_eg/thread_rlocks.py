# rlock is a re-entrant lock
# if we need to acquire and release a lock frequently us an rlock
import threading
import time
class MyWorker():
    '''Modify data using a re-entrant lock'''
    def __init__(self):
        self.a = 1
        self.b = 2
        # subsequent acquisitions  of an RLock are not-blocking
        self.rlock = threading.RLock()
    def modifyA(self):
        with self.rlock:
            print(f'RLock acquired {self.rlock._is_owned()} to modify A')
            self.a += 1
            time.sleep(1)
    def modifyB(self):
        with self.rlock:
            print(f'RLock acquired {self.rlock._is_owned()} to modify B')
            self.b -= 1
            time.sleep(1)
    def modifyBoth(self):
        self.modifyA()
        self.modifyB()

def main():
    '''use the class'''
    w = MyWorker()
    w.modifyA()
    w.modifyB()
    w.modifyBoth()

if __name__ == '__main__':
    main()
