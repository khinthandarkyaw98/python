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





