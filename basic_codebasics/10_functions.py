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

# execrise 1
def calculate_area1(b=1,h=1):
    """
    :param b: base
    :param h: height
    :return area1: area of the triangle
    """
    area1 = 1/2*(b*h)
    return area1

b = int(input("Enter the base of the triangle in cm\n"))
h = int(input("Enter the height of the triangle in cm\n"))
print("The area of the triangle is ",calculate_area1(b,h)," sq_cm.")

# exercise 2
shape = input("is it 'triangle' or 'rectangle'?")

def calculate_area2(x, y):
    """
    :param x:
    :param y:
    :return area2: area of the rectangle
    """
    area2 = x * y
    return area2

if shape == 'square':
    print("The area of the triangle is", calculate_area2(b, h), " sq_cm.")
else:
    print("The area of the rectangle is", calculate_area1(b, h), " sq_cm.")