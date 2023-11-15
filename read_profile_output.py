# this file will open a cProfile report and show the results
import pstats # may need to pip install

def main():
    '''open a cProfile report and show the results'''
    p = pstats.Stats('performance/profile_output')
    p.print_stats()

if __name__ == '__main__':
    main()