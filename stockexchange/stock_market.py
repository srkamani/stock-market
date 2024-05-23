from math import prod

from stockexchange.stock import Stock
from stockexchange.stock_market_validation import validate_price, validate_quantity, validate_buy_sell_indicator


class StockMarket:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, stock_type, last_dividend, fixed_dividend=None, par_value=None):
        # no validation for now, as this is used for initial data set up
        self.stocks[symbol] = Stock(stock_type, last_dividend, fixed_dividend, par_value)

    def dividend_yield(self, symbol, price):
        self.validate_symbol(symbol)
        validate_price(price)
        return self.stocks[symbol].dividend_yield(price)

    def pe_ratio(self, symbol, price):
        self.validate_symbol(symbol)
        return self.stocks[symbol].pe_ratio(price)

    def record_trade(self, symbol, quantity, buy_sell_indicator, traded_price):
        self.validate_trade_data(symbol, quantity, buy_sell_indicator, traded_price)
        self.stocks[symbol].record_trade(quantity, buy_sell_indicator, traded_price)

    def volume_weighted_stock_price(self, symbol):
        self.validate_symbol(symbol)
        return self.stocks[symbol].volume_weighted_stock_price()

    def geometric_mean(self):
        prices = []
        for stock in self.stocks.values():
            vws_price = stock.volume_weighted_stock_price()
            if vws_price:
                prices.append(vws_price)
        return prod(prices) ** (1 / len(prices)) if prices else None

    def geometric_mean_all_trades(self):
        prices = []
        for stock in self.stocks.values():
            price = stock.stock_price()
            if price:
                prices.append(price)
        return prod(prices) ** (1 / len(prices)) if prices else None

    def validate_symbol(self, symbol):
        if symbol not in self.stocks.keys():
            raise ValueError(f"Stock with symbol '{symbol}' does not exist")

    def validate_trade_data(self, symbol, quantity, buy_sell_indicator, traded_price):
        self.validate_symbol(symbol)
        validate_quantity(quantity)
        validate_price(traded_price)
        validate_buy_sell_indicator(buy_sell_indicator)

    def print_trades(self):
        for symbol, stock in self.stocks.items():
            print(symbol, stock.trades)

    def print_stocks(self):
        for symbol, stock in self.stocks.items():
            print(symbol, str(stock))
