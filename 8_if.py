"""
Exercise: Python If Condition
Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
Write a program that asks user to enter a city name and it should tell which country the city belongs to
Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal
"""

# list of cities per country
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# which country belongs to
city = input("Write the name of a city\n")
city = city.lower()

if city in india:
    print(f"{city} is a city of India.")
elif city in pakistan:
    print(f"{city} is a city of Pakistan.")
elif city in bangladesh:
    print(f"{city} is a city of Bangladesh.")
else:
    print(f"{city} is out of my knowledge.")

# checks if two cities belong to the same country
city1 = input("Enter the name of the  first city.\n")
city2 = input("Enter the name of the second city.\n")
city1 = city1.lower()
city2 = city2.lower()

if city1 in india and city2 in india:
    print("Both cities are in India.")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in Pakistan.")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh.")
else:
    print("They do not belong to the same country.")

# if the sugar level is normal
sugar_level = int(input("Enter your fasting sugar level.\n"))

if sugar_level < 80:
    print("Low sugar level.")
elif sugar_level >= 80 and sugar_level <= 100:
    print("Normal sugar level.")
else:
    print("High sugar level.")