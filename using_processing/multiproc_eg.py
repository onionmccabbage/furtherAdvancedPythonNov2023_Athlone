import multiprocessing
import os # a reference to the the operating system

def whichProc():
    '''show whic process ID this function is running within'''
    print(f'Method is running on process ID {os.getpid()}')

if __name__ == '__main__':
    # NB the Process object is a process accessor (not an actual process)
    proc_l = []
    num_processors = os.cpu_count()
    # We can run more processes than the number of cpu cores!!!
    for n in range(num_processors*100):
        p = multiprocessing.Process(target=whichProc) # just like we do in Threading
        proc_l.append(p)
        p.start()
    for _ in proc_l:
        _.join() # good practice
    print(f'Main thread is running on {os.getpid()}')
    whichProc() # using the same process ID as the main thread