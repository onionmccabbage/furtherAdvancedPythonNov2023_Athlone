from order import Order
from stock_trade import StockTrade

class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if type(new_stock)==StockTrade:
            self.__stock = new_stock
        else:
            raise TypeError('Missing required stock')
    def execute(self):
        return self.stock.sell()
    
if __name__ == '__main__':
    s = StockTrade()
    bs = SellStock(s)
    bs.execute() # we execute the command