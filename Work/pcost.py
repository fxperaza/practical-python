# pcost.py
#
import sys
import csv
# Exercise 1.27
# fields on each line: name, total shares, share price
# field offsets
name = 0
shares = 1
price = 2

def pcost(filename):
    total_price = 0

    f = open(filename, 'rt')
    rows = csv.reader(f)

    # read, discard the headers line
    headers = next(rows)
    # each remaining line should have individual stock data
    #for line in f:
    for row in rows:
        #stock_fields = line.split(',')
        try:
            #nshares = int(stock_fields[shares])
            nshares = int(row[shares])
        except ValueError:
            print("Couldn\'t parse", row)
        
        try:
            #share_price = float(stock_fields[price])
            share_price = float(row[price])
        except ValueError:
            print("Couldn\'t parse", row)
        
        total_price += nshares * share_price

    f.close()
    return total_price

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    total_cost = pcost(filename)
    print(f'Total cost was {total_cost}')

if __name__ == '__main__':
    main()
