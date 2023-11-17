from contextlib import contextmanager
import sys

@contextmanager # just use the bilt-in context manager decorator
def redirect(new_stream):
    old_st = sys.stdout
    sys.stdout = new_stream # we sould validate
    yield # our function will yield the next available context to be written
    sys.stdout = old_st # put things back how they were

def main():
    print('using normal context')
    with open('my_log.txt', 'at') as fobj: # the with operator will close the file object when done
        with redirect(fobj):
            print('redirected output')
        print('back to normal')

if __name__ == '__main__':
    main()