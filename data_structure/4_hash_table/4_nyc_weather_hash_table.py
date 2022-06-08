# my solution

weather = []
with open("nyc_weather.csv", "r") as f:
    for line in f:
        token = line.split(',')
        date = token[0]
        temperature = token[1]
        if '\n' in temperature:
            temperature = temperature[:len(temperature)-1]
        weather.append([date, temperature])

sum = 0
arr = []
for index, element in enumerate(weather):
    if index > 0:
        sum += int(element[1])

        arr.append(int(element[1]))

average = sum / index
print("average temperature = ", average)
print("maximum temperature = ", max(arr))

#############################################################################

# the best data structure to use here
# is a list bc all we want is to access the temperature elements




