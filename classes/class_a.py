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
class Point:
    '''A point in 2-d space'''
    def __init__(self, x, y):
        if type(x) in (int, float):
            self.x = x
        else:
            self.x = 0 # set a sensible default
        if type(y) in (int, float):
            self.y = y
        else:
            raise TypeError('value of y must be numeric') # we can raise an exception

if __name__ == '__main__':
    p = Point(False,4)
    print( p.x ) # 0

