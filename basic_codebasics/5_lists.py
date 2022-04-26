"""
Exercise: Python Lists
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""

# 1. solution
expenses = [2200, 2350, 2600, 2130, 2190]

# (1)
print("In February, this much money was spent compared to January: ", expenses[1]-expenses[0])

# (2)
print("Total expenses in first three months: ", expenses[0] + expenses[1] + expenses[2])

# (3)
print("Did I spend $2000 in any month?", 2000 in expenses)

# (4)
expenses.append(1980)
print("Expenses in June ", expenses)

# (5)
expenses[3] -= 200
print("After refund in April: ", expenses)

# 2. solution

heros=['spider man','thor','hulk','iron man','captain america']

# (1)
print("Length of list: ", len(heros))

# (2)
heros.append('black panther')
print("After adding 'black panther' at the end of the list: ", heros)

# (3)
heros.pop(-1) #heros.remove('black panther')
heros.insert(3,'black panther')
print("Added 'black panther' after 'hulk: '", heros)

# (4)
heros[1:3] = ['doctor strange']
print("Remove 'Thor' and 'hulk', and replace the list with 'doctor strange': ", heros)

# (5)
heros.sort()
print("In alphabetical order : ", heros)
