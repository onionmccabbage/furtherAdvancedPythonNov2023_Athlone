# the Fibonacci sequence is a classic mathematical problem
import timeit
# profile is useful to see what our function is using (time, memory)
from memory_profiler import profile
# for functional programming there are some handy tools
from functools import reduce

# Python includes a profiler tool called cProfile
# use it like this:
# python -m cProfile -o profile_output fib.py
# this will generate a non-text file called profile_output
# We then write further Python code to read that file

def fib(n): # this is probably the most inefficent way to do it
    '''calculate the fibonacci number from n'''
    # 1, 2, 3, 5, 8, 13, 21 ...
    if n<=1:
        return 1
    else:
        # apply fib recursively
        return ( fib(n-1) + (fib(n-2)) )
    
def fib_2(n):
    '''a more performant solution'''
    sequence = (0,1)
    for _ in range(2, n+2): # remember we need to return the sum of the last TWO members
        '''repeatedly add the last two values of the sequence'''
        # NB here we have a one-member tuple (so remember the trailing comma)
        sequence += (reduce( lambda a,b: a+b, sequence[-2:] ),) # works for a tuple
    # we must return
    return sequence[-1] # the last member

def fib_3(n): # on my laptop this is fastest
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b # this is classic stateful - destroy prev state replace with new state
    return a

# @profile
def main():
    # n=40 # about 30 sec on my laptop
    n=1024
    # r1 = fib_2(n) # Total time 0.0021428000000000003
    r2 = fib_3(n) # Total time 0.0006612000000000284
    print(f'Fibonacci up to {n} is {r2}')

if __name__ == '__main__':
    start = timeit.default_timer()
    main() # this will call the progile decorator
    end = timeit.default_timer()
    print(f'Total time {end-start}')
