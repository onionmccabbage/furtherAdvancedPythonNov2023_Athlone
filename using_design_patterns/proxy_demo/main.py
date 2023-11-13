# main is a common pattern in Python. It is a facade to the other modules
from customer import Customer

def main():
    '''bring together the bank and customer'''
    cus = Customer()
    cus.makePayment()

if __name__ == '__main__':
    for user in range(10):
        main()