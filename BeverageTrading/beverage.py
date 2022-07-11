import datetime as dt
from scipy.stats.mstats import gmean

class Beverage:
    """
    reference_data is the dictionary with all the reference data pertaining to the Beverage Index Stocks
    trade_ledger is the dictionary used as an in-memory cache to store all the trade records
    """
    reference_data = {
        'TEA': {
            'Type': 'Common',
            'Last Dividend': 0,
            'Fixed Dividend': None,
            'Par Value': 100,
        },
        'POP': {
            'Type': 'Common',
            'Last Dividend': 8,
            'Fixed Dividend': None,
            'Par Value': 100,
        },
        'ALE': {
            'Type': 'Common',
            'Last Dividend': 23,
            'Fixed Dividend': None,
            'Par Value': 60,
        },
        'GIN': {
            'Type': 'Preferred',
            'Last Dividend': 8,
            'Fixed Dividend': 0.02,
            'Par Value': 100,
        },
        'JOE': {
            'Type': 'Common',
            'Last Dividend': 13,
            'Fixed Dividend': None,
            'Par Value': 250,
        },
    }

    def __init__(self):
        self.trade_ledger = dict()

    def check_ticker(self, ticker):
        """
        Validate whether the given ticker is in the reference data or not

        :param ticker:
        :return:
        """
        if ticker.upper() not in self.reference_data:
            return None
        return ticker.upper()

    def calculate_dividend_yield(self, ticker, price):
        """
        Compute and return the dividend yield for the given ticker at the given price

        :param ticker:
        :param price:
        :return:
        """
        ref_data = self.reference_data[ticker]
        if price == 0:
            return 'inf'
        if ref_data['Type']=='Common':
            return ref_data['Last Dividend'] / price
        return ref_data['Fixed Dividend'] * ref_data['Par Value'] / price

    def calculate_pe_ratio(self, ticker, price):
        """
        Compute and return the PE ratio for the given ticker at the given price

        :param ticker:
        :param price:
        :return:
        """
        ref_data = self.reference_data[ticker]
        if ref_data['Last Dividend'] == 0 or ref_data['Last Dividend'] is None:
            return 'inf'
        return price / ref_data['Last Dividend']


    def record_trade(self, ticker, quantity, direction, price):
        """
        Enter the trade as a record in the trade ledger

        :param ticker:
        :param quantity:
        :param direction:
        :return:
        """
        timestamp = dt.datetime.now().timestamp()
        self.trade_ledger[int(timestamp)] = {
            'ticker': ticker,
            'direction': direction,
            'quantity': quantity,
            'price': price
        }

        return 1

    def calculate_volume_weighted_price(self, ticker, mins_past=5):
        """

        :param ticker:
        :param mins_past: 5 minutes default given the requirements
        :return:
        """
        amount = 0
        total_quantity = 0
        timestamp_5mins_ago = int(dt.datetime.now().timestamp())-mins_past*60

        for timestamp in self.trade_ledger.keys():
            if timestamp >= timestamp_5mins_ago and self.trade_ledger[timestamp]['ticker']==ticker:
                amount += self.trade_ledger[timestamp]['quantity'] * self.trade_ledger[timestamp]['price']
                total_quantity += self.trade_ledger[timestamp]['quantity']

        if total_quantity:
            return amount/total_quantity
        return None

    def calculate_gbse_index(self):
        """
        Compute the index value based on geometric mean of the volume weighted stock price for all the stocks in the index

        :return:
        """
        vol_weighted_prices = []
        for ticker in self.reference_data:
            vwap = self.calculate_volume_weighted_price(ticker)
            if vwap:
                vol_weighted_prices.append(vwap)
        if len(vol_weighted_prices):
            return gmean(vol_weighted_prices)
        return None
