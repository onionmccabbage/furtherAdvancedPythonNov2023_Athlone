# functional programming uses functions instead of classes
def isEven(n):
    '''True if even, False if not'''
    return n%2 == 0

def addThem(m, n):
    return m+n

def main():
    '''use map and filter to apply our funtions'''
    r = map(isEven, range(-10, 11))
    print(r)
    print(r.__next__()) # True
    print(r.__next__()) # False
    print(r.__next__()) # True
    print(next(r)) # False (alternative syntax for next)
    # we can iterate over a map object
    for _ in r: # carry on from where the map object left off
        print(f'Even:{_}', end=', ')
    # print(r.__next__()) # stop iteration is raised
    # using filter
    matching = filter(isEven, range(-10, 11))
    print(matching)
    print(matching.__next__()) # -10
    print(matching.__next__()) # -8
    # for _ in matching:
    #     print(f'{_}', end=', ' )
    while True: # be careful with endless loops
        try:
            print(matching.__next__())
        except StopIteration as s: # it is common to handle stop iteration
            pass
            break
        finally:
            pass

if __name__ == '__main__':
    main()