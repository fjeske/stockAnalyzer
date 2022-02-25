"""This code loads the tickers from the s&p 500 index"""

import pandas as pd
from load_data import DataLoader
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

import pandas_datareader as pdr

def load_sp500_ticker():
    sp_500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    sp_500_tickers = sp_500_tickers[0]

    # df = sp_500_tickers[['Symbol', 'GICS Sector']]

    return sp_500_tickers['Symbol'].values.tolist()

#print(tickers)

def get_sectors(data):
    pass


#print(df['GICS Sector'].unique())

# financial_stocks = df[(df['GICS Sector'] == 'Financials')]

# ticker = financial_stocks['Symbol'].iloc[0]

# data = DataLoader()

# data.load_data(ticker=ticker, start='2021-1-1')

# data.get_data()

# data.print_stock_info()

# stock_data = pdr.get_data_fred(ticker)

# print(stock_data)

fname = 'EUNL_holdings.csv'
msci_world = pd.read_csv(fname, header=2, decimal=',')

msci_world_stocks = msci_world[(msci_world['Anlageklasse'] == 'Aktien')]

# print(msci_world_stocks.columns)

msci_world_stocks['Gewichtung (%) kummuliert'] = msci_world_stocks['Gewichtung (%)'].cumsum()

clean_df = msci_world_stocks[['Emittententicker', 'Name', 'Sektor', 'Marktwert', 'Gewichtung (%)', 'Gewichtung (%) kummuliert', 'Nominalwert']]

# print(clean_df['Sektor'].unique())

it_stocks = clean_df[(clean_df['Sektor'] == 'Immobilien')][:7]
print(it_stocks)

sector_weights = {}
sector_allocation = {}

top_n = 10

n_stocks = clean_df.shape[0]

# print(n_stocks)

for sector in clean_df['Sektor'].unique():
    sector_stocks = clean_df[(clean_df['Sektor'] == sector)]
    sector_weight = sector_stocks['Gewichtung (%)'].sum()

    # calculates the weight of the stocks from the sector in the index
    n_of_stocks_in_sector = clean_df[(clean_df['Sektor'] == sector)].shape[0]
    sector_prct = n_of_stocks_in_sector / n_stocks
    sector_allocation[sector] = sector_prct

    sector_weights[sector] = sector_weight

# print(sector_allocation)

# calculates number of stocks to buy from a certain sector
n_stocks_to_buy = 100
sector_list = list(sector_allocation.keys())
np_sector_allocation = np.fromiter(sector_allocation.values(), dtype=float)

print(sector_list)
print(np.ceil(np_sector_allocation * 100))

# plt.plot(clean_df.index, clean_df['Gewichtung (%) kummuliert'])

# plt.show()

# print(clean_df[(clean_df['Gewichtung (%) kummuliert'] <= 50.0)])