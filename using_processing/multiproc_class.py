import multiprocessing
from multiprocessing import Process
import os

class MyProc(Process):
    '''Inherit from Process'''
    def __init__(self):
        super(MyProc, self).__init__()
    def run(self):
        '''override the built in run method'''
        print(f'''Child process ID is {os.getpid()} aka {multiprocessing.current_process().pid} 
              parent is {multiprocessing.parent_process().pid}''')

def main():
    '''start a few processes'''
    proc_l = []
    for p in range(os.cpu_count()):
        proc = MyProc()
        proc_l.append(proc)
        proc.start()
    for _ in proc_l:
        _.join()

if __name__ == '__main__':
    main()
    print(f'Main process is {os.getpid()}')