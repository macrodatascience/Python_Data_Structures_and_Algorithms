import unittest
from beverage import Beverage

class TestBeverageExchange(unittest.TestCase):

    def test_check_ticker(self):
        beverage = Beverage()
        self.assertEqual(beverage.check_ticker('joe'), 'JOE')  # add assertion here
        self.assertEqual(beverage.check_ticker('TEA'), 'TEA')
        self.assertEqual(beverage.check_ticker('POP'), 'POP')
        self.assertEqual(beverage.check_ticker('Ale'), 'ALE')
        self.assertEqual(beverage.check_ticker('Gin'), 'GIN')

    def test_calculate_dividend_yield(self):
        beverage = Beverage()
        self.assertEqual(beverage.calculate_dividend_yield('JOE', 100), 0.13)  # add assertion here
        self.assertEqual(beverage.calculate_dividend_yield('TEA', 200), 0)
        self.assertEqual(beverage.calculate_dividend_yield('POP', 100), 0.08)
        self.assertEqual(beverage.calculate_dividend_yield('ALE', 100), 0.23)
        self.assertEqual(beverage.calculate_dividend_yield('GIN', 100), 0.02)

    def test_calculate_pe_ratio(self):
        beverage = Beverage()
        self.assertEqual(beverage.calculate_pe_ratio('JOE', 130), 10)  # add assertion here
        self.assertEqual(beverage.calculate_pe_ratio('TEA', 200), 'inf')
        self.assertEqual(beverage.calculate_pe_ratio('POP', 100), 12.5)
        self.assertEqual(beverage.calculate_pe_ratio('ALE', 115), 5)
        self.assertEqual(beverage.calculate_pe_ratio('GIN', 120), 15)

    def test_record_trade_and_volume_weighted_price_and_gbse_index(self):
        beverage = Beverage()
        self.assertIsNotNone(beverage.record_trade('JOE', 100, 'buy', 40))  # add assertion here
        self.assertEqual(beverage.calculate_volume_weighted_price('JOE', 5), 40)
        self.assertAlmostEqual(beverage.calculate_gbse_index(), 40)

        self.assertIsNotNone(beverage.record_trade('TEA', 200, 'buy', 50))
        self.assertEqual(beverage.calculate_volume_weighted_price('TEA', 5), 50)
        self.assertAlmostEqual(beverage.calculate_gbse_index(), 50)

        self.assertIsNotNone(beverage.record_trade('POP', 300, 'buy', 55))
        self.assertEqual(beverage.calculate_volume_weighted_price('POP', 5), 55)
        self.assertAlmostEqual(beverage.calculate_gbse_index(), 55)

        self.assertIsNotNone(beverage.record_trade('ALE', 150, 'buy', 45))
        self.assertEqual(beverage.calculate_volume_weighted_price('ALE', 5), 45)
        self.assertAlmostEqual(beverage.calculate_gbse_index(), 45)

        self.assertIsNotNone(beverage.record_trade('GIN', 120, 'buy', 75))
        self.assertEqual(beverage.calculate_volume_weighted_price('GIN', 5), 75)
        self.assertAlmostEqual(beverage.calculate_gbse_index(), 75)


if __name__ == '__main__':
    unittest.main()
