import numpy as np

a = np.arange(12).reshape(3, 4)

print(f"a = \n{a}")
# output
# a =
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print("cell with for loop = ")
for row in a:
    for cell in row:
        print(cell, " ", end="")

# above for loop can be replaced with flatten()
print("\ncell with flatten() = ")
for cell in a.flatten():
    print(cell, " ", end= "")

# output
# cell with for loop =
# 0  1  2  3  4  5  6  7  8  9  10  11
# cell with flatten() =
# 0  1  2  3  4  5  6  7  8  9  10  11

# nditer

print("\ncell with nditer(array, order = 'C') = ")
# C order
for cell in np.nditer(a, order = "C"): # order = "C" means row by row
    print(cell, " ", end= "")
# output
# cell with nditer(array, order) =
# 0  1  2  3  4  5  6  7  8  9  10  11

# fortran order
print("\ncell with nditer(array, order = 'F') = ")
for cell in np.nditer(a, order = "F"): # order = "F" means column by column
    print(cell, " ", end= "")

# excute the entire column by column:
# use 'flags = ['external_loop']'
print("\ncell with nditer(array, order = 'F', flags = ['external_loop'] = ")
for cell in np.nditer(a, order = "F", flags = ["external_loop"]):
    print(cell)

print()

################################################################################################
################################################################################################

# do operation of the element in the array
for x in np.nditer(a, op_flags = ['readwrite']):
    x[...] = x * x

print("The square of the elements in the array:")
print(a) # we cannot use x

# output
# The square of the elements in the array:
# [[  0   1   4   9]
#  [ 16  25  36  49]
#  [ 64  81 100 121]]

b = np.arange(3, 15, 4).reshape(3, 1)

# Iterating two arrays : element-wise for each row
# this is broadcasting: there should be same dimension; otherwise one of them is 1
print("\nIterating both two arrays by elment-wise for each row")
for x, y in np.nditer([a, b]):
    print(x, y)