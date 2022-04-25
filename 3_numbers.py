"""
Exercise: Numbers in python
You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
Print binary representation of number 17
"""
# 1. solution
length =  92
width = 48.8
total_area = length * width
print('toal area', total_area)

# 2. solution
item_bought = 9
each_cost = 1.49
give_money = 20
receive = give_money - (item_bought * each_cost)
print('The shopkeeper is going to give you', receive, 'dollars.')

# 3. solution
length = 5.5
area = length**2
cost_per_sqft = 500
cost_bathroom = area * cost_per_sqft
print('The cost of the bathroom tiles :', cost_bathroom, 'Rs.')

# 4. solution
number = 17
print('The binary representation of number', number, 'is', bin(number)+'.')
print('Binary representation of number 17 =', format(number, 'b'))

