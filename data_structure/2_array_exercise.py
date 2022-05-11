"""
Question : https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
"""
# ex 1
expense = [2200, 2350, 2600, 2130, 2190]

# (1)
print(f"In Feb, extra {expense[1]-expense[0]} dollars "
      f"were spent compared to January. ")

# (2)
def total_exp(expense, i):
    total = 0
    for j in range(i):
        total += expense[j]
    return total

print(f"total expense in first quarter of the year = {total_exp(expense, 3)}"
      f" dollars ")

# (3)
def find(expense):
    for i in range(len(expense)):
        if expense[i] == 2000:
            return i
        else:
            return 6

ret = find(expense)
retu = ret + 1

month = {1: 'January',
         2: 'February',
         3: 'March',
         4: 'April',
         5: 'May'}

for k, val in month.items():
    if retu == k:
        print(f"2000 dollars were spent in {val}")
        break
    else:
        print("Sorry, the customer did not spend exactly 2000 dollars in any month.")
        break

# (3) can be simply solved as followings.
print("Did I spend $ 2000 in any mont?", 2000 in expense)

# (4)
expense.append(1980)
print("After adding the expenses of June to the list :", expense)

# (5)
expense.insert(3, expense[3]-200)
print(f"After returning the item bought in April and receiving the refund"
      f" of $ 200, the monthly expense list became {expense}")

"""
In Feb, extra 150 dollars were spent compared to January. 
total expense in first quarter of the year = 7150 dollars 
Sorry, the customer did not spend exactly 2000 dollars in any month.
Did I spend $ 2000 in any mont? False
After adding the expenses of June to the list : [2200, 2350, 2600, 2130, 2190, 1980]
After returning the item bought in April and receiving the refund of $ 200, the monthly expense list became [2200, 2350, 2600, 1930, 2130, 2190, 1980]
"""
print()
#################################################################################################################################################################################

# ex 2
heros=['spider man','thor','hulk','iron man','captain america']

# (1)
print(f"Length of the list'heros' = {len(heros)}")

# (2)
heros.append('black panther')
print(f"After adding 'black panther' at the end of the list, "
      f"\nthe list becomes \n{heros}")

# (3)
heros.pop(-1) # remove the last element in the list of heros
heros.insert(3, 'black panther') # add 'black panther' after 'hulk'
print("The list in which 'black panther' is added after 'hulk':\n", heros)

# (4)
# heros.remove('thor') # remove 'thor'
# heros.remove('hulk') # remove 'hulk'
# heros.insert(1, 'doctor strange')
heros[1: 3] = ['doctor strange'] # do not forget to put 'doctor strange' in the square bracket
print(f"Solution for ex(4): {heros}")

# (5)
heros.sort()
print("After sorting: ", heros)

################################################################################################################

# exercise 3

num = int(input("Enter a maximum number."))

print("Odd numbers are: ")

def odd(num):
    a = []
    if num <= 0:
        return None
    else:
        for i in range(num):
            if i%2 != 0:
                a.append(i)
        return a

print(odd(num))


