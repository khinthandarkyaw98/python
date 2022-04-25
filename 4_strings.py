"""
Exercise: String in Python
Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index
Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
"""
# 1. solution
street = 'ABC'
city = 'New York'
country = 'USA'
address_1 = street + '\n' + city + '\n' + country
address_2 =  f"""{street}
{city}
{country}
"""
print("In + operator format", address_1, '\n')
print("In fstring format", address_2, '\n')


# 2. solution
line = "Earth revolves around the sun"
print(line[6:14]) #print("revolves")
print(line[-3:])  #print("sun")

# 3. solution
y = 3 # fruit_aday
x = 5 # veggie_aday
print(f"I eat {x} veggies and {y} fruits daily")
print()

# 4. solution
s='maine 200 banana khaye'
# correct statement : 'maine 10 samosa khaye'
#using two lines
s = s.replace('200', '10')
s = s.replace('banana', 'samosa')
print("Using two lines: ", s)

#using one ine
s = s.replace('200', '10').replace('banana', 'samosa')
print()
print("Using one line: ", s)


