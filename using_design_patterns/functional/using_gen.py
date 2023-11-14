# a generator never stores all its values in memory
# we can build a custom generator
def tally(incr=1, maxi=False):
    '''keep an endless tally'''
    score = 0
    while True:
        yield score # by using yield we have a generator
        score += incr
        if maxi != False and score > maxi:
            raise StopIteration # this is the correct way to stop a generator
            break

def main():
    '''use our generator'''
    game = tally()
    print(type(game)) # generator
    print(game.__next__()) # 0
    print(game.__next__()) # 1
    print(game.__next__()) # 2
    print(next(game)) # 3
    # re-use the generator
    game = tally(5)
    print(game.__next__()) # 0
    print(game.__next__()) # 5
    # use generator with maxima
    game = tally(3, 12)
    try:
        print(game.__next__()) # 0
        print(game.__next__()) # 3
        print(game.__next__()) # 6
        print(game.__next__()) # 9
        print(game.__next__()) # 12
        print(game.__next__()) # raises stop iteration
    except StopIteration as s:
        pass


if __name__ == '__main__':
    # we can build a generator like this
    even_g = (i for i in range(100) if i%2==0)
    print(even_g) # a generator
    main()