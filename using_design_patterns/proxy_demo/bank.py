from payment import Payment
import random # this bank will randomly permit or deny payment

class Bank(Payment):
    '''This is a bank for making payments'''
    def __init__(self):
        self.card = None
        self.account = None
    def setCard(self, card):
        self.card = card # we could use __init__
    def __getAccount(self):
        self.account = self.card
        return self.account
    def __hasFunds(self):
        print(f'Bank is checking if {self.__getAccount()} has funds')
        return bool(random.getrandbits(1)) # True or False
    def doPay(self):
        if self.__hasFunds():
            print('bank is paying')
            return True
        else:
            print('Insufficient funds')
            return False
        
if __name__ == '__main__':
    b = Bank()
    r = b.doPay()
    print(r)