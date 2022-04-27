"""
Exercise: Functions in python
Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height
Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape

Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
"""

# Exercies 1 & 2
def calculate_area(x, y, shape = "triangle"):
    if shape == "triangle":
        triangle_area = 1/2 * (x * y)
        return triangle_area
    elif shape == "rectangle":
        rectangle_area = x * y
        return  rectangle_area
    else:
        triangle_area = 1 / 2 * (x * y)
        return triangle_area


b = int(input("Enter base of the triangle in cm."))
h = int(input("Enter height of the triangle in cm."))
shape = input("is it 'triangle' or 'rectangle'?")
area = calculate_area(b, h, shape)
print(f"The area of the {shape} = ", area)

def print_pattern(n = 5):
    for i in range(n):
        p = " "
        for j in range(i+1):
            p +=  "*"
        print(p)

# Exercise 3
num = int(input("Enter the number."))
print_pattern(num)



