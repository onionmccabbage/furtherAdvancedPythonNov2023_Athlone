# positional and keyword arguments

def fnA(*args): # * will allow as many positional arguments as we like
    '''explore the positional arguments'''
    # we can emulate overloading (Python does not have overloading)
    if len(args)==0:
        print('zero-arg version of the function')
    if len(args)==1:
        print('one-arg version of the function')
    if len(args)==2:
        print('two-arg version of the function')
    return args # a tuple

def fnB(**kwargs):
    '''explore the keyword arguments'''
    return kwargs

if __name__ == '__main__':
    # some positional keywords
    t = fnA('param', 33.3)
    print(type(t), t)
    d = fnB(x=3, y=4, t=t)
    print(type(d), d)
    # we can iterate over the members of a dictionary
    for (k, v) in d.items():
        print(k, v)
