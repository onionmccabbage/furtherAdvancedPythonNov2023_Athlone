# Abstract Base Class (ABC)
from abc import ABCMeta, abstractmethod

# we can declare an abstract class (one that we will never imlement)
class Planar(metaclass=ABCMeta):
    '''An abstract class for planar spacial points'''
    __slots__ = ('__x', '__y', '__z') # we only permit these properties
    def __init__(self):
        pass
    @abstractmethod # a method we insist must be implemented in any concrete class
    def hypot(self):
        '''Derive the hypotenuse from the x and y values'''

# in Abstracvt classes we merely defien the structure with NO implwementation