"""
This class saves all data for a certain stock with a ticker symbol
"""
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
from dateutil.relativedelta import relativedelta

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_stock_price_data(self):
        """ this method saves the stock price data for 1 year"""
        start_date = dt.datetime.now().date()
        end_date = start_date - relativedelta(years=1)

        data = yf.Ticker(self.ticker)

        self.data = data.history(period="1y")

    def calaculate_1y_ath(self):
        max_value = self.data['Close'].idxmax().date()
        value = self.data['Close'].loc[[max_value]][0]
        self.ath_value = value

    def is_10_prct_below_ath(self):
        pass

    def get_prct_from_ath(self):
        current_value = self.data.iloc[-1]['Close']
        prct_diff = np.round((1 - (current_value / self.ath_value)) * 100)
        print(prct_diff)

def main():
    # aapl = Stock(ticker='AAPL')

    # aapl.get_stock_price_data()

    # aapl.calaculate_1y_ath()

    # aapl.get_prct_from_ath()

    tsla = Stock(ticker='FB')

    tsla.get_stock_price_data()

    tsla.calaculate_1y_ath()

    tsla.get_prct_from_ath()


if __name__ == "__main__":
    main()