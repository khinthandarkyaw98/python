stock_prices = []
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day, price])

print(stock_prices[0])

# find stock price on March 9
for element in stock_prices:
    if element[0] == 'march 9':
        print("stock price on March 9 = ", element[1])