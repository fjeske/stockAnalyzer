"""This code loads the tickers from the s&p 500 index"""

import pandas as pd
from load_data import DataLoader
import yfinance as yf
import matplotlib.pyplot as plt

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

# it_stocks = clean_df[(clean_df['Sektor'] == 'IT')]
# print(it_stocks['Gewichtung (%)'].sum())

sector_weights = {}

for sector in clean_df['Sektor'].unique():
    sector_stocks = clean_df[(clean_df['Sektor'] == sector)]
    sector_weight = sector_stocks['Gewichtung (%)'].sum()

    sector_weights[sector] = sector_weight

print(sector_weights)

# plt.plot(clean_df.index, clean_df['Gewichtung (%) kummuliert'])

# plt.show()

# print(clean_df[(clean_df['Gewichtung (%) kummuliert'] <= 50.0)])