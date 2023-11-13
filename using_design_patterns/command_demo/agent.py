from buy_stock import BuyStock
from order import Order
from stock_trade import StockTrade

class Agent:
    '''the agent can isue commands'''
    def __init__(self):
        self.__order_queue = []
    def place_order(self, order):
        self.__order_queue.append(order)
        # the queue might be asynchronous and include latency
        order.execute()

if __name__ == '__main__':
    a = Agent()
    s = StockTrade()
    b = BuyStock(s)
    a.place_order(b)
