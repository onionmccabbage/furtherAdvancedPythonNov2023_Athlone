def validString(f):
    def newFunc(*args, **kwargs):
        for arg in args:
            if type(arg)== str and arg != '':
                pass
            else:
                err_msg =  f'The positional argument {arg} needs to be a non-empty string'
                raise TypeError(err_msg)
        return f(*args, **kwargs) # call the original function
    return newFunc # we do not call this function, just return it

def ooblywoobly(f):
    return f

@ooblywoobly # yes we can use more than one decorator - BUT be careful
@validString
def toUpper(s):
    return s.upper()

if __name__ == '__main__':
    t = 'hello'
    T = toUpper(t) # all fine
    q = 33.33
    Q = toUpper(q) # oh dear
