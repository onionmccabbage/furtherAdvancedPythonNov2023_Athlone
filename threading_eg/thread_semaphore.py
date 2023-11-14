import random
import time
import threading

# a global asset
ticketsAvailable = 100

class TicketSeller(threading.Thread):
    '''use a semaphore for concurrent accessto an asset (tickets)'''
    ticketsSold = 0
    def __init__(self, sem): # pass in the semaphore object
        threading.Thread.__init__(self)
        self.__sem = sem
    def run(self):
        global ticketsAvailable
        running = True
        while running: # this is a run loop
            self.__sem.acquire()
            self.randomDelay() # emulate some time-dependant situation
            if ticketsAvailable <=0:
                running = False # stop the run loop
            else:
                self.ticketsSold += 1
                ticketsAvailable -= 1
            self.__sem.release()
        print(f'Ticket seller {self.getName()} sold {self.ticketsSold}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/16) # 0, 0.25, 0.5 ...

def main():
    '''use a semaphore to permit concurrent access to ticket sales'''
    sem = threading.Semaphore(8) # choose how many concurrent ticket sellers 
    sellers_l = []
    for _ in range(0, 8): # no point having more tickets sellers than the semapore permits
        seller = TicketSeller(sem)
        sellers_l.append(seller)
        seller.start()
    # once all the threads are started we should join them
    for s in sellers_l:
        s.join()



if __name__ == '__main__':
    main()

    
