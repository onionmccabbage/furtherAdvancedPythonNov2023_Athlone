# the Fibonacci sequence is a classic mathematical problem
import timeit
# profile is useful to see what our function is using (time, memory)
from memory_profiler import profile

# Python includes a profiler tool called cProfile
# use it like this:
# python -m cProfile -o profile_output fib.py
# this will generate a non-text file called profile_output
# We then write further Python code to read that file

def fib(n):
    '''calculate the fibonacci number from n'''
    # 1, 2, 3, 5, 8, 13, 21 ...
    if n<=1:
        return 1
    else:
        # apply fib recursively
        return ( fib(n-1) + (fib(n-2)) )
    
# @profile
def main():
    # n=40 # about 30 sec on my laptop
    n=16
    r = fib(n) # 34
    print(f'Fibonacci up to {n} is {r}')

if __name__ == '__main__':
    start = timeit.default_timer()
    main() # this will call the progile decorator
    end = timeit.default_timer()
    print(f'Total time {end-start}')
