import unittest
from stockexchange.stock_market import StockMarket
from stockexchange.stock import StockType


class TestStockMarket(unittest.TestCase):
    def setUp(self):
        self.stock_market = StockMarket()

    def test_add_stock(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        self.assertIn('TEA', self.stock_market.stocks)

    def test_dividend_yield(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        print(self.stock_market.dividend_yield('TEA', 100))
        self.assertIsNotNone(self.stock_market.dividend_yield('TEA', 100))

    def test_dividend_yield_invalid_symbol(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        with self.assertRaises(ValueError) as context:
            self.stock_market.dividend_yield('TEA-INVALID', 100)
        self.assertEqual(str(context.exception), "Stock with symbol 'TEA-INVALID' does not exist")

    def test_pe_ratio(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        self.assertIsNone(self.stock_market.pe_ratio('TEA', 100))

    def test_record_trade(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        self.stock_market.record_trade('TEA', 10, 'BUY', 100)
        self.assertEqual(len(self.stock_market.stocks['TEA'].trades), 1)

    def test_volume_weighted_stock_price(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        self.stock_market.record_trade('TEA', 10, 'BUY', 100)
        self.assertIsNotNone(self.stock_market.volume_weighted_stock_price('TEA'))

    def test_geometric_mean_all_trades(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        self.stock_market.record_trade('TEA', 10, 'BUY', 100)
        self.assertEqual(self.stock_market.geometric_mean_all_trades(),100)

    def test_validate_symbol(self):
        with self.assertRaises(ValueError):
            self.stock_market.validate_symbol('INVALID')

    def test_validate_trade_data_qty(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        with self.assertRaises(ValueError) as context:
            self.stock_market.validate_trade_data('TEA', -10, 'buy', 100)
        self.assertEqual(str(context.exception), "Invalid quantity. Please enter a valid positive number.")

    def test_validate_trade_data_indicator(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        with self.assertRaises(ValueError) as context:
            self.stock_market.validate_trade_data('TEA', 110, 'INVALID', 100)
        self.assertEqual(str(context.exception), "Invalid buy/sell indicator. Please enter 'buy' or 'sell'.")

    def test_validate_trade_data_price(self):
        self.stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100)
        with self.assertRaises(ValueError) as context:
            self.stock_market.validate_trade_data('TEA', 110, 'buy', -100)
        self.assertEqual(str(context.exception), "Invalid Price. Please enter a valid positive number.")


if __name__ == '__main__':
    unittest.main()
