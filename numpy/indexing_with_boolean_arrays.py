import numpy as np

a = np.arange(12).reshape(3, 4)

print(f"a \n = {a}")

# output
# a
#  = [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

b = a > 4

print(f"b \n = {b}\n")
# output
# b
#  = [[False False False False]
#  [False  True  True  True]
#  [ True  True  True  True]]

c = a[b]
print(f"a[b] = {c}")
# output
# a[b] = [ 5  6  7  8  9 10 11]

# set all a > 4 to -1
a[b] = -1 # c = -1 does not work
print(f"\n a \n= {a}")
# output
#  a
# = [[ 0  1  2  3]
#  [ 4 -1 -1 -1]
#  [-1 -1 -1 -1]]
