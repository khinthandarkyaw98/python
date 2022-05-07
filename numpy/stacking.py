import numpy as np

a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print()
print("a = \n", a)
print()
print("b = \n", b)
# output
# a =
#  [[0 1]
#  [2 3]
#  [4 5]]

# b =
#  [[ 6  7]
#  [ 8  9]
#  [10 11]]

c = np.vstack((a,b)) # tuple (())
print(f"vertical_stacking = \n"
      f"{c}")

# output
# vertical_stacking =
# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]]

d = np.hstack((a,b)) # tuple (())
print(f"horizontal_stacking = \n"
      f"{d}")

# output
# horizontal_stacking =
# [[ 0  1  6  7]
#  [ 2  3  8  9]
#  [ 4  5 10 11]]
