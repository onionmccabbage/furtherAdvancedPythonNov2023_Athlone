# the command pattern lets us queue up commands and make sure they are implemented in order
from stock_trade import StockTrade
from agent import Agent
from buy_stock import BuyStock
from sell_stock import SellStock

def main(): # this is conventional
    '''call the other classes and issue commands'''
    stock = StockTrade()
    buy   = BuyStock(stock)
    sell  = SellStock(stock)
    agent = Agent()
    # invoke commands
    agent.place_order(buy)
    agent.place_order(sell)
    agent.place_order(buy)
    agent.place_order(buy)
    agent.place_order(buy)
    agent.place_order(sell)
    agent.place_order(buy)
    agent.place_order(buy)
    agent.place_order(sell)
    agent.place_order(sell)
    agent.place_order(sell)

if __name__ == '__main__':
    main()