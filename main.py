"""
This is the main sctipt for the Stock-Analyzer
"""
from load_data import DataLoader

def main():
    print("Hello fellow stock enthusiast!")
    data = DataLoader()
    msft = data.load_data(ticker='MSFT', start='2021-1-1')
    print(msft)


if __name__ == "__main__":
    main()