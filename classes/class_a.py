from class_abc import Planar

# In Python everything is an Object
# modern OOP tends to use classes
# Only use a class when nothing else will do
a = 3
b = 7.4
c = True
s = 'hello' # an ordinal immutable collection of characters
t = () # an ordinal immutable collection of any data type
l= [] # an ordinal mutable collection of any data type
d = {}
s = {a, b, c, s, t}

# maybe we need to represent a point in 2-d space
p_t = ('3',None) # x and y values
p_d = {'x':3, 'y':4}

# If we need to validate members of our structure, we might use a class

# we can choose to implicitly or explicitly inherit from object
class Point(Planar):
    '''A point in 2-d space'''
    __slots__ = ('__x','__y') # we can restrict the permitted mangled properties of this class
    def __init__(self, x, y):
        self.x = x # this will call the setter method for x
        self.y = y # the setter method for y
    @property # this decorator makes the function appear to be a property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        '''set the value of self.x'''
        if type(x) in (int, float):
            self.__x = x
        else:
            self.__x = 0 # set a sensible default
    @property
    def y(self):
        return self.__y # return the name-mangled value
    @y.setter
    def y(self, y):
        '''set the value of self.y'''
        if type(y) in (int, float):
            self.__y = y # here we 'mangle' the name of the property
        else:
            raise TypeError('value of y must be numeric') # we can raise an exception
    def hypot(self):
        '''we are obliged to implement hypot since it is in the abstract base class'''
        h = (self.x**2 + self.y**2)**0.5
        return h
    def __str__(self):
        '''we override the default __str__ method with our own for printing'''
        return f'Point at {self.x}, {self.y} with h:{self.hypot()}'

# 'dunder' is double-underscore. Often used to refer to the built-in properties and methods of Python
# __slots__, __init__, __str__ etc.
if __name__ == '__main__':
    p = Point(False,4)
    p.x = 3 # calls the setter method as if it was a property
    # p.y = None # Exception
    print( p.x ) # 0
    # print(f'The point at x:{p.x} y:{p.y} has a hypotenuse of {p.hypot()}') # 5.0
    print(p) # this will use our __str__ method
    # problem - all classes ultimately inherit from object, and objects permit ANY arbitrary property
    # p.oops = 'we can add any arbitrary property to any class'
    # print(p.oops)

