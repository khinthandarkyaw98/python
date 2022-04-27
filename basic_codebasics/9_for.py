"""
Exercise: Python for loop
After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads

Print square of all numbers between 1 to 10 except even numbers
Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message
Write a program that prints following shape


**
***
****
*****
"""
# exercise 1

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads_total = 0
for i in result:
    if i == "heads":
        heads_total += 1
    else:
        heads_total = heads_total

print("The total number of heads = ", heads_total)

# exercise 2

print("\nThe numbers from 1 to 10 with the exception of even numbers are")

for i in range(1, 11):
    if i%2 == 0:
        continue
    print(i)

# exercise 3

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
exp = int(input("Enter the expense amount in number.\n"))

month = -1
for j in range(len(expense_list)):
    if expense_list[j] == exp:
        month = j
        break

if month != -1 :
    print(f"{exp} is found in {month_list[month]}")

else:
    print("You did not spend in any month.")


# exercise 4

for k in range(1,6):
    if k == 5:
        print("Congrtulations! You finished 5 miles.")
        break
    print(f"you ran {k} miles.")
    tired = input("are you tired?")
    if tired == 'yes':
        print(f"You did not finish the race but you ran {k} miles.")
        break
    else:
        continue

# exercise 5

for i in range(1,6):
    print("*" * i)
