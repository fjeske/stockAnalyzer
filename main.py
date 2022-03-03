"""
This is the main sctipt for the Stock-Analyzer
"""
from load_data import StockData
import numpy as np

def main():
    print("Hello fellow stock enthusiast!")
    stock_data = StockData(src_filename='EXSA_holdings.csv')

    print(f"Anzahl der Sektoren: {len(stock_data.sectors)}")

    # stock_data.pick_rand_stock_for_sector()

    stock_data.pick_top_k_stock_for_sector(k=5)

    # print the entire portfolio based on equal diversifaction across all sectors
    for sector in stock_data.portfolio.keys():
        print(f"Sektor: {sector}")
        print(stock_data.portfolio[sector])

if __name__ == "__main__":
    main()