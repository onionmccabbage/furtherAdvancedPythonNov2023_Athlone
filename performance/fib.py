# the Fibonacci sequence is a classic mathematical problem
import timeit

def fib(n):
    '''calculate the fibonacci number from n'''
    # 1, 2, 3, 5, 8, 13, 21 ...
    if n<=1:
        return 1
    else:
        # apply fib recursively
        return ( fib(n-1) + (fib(n-2)) )
    
def main():
    n=8
    r = fib(n) # 34
    print(f'Fibonacci up to {n} is {r}')

if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print(f'Total time {end-start}')
