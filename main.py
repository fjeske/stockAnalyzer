"""
This is the main sctipt for the Stock-Analyzer
"""
from load_data import StockData
import numpy as np
import json
import datetime as dt

def main():
    print("Hello fellow stock enthusiast!")
    stock_data = StockData(src_filename='./data/EUNL_holdings.csv')

    print(f"Anzahl der Sektoren: {len(stock_data.sectors)}")

    # stock_data.pick_rand_stock_for_sector()

    stock_data.pick_top_k_stock_for_sector(k=5)

    # save data in a dict
    stock_list = {}

    # print the entire portfolio based on equal diversifaction across all sectors
    for sector in stock_data.portfolio.keys():
        #print(f"Sektor: {sector}")
        stock_list[sector] = stock_data.portfolio[sector]
        #print(stock_data.portfolio[sector])
    #print(stock_list)

    # save data in json file
    date = str(dt.datetime.today()).split()[0].replace('-', '_')
    with open(date + '.json', 'w') as fp:
        json.dump(stock_list, fp)

    # print stock data
    # tickers = stock_data.stock_data['Emittententicker'][:50]
    # print(tickers)


if __name__ == "__main__":
    main()
