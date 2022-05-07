import numpy as np

# normal list slicing
a = [1, 2, 3]
print(f"normal list slicing =\n"
      f"{a[0:2]}")  # [1, 2]

# numpy slicing
b = np.array([5, 6, 7])
print(f"numpy array slicing = \n"
      f"{b[0:2]}") # [5 6]

print(f"b[-1] = \n"
      f"{b[-1]}") # 7

c = np.array([
                [1, 3, 8],
                [2, 5, 10],
                [7, 0, 8]
            ])

print(f"c[0:2] = \n"
      f"{c[0:2]}")
# output
#c[0:2] =
#[[1 3]
# [2 5]]

print(f"c[0:2,2] = \n"
      f"{c[0:2,2]}")

#output
#c[0:2,2] =
#[ 8 10]

print(f"c[-1] = \n"
      f"{c[-1]}")

#output
# c[-1] =
# [7 0 8]

print(f"c[-1, 0:2] = \n"
      f"{c[-1, 0:2]}")
#output
# c[-1, 0:2] =
# [7 0]

print(f"c[:, 1:3] = \n"
      f"{c[:, 1:3]}")
#output c[:, 1:3] = c[all_row, 1col_2col]
# c[:, 1:3] =
# [[ 3  8]
#  [ 5 10]
#  [ 0  8]]

d = np.array([
                [6, 7, 8],
                [1, 2, 3],
                [9, 3, 2]
            ])
for row in d:
    print(f"d =\n"
          f"{d}")
#output
# d =
#[[6 7 8]
#[1 2 3]
#[9 3 2]]

print("\n one dimensional:")
for cell in d.flat:
    print(cell, end="")
#output
#  one dimensional:
# 678123932


############################################################################
############################################################################

a = np.arange(30).reshape(2, 15)
b = np.hsplit(a, 3)

print(f"\n a = \n{a}")
print("horizontal_spliting")
print(f"np.hsplit(a, 3) = \n {b}")

c = np.vsplit(a, 2)
print("vertical_spliting")
print(f"np.vsplit(a, 3) = \n {c}")

# output
# a =
# [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#  [15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]]

# horizontal_spliting
# np.hsplit(a, 3) =
#  [array([[ 0,  1,  2,  3,  4],
#        [15, 16, 17, 18, 19]]), array([[ 5,  6,  7,  8,  9],
#        [20, 21, 22, 23, 24]]), array([[10, 11, 12, 13, 14],
#        [25, 26, 27, 28, 29]])]

# vertical_spliting
# np.vsplit(a, 3) =
#  [array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]]),
#  array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])]
