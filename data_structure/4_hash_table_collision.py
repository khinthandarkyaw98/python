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

#complexity of search using a list is O(n)

# processing using python dictionary

stock_prices = {}
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print("stock prices on March 9 = ", stock_prices['march 9'])

# Complexity of search using dictionary is O(1)

# Implement Hash Table
