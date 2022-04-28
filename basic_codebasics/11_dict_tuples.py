"""
Exercise : Python Dict and Tuples
Link for the question of the exercise
 : https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_tuple_exercise.md
"""
# ex 1
# i
population = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}
# ii
# (a)
def format_pattern(population):
    for k,v in population.items():
        print(k, "==>", v)

format_pattern(population)
# (b)
def add_dict(country):
    if country not in population:
        popu = int(input("Enter the number of its population."))
        population[country] = popu
        return population
    else:
        return population


country = input("Enter the name of the country.")
print(add_dict(country))
# (c)
def remove_dict(country):
    if country in population:
        del population[country]
        return population
    else:
        return population

country = input("Enter to remove the country from the dictionary.")
a = remove_dict(country)
format_pattern(a)
# (d)
def show_popu(name):
    if name in population:
        print(population[name])
    else:
        print("Not found.")

name = input("Enter the name of the country.")
show_popu(name)

# exercise 2
operation = {"info": [600,630,620],
             "ril": [1430,1490,1567],
             "mtl": [234,180,160]}

#i(a)
def op_print(operation):
    for k, v in operation.items():
        sum = 0
        for i in range(len(v)):
            sum += v[i]
        avg = sum/len(v)
        print(k, "==>", v, "==>", "avg:", avg)

op_print(operation)

def add_op(stock=None, price=None):
    if stock in operation:
        operation[stock].append(price)
        return operation
    else:
        operation[stock] = [price]
        return operation

stock = input(print("Enter the name of the stock."))
price = int(input(print("Enter the price of the stock")))
b = add_op(stock, price)
format_pattern(b)

# Exercise 3
import math
def circle_cal(radius = 1):
    area = math.pi * (radius **2)
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter

r = float(input("Enter the radius of a circle."))
a, cir, d = circle_cal(r)
print(f"""Circle_area = {a}
Circle_circumference = {cir}
Circle_diameter = {d}
""")

