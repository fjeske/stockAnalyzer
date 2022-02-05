"""This code loads the tickers from the s&p 500 index"""

import pandas as pd

sp_500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

sp_500_tickers = sp_500_tickers[0]

df = sp_500_tickers[['Symbol', 'GICS Sector']]

tickers = sp_500_tickers['Symbol'].values.tolist()

#print(tickers)

def get_sectors(data):
    pass


print(df['GICS Sector'].unique())

financial_stocks = df[(df['GICS Sector'] == 'Financials')]

#print(financial_stocks)