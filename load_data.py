"""Class for loading stock data"""
import yfinance as yf
from datetime import datetime
import pandas as pd
import numpy as np


class StockData:
    """
    
    """
    def __init__(self, src_filename):
        self.src_filename = src_filename
        self.portfolio = dict()
        self.stock_data = pd.read_csv(self.src_filename, header=2, decimal=',')
        self.stock_data = self.stock_data[(self.stock_data['Anlageklasse'] == 'Aktien')]
        self.sectors = self.stock_data['Sektor'].unique()

    def pick_rand_stock_for_sector(self):
        """picks random stock from the index"""
        for i, sector in enumerate(self.sectors):
            print(f"\nSektor: {sector}\n")
            stocks = self.stock_data[(self.stock_data['Sektor'] == sector)]
            rand_number = np.random.randint(0, len(stocks))
            print(f"Random index number: {rand_number}")
            print(f"Number of stocks in the sector: {len(stocks)}")

            print(stocks[['Name', 'Marktwert']].iloc[rand_number])

    def pick_top_k_stock_for_sector(self, k=1):
        """This method prints top k market cap weighted stocks per sector"""
        for sector in self.sectors:
            # print(f"\nSektor: {sector}\n")
            stocks = self.stock_data[(self.stock_data['Sektor'] == sector)][:k]

            # print(stocks[['Name', 'Marktwert']])
            
            # add the stocks from the sector to the portfolio
            self.portfolio[sector] = list(stocks['Name'].values)
            # self.portfolio.append(list(stocks['Name'].values))