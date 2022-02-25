"""
This is the main sctipt for the Stock-Analyzer
"""
from load_data import StockData
import numpy as np

def main():
    print("Hello fellow stock enthusiast!")
    stock_data = StockData(src_filename='EUNL_holdings.csv')

    stock_data.load_data()

    stock_data.load_sectors()

    print(f"Anzahl der Sektoren: {len(stock_data.sectors)}")

    # stock_data.pick_rand_stock_for_sector()

    stock_data.pick_top_k_stock_for_sector(k=5)

    # print the entire portfolio based on equal diversifaction across all sectors
    print(stock_data.portfolio)

if __name__ == "__main__":
    main()