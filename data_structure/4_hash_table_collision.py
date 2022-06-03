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

def get_hash(key): # in {'march 6', 310.0}, key = 'march 6'
    hash = 0
    for char in key:
        hash += ord(char) #  returns the number representing
        # the unicode code of a specified character.
        return hash % 100 # let's set the size 100
        # this returns the index value of the dictionary

print(get_hash('march 6'))

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True

        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key) # this is index number of the selected row in which many arrays may exist
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index] # arr_index = index of the row, index indicates the specific array from many arrays in the row

t = HashTable()
t['march 6'] = 120
t['march 6'] = 10
t['march 17'] = 260
print(t.arr)
print(t['march 17'])
del t['march 17']
print(t.arr)




