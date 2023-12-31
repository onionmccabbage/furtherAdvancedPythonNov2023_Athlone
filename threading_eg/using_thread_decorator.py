# We can write a decorator to be used when we need to lock ANY method

from threading import Lock

lock = Lock() # a globally available lock factory

def lockMethod(meth):
    '''This function can be used to decorate any other function or method to make it thread safe'''
    def lockedMethod(self, *args, **kwargs):
        try:
            already_locked = meth.getattr('__is_locked') # True is locked
        except:
            # raise Exception('Method is already locked')
            # lock.acquire() # get exclusive use of the global lock
            # result = meth(self, *args, **kwargs)
            # lock.release()
            # return result
            with lock: # when 'with' ends, it will automatically release the lock
                return meth(self, *args, **kwargs)
    lockMethod.__name__ = f'locked_{meth.__name__}'
    lockedMethod.__is_locked = True # a marker to indicate the method is locked
    return lockedMethod

def make_thread_safe(cls, meth_l, lock):
    '''take a method list and apply locks to ach method in that list'''
    init = cls.__init__ # take a copy of the original __init__ method
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lock
    cls.__init__ = new_init # make our new init the __init__ of our class
    # iterate over each method in the method list and apply lock
    for meth in meth_l:
        old_meth = getattr(cls, meth)
        new_meth = lockMethod(old_meth)
        setattr(cls, meth, new_meth) # replace the orignal method with our locked version
    return cls

# in order to use as a decorator we need...
def lockClass(meth_list, lock):
    return lambda cls: make_thread_safe(cls, meth_list, lock)

# we will decorate this class to lock the 'add' method
@lockClass(['add', 'remove'], Lock) # both 'add' and 'remvoe' are now thread-safe
class MySet(set): # this class inherits from 'set'
    '''this class extends the 'set' object. 'set' has 'add' and 'remove' '''
    def __init__(self, new_set):
        set.__init__(self, new_set) # just make a normal set
    # here is a method we may wish to lock
    # @lockMethod
    def myMethod(self, new_value):
        '''check that the new value is an integer'''
        if type(new_value) == int:
            self.add(new_value) # cal the add method of 'set'
        else:
            pass # we could use a default or raise an exception

def main():
    ms = MySet({3,2,5,5,7,3,8,4,-34,-6,0,2})
    ms.myMethod(-3) # all good
    ms.add('fine') # this works, since 'add' allows any data type
    ms.myMethod('oops') # fails silently
    ms.remove(4) # all good
    print(ms) # does not include 'oops'
    # print(ms.myMethod.__is_locked) # True

if __name__ == '__main__':
    main()
    