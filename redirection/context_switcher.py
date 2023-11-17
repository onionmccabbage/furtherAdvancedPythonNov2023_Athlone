# we may need to send output to a different context
# by default all printed oputput is send to a standard output stream 'stdout'
import sys

class Redirect:
    '''Redirect output to as different stream (a file)
    then set the output stream back to what it was'''
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout
    def __enter__(self):
        '''When this class begins it will run __enter__'''
        self.orig_stdout = sys.stdout # remember the current stdout
        sys.stdout = self.new_stdout # swap our new stdout
    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''When this class ends, it will run __exit__
        very fussy - we MUST provide exc_type, exc_value, exc_traceback'''
        sys.stdout = self.orig_stdout # put it back how it was

if __name__ == '__main__':
    print(sys.stdout)