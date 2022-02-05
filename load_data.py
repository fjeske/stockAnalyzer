"""Class for loading stock data"""
import yfinance as yf
from datetime import datetime

class DataLoader:

    def __init__(self):
        self.today = datetime.today().strftime('%Y-%m-%d')

    def load_data(self, ticker, start, end=None, period='1d'):
        self.ticker = ticker
        self.start = start
        if end is None:
            self.end = datetime.today().strftime('%Y-%m-%d')
        elif end is not None:
            self.end = end
        self.period = period

    def get_data(self):
        self.stock = yf.Ticker(self.ticker)

    def print_stock_info(self):
        print(self.stock.info)