# We can write a decorator to be used when we need to lock ANY method

from threading import Lock

lock = Lock() # a globally available lock factory

def lockMethod(meth):
    '''This function can be used to decorate any other function or method to make it thread safe'''
    def lockedMethod(self, *args, **kwargs):
        lock.acquire() # get exclusive use of the global lock
        result = meth(self, *args, **kwargs)
        lock.release()
        return result
    lockMethod.__name__ = f'locked_{meth.__name__}'
    lockedMethod.__is_locked = True # a marker to indicate the method is locked
    return lockedMethod

class MySet(set): # this class inherits from 'set'
    '''this class extends the 'set' object. 'set' has 'add' and 'remove' '''
    def __init__(self, new_set):
        set.__init__(self, new_set) # just make a normal set
    # here is a method we may wish to lock
    def myMethod(self, new_value):
        '''check that the new value is an integer'''
        if type(new_value) == int:
            self.add(new_value) # cal the add method of 'set'
        else:
            pass # we could use a default or raise an exception

def main():
    ms = MySet({3,2,5,5,7,3,8,4,-34,-6,0,2})
    ms.myMethod(-3) # all good
    ms.myMethod('oops') # fails silently
    print(ms) # does not include 'oops'

if __name__ == '__main__':
    main()
    