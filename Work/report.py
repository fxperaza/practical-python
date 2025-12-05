# report.py
#
# Exercise 2.4
import csv
import os

def read_portfolio(filename):
    '''Reads portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            #holding = (row[0], int(row[1]), float(row[2]))
            holding = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    """
    Read file having lines containing 1) Stock Name 2) Stock Price and
    store the stock data in a dictionary
    """
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 0:
                continue
            prices[row[0]] = float(row[1])
    return prices

def evaluate_portfolio(portfolio, prices):
    unique_holdings = set()
    net = 0.0
    stocks = read_prices(prices)
    holdings = read_portfolio(portfolio)

    for holding in holdings:
        stock_name = holding['name']
        if stock_name not in unique_holdings:
            unique_holdings.add(stock_name)

        stock_initial_price = holding['price']
        stock_shares = holding['shares']
        if stock_name in stocks:
            stock_current_price = stocks[stock_name]
            delta = (stock_current_price - stock_initial_price) * stock_shares 
            net += delta
        print(f'stock:{stock_name} org price:{stock_initial_price} cur price:{stock_current_price}')

    print(f'{len(unique_holdings)} individual stocks')
    return net

def make_report(portfolio, prices):
    table_entries = []
    stocks = read_prices(prices)
    holdings = read_portfolio(portfolio)

    for holding in holdings:
        name = holding['name']
        initial_price = holding['price']
        shares = holding['shares']
        if name in stocks:
            current_price = stocks[name]
            delta = current_price - initial_price
            table_entries.append((name, shares, current_price, delta))

    return table_entries

file1 = 'Data/portfolio.csv'
file2 = 'Data/prices.csv'

def main():
    #cwd = os.getcwd()
    #print('Main with cwd:', cwd)
    headers = ('Name', 'Shares', 'Price', 'Change')
    hs = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
    #seps = f'{'-'*len(headers[0]):>10s} {'-'*len(headers[1]):>10s} {'-'*len(headers[2]):>10s} {'-'*len(headers[3]):>10s}'
    seps = f'{'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s}'
    report = make_report(file1, file2)
    print(hs)
    print(seps)

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

if __name__ == '__main__':
    main()
