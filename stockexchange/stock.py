from enum import Enum
from datetime import datetime, timedelta


class StockType(Enum):
    COMMON = 1
    PREFERRED = 2


class Stock:
    def __init__(self, stock_type, last_dividend, fixed_dividend=None, par_value=None):
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades = []

    def dividend_yield(self, price):
        if self.stock_type == StockType.COMMON:
            return self.last_dividend / price if price != 0 else None
        elif self.stock_type == StockType.PREFERRED:
            return (self.fixed_dividend / 100) * self.par_value / price if price != 0 else None

    def pe_ratio(self, price):
        dividend_yield = self.dividend_yield(price)
        return price / dividend_yield if dividend_yield else None

    def record_trade(self, quantity, buy_sell_indicator, traded_price):
        self.trades.append((datetime.now(), quantity, buy_sell_indicator, traded_price))

    def volume_weighted_stock_price(self):
        now = datetime.now()
        fifteen_minutes_ago = now - timedelta(minutes=15)
        relevant_trades = [trade for trade in self.trades if trade[0] >= fifteen_minutes_ago]
        if not relevant_trades:
            return None
        total_value = sum(quantity * traded_price for _, quantity, _, traded_price in relevant_trades)
        total_quantity = sum(quantity for _, quantity, _, _ in relevant_trades)
        return total_value / total_quantity

    def stock_price(self):
        total_value = sum(quantity * traded_price  for _, quantity, _, traded_price in self.trades)
        total_quantity = sum(quantity for _, quantity, _, _ in self.trades)
        return total_value / total_quantity if total_quantity > 0 else None

    def __str__(self):
        return f"Stock(stock_type={self.stock_type}, last_dividend={self.last_dividend}, " \
               f"fixed_dividend={self.fixed_dividend}, par_value={self.par_value})"

