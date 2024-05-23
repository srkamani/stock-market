import unittest
from stockexchange.stock import Stock, StockType


class TestStock(unittest.TestCase):
    def setUp(self):
        self.common_stock = Stock(StockType.COMMON, 10)
        self.preferred_stock = Stock(StockType.PREFERRED, 20, fixed_dividend=2, par_value=100)

    def test_dividend_yield_common(self):
        self.assertEqual(self.common_stock.dividend_yield(100), 0.1)

    def test_dividend_yield_common_zero_price(self):
        self.assertIsNone(self.common_stock.dividend_yield(0))

    def test_dividend_yield_preferred(self):
        self.assertEqual(self.preferred_stock.dividend_yield(100), 0.02)

    def test_dividend_yield_preferred_zero_price(self):
        self.assertIsNone(self.preferred_stock.dividend_yield(0))

    def test_pe_ratio_common(self):
        self.assertEqual(self.common_stock.pe_ratio(100), 1000)

    def test_pe_ratio_common_zero_dividend(self):
        self.assertIsNone(self.common_stock.pe_ratio(0))

    def test_pe_ratio_preferred(self):
        self.assertEqual(self.preferred_stock.pe_ratio(100), 5000)

    def test_pe_ratio_preferred_zero_dividend(self):
        self.assertIsNone(self.preferred_stock.pe_ratio(0))

    def test_record_trade(self):
        self.common_stock.record_trade(10, 'BUY', 100)
        self.assertEqual(len(self.common_stock.trades), 1)

    def test_volume_weighted_stock_price(self):
        self.common_stock.record_trade(20, 'BUY', 100)
        self.common_stock.record_trade(20, 'BUY', 200)
        self.assertEqual(self.common_stock.volume_weighted_stock_price(), 150.0)

    def test_volume_weighted_stock_price_no_trades(self):
        self.assertIsNone(self.common_stock.volume_weighted_stock_price())

    def test_stock_price(self):
        self.common_stock.record_trade(10, 'BUY', 100)
        self.assertIsNotNone(self.common_stock.stock_price())

    def test_stock_price_no_trades(self):
        self.assertIsNone(self.common_stock.stock_price())


if __name__ == '__main__':
    unittest.main()
