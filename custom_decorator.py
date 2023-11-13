# we can write a function to decorate other functions
# A decorator adds functionality to an existing function

# a custom decorator
def showArgs(f): # this funtion will take another function as it's argument
    '''this function can be used ot decorate any other function
    It will reveal the positional arguments and keyword arguments of the decorated function'''
    def newFunc(*args, **kwargs): # by convention args kwargs
        msg = f'Running a function called {f.__name__}\n' # terminate with a new line character
        msg += f'The positional arguments are {args}\n' # the positional args always in a tuple
        msg += f'The keyword arguments are {kwargs}\n' # the keyword args always in a dict
        print(msg)
        # we need to return a call to the original function
        return f(*args, **kwargs)
    return newFunc #we do not invoke it here

@showArgs
def isOdd(n):
    '''return True if Odd, False if not'''
    return n%2 !=0 # n%2 is modulo arithmetic - return the remainder of division

# we can apply our custom decorator to any function
@showArgs
def squares(m,n):
    '''return the squares of integers from n to m'''
    s = []
    for i in range(m, n):
        s.append(i*i)
    return s

if __name__ == '__main__':
    for i in range(0, 15):
        print(  isOdd(i) , end=', ' )
    
    print( squares(m=-10,n=11)) # Call with keyword arguments
    print( squares(-10, 11))    # Call with positional argument
    print( squares(-10, n=11))  # Call with both types of argument
