weather = {}
with open("nyc_weather.csv", "r") as f:
    for line in f:
        token = line.split(",")
        date = token[0]
        temperature = token[1]
        if '\n' in temperature:
            temperature = temperature[:len(temperature)-1]
        weather[date] = temperature

print(f"Temperature on Jan 9 = {weather['Jan 9']}")
print(f"Temperature on Jan 4 = {weather['Jan 4']}")

"""
The best data structure to use here is a dictionary which is internally a hash table because 
we want to know the temperature for specific day, requiring key, value pair access where we
can look up an element by day using O(1) complexity.
"""