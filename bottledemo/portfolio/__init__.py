from bottle import template

class Coin:
    def __init__(self, coin_id, current, buy, quantity):
        self.coin_id = coin_id
        self.current = current
        self.buy = buy
        self.quantity = quantity

PORTFOLIO = [
    Coin("bitcoin", 23000, 20000, 0.5),
    Coin("ethereum", 1700, 1800, 10.0),
    Coin("solana", 40, 35, 100.0),
]
