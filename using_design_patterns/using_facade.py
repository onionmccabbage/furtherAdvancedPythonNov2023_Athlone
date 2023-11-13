# A facade brings together disparate entities via a single facade (usually in separate modules)
class Coder():
    '''write code to solve problems'''
    def __init__(self):
        print('write some code')
    def __is_available(self): # __ will mangle this method so it is only visible inside this class
        '''check coding skills are available'''
        print('Write some code')
    def bookTime(self):
        if self.__is_available():
            print('Coder has been booked')

class Tester():
    '''Test code to ensure diligence'''
    def __init__(self):
        print('Preparing some test')
    def testing(self):
        print('Tests are in place')

class Technician():
    '''Provide technical resources'''
    def __init__(self):
        print('Preparing equipment for the team')
    def doStuff(self):
        print('Network, machines, VMs all in place')

class Artisan():
    '''Design stuff'''
    def __init__(self):
        print('design things')
    def makePrototype(self):
        print('Wireframes are ready')

class Manager():
    '''This is a facade to the other classes'''
    def __init__(self):
        print('Managers says I can arrange the team')
    def arrange(self):
        '''the manager facade will provide instances of all the subsystems'''
        self.coder      = Coder()
        self.tester     = Tester()
        self.technician = Technician()
        self.artisan    = Artisan()
        # put the assets to work
        #we can easily add other assets here
        self.coder.bookTime()
        self.tester.testing()
        self.technician.doStuff()
        self.artisan.makePrototype()

class Client():
    '''Client needs resources to solve a problem'''
    def __init__(self):
        print('We need a team for our project')
    def askManager(self):
        print('Lets talk to the manager')
        self.manager = Manager() # here is an instance of the facade
        self.manager.arrange()
    def __del__(self):
        print('All done')

if __name__ == '__main__':
    '''a facade can make uggly stuff look easy'''
    customer = Client()
    customer.askManager()
